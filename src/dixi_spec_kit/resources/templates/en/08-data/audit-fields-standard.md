# Audit Fields Standard

## Purpose

Define the standard fields that every persistent entity carries to answer who created or changed a record, when, and from where. A single convention makes troubleshooting, compliance reviews and data migrations predictable.

- Scope: {{pending: which stores and entities must follow this standard}}

## Standard fields

| Field | Type | Required | Set by | Description |
| --- | --- | --- | --- | --- |
| `id` | {{pending: identifier type, for example UUID or ULID}} | Yes | Application | Stable, non-reusable identifier |
| `created_at` | Timestamp with time zone (UTC) | Yes | Persistence layer | Creation instant |
| `created_by` | Actor reference | Yes | Application | User, service or job that created the record |
| `updated_at` | Timestamp with time zone (UTC) | Yes | Persistence layer | Last modification instant |
| `updated_by` | Actor reference | Yes | Application | Last actor that modified the record |
| `deleted_at` | Timestamp, nullable | If soft delete is used | Application | Logical deletion instant |
| `version` | Integer | {{pending: yes or no}} | Persistence layer | Optimistic concurrency counter |
| `tenant_id` | Reference | If multi-tenant | Application | Owning tenant |

## Rules

- [ ] Timestamps are stored in UTC; conversion to local time happens only in presentation.
- [ ] Actor references point to a stable identifier, never to a name or e-mail.
- [ ] System actors (jobs, integrations) have their own identifiers, distinct from users.
- [ ] Audit fields are not editable through public APIs.
- [ ] Soft-deleted records are excluded from default queries and follow the [retention policy](retention-policy.md).
- [ ] Field names are consistent across all stores: {{pending: naming convention, for example snake_case}}

## Change history

Audit fields show the last change only. Decide whether a full history is needed:

| Option | When it fits | Decision |
| --- | --- | --- |
| Last change only | Low-risk data | {{pending: choose per entity category}} |
| History table per entity | Need to see previous values | |
| Append-only audit log | Regulated actions, security events | |

Audit logs must not copy Sensitive values in clear text; see the [PII classification](pii-classification.md).

## Audited actions

| Action | Entity | Recorded data | Retention |
| --- | --- | --- | --- |
| Login / logout | Session | Actor, time, origin | {{pending: period}} |
| Permission change | Role, user | Actor, before, after | |
| Data export | | | |

## How to verify

- Module specs reference this standard instead of redefining fields (see the [module spec example](../04-modules/example/module-spec.md)).
- `dixi check` and `/dixi.data` or `$dixi-data` can be used to review new entities against this list.

## Related

- [PII classification](pii-classification.md)
- [Retention policy](retention-policy.md)
- [Module spec example](../04-modules/example/module-spec.md)
- [Test plan](../11-quality/test-plan.md)
