# Zero-Downtime Migrations

## Purpose

Describe how to change schemas and data while the system keeps serving traffic. It applies when maintenance windows are not acceptable and builds on the [migration strategy](migration-strategy.md).

- Availability target that requires this: {{pending: availability objective and acceptable degradation during migrations}}

## Compatibility rule

At any moment, the running application versions (old and new, during a rolling deployment) must work with the current schema. Therefore:

- Schema changes are backward compatible with the previous application version.
- Application changes are compatible with both the previous and the next schema.

## Change matrix

| Change | Blocking risk | Zero-downtime technique |
| --- | --- | --- |
| Add column with default | Table rewrite on some engines | Add nullable, set default for new rows, backfill in batches |
| Add required constraint | Full scan with lock | Add a not-validated check, backfill, validate separately |
| Add foreign key | Lock on both tables | Add not validated, validate later |
| Create index | Writes blocked | Non-blocking index creation if supported |
| Rename column or table | Breaks old version | Expand and contract with dual write |
| Split or merge tables | Breaks readers | New structure, dual write, shadow reads, switch, retire |

## Application-level techniques

- **Feature flags**: switch reads and writes to the new structure without a deployment, and switch back fast.
- **Dual write**: write to old and new structures; decide which is authoritative and how divergence is detected.
- **Shadow reads**: read from both, serve the old result, compare and log differences until they reach zero.
- **Change capture**: stream changes from the source to the destination when dual write in code is not practical.

## Multi-tenant rollout

| Approach | Description | Decision |
| --- | --- | --- |
| Per tenant | Migrate tenants in waves, starting with internal or low-risk ones | {{pending: choose approach}} |
| All at once | One change for everyone, only for small and safe changes | |

## Anti-patterns

- Renaming in place in a single deployment.
- Long transactions that hold locks during a backfill.
- Dropping the old structure in the same release that stops using it.
- Backfills without throttling during peak traffic.

## Checklist per schema change

- [ ] Lock behaviour of each statement is known for the chosen engine.
- [ ] Statement timeouts and lock timeouts are set for the migration session.
- [ ] Both application versions were tested against the new schema.
- [ ] Backfill is batched, idempotent and resumable (see the [data migration playbook](data-migration-playbook.md)).
- [ ] Metrics to watch and abort criteria are defined.
- [ ] Contract phase is scheduled, with an owner.

## Related

- [Migration strategy](migration-strategy.md)
- [Data migration playbook](data-migration-playbook.md)
- [Data architecture](../data-architecture.md)
- [Test plan](../../11-quality/test-plan.md)
