# PyPI publishing

## Purpose

Steps for a maintainer to enable and use the PyPI publication defined in [ADR-106](../09-architecture/adr/ADR-106-pypi-trusted-publishing.md). Nothing here needs a token.

## One-time setup

1. **GitHub environment.** In `dixi-project/dixi-spec-kit` → Settings → Environments → New environment, name `pypi`. Recommended: *Required reviewers* (a maintainer approves each upload) and *Deployment branches and tags* limited to tags matching `v*`.
2. **PyPI pending publisher.** Sign in to pypi.org → Your account → Publishing → *Add a new pending publisher* (GitHub):
   - PyPI project name: `dixi-spec-kit`
   - Owner: `dixi-project`
   - Repository name: `dixi-spec-kit`
   - Workflow name: `publish.yml`
   - Environment name: `pypi`

   The pending publisher reserves nothing until the first upload; after it, it becomes a normal trusted publisher of the project.

## Each release

1. Bump the version (`pyproject.toml`, `src/dixi_spec_kit/__init__.py`, the version test and the CHANGELOG) in a pull request and merge it. In the CHANGELOG section of the version, name the pull request of every entry, for example `(#57)`. For pull requests that need no entry, such as documentation-only ones, add one line to the section, alone on that line: `<!-- no changelog entry: #49, #50 -->`; it is not published in the release notes. The same text quoted inside an entry, as in this sentence, is not a marker and stays in the notes.
2. Only after that pull request is merged: `git switch main && git pull --ff-only public main`, remove other versions from `dist/`, then `make release VERSION=X.Y.Z`. It refuses before creating anything if `public/main` does not carry the version (the release PR is not merged), the checkout is not `public/main` or has local changes, the tag already exists, or `dist/` does not hold exactly this version; it runs `make verify`, lists the pull requests merged since the previous tag whose number or branch the CHANGELOG section does not mention and asks you to type `yes` to go on without them, then shows the release and its notes (the CHANGELOG section) and asks you to type the version before calling `gh release create`. Publishing the release starts `publish.yml`.
3. If the environment requires reviewers, approve the `publish` job in the Actions tab.
4. Check `https://pypi.org/project/dixi-spec-kit/` and install in a clean shell: `pipx install dixi-spec-kit` or `uv tool install dixi-spec-kit`, then `dixi --version`.

## After a release

The real version is the one PyPI serves: check https://pypi.org/project/dixi-spec-kit/ and, in a clean shell, `uv tool install --force --refresh dixi-spec-kit` (or `pipx install --force dixi-spec-kit`) and `dixi --version`. Without `--refresh`, `uv` may install the version it has cached.

Badges are images served through caches and say nothing about whether the release worked. The README shows the latest GitHub release, which changes about five minutes after `make release`. A badge of the PyPI version is sent with a cache lifetime of six hours and GitHub keeps its own copy of README images, so on 2026-11-12 it still showed v1.10.0 hours after v1.11.0 was on PyPI; that is why the README does not use it.

## If something fails

- **Tag does not match the package version:** nothing was uploaded; the release was created before its pull request was merged. Delete the release and the tag (`gh release delete vX.Y.Z -R dixi-project/dixi-spec-kit --cleanup-tag --yes`, `git tag -d vX.Y.Z`) and release again with `make release`.
- **`invalid-publisher` from PyPI:** one of the five pending-publisher fields does not match exactly (case included). Fix it on PyPI and re-run the failed job.
- **A bad version reached PyPI:** PyPI never allows replacing a file. Yank it on PyPI and publish a new patch version.

## Related

- [ADR-106](../09-architecture/adr/ADR-106-pypi-trusted-publishing.md)
- [Repository settings](repository-settings.md)
- [Publication readiness](publication-readiness.md)
