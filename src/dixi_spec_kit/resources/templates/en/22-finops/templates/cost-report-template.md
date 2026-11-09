# Cost report template

## Purpose

Give the monthly cost review a fixed structure: what was spent, how it compares with the budget and the estimates, why it changed and what will be done.

Status: draft. {{pending: name who prepares and who reviews the report}}

Copy this file for each period, for example `cost-report-YYYY-MM.md`, and fill every placeholder. State the data source and its date; billing data can be delayed.

## Period

- Period: {{pending: month and year}}
- Prepared by / reviewed by: {{pending: roles}}
- Data source and extraction date: {{pending: source, date}}
- Currency: {{pending: currency}}

## Summary

| Metric | This period | Previous period | Budget | Variance |
|--------|-------------|-----------------|--------|----------|
| Total cost | {{pending: amount}} | {{pending: amount}} | {{pending: amount}} | {{pending: % and amount}} |
| Production | {{pending: amount}} | {{pending: amount}} | {{pending: amount}} | {{pending: variance}} |
| Non-production | {{pending: amount}} | {{pending: amount}} | {{pending: amount}} | {{pending: variance}} |
| AI usage | {{pending: amount}} | {{pending: amount}} | {{pending: amount}} | {{pending: variance}} |

## Unit costs

| Unit | This period | Previous period | Target |
|------|-------------|-----------------|--------|
| Cost per active user | {{pending: value}} | {{pending: value}} | {{pending: target}} |
| {{pending: other unit}} | {{pending: value}} | {{pending: value}} | {{pending: target}} |

## Top cost lines

| Line | Cost | Change | Owner | Explanation |
|------|------|--------|-------|-------------|
| {{pending: service or category}} | {{pending: amount}} | {{pending: %}} | {{pending: role}} | {{pending: why}} |

## Estimates versus actuals

| Item | Estimate (assumptions) | Actual | Difference | Lesson |
|------|------------------------|--------|------------|--------|
| {{pending: feature or change}} | {{pending: estimate}} | {{pending: actual}} | {{pending: difference}} | {{pending: lesson}} |

## Incidents and anomalies

{{pending: cost spikes this period, with links to their playbook records}}

## Actions

| Action | Expected saving (assumptions) | Owner | Due |
|--------|-------------------------------|-------|-----|
| {{pending: action}} | {{pending: estimate}} | {{pending: role}} | {{pending: date}} |

## Related

- [Cost strategy](../cost-strategy.md)
- [Budget alerts](../budget-alerts.md)
- [AI cost management](../ai-cost-management.md)
- [Cost spike playbook](../../15-operations/playbooks/cost-spike.md)
