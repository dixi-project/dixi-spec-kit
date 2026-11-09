# Data Migration Playbook

## Purpose

Guide the movement or transformation of existing data: backfills, moves between stores, imports from legacy systems and restructuring. It complements the [migration strategy](migration-strategy.md), which covers schema changes.

## Pre-flight

- [ ] Source and destination identified, with owners.
- [ ] Volume measured: rows, size, growth during the migration window.
- [ ] Data quality profiled: nulls, duplicates, invalid values, orphan references.
- [ ] Mapping documented field by field, including transformations and defaults.
- [ ] Personal data identified using the [PII classification](../pii-classification.md).
- [ ] Rollback path defined before starting.
- [ ] Stakeholders informed of the window and the expected impact.

## Choosing a pattern

| Pattern | When it fits | Main risk |
| --- | --- | --- |
| One-off bulk copy | Small data, a maintenance window is acceptable | Downtime |
| Bulk copy plus backfill of changes | Medium data, short freeze is acceptable | Missed changes |
| Dual write plus backfill | Source stays live during the move | Divergence between copies |
| Continuous change capture | Large or very active data | Operational complexity |

Selected pattern: {{pending: pattern and reason}}

## Batching and idempotency

- Process in batches by a stable key; record the last processed key to resume.
- Throttle to protect live traffic: {{pending: batch size and pause between batches}}
- Each batch is idempotent: running it twice gives the same result (upsert, not insert).
- Failures in one batch are logged and retried without stopping the whole run.

## Observability during the run

| Signal | Threshold that pauses the run |
| --- | --- |
| Rows processed per minute | |
| Error rate | |
| Source and destination latency | |
| Replication lag | |

## Verification

- [ ] Row counts match between source and destination, per partition or tenant.
- [ ] Checksums or hashes match on key columns.
- [ ] A random sample is compared field by field.
- [ ] Business totals (for example sums of amounts) match.
- [ ] Reconciliation keeps running until the source is retired.

## Rollback

- During the run: stop, keep the source as the system of record, discard or mark partial data.
- After cutover: {{pending: how to switch back and how long the source is kept}}

## Plan template

| Item | Value |
| --- | --- |
| Source to destination | |
| Volume | |
| Pattern | |
| Window and cutover time | |
| Verification steps | |
| Rollback steps | |
| Owner and approver | |

Old copies created for the migration follow the [retention policy](../retention-policy.md).

## Related

- [Migration strategy](migration-strategy.md)
- [PII classification](../pii-classification.md)
- [Retention policy](../retention-policy.md)
- [Data architecture](../data-architecture.md)
