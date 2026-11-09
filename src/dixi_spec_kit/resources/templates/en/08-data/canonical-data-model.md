# Canonical Data Model

## Purpose

Define the shared business entities, their meaning and their canonical representation, so that modules, contracts and reports use the same names and the same semantics. The canonical model is the vocabulary; each module may store data differently, but it translates to this model at its boundaries.

- Owner: {{pending: person or role accountable for the canonical model}}

## Entities

| Entity | Definition (one sentence) | Owning module | Identifier | Lifecycle states |
| --- | --- | --- | --- | --- |
| {{pending: core entity}} | | | | |
| | | | | |

Definitions use business language from the domain specs, not technical terms.

## Attribute conventions

| Concern | Convention |
| --- | --- |
| Identifiers | {{pending: format, for example UUID, ULID or prefixed string}} |
| Dates and times | ISO 8601, UTC |
| Money | Amount in minor units plus ISO 4217 currency code |
| Language and locale | BCP 47 tags, for example `es`, `en`, `pt-BR` |
| Country | ISO 3166-1 alpha-2 |
| Enumerations | Uppercase snake case; unknown values are rejected |
| Translatable text | Stored per locale, never a single hardcoded language |
| Booleans | Positive names (`is_active`, not `is_not_disabled`) |

## Entity detail template

Copy this block for each entity.

### {{pending: entity name}}

| Attribute | Type | Required | Classification | Description |
| --- | --- | --- | --- | --- |
| `id` | | Yes | Internal | |
| | | | | |

- Invariants: {{pending: rules that must always hold}}
- Relationships: see the [ERD overview](models/erd-overview.md).
- Audit fields: follow the [audit fields standard](audit-fields-standard.md).
- Personal fields: classified in the [PII classification](pii-classification.md).

## Mapping to contracts

| Entity | Contract | Representation differences |
| --- | --- | --- |
| | [Contract example](../07-contracts/example.md) | |

## Change rules

- [ ] Adding an optional attribute is backward compatible.
- [ ] Renaming or removing an attribute requires a deprecation period and a migration plan.
- [ ] Changing the meaning of an attribute is treated as a new attribute.
- [ ] Every change updates contracts and tests in the same change set.

## Related

- [Data architecture](data-architecture.md)
- [ERD overview](models/erd-overview.md)
- [Audit fields standard](audit-fields-standard.md)
- [PII classification](pii-classification.md)
- [Contract example](../07-contracts/example.md)
- [Domain spec example](../03-domains/example/domain-spec.md)
