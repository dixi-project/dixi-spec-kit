# Checklist 05 — Data management

> **Evidence rule.** Score only what an artifact proves. A missing artifact is recorded as "no evidence" and scored 0; it is never filled with an assumption presented as fact.

## Purpose

Assess whether the project knows what data it holds, where, why and for how long; whether data is modelled, migrated and backed up safely; and whether personal data is handled according to documented rules.

Status: draft. {{pending: confirm which datastores and data flows are in scope}}

## Inputs

- [Data architecture](../../08-data/data-architecture.md) and [Canonical data model](../../08-data/canonical-data-model.md)
- [PII classification](../../08-data/pii-classification.md) and [Retention policy](../../08-data/retention-policy.md)
- [Audit fields standard](../../08-data/audit-fields-standard.md)
- [Migration strategy](../../08-data/migrations/migration-strategy.md)
- [Backup and recovery](../../14-delivery/backup-and-recovery.md)
- [GDPR readiness](../../23-compliance/gdpr/gdpr-readiness.md), when personal data is in scope

## Items

| ID | Question | Evidence (artifact) | Score 0–5 | Finding |
|----|----------|---------------------|-----------|---------|
| DAT-01 | Is there an inventory of datastores, owners and data categories? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| DAT-02 | Is personal and sensitive data classified at field level? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| DAT-03 | Are retention periods defined and deletion automated? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| DAT-04 | Is the data model documented and consistent across services? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| DAT-05 | Are schema migrations versioned, reviewed and reversible? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| DAT-06 | Are records auditable (who changed what and when)? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| DAT-07 | Is production data kept out of development and test environments? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| DAT-08 | Can a data subject request (export, erasure) be fulfilled end to end? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| DAT-09 | Is data quality monitored for critical entities? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| DAT-10 | Are data locations and transfers known and recorded? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |

## Red flags

- Nobody can list where personal data is stored.
- Copies of production data in laptops or shared drives.
- Deletion promised to users but not implemented.

## Output

- Area score: {{pending: score and method}}
- Findings carried to the [DD report](../dd-report-template.md).

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 04 — Security](04-security.md)
- [Checklist 06 — Processes](06-processes.md)
- [Final checklist](11-final-report.md)
