"""Create the GitHub release vX.Y.Z only when it is safe: `make release VERSION=X.Y.Z`.

Refuses, before creating anything, when the release pull request is not merged (public/main does not
carry the version), the checkout is not public/main or has local changes, the tag already exists, or
dist/ does not hold exactly this version's wheel and sdist. Runs `make verify`, checks dist/ again,
shows what it will do and asks the person to type the version before calling `gh release create`.
Publishing the release starts publish.yml; the PyPI upload still waits for a maintainer's approval.
"""
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
REPO = "dixi-project/dixi-spec-kit"
REMOTE = "public"
VERSION = re.compile(r"(0|[1-9][0-9]{0,3})\.(0|[1-9][0-9]{0,3})\.(0|[1-9][0-9]{0,3})")


def pyproject_version(text):
    match = re.search(r'^version = "([^"]+)"$', text, re.MULTILINE)
    if not match:
        raise ValueError("no version in pyproject.toml")
    return match.group(1)


def changelog_notes(text, version):
    match = re.search(rf"^## \[{re.escape(version)}\][^\n]*\n(.*?)(?=^## \[|\Z)", text, re.MULTILINE | re.DOTALL)
    if not match or not match.group(1).strip():
        raise ValueError(f"CHANGELOG.md has no [{version}] section")
    return match.group(1).strip() + "\n"


def release_problems(version, main_version, local_head, remote_head, dirty, tag_exists, dist_names):
    if not VERSION.fullmatch(version or ""):
        return [f"invalid version {version!r}: use X.Y.Z"]
    problems = []
    if main_version != version:
        problems.append(f"{REMOTE}/main has version {main_version}: merge the release pull request for "
                        f"{version} first, then pull")
    if local_head != remote_head:
        problems.append(f"the checkout is not {REMOTE}/main: run `git switch main && git pull --ff-only "
                        f"{REMOTE} main`")
    if dirty:
        problems.append("the working tree has local changes: commit or remove them")
    if tag_exists:
        problems.append(f"tag v{version} already exists: delete the wrong release first "
                        f"(`gh release delete v{version} -R {REPO} --cleanup-tag --yes`, `git tag -d v{version}`)")
    expected = sorted([f"dixi_spec_kit-{version}-py3-none-any.whl", f"dixi_spec_kit-{version}.tar.gz"])
    if sorted(dist_names) != expected:
        problems.append(f"dist/ must hold exactly {', '.join(expected)}; found {', '.join(sorted(dist_names)) or 'nothing'}")
    return problems


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()


def dist_names():
    folder = ROOT / "dist"
    return [p.name for p in folder.iterdir() if p.is_file()] if folder.is_dir() else []


def state(version):
    git("fetch", "--quiet", REMOTE, "--tags", "--force")
    tags = subprocess.run(["git", "ls-remote", "--tags", REMOTE, f"refs/tags/v{version}"], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout.strip()
    return dict(version=version, main_version=pyproject_version(git("show", f"{REMOTE}/main:pyproject.toml")),
                local_head=git("rev-parse", "HEAD"), remote_head=git("rev-parse", f"{REMOTE}/main"),
                dirty=bool(git("status", "--porcelain", "--untracked-files=no")),
                tag_exists=bool(tags), dist_names=dist_names())


def refuse(problems):
    print("Release refused; nothing was created:", file=sys.stderr)
    for problem in problems:
        print(f"- {problem}", file=sys.stderr)
    return 1


def main(argv):
    if len(argv) != 1:
        print("usage: make release VERSION=X.Y.Z", file=sys.stderr)
        return 2
    version = argv[0]
    current = state(version)
    # dist/ is rebuilt by make verify: check everything else first, then dist after the build.
    problems = [p for p in release_problems(**{**current, "dist_names": [
        f"dixi_spec_kit-{version}-py3-none-any.whl", f"dixi_spec_kit-{version}.tar.gz"]})]
    stale = [n for n in current["dist_names"] if f"-{version}" not in n]
    if stale:
        problems.append(f"dist/ holds files of another version ({', '.join(sorted(stale))}): remove them")
    if problems:
        return refuse(problems)
    if subprocess.run(["make", "verify"], cwd=ROOT).returncode != 0:
        return refuse(["make verify failed"])
    problems = release_problems(**state(version))
    if problems:
        return refuse(problems)
    notes = changelog_notes((ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), version)
    print(f"\nReady to create release v{version} from {REMOTE}/main ({current['remote_head'][:7]}) with:")
    for name in sorted(dist_names()):
        print(f"  dist/{name}")
    print("\nNotes (from CHANGELOG.md):\n" + notes)
    if input(f"Type {version} to create the release: ").strip() != version:
        return refuse(["not confirmed"])
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as handle:
        handle.write(notes)
    command = ["gh", "release", "create", f"v{version}", "-R", REPO, "--target", current["remote_head"],
               "--title", f"DIXI Spec Kit {version}", "--notes-file", handle.name,
               *[str(ROOT / "dist" / n) for n in sorted(dist_names())]]
    result = subprocess.run(command, cwd=ROOT)
    Path(handle.name).unlink(missing_ok=True)
    if result.returncode == 0:
        print("\nNext: approve the `pypi` deployment of the `publish` run in GitHub Actions.")
    return result.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
