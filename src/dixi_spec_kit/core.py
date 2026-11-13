import hashlib
from importlib.resources import files
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

from . import __version__
from .filesystem import (Issue, decode_json, directory, read_file, read_json,
                         root_directory, safe_path, supported, write_file)


PARENTS = {"goal": set(), "domain": {"goal"}, "module": {"domain"},
           "feature": {"module"}, "contract": {"feature", "module"},
           "test": {"feature", "contract"}}
METADATA = ".dixi/project.json"
AGENTS = ("none", "claude", "codex", "skills")
HOOK_AGENTS = ("claude", "codex")
PROFILES = ("minimal", "site", "app", "platform")
MAX_MANAGED = 1000
CODEX_POLICY = b"policy:\n  allow_implicit_invocation: false\n"
CLAUDE_REQUIRED = ("discover", "specify", "clarify", "plan", "tasks", "build", "verify", "review", "analyze", "status")
CLAUDE_COMMANDS = CLAUDE_REQUIRED + ("domain", "architecture", "contract", "threat-model", "handoff", "change",
                                     "data", "quality", "ai", "release", "promote", "operate", "finops",
                                     "compliance", "duediligence", "interview", "risk-review",
                                     "constitution", "checklist", "converge", "onboard", "bugfix", "issues")
SUBAGENTS = ("architect", "tester", "developer", "reviewer")
CONTROLS = ("protect_tests", "guard_secrets", "guard_attestation", "mode_gate", "verify_on_stop")
TEST_PATH = re.compile(r"(^|/)(tests?|__tests__|spec)/|(^|/)test_[^/]*$|_test\.[^/]+$|\.(test|spec)\.[^/]+$|\.feature$")
EXCLUDED_PATH = re.compile(r"(\.md$|^docs/|(^|/)(package-lock\.json|yarn\.lock|pnpm-lock\.yaml|poetry\.lock|uv\.lock|"
                           r"Cargo\.lock|go\.sum|Gemfile\.lock|composer\.lock)$|\.min\.(js|css)$|(^|/)generated/)")
TRACE = ".dixi/traceability.json"
INLINE_LINK = re.compile(r"!?\[[^\[\]\n]{0,999}\]\(([^)\n]{1,4096})\)")
KIT_VERSION = re.compile(r"(0|[1-9][0-9]{0,3})\.(0|[1-9][0-9]{0,3})\.(0|[1-9][0-9]{0,3})(?:\.dev[0-9]{1,4}|rc[0-9]{1,4})?")
REFERENCE_LINK = re.compile(r"^ {0,3}\[[^\[\]\n]{1,999}\]:[ \t]*(<[^>\n]{1,4096}>|[^\s<>]{1,4096})(?=[ \t]|$)", re.MULTILINE)


def templates(language):
    data = files("dixi_spec_kit").joinpath("resources", f"project.{language}.json").read_bytes()
    payload = decode_json(data, "resources")
    if not isinstance(payload, dict) or not 1 <= len(payload) <= 500:
        raise Issue("invalid_resources", 5)
    if any(not safe_path(k) or not isinstance(v, str) for k, v in payload.items()):
        raise Issue("invalid_resources", 5)
    return payload


def profile_manifest():
    data = decode_json(files("dixi_spec_kit").joinpath("resources", "profiles.json").read_bytes(), "resources")
    entries = data.get("files") if isinstance(data, dict) else None
    if (not isinstance(entries, dict) or data.get("version") != 1
            or any(not safe_path(k) or not isinstance(v, str) or not re.fullmatch(r"[ynr]{3}", v)
                   for k, v in entries.items())):
        raise Issue("invalid_resources", 5)
    return entries


def profile_files(language, profile, regulated):
    if profile == "minimal":
        return {}
    column = PROFILES.index(profile) - 1
    folder = files("dixi_spec_kit").joinpath("resources", "templates", language)
    payload = {}
    for name, codes in profile_manifest().items():
        if codes[column] == "y" or (regulated and codes[column] == "r"):
            payload[name] = folder.joinpath(*name.split("/")).read_bytes()
    return payload


