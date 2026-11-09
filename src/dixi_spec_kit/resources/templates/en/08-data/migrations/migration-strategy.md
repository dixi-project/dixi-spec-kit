# Migration Strategy

## Purpose

Set the rules for changing database schemas safely: how migrations are written, reviewed, applied and reverted. Schema changes are code changes and follow the same discipline.

- Migration tool: {{pending: migration tool and where migration files live}}
- Who can apply migrations in production: {{pending: role or pipeline step}}

## Principles

- Migrations are versioned, ordered and stored in the repository.
- A migration is never edited after it has been applied to a shared environment; write a new one.
- Schema changes and application changes are deployable independently.
- Prefer small, reversible steps over one large change.
- Destructive steps (drop, narrowing type changes) come last, after a verification period.

## Expand and contract

1. **Expand**: add the new structure (column, table, index) without removing the old one.
2. **Migrate**: write to both, backfill existing data, then switch reads.
3. **Contract**: remove the old structure once nothing uses it.

Each phase is a separate deployment.

## Decisions by type of change

| Change | Safe approach | Reversible |
| --- | --- | --- |
| Add nullable column | Single migration | Yes |
| Add required column | Add nullable, backfill, then add constraint | Yes, until contract |
| Rename column | Expand and contract, never in place | Yes, until contract |
| Drop column | Stop using it, wait one release, then drop | No |
| Change column type | New column, backfill, switch, drop old | Partly |
| Add index on large table | Non-blocking creation if the engine supports it | Yes |
| Add constraint | Add as not validated, then validate | Yes |

## Workflow

- [ ] Describe the change and its phases in the feature or module spec.
- [ ] Write the migration and its rollback.
- [ ] Run it against a copy with realistic volume and record the duration.
- [ ] Review: locking, duration, backward compatibility, data loss.
- [ ] Apply in lower environments, then production, through the pipeline.
- [ ] Verify with queries defined in advance.

## Rollback

{{pending: rollback approach, for example down migrations, forward fixes only, or restore from backup}}

## Migration record

| Field | Value |
| --- | --- |
| Goal | |
| Phases | |
| Expected duration and locks | |
| Rollback plan | |
| Verification queries | |
| Owner | |

For data moves (not only schema), use the [data migration playbook](data-migration-playbook.md).

## Related

- [Data migration playbook](data-migration-playbook.md)
- [Data architecture](../data-architecture.md)
- [Canonical data model](../canonical-data-model.md)
- [Test plan](../../11-quality/test-plan.md)
