# ADR-106 — Publish to PyPI through Trusted Publishing

## Purpose

Decide how DIXI Spec Kit reaches PyPI, so that `pipx install dixi-spec-kit` and `uv tool install dixi-spec-kit` work without cloning or downloading release files, without storing a publishing token anywhere.

## Status

Accepted on 2026-11-10 by the responsible person (Trusted Publishing chosen over manual uploads). The first upload happens with the first release published after the PyPI side is configured ([guide](../../docs/pypi-publishing.md)).

## Context

- Since v1.0.0 the kit installs from Git (`uv tool install git+https://…@vX.Y.Z`) or from the wheel attached to each GitHub release. Publication on PyPI was deferred ([publication readiness](../../docs/publication-readiness.md)); the name `dixi-spec-kit` was free on 2026-11-08 ([B3](../../docs/b3-verification.md)).
- [ADR-103](ADR-103-ci-publica-en-github-actions.md) keeps public CI free of credentials: `contents: read`, actions pinned by full SHA, no secrets.
- PyPI supports Trusted Publishing: a GitHub Actions job requests a short-lived OpenID Connect token (`id-token: write`) and PyPI exchanges it for an upload token valid for minutes, only for the configured repository, workflow file and environment.
- Releases are created by a maintainer, from `main`, after signed pull requests and green CI.

## Decision

1. **Trusted Publishing only.** `.github/workflows/publish.yml` runs when a GitHub release is published. No API token is created or stored, and no `secrets.*` is referenced.
2. **Two jobs, least privilege.** `build` (permissions `contents: read`) checks that the tag equals `v` + the version in `pyproject.toml`, runs `make verify` (which builds `dist/`), requires exactly one wheel and one sdist, and uploads them as an artifact. `publish` downloads that artifact and uploads it with `pypa/gh-action-pypi-publish`; it is the only job with `id-token: write`.
3. **Protected environment.** `publish` runs in the GitHub environment `pypi`, which the maintainer can restrict to tags `v*` and to required reviewers, so a person approves every upload.
4. **Pinned actions.** Every `uses:` is pinned to a full commit SHA with the version in a comment, as in `verify.yml`.
5. **Same artifacts.** The files on PyPI are built by CI from the tagged commit; the files attached to the GitHub release may be built locally by the maintainer, so both sets are verified by the same `make verify`.

## Alternatives considered

- **Manual upload with `twine` and a PyPI token.** Rejected: a long-lived secret on a laptop, and uploads that depend on one machine's state.
- **Token stored as a repository secret.** Rejected: contradicts ADR-103 and widens the blast radius of a compromised workflow.
- **Stay on Git and release files only.** Rejected for now: PyPI is the expected install path for Python CLIs and the name is available.

## Consequences

- Before the first upload the maintainer creates the `pypi` environment in GitHub and a "pending publisher" in PyPI (owner `dixi-project`, repository `dixi-spec-kit`, workflow `publish.yml`, environment `pypi`).
- A release whose tag does not match the package version fails before anything is uploaded.
- PyPI versions are immutable: a broken release is fixed with a new version, never by replacing files.
- The READMEs announce `pipx install dixi-spec-kit` only after the first upload succeeds.
- Test: `tests/test_publish_workflow.py` checks the trigger, permissions, environment, pinned actions and the tag check.

## Related

- [ADR-100](ADR-100-distribucion-publica-v1.md)
- [ADR-103](ADR-103-ci-publica-en-github-actions.md)
- [PyPI publishing guide](../../docs/pypi-publishing.md)
