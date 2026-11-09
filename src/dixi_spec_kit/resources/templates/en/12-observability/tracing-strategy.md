# Tracing Strategy

## Purpose

Define how a single request or message is followed across services, queues and scheduled jobs, so the team can find where time and errors happen in a distributed system.

## Decisions

- Context propagation format: {{pending: an open standard such as W3C Trace Context; record in an ADR}}
- Instrumentation approach: {{pending: automatic, manual or mixed per stack}}
- Collector or agent topology: {{pending: sidecar, per host or central}}
- Trace backend: {{pending: decide and record in an ADR}}

## Propagation

- Inbound HTTP: read the incoming context; start a new trace only when none exists or the caller is untrusted.
- Outbound HTTP: inject the context into every call to internal services.
- Queues and events: write the context into message headers on publish and continue it on consume, as a link or child span.
- Scheduled jobs: start a new trace per run and record the job name.
- Never propagate context to third parties unless agreed; it can leak internal identifiers.

## Span conventions

| Span | Name pattern | Required attributes |
|---|---|---|
| HTTP server | `METHOD /route/template` | route, status code |
| HTTP client | `METHOD host` | target service, status code |
| Database | operation and table | system, operation (no full statements with values) |
| Message publish or consume | `queue publish` / `queue process` | queue name, message ID |

Do not put personal data, secrets or full payloads in span attributes.

## Sampling

- Default rate: {{pending: percentage of traces kept}}
- Always keep: errors, slow requests above {{pending: threshold}} and traces for synthetic checks.
- Decision point: {{pending: head-based, tail-based or both}}

## Correlation

- Logs include the trace identifier so a trace links to its log lines.
- Metrics can carry exemplars that point to a sample trace, if the backend supports them.

## Verification

- [ ] One end-to-end trace crosses web, service, queue and worker without breaking
- [ ] Sampling keeps errors even when the default rate is low
- [ ] No personal data found in a sample of span attributes

## Related

- [Observability strategy](observability-strategy.md)
- [Logging map](logging-map.md)
- [Event architecture](../09-architecture/event-architecture.md)
- [Workers and queues](../14-delivery/workers-and-queues.md)
