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

## Checks cancelled while waiting for a runner

A required check can end as cancelled without having run a single step. The cause is on GitHub's side: when no hosted runner takes the job in about fifteen minutes, GitHub cancels it with the annotation "The job was not acquired by Runner of type hosted even after multiple attempts", often next to a notice about capacity constraints of the macOS arm64 runners. It happened with the `make verify` jobs on `macos-latest` on 2026-11-12 and again on 2026-11-13.

The workflow cannot prevent it: `timeout-minutes` does not count while a job waits for a runner, only once it runs. The matrix job has a limit of 30 minutes, which cancels a job that hangs; raising it from 15 did not avoid these cancellations, as first assumed in TASK-027.

When it happens, nothing is wrong with the change: open the run in the Actions tab and choose "Re-run failed jobs". Only the cancelled jobs run again, and the pull request can be merged when they pass. If macOS capacity makes this frequent, the alternative is to stop requiring the macOS checks in the ruleset, a decision of the maintainers.

## Clean history before making it public

The preparation work (with non-distributable inherited material and a PR that cannot be deleted) was archived in a separate private repository. This repository was created fresh, with `main` built from an explicit inclusion list, and before making it public `git ls-remote` was used to confirm that it contained only `main`.

## Related

- [ADR-100](../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-103](../09-architecture/adr/ADR-103-ci-publica-en-github-actions.md)
- [Publication gate](publication-readiness.md)
- [PyPI publishing](pypi-publishing.md)
- [Contributing](../CONTRIBUTING.md)
