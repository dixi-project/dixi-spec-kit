# Master Data

## Purpose

Identify the reference and master data shared across modules (catalogues, organisations, locations, currencies, categories), name the single source for each and define how changes are governed and distributed.

- Data steward: {{pending: person or role accountable for master data quality}}

## Master and reference data inventory

| Dataset | Type (master or reference) | System of record | Owner | Consumers | Update frequency |
| --- | --- | --- | --- | --- | --- |
| Countries | Reference | Standard list (ISO 3166-1) | | | Rare |
| Currencies | Reference | Standard list (ISO 4217) | | | Rare |
| Languages | Reference | Standard tags (BCP 47) | | | Rare |
| {{pending: core master dataset, for example products or organisations}} | Master | | | | |

## Governance rules

- [ ] Each dataset has one system of record; other copies are read-only replicas.
- [ ] Identifiers are stable and never reused, even after deactivation.
- [ ] Records are deactivated, not deleted, when other data references them.
- [ ] Translatable labels exist for every supported language.
- [ ] Changes go through: {{pending: approval flow for master data changes}}

## Distribution

| Mechanism | When it fits | Used for |
| --- | --- | --- |
| Read API from the owner | Low volume, needs fresh data | |
| Change events | Consumers keep a local copy | |
| Periodic snapshot | Analytics, large datasets | |

Consumers must tolerate unknown or new values without failing.

## Data quality

| Rule | Dataset | Check | Frequency | Action on failure |
| --- | --- | --- | --- | --- |
| No duplicates by natural key | | | | |
| Mandatory attributes present | | | | |
| References resolve | | | | |

## Matching and deduplication

{{pending: how duplicates are detected and merged, and who approves merges}}

- Merges keep a mapping from old to surviving identifiers.
- Merges are audited according to the [audit fields standard](audit-fields-standard.md).

## Related

- [Canonical data model](canonical-data-model.md)
- [Reporting dimensions](reporting-dimensions.md)
- [Data architecture](data-architecture.md)
- [Audit fields standard](audit-fields-standard.md)
