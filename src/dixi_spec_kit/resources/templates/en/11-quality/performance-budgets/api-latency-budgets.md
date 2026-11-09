# API latency budgets

## Purpose

Set latency and error budgets for the project's APIs so that slow or failing endpoints are detected as regressions, not discovered by users.

Status: draft. {{pending: decide the budgets per endpoint group}}

## Budgets

| Endpoint group | Example | p50 | p95 | p99 | Error rate |
|----------------|---------|-----|-----|-----|------------|
| Reads | {{pending: endpoint}} | {{pending: ms}} | {{pending: ms}} | {{pending: ms}} | {{pending: %}} |
| Writes | {{pending: endpoint}} | {{pending: ms}} | {{pending: ms}} | {{pending: ms}} | {{pending: %}} |
| Search or listing | {{pending: endpoint}} | {{pending: ms}} | {{pending: ms}} | {{pending: ms}} | {{pending: %}} |
| Background or async | {{pending: job}} | {{pending: ms}} | {{pending: ms}} | {{pending: ms}} | {{pending: %}} |

Example only, not a recommendation: a team might start by measuring current latency and setting budgets slightly above it, then tighten over time.

## Conditions

Budgets apply under stated conditions; record them so results are comparable.

- Load: {{pending: requests per second or concurrent users}}
- Payload size: {{pending: typical and maximum}}
- Measured from: {{pending: client, gateway or service}}
- Excluded: {{pending: for example cold starts, if justified}}

## Asynchronous work

For queued or event-driven work, budget the time from message published to work completed, and the maximum queue depth. {{pending: async budgets}}

## Checks

- Performance tests in the [performance test plan](../performance-test-plan.md) verify these budgets.
- {{pending: whether production monitoring alerts on budget breaches}}

## When a budget is exceeded

Find the cause and fix it. Raising a budget needs a recorded decision by the responsible person, with a reason; it is never done to make a run pass.

## Related

- [Performance test plan](../performance-test-plan.md)
- [Web vitals budgets](web-vitals-budgets.md)
- [Non-functional requirements](../non-functional-requirements.md)
- [Contract](../../07-contracts/example.md)
