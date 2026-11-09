# Release Pipeline

## Purpose

Describe how a verified artifact is promoted to staging and then to production. Promotion to production always waits for a human approval; nothing is deployed to production automatically.

## Input

An artifact produced by the build pipeline from a commit on the main branch, with `make verify` green.

## Stages

| # | Stage | Action | Gate to continue |
|---|---|---|---|
| 1 | Prepare | Collect artifact, release notes and migration plan | Artifact exists and matches the commit |
| 2 | Migrate staging | Run the migration pipeline against staging | Migrations succeed |
| 3 | Deploy staging | Deploy the artifact | Deployment healthy |
| 4 | Verify staging | Version check, smoke checks, `make verify` result attached | All pass |
| 5 | Approval | A person reviews evidence and approves | **Explicit human approval recorded** |
| 6 | Migrate production | Run the migration pipeline against production | Migrations succeed |
| 7 | Deploy production | Deploy using the chosen strategy | Deployment healthy |
| 8 | Bake | Watch errors and latency for the new version | No alerts during bake time |
| 9 | Close | Mark the release as done, keep the previous artifact | n/a |

If any gate fails, the pipeline stops; after stage 7, a failure triggers the rollback procedure.

## Approval

- Approvers: {{pending: roles}}; the author of the change cannot be the only approver.
- Evidence shown to the approver: commit, release notes, `make verify` result, staging checks.
- Approval expires after {{pending: hours}}; a new approval is needed after that.
- Agents may prepare the release (for example with `/dixi.release`) but never approve it.

## Release notes

- Generated from merged pull requests, reviewed by a person.
- Include: user-facing changes, migrations, flags, known risks and rollback notes.
- Version scheme: {{pending: semantic versioning, date-based or other}}.

## Blocked windows

{{pending: periods when production releases are not allowed, and who can grant exceptions}}

## Related

- [Build pipeline](build-pipeline.md)
- [Migration pipeline](migration-pipeline.md)
- [Deployment strategy](../deployment-strategy.md)
- [Rollback strategy](../rollback-strategy.md)
- [Continuous verification](../continuous-verification.md)
