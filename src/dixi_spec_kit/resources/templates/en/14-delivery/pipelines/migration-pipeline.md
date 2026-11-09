# Migration Pipeline

## Purpose

Describe how database schema and data migrations are applied safely, in order and with a way back. Migrations run as part of a release, never by hand against production.

## Rules

- Migrations are versioned files in the repository, applied in order and recorded in the database.
- Each migration is backward compatible with the version currently running (expand, migrate, contract).
- Destructive steps (drop column, drop table) ship in a later release, after no code uses the old structure.
- Large data backfills run in batches and can be paused and resumed.
- No migration contains secrets or real personal data.

## Steps

| # | Step | Action | Gate |
|---|---|---|---|
| 1 | Verify | `make verify` and migration tests on a fresh database | All pass |
| 2 | Dry run | Apply to a copy with a realistic volume of synthetic data | Completes within {{pending: minutes}} |
| 3 | Backup point | Confirm a recent backup or snapshot exists | Backup newer than {{pending: hours}} |
| 4 | Staging | Apply to staging | Succeeds; application healthy |
| 5 | Approval | Included in the production release approval | **Human approval recorded** |
| 6 | Production | Apply to production with a lock timeout of {{pending: seconds}} | Succeeds; application healthy |

## Locks and timing

- Set a lock timeout so a migration fails fast instead of blocking traffic.
- Build indexes without blocking writes when the database supports it.
- Long migrations run in {{pending: low-traffic window}}.

## Rollback

- Each migration states whether it can be reversed and how.
- Irreversible migrations require a restore plan written before approval.
- Prefer rolling the application back while keeping an expanded schema over reversing a migration.

## Decisions

- Migration tool: {{pending: decide and record in an ADR}}
- Who can run a manual migration in an emergency: {{pending: roles and break-glass process}}

## Related

- [Migration strategy](../../08-data/migrations/migration-strategy.md)
- [Data migration playbook](../../08-data/migrations/data-migration-playbook.md)
- [Release pipeline](release-pipeline.md)
- [Backup and recovery](../backup-and-recovery.md)
