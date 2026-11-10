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

1. Bump the version (`pyproject.toml`, `src/dixi_spec_kit/__init__.py`, the version test and the CHANGELOG) in a pull request and merge it.
2. Create the GitHub release with tag `vX.Y.Z` from `main`, as usual. Publishing the release starts `publish.yml`.
3. If the environment requires reviewers, approve the `publish` job in the Actions tab.
4. Check `https://pypi.org/project/dixi-spec-kit/` and install in a clean shell: `pipx install dixi-spec-kit` or `uv tool install dixi-spec-kit`, then `dixi --version`.

## If something fails

- **Tag does not match the package version:** nothing was uploaded. Delete the release and the tag, fix the version, and release again.
- **`invalid-publisher` from PyPI:** one of the five pending-publisher fields does not match exactly (case included). Fix it on PyPI and re-run the failed job.
- **A bad version reached PyPI:** PyPI never allows replacing a file. Yank it on PyPI and publish a new patch version.

## Related

- [ADR-106](../09-architecture/adr/ADR-106-pypi-trusted-publishing.md)
- [Repository settings](repository-settings.md)
- [Publication readiness](publication-readiness.md)
