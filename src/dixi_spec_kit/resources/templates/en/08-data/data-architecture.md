# Data Architecture

## Purpose

Describe where the project's data lives, how it moves and who owns each part. This is the map that the canonical model, the ERD and the migration documents refer to.

- Owner: {{pending: person or role accountable for the data architecture}}

## Data stores

| Store | Kind (relational, document, key-value, search, object, queue) | Purpose | Owner module | Classification ceiling |
| --- | --- | --- | --- | --- |
| {{pending: primary store}} | | System of record | | |
| | | Cache | | |
| | | Search index | | |
| | | Files and media | | |

Choose store kinds by access pattern, not by habit. Record the choice in an architecture decision.

## Ownership rules

- [ ] Each entity has exactly one owning module that writes it.
- [ ] Other modules read through contracts (API, events), not through direct table access.
- [ ] Derived stores (caches, indexes, reports) can be rebuilt from the system of record.
- [ ] Cross-module joins in the database are avoided or explicitly approved.

## Data flows

| Flow | Source | Destination | Mechanism (sync call, event, batch, CDC) | Frequency | Consistency |
| --- | --- | --- | --- | --- | --- |
| | | | | | {{pending: strong or eventual}} |

## Multi-tenancy

{{pending: tenancy model, for example single tenant, shared schema with tenant column, schema per tenant or database per tenant}}

- Isolation is enforced at: {{pending: application layer, database policies or both}}
- Every query on tenant data filters by tenant; tests cover cross-tenant access.

## Consistency and transactions

- Transactions stay inside one owning module.
- Cross-module workflows use events or sagas with compensating actions.
- Idempotency keys protect operations that can be retried.

## Backup and recovery

| Store | Backup frequency | Recovery point objective | Recovery time objective | Restore tested |
| --- | --- | --- | --- | --- |
| | {{pending: frequency}} | | | {{pending: date of last restore exercise}} |

## Sizing and growth

| Store | Current size | Expected growth | Partitioning or archiving plan |
| --- | --- | --- | --- |
| | | | |

## Related

- [Canonical data model](canonical-data-model.md)
- [ERD overview](models/erd-overview.md)
- [Migration strategy](migrations/migration-strategy.md)
- [PII classification](pii-classification.md)
- [Retention policy](retention-policy.md)
- [Audit fields standard](audit-fields-standard.md)
