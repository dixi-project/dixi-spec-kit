# Performance test plan

## Purpose

Plan how the project checks that it meets its performance budgets under realistic load, before users find the limits. This plan describes intended tests; it is not a record of executed tests.

Status: draft. {{pending: confirm the performance test scope and environment}}

## Objectives

- Confirm the [API latency budgets](performance-budgets/api-latency-budgets.md) and [web vitals budgets](performance-budgets/web-vitals-budgets.md).
- Find the capacity limit and how the system fails beyond it.
- Detect performance regressions between releases.

## Test types

| Type | Question it answers | Load profile | When |
|------|---------------------|--------------|------|
| Baseline | How does one user experience the system? | Single user | {{pending: when}} |
| Load | Does it meet budgets at expected traffic? | {{pending: expected traffic}} | {{pending: when}} |
| Stress | Where does it break, and how? | Increasing until failure | {{pending: when}} |
| Soak | Does it degrade over time? | Expected traffic for hours | {{pending: when}} |
| Spike | Does it survive sudden bursts? | Short bursts above expected | {{pending: when}} |

## Scenarios

| Scenario | Endpoint or journey | Share of traffic | Data needs |
|----------|---------------------|------------------|------------|
| {{pending: scenario}} | {{pending: endpoint}} | {{pending: share}} | {{pending: data}} |

## Environment

- {{pending: where tests run and how close it is to production}}
- Use generated data; never load test with real personal data.
- Never run load tests against systems you do not own or without permission.

## Pass criteria

A run passes when all budgets hold at the target load and error rate stays within {{pending: error budget}}. Results that miss a budget are investigated; budgets are not relaxed to make a run pass.

## Reporting

Record date, version, environment, load profile, results per scenario and open issues.

## Related

- [API latency budgets](performance-budgets/api-latency-budgets.md)
- [Web vitals budgets](performance-budgets/web-vitals-budgets.md)
- [Non-functional requirements](non-functional-requirements.md)
- [Regression plan](regression-plan.md)