def check_profile(profile, regulated):
    if profile not in PROFILES or type(regulated) is not bool:
        raise Issue("invalid_arguments", 2)
    if regulated and profile == "minimal":
        raise Issue("regulated_requires_profile", 2)


def recorded_profile(metadata):
    return metadata.get("profile", "minimal"), metadata.get("regulated", False)


def codex_files(language):
    folder = files("dixi_spec_kit").joinpath("resources", "codex", language)
    payload = {}
    for name in CLAUDE_COMMANDS:
        payload[f".agents/skills/dixi-{name}/SKILL.md"] = folder.joinpath(f"dixi-{name}.md").read_bytes()
        payload[f".agents/skills/dixi-{name}/agents/openai.yaml"] = CODEX_POLICY
    return payload


def skills_files(language):
    """Agent Skills (agentskills.io) for any compatible agent, derived from the Codex skills (ADR-108 phase D).

    Same `.agents/skills/` path and Codex policy file; adds `disable-model-invocation: true` (honoured by Cursor,
    VS Code/Copilot and OpenCode) and replaces the Codex-only `$dixi-<op>` syntax with the skill name.
    """
    folder = files("dixi_spec_kit").joinpath("resources", "codex", language)
    payload = {}
    for name in CLAUDE_COMMANDS:
        text = folder.joinpath(f"dixi-{name}.md").read_text(encoding="utf-8")
        text = text.replace("\n---\n", "\ndisable-model-invocation: true\n---\n", 1)
        text = re.sub(r"\$dixi-([a-z0-9-]+)", r"dixi-\1", text)
        payload[f".agents/skills/dixi-{name}/SKILL.md"] = text.encode("utf-8")
        payload[f".agents/skills/dixi-{name}/agents/openai.yaml"] = CODEX_POLICY
    return payload


def required_adapter_files(agent):
    if agent == "claude":
        return {"CLAUDE.md"} | {f".claude/commands/dixi.{name}.md" for name in CLAUDE_REQUIRED}
    if agent in ("codex", "skills"):
        return {f".agents/skills/dixi-{name}/{suffix}" for name in CLAUDE_REQUIRED
                for suffix in ("SKILL.md", "agents/openai.yaml")}
    return set()


def adapter_files(agent, language):
    if agent == "none":
        return {}
    if agent == "codex":
        return codex_files(language)
    if agent == "skills":
        return skills_files(language)
    folder = files("dixi_spec_kit").joinpath("resources", "claude", language)
    payload = {"CLAUDE.md": folder.joinpath("CLAUDE.md").read_bytes()}
    for name in CLAUDE_COMMANDS:
        payload[f".claude/commands/dixi.{name}.md"] = folder.joinpath(f"dixi.{name}.md").read_bytes()
    for name in SUBAGENTS:
        payload[f".claude/agents/dixi-{name}.md"] = folder.joinpath("agents", f"dixi-{name}.md").read_bytes()
    try:
        for data in payload.values():
            data.decode("utf-8")
    except UnicodeError:
        raise Issue("invalid_resources", 5) from None
    return payload


def hook_command(agent, script):
    if agent == "claude":
        return f'python3 "$CLAUDE_PROJECT_DIR/.dixi/hooks/{script}.py"'
    return f'python3 "$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.dixi/hooks/{script}.py"'


def hook_group(agent, scripts, matcher=None, timeout=None):
    handlers = []
    for script in scripts:
        handler = {"type": "command", "command": hook_command(agent, script)}
        if timeout:
            handler["timeout"] = timeout
        handlers.append(handler)
    return ({"matcher": matcher} if matcher else {}) | {"hooks": handlers}


