# Checklist 08 — Financial (technology)

> **Evidence rule.** Score only what an artifact proves. A missing artifact is recorded as "no evidence" and scored 0; it is never filled with an assumption presented as fact. Do not estimate figures to fill gaps; take them from billing exports or accounting records.

## Purpose

Assess the technology side of the finances: what the product costs to run, how that cost scales with use, which commitments exist, and whether spending is visible and controlled. Corporate finance is out of scope unless the DD type requires it.

Status: draft. {{pending: decide which cost data may be shared and at what granularity}}

## Inputs

- [Cost strategy](../../22-finops/cost-strategy.md)
- [Budget alerts](../../22-finops/budget-alerts.md)
- [AI cost management](../../22-finops/ai-cost-management.md), when AI features exist
- [Cost report template](../../22-finops/templates/cost-report-template.md)
- [Pricing rules](../../01-business/rules/pricing-rules.md) and [Strategic goals](../../01-business/strategic-goals.md)
- [Vendor catalogue](../../15-operations/vendor-management/vendor-catalog.md)

## Items

| ID | Question | Evidence (artifact) | Score 0–5 | Finding |
|----|----------|---------------------|-----------|---------|
| FIN-01 | Is the monthly run cost known per environment and major component? | {{pending: link to billing export}} | {{pending: score}} | {{pending: finding}} |
| FIN-02 | Is unit cost known (per customer, transaction or active user)? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| FIN-03 | Does cost scale predictably with usage, and is that modelled? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| FIN-04 | Are budgets and alerts in place, and were past alerts acted on? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| FIN-05 | Are long-term commitments and licences listed with renewal dates? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| FIN-06 | Are usage-based costs (e.g. AI models, messaging) capped or monitored? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| FIN-07 | Is there a cost owner who reviews spend on a schedule? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| FIN-08 | Is the cost of known technical debt or remediation estimated with a stated method? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |

## Red flags

- No one can state the current monthly cost from records.
- Unbounded usage-based spend with no alert.
- Critical services paid from personal accounts or cards.

## Output

- Area score: {{pending: score and method}}
- Findings carried to the [DD report](../dd-report-template.md).

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 07 — Team](07-team.md)
- [Checklist 09 — Vendors and partners](09-vendors-partners.md)
- [Final checklist](11-final-report.md)
