# Cost strategy

## Purpose

Set the principles for spending on infrastructure, vendors and AI usage, so that cost is a design input from the start and every important cost has an owner.

Status: draft. {{pending: name the owner of the cost strategy}}

## Principles

1. **Cost is a requirement.** Every feature spec states its expected running cost when it is not trivial.
2. **Every cost has an owner.** A line on the bill without an owner is investigated and either assigned or removed.
3. **Estimate before building.** Estimates list their assumptions and source (vendor price page, past bills, load test), and a date.
4. **Measure after shipping.** Compare the estimate with the real cost after {{pending: weeks}} and record the difference.
5. **Optimise where it matters.** Spend effort on the largest lines first; small savings that add complexity are not worth it.
6. **Unit cost over total cost.** Track cost per user, per request or per tenant, so growth and waste can be told apart.

## Budget

| Scope | Monthly budget | Owner | Alert thresholds |
|-------|----------------|-------|------------------|
| Whole project | {{pending: amount and currency}} | {{pending: role}} | See [budget alerts](budget-alerts.md) |
| Production | {{pending: amount}} | {{pending: role}} | {{pending: thresholds}} |
| Non-production | {{pending: amount}} | {{pending: role}} | {{pending: thresholds}} |
| AI usage | {{pending: amount}} | {{pending: role}} | See [AI cost management](ai-cost-management.md) |

No amount in this document is a recommendation; each one is a project decision.

## Estimate format

| Item | Assumption | Unit price (source, date) | Quantity | Monthly estimate |
|------|------------|---------------------------|----------|------------------|
| {{pending: e.g. compute for API}} | {{pending: e.g. 2 instances, always on}} | {{pending: price, source, date}} | {{pending: quantity}} | {{pending: result}} |

## Decisions that need a cost note

- Choosing or changing a vendor or a hosting model.
- Adding a new environment, region or always-on resource.
- Adding or changing an AI model, or a feature that calls one per user action.
- Raising retention for logs, backups or analytics data.

## Review rhythm

- Monthly cost review with the [cost report template](templates/cost-report-template.md).
- Quarterly review of this strategy and the budget. {{pending: confirm the participants}}

You can use `/dixi.finops` (Claude Code) or `$dixi-finops` (Codex) to prepare the review; a person approves decisions.

## Related

- [Budget alerts](budget-alerts.md)
- [AI cost management](ai-cost-management.md)
- [Cost report template](templates/cost-report-template.md)
- [Cost spike playbook](../15-operations/playbooks/cost-spike.md)
- [Project](../00-master-spec.md)
