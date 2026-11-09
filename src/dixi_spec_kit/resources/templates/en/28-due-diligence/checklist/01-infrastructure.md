# Checklist 01 — Infrastructure

> **Evidence rule.** Score only what an artifact proves. A missing artifact is recorded as "no evidence" and scored 0; it is never filled with an assumption presented as fact.

## Purpose

Assess whether the infrastructure is defined, reproducible, observable, recoverable and affordable, using the scale in the [DD strategy](../dd-strategy.md).

Status: draft. {{pending: confirm which environments and hosting accounts are in scope}}

## Inputs

- [Deployment architecture](../../09-architecture/deployment-architecture.md)
- [Environments](../../14-delivery/environments.md) and [Infrastructure modules](../../14-delivery/infra-modules.md)
- [Backup and recovery](../../14-delivery/backup-and-recovery.md), [DR strategy](../../14-delivery/disaster-recovery/dr-strategy.md), [RTO/RPO matrix](../../14-delivery/disaster-recovery/rto-rpo-matrix.md)
- [Observability strategy](../../12-observability/observability-strategy.md) and [SLIs, SLOs and SLAs](../../12-observability/slis-slos-slas.md)
- [Cost strategy](../../22-finops/cost-strategy.md)

## Items

| ID | Question | Evidence (artifact) | Score 0–5 | Finding |
|----|----------|---------------------|-----------|---------|
| INF-01 | Is all infrastructure defined as code and reviewed like application code? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| INF-02 | Are environments separated, with production access restricted? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| INF-03 | Can an environment be rebuilt from the repository alone? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| INF-04 | Are backups automatic, encrypted and restore-tested with records? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| INF-05 | Are recovery objectives defined and exercised? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| INF-06 | Are metrics, logs and alerts in place for critical paths? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| INF-07 | Are service level objectives defined and measured? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| INF-08 | Is capacity planned and scaling tested? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| INF-09 | Is cost visible per environment or component, with alerts? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| INF-10 | Is there a single point of failure or a single person who holds access? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |

## Red flags

- Production changed by hand with no record.
- Backups never restored.
- Root or owner credentials shared or held by one person only.

## Output

- Area score: {{pending: score and method}}
- Findings carried to the [DD report](../dd-report-template.md).

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 02 — Architecture](02-architecture.md)
- [Final checklist](11-final-report.md)
