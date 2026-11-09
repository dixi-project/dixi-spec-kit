# Checklist 06 — Processes

> **Evidence rule.** Score only what an artifact proves. A missing artifact is recorded as "no evidence" and scored 0; it is never filled with an assumption presented as fact.

## Purpose

Assess how work moves from idea to production and back: planning, specification, review, release, rollback, incident handling and learning. Processes count only when records show they are followed.

Status: draft. {{pending: decide the sample period for process records}}

## Inputs

- [Roadmap](../../16-product/roadmap.md) and [Feature lifecycle](../../16-product/feature-lifecycle.md)
- [Verification ladder](../../11-quality/verification-ladder.md)
- [CI/CD overview](../../14-delivery/ci-cd-overview.md), [Deployment strategy](../../14-delivery/deployment-strategy.md), [Rollback strategy](../../14-delivery/rollback-strategy.md)
- [Incident levels](../../15-operations/incident-levels.md) and [Escalation matrix](../../15-operations/escalation-matrix.md)
- [Postmortem template](../../10-engineering/templates/postmortem-template.md)
- [Decision log](../../18-knowledge-base/decision-log.md)

## Items

| ID | Question | Evidence (artifact) | Score 0–5 | Finding |
|----|----------|---------------------|-----------|---------|
| PRO-01 | Is work planned and prioritised in a visible backlog? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| PRO-02 | Are features specified with acceptance criteria before building? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| PRO-03 | Is every change traceable from requirement to test to release? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| PRO-04 | Are releases automated, frequent and reversible? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| PRO-05 | Is there an incident process with severity levels and on-call? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| PRO-06 | Are postmortems written and their actions closed? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| PRO-07 | Are decisions recorded where the team can find them? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| PRO-08 | Are delivery metrics tracked (lead time, change failure rate, recovery time)? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| PRO-09 | Is use of AI agents in development governed by documented rules? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |

## Red flags

- Releases depend on one person running manual steps.
- Incidents are fixed but never reviewed.
- No record links shipped changes to their review.

## Output

- Area score: {{pending: score and method}}
- Findings carried to the [DD report](../dd-report-template.md).

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 05 — Data management](05-data-management.md)
- [Checklist 07 — Team](07-team.md)
- [Final checklist](11-final-report.md)