def control_files(agent):
    if agent not in HOOK_AGENTS:
        return {}
    folder = files("dixi_spec_kit").joinpath("resources", "hooks")
    payload = {f".dixi/hooks/{name}.py": folder.joinpath(f"{name}.py").read_bytes() for name in CONTROLS}
    shell = ("mode_gate", "guard_secrets", "guard_attestation", "protect_tests")
    stop = [hook_group(agent, ["verify_on_stop"], timeout=300)]
    if agent == "claude":
        events = {"PreToolUse": [hook_group(agent, shell, "Bash"), hook_group(agent, ["guard_secrets"], "Read|Grep"),
                                 hook_group(agent, ["protect_tests"], "Edit|Write|MultiEdit|NotebookEdit")],
                  "Stop": stop, "SubagentStop": stop}
        name = ".claude/settings.json"
    else:
        events = {"PreToolUse": [hook_group(agent, shell, "^Bash$"), hook_group(agent, ["protect_tests"], "^apply_patch$")],
                  "Stop": stop, "SubagentStop": stop}
        name = ".codex/hooks.json"
    payload[name] = (json.dumps({"hooks": events}, indent=2) + "\n").encode()
    return payload


def message(key, **params):
    return {"key": key, "params": params}


def initialize(destination, language, agent="none", profile="minimal", regulated=False, controls=False):
    check_profile(profile, regulated)
    if controls and agent not in HOOK_AGENTS:
        raise Issue("controls_require_agent", 2)
    text = str(destination)
    path = Path(os.getcwd()) if text and text.rstrip("/") == "." else Path(text)
    if not text or ".." in path.parts or not path.name:
        raise Issue("unsafe_destination", 3)
    payload = {name: text.encode("utf-8") for name, text in templates(language).items()}
    payload.update(profile_files(language, profile, regulated))
    payload.update(adapter_files(agent, language))
    if controls:
        payload.update(control_files(agent))
    metadata = {"schema_version": 1, "kit_version": __version__, "language": language,
                "agent": agent, "policy": "portable", "profile": profile, "regulated": regulated,
                "controls": bool(controls),
                "managed_files": {name: hashlib.sha256(data).hexdigest() for name, data in payload.items()}}
    try:
        with root_directory(path.parent) as parent:
            try:
                os.mkdir(path.name, mode=0o700, dir_fd=parent)
            except FileExistsError:
                pass
            with directory(parent, [path.name]) as root:
                if os.listdir(root):
                    raise Issue("destination_conflict", 3)
                write_file(root, ".dixi-init.lock", b"")
                for name, data in payload.items():
                    write_file(root, name, data)
                write_file(root, METADATA, (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode())
                os.unlink(".dixi-init.lock", dir_fd=root)
    except Issue as error:
        if error.key == "unsafe_path":
            error.key, error.code = "unsafe_destination", 3
        raise
    except FileExistsError:
        raise Issue("destination_conflict", 3) from None
    return [message("initialized", path=str(path)), message("structure_only")]


def initialize_existing(destination, language, agent="none", profile="minimal", regulated=False, controls=False):
    """Add DIXI to a folder that already has files: create only what is missing, never overwrite (T13).

    A file that already exists with other content, a symlink or a path under a symlinked folder is kept as it
    is and reported as a conflict. Every kit file is recorded with the kit's hash, so `upgrade` never treats a
    kept file as updatable.
    """
    path = Path(os.getcwd()) if str(destination).rstrip("/") in ("", ".") else Path(str(destination))
    if not path.is_dir() or path.is_symlink():
        return initialize(destination, language, agent, profile, regulated, controls), None
    check_profile(profile, regulated)
    if controls and agent not in HOOK_AGENTS:
        raise Issue("controls_require_agent", 2)
    if ".." in path.parts:
        raise Issue("unsafe_destination", 3)
    payload = {name: text.encode("utf-8") for name, text in templates(language).items()}
    payload.update(profile_files(language, profile, regulated))
    payload.update(adapter_files(agent, language))
    if controls:
        payload.update(control_files(agent))
    metadata = {"schema_version": 1, "kit_version": __version__, "language": language,
                "agent": agent, "policy": "portable", "profile": profile, "regulated": regulated,
                "controls": bool(controls),
                "managed_files": {name: hashlib.sha256(data).hexdigest() for name, data in payload.items()}}
    details = {"created": [], "adopted": [], "conflicts": []}
    try:
        with root_directory(path) as root:
            try:
                read_file(root, METADATA)
                raise Issue("already_initialized", 3, path=str(path))
            except Issue as error:
                if error.key != "missing_file":
                    raise
            try:
                write_file(root, ".dixi-init.lock", b"")
            except FileExistsError:
                raise Issue("destination_conflict", 3) from None
            try:
                for name, data in sorted(payload.items()):
                    try:
                        write_file(root, name, data)
                        details["created"].append(name)
                    except FileExistsError:
                        try:
                            same = read_file(root, name) == data
                        except Issue:
                            same = False
                        details["adopted" if same else "conflicts"].append(name)
                    except Issue:
                        details["conflicts"].append(name)
                write_file(root, METADATA, (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode())
            finally:
                os.unlink(".dixi-init.lock", dir_fd=root)
    except Issue as error:
        if error.key == "unsafe_path":
            error.key, error.code = "unsafe_destination", 3
        raise
    except FileExistsError:
        raise Issue("destination_conflict", 3) from None
    return [message("initialized_existing", path=str(path), created=len(details["created"]),
                    adopted=len(details["adopted"]), conflicts=len(details["conflicts"])),
            message("structure_only")], details


def project_metadata(root):
    try:
        data = read_json(root, METADATA)
    except Issue as error:
        if error.key == "missing_file":
            raise Issue("missing_project", 2) from None
        raise
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int:
        raise Issue("invalid_metadata")
    if data["schema_version"] != 1:
        raise Issue("unsupported_schema", 4)
    if (not isinstance(data.get("kit_version"), str) or data.get("language") not in ("es", "en")
            or data.get("agent") not in AGENTS or data.get("policy") != "portable"):
        raise Issue("invalid_metadata")
    version = KIT_VERSION.fullmatch(data["kit_version"])
    if not version:
        raise Issue("invalid_metadata")
    if version.group(1) != __version__.split(".")[0]:
        raise Issue("unsupported_schema", 4)
    inventory = data.get("managed_files")
    if not isinstance(inventory, dict) or not 1 <= len(inventory) <= MAX_MANAGED:
        raise Issue("invalid_metadata")
    for name, digest in inventory.items():
        if not safe_path(name) or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise Issue("invalid_metadata")
    profile, regulated = recorded_profile(data)
    if profile not in PROFILES or type(regulated) is not bool or (regulated and profile == "minimal"):
        raise Issue("invalid_metadata")
    controls = data.get("controls", False)
    if type(controls) is not bool or (controls and data["agent"] not in HOOK_AGENTS):
        raise Issue("invalid_metadata")
    required = set(templates(data["language"])) | required_adapter_files(data["agent"])
    if not required <= set(inventory):
        raise Issue("invalid_metadata")
    extensions = data.get("extensions", {})
    if not isinstance(extensions, dict) or len(extensions) > 100:
        raise Issue("invalid_metadata")
    for ext_id, entry in extensions.items():
        if (not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", ext_id) or not isinstance(entry, dict)
                or not isinstance(entry.get("version"), str) or not isinstance(entry.get("files"), dict)
                or len(entry["files"]) > MAX_MANAGED):
            raise Issue("invalid_metadata")
        for name, digest in entry["files"].items():
            if not safe_path(name) or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise Issue("invalid_metadata")
    presets = data.get("presets", {})
    if not isinstance(presets, dict) or len(presets) > 100:
        raise Issue("invalid_metadata")
    for preset_id, entry in presets.items():
        if (not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", preset_id) or not isinstance(entry, dict)
                or not isinstance(entry.get("version"), str) or type(entry.get("priority")) is not int
                or not isinstance(entry.get("files"), dict) or not isinstance(entry.get("copy"), dict)):
            raise Issue("invalid_metadata")
        for name, digest in [*entry["files"].items(), *entry["copy"].items()]:
            if not safe_path(name) or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise Issue("invalid_metadata")
    return data


def traceability(root):
    data = read_json(root, TRACE)
    if (not isinstance(data, dict) or type(data.get("schema_version")) is not int
            or data["schema_version"] != 1 or not isinstance(data.get("items"), list)
            or len(data["items"]) > 500):
        raise Issue("invalid_trace")
    items = data["items"]
    by_id = {}
    for item in items:
        if (not isinstance(item, dict) or not isinstance(item.get("id"), str)
                or not re.fullmatch(r"[A-Za-z][A-Za-z0-9._-]{0,127}", item["id"])
                or not isinstance(item.get("kind"), str) or item["kind"] not in PARENTS
                or not safe_path(item.get("path")) or not isinstance(item.get("parents"), list)
                or len(item["parents"]) > 500 or any(not isinstance(p, str) for p in item["parents"])):
            raise Issue("invalid_trace")
        if item["id"] in by_id or len(item["parents"]) != len(set(item["parents"])):
            raise Issue("invalid_trace")
        by_id[item["id"]] = item
    issues = []
    for item in items:
        allowed = PARENTS[item["kind"]]
        if bool(item["parents"]) != bool(allowed) or any(
                p not in by_id or by_id[p]["kind"] not in allowed for p in item["parents"]):
            issues.append(message("invalid_parent", path=item["id"]))
    return items, issues


def markdown_links(root, name, data, removable=frozenset()):
    try:
        text = data.decode("utf-8")
    except UnicodeError:
        raise Issue("invalid_file", path=name) from None
    issues = []
    targets = INLINE_LINK.findall(text) + REFERENCE_LINK.findall(text)
    if len(targets) > 500:
        raise Issue("invalid_file", path=name)
    for target in targets:
        target = target.strip()
        if not target:
            continue
        target = target[1:target.index(">")] if target.startswith("<") and ">" in target else target.split()[0]
        try:
            link = urlsplit(target)
            if link.scheme in {"http", "https", "mailto"}:
                continue
            if link.scheme or link.netloc or link.path.startswith("/"):
                raise Issue("unsafe_path")
            if not link.path:
                continue
            relative = posixpath.normpath(posixpath.join(str(PurePosixPath(name).parent), unquote(link.path)))
            try:
                read_file(root, relative)
            except Issue as error:
                if error.key != "missing_file" or relative not in removable:
                    raise
        except (Issue, ValueError):
            issues.append(message("invalid_link", path=name))
    return issues


def check_project(path):
    issues = []
    with root_directory(path) as root:
        metadata = project_metadata(root)
        names = set(metadata["managed_files"])
        optional = set(profile_manifest()) & names
        try:
            items, graph_issues = traceability(root)
            issues.extend(graph_issues)
            names.update(item["path"] for item in items)
        except Issue as error:
            issues.append(message(error.key, **error.params))
        for name in sorted(names):
            try:
                data = read_file(root, name)
                if name.endswith(".md"):
                    issues.extend(markdown_links(root, name, data, optional))
            except Issue as error:
                if error.key == "missing_file" and name in optional:
                    continue
                issues.append(message(error.key, **error.params))
    return (1 if issues else 0), issues + [message("structure_only")]


def doctor(path, language):
    if not supported():
        raise Issue("unsupported_platform", 4)
    templates(language)
    results = [message("runtime", version=sys.version.split()[0]), message("resources_ok")]
    with root_directory(path) as root:
        try:
            metadata = project_metadata(root)
            profile, regulated = recorded_profile(metadata)
            results.append(message("profile", profile=profile, regulated=regulated))
            results.append(message("controls", controls=metadata.get("controls", False)))
            if metadata["agent"] == "claude":
                installed = sum(f".claude/commands/dixi.{name}.md" in metadata["managed_files"]
                                for name in CLAUDE_COMMANDS)
                results.append(message("agent_claude", language=metadata["language"],
                                       commands=installed, available=len(CLAUDE_COMMANDS)))
                if installed < len(CLAUDE_COMMANDS):
                    results.append(message("upgrade_hint"))
            elif metadata["agent"] == "codex":
                installed = sum(f".agents/skills/dixi-{name}/SKILL.md" in metadata["managed_files"]
                                for name in CLAUDE_COMMANDS)
                results.append(message("agent_codex", language=metadata["language"],
                                       skills=installed, available=len(CLAUDE_COMMANDS)))
                if installed < len(CLAUDE_COMMANDS):
                    results.append(message("upgrade_hint"))
            elif metadata["agent"] == "skills":
                installed = sum(f".agents/skills/dixi-{name}/SKILL.md" in metadata["managed_files"]
                                for name in CLAUDE_COMMANDS)
                results.append(message("agent_skills", language=metadata["language"],
                                       skills=installed, available=len(CLAUDE_COMMANDS)))
                if installed < len(CLAUDE_COMMANDS):
                    results.append(message("upgrade_hint"))
            else:
                results.append(message("agent_none", language=metadata["language"]))
        except Issue as error:
            if error.code != 2:
                raise
            results.append(message("no_project_optional"))
    return results


def strip_code(text):
    text = re.sub(r"(?ms)^ {0,3}(```|~~~).*?^ {0,3}\1[^\n]*$", "", text)
    return re.sub(r"`[^`\n]*`", "", text)


def placeholders(path):
    counts = {}
    with root_directory(path) as root:
        metadata = project_metadata(root)
        for name in sorted(metadata["managed_files"]):
            if not name.endswith(".md"):
                continue
            try:
                text = read_file(root, name).decode("utf-8", errors="replace")
            except Issue as error:
                if error.key == "missing_file":
                    continue
                raise
            count = len(re.findall(r"\{\{pending:", strip_code(text)))
            if count:
                counts[name] = count
    return counts


# What /dixi.promote reviews before a person changes MODE: item, the document expected and where to look for it.
PROMOTION_EVIDENCE = (
    ("tests", "11-quality/strategy.md", ((("11-quality",), r"strategy\.md"),)),
    ("threats", "13-security/<slug>-threat-model.md", ((("13-security",), r".*threat-model.*\.md"),)),
    ("data", "08-data/<slug>.md", ((("08-data",), r".+\.md"),)),
    ("operations", "15-operations/<service>.md", ((("15-operations",), r".+\.md"),)),
    ("release", "docs/releases/<version>.md", ((("docs", "releases"), r".+\.md"),)),
    ("owners", "CODEOWNERS", (((), "CODEOWNERS"), ((".github",), "CODEOWNERS"), (("docs",), "CODEOWNERS"))),
)


def mode_report(path):
    """Read MODE and, for mvp, which promotion items have a document without `{{pending: …}}` blanks. Never writes."""
    with root_directory(path) as root:
        project_metadata(root)
        mode = read_file(root, "MODE").decode("utf-8", errors="replace").strip()
        if mode not in ("mvp", "prod"):
            raise Issue("mode_invalid", value=mode[:40])
        evidence = []
        for item, expected, places in PROMOTION_EVIDENCE if mode == "mvp" else ():
            found = []
            for parts, pattern in places:
                try:
                    with directory(root, parts) as folder:
                        names = sorted(os.listdir(folder))
                except (FileNotFoundError, Issue):
                    continue
                for name in names:
                    if name == "README.md" or not re.fullmatch(pattern, name):
                        continue
                    relative = "/".join((*parts, name))
                    try:
                        text = read_file(root, relative).decode("utf-8", errors="replace")
                    except Issue:
                        continue
                    if text.strip() and "{{pending:" not in strip_code(text):
                        found.append(relative)
            evidence.append({"item": item, "status": "present" if found else "missing", "expected": expected,
                             "found": found})
    return {"mode": mode, "evidence": evidence, "missing": sum(entry["status"] == "missing" for entry in evidence)}


def pr_size(path, base, limit):
    def git(*args):
        try:
            result = subprocess.run(["git", *args], cwd=path, capture_output=True, text=True, timeout=60)
        except (OSError, subprocess.SubprocessError):
            raise Issue("pr_size_git", 2, base=base) from None
        if result.returncode != 0:
            raise Issue("pr_size_git", 2, base=base)
        return result.stdout

    git("rev-parse", "--verify", "--quiet", f"{base}^{{commit}}")
    size = {"base": base, "counted": 0, "tests": 0, "excluded": 0, "max": limit}
    for line in git("diff", "--numstat", "--no-renames", f"{base}...HEAD").splitlines():
        parts = line.split("\t", 2)
        if len(parts) != 3:
            continue
        lines = sum(int(value) for value in parts[:2] if value.isdigit())
        name = parts[2]
        key = "tests" if TEST_PATH.search(name) else "excluded" if EXCLUDED_PATH.search(name) else "counted"
        size[key] += lines
    return size
