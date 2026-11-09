# Observability Strategy

## Purpose

Explain how the team will know what the system is doing in production: which signals are collected, how they are correlated and who looks at them. This document sets the rules; the catalogs in this area hold the details.

## Signals

| Signal | Answers | Detail in |
|---|---|---|
| Metrics | Is it healthy? How much, how fast? | [Metrics catalog](metrics-catalog.md) |
| Logs | What happened in this specific event? | [Logging map](logging-map.md) |
| Traces | Where did the time go across components? | Tracing strategy (platform profile) |
| Health checks | Is it up right now? | [Alerting rules](alerting-rules.md) |

## Decisions

- Instrumentation standard: {{pending: prefer an open, vendor-neutral standard; record in an ADR}}
- Telemetry backend: {{pending: decide and record in an ADR}}
- Retention per signal: {{pending: days for metrics, logs and traces}}
- Sampling policy: {{pending: what share of traces is kept and which are always kept}}
- Budget for telemetry: {{pending: monthly limit and who watches it}}

## Required attributes

Every signal carries the same identifying attributes so they can be joined:

- `service.name`: the component that emits it.
- `service.version`: the commit identifier of the deployed build.
- `deployment.environment`: local, staging or production.
- A correlation or trace identifier propagated across calls and queues.

## Endpoints every service exposes

- A health endpoint that answers quickly and does not depend on slow downstreams.
- A version endpoint that returns the same commit identifier as `service.version`.

## Rules

- No secrets, tokens or personal data in any signal; mask before emitting.
- Instrument the main business flow first, then the rest.
- Dashboards and alerts are versioned next to the code when the tooling allows it.
- Each new service completes the checklist below before reaching production.

## New service checklist

- [ ] Required attributes present in metrics, logs and traces
- [ ] Health and version endpoints exposed
- [ ] Structured logs with a correlation identifier
- [ ] Rate, errors and duration metrics for its entry points
- [ ] At least one indicator in [SLIs, SLOs and SLAs](slis-slos-slas.md)
- [ ] Alerts with a runbook, following [alerting rules](alerting-rules.md)
- [ ] An entry in the [dashboard map](dashboard-map.md)

## Related

- [Runbooks](runbooks/README.md)
- [Logging standard](../10-engineering/logging-standard.md)
- [Non-functional requirements](../11-quality/non-functional-requirements.md)
- [Continuous verification](../14-delivery/continuous-verification.md)
- [Project](../00-master-spec.md)
