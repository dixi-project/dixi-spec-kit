# Budget alerts

## Purpose

Detect overspending early with alerts on actual and forecast cost, and make sure every alert reaches someone who can act on it.

Status: draft. {{pending: name the owner of budget alerts}}

## Alert types

| Type | Fires when | Why |
|------|-----------|-----|
| Actual threshold | Spend so far this month passes a percentage of the budget | Catches steady overspending |
| Forecast threshold | Projected month-end spend passes the budget | Warns before money is spent |
| Anomaly | Daily spend jumps well above its recent pattern | Catches sudden spikes, loops, abuse |
| Usage quota | A metered resource (AI tokens, API calls, storage) passes a limit | Catches cost that billing reports late |

## Thresholds

| Scope | Budget | Actual alerts | Forecast alert | Recipients |
|-------|--------|---------------|----------------|------------|
| Whole project | {{pending: amount}} | {{pending: e.g. 50%, 80%, 100%}} | {{pending: e.g. 100%}} | {{pending: roles, e.g. finops@example.com}} |
| Production | {{pending: amount}} | {{pending: thresholds}} | {{pending: threshold}} | {{pending: roles}} |
| Non-production | {{pending: amount}} | {{pending: thresholds}} | {{pending: threshold}} | {{pending: roles}} |
| AI usage | {{pending: amount}} | {{pending: thresholds}} | {{pending: threshold}} | {{pending: roles}} |

The percentages are examples. Choose values that leave time to react.

## Routing

- Informational thresholds go to a cost channel or e-mail.
- 100% actual, forecast over budget and anomalies also notify the cost owner directly.
- An anomaly above {{pending: amount or percent}} opens the [cost spike playbook](../15-operations/playbooks/cost-spike.md).

## Hard limits

{{pending: decide where spending is capped automatically (quotas, rate limits) and where only alerts are used}}

Hard limits protect against runaway cost but can cause outages. Use them for non-production, experiments and public endpoints that call paid APIs; prefer alerts for production paths users depend on.

## Hygiene

- Every alert has an owner and a documented action.
- Test the alert path once by lowering a threshold in a sandbox.
- Remove alerts nobody acts on; replace them with useful ones.
- Billing data is often delayed by hours; usage quotas close that gap.

## Related

- [Cost strategy](cost-strategy.md)
- [AI cost management](ai-cost-management.md)
- [Cost spike playbook](../15-operations/playbooks/cost-spike.md)
- [Cost report template](templates/cost-report-template.md)
