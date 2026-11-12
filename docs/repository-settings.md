# Public repository settings

## Purpose

Record the configuration of `dixi-project/dixi-spec-kit` that guarantees: `main` public and downloadable by anyone, forks and PRs open, and merging reserved to maintainers with review and checks. Applied and verified on 2026-11-08.

## Settings

| Setting | Value |
|---|---|
| Visibility | Public, only after reviewing the final history (below). |
| Default branch | `main`. |
| Forks | Allowed. |
| Write access | Dixi maintainers only; external collaborators without write permission. |
| Merge | Squash or merge commit; delete branches on merge. |
| Private vulnerability reporting | Enabled (Settings → Security). |
| Actions | Approval required for workflows from new contributors' PRs. |
| Pages | Source: GitHub Actions (Settings → Pages). `.github/workflows/pages.yml` builds the documentation site with `scripts/build-site.py` on every pull request and publishes it from `main` to https://dixi-project.github.io/dixi-spec-kit/. |

## Protection of `main` (ruleset)

Applied on 2026-11-08 as the `main-protegida` ruleset (default branch, no `bypass_actors`):

| Rule | Value |
|---|---|
| Deletion of `main` | Prohibited |
| Force push | Prohibited |
| Pull request | Required; threads resolved; stale reviews dismissed on push |
| Approvals | 0 while there is a single maintainer (GitHub does not allow approving your own PR). External PRs are reviewed by the maintainer before merging. Raise to 1 with CODEOWNERS when there is a second maintainer |
| Required checks | `make verify` (ubuntu/macos × Python 3.11/3.13) and `DCO sign-off`, with the branch up to date |

Check with: `gh api repos/dixi-project/dixi-spec-kit/rulesets`. Rulesets require a public repository or GitHub Pro.

## Clean history before making it public

The preparation work (with non-distributable inherited material and a PR that cannot be deleted) was archived in a separate private repository. This repository was created fresh, with `main` built from an explicit inclusion list, and before making it public `git ls-remote` was used to confirm that it contained only `main`.

## Related

- [ADR-100](../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-103](../09-architecture/adr/ADR-103-ci-publica-en-github-actions.md)
- [Publication gate](publication-readiness.md)
- [PyPI publishing](pypi-publishing.md)
- [Contributing](../CONTRIBUTING.md)
