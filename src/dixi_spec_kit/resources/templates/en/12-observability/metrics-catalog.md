# Metrics Catalog

## Purpose

List every metric the system emits with a stable name, a unit and an owner, so dashboards, alerts and SLIs refer to the same thing. A metric not in this catalog should not be relied on.

## Naming rules

- Lowercase words separated by dots or underscores, consistently: {{pending: choose one convention}}.
- Include the unit in the name or its metadata (seconds, bytes, requests).
- Use counters for things that only grow, gauges for current values and histograms for durations and sizes.
- Keep label cardinality bounded: never use user IDs, e-mails, full URLs or free text as labels.

## Baseline metrics per entry point

For each HTTP endpoint, queue consumer or scheduled job, record at least rate, errors and duration:

| Metric | Type | Unit | Labels | Purpose |
|---|---|---|---|---|
| `http.server.request.duration` | histogram | seconds | route, method, status class | Latency and throughput |
| `http.server.request.errors` | counter | requests | route, status class | Error rate |
| `job.run.duration` | histogram | seconds | job | Scheduled job time |
| `job.run.failures` | counter | runs | job | Scheduled job failures |
| `queue.messages.pending` | gauge | messages | queue | Backlog |
| `queue.messages.dead_lettered` | counter | messages | queue | Poison messages |

## Resource metrics

| Metric | Type | Unit | Purpose |
|---|---|---|---|
| CPU usage | gauge | ratio | Capacity |
| Memory usage | gauge | bytes | Capacity and leaks |
| Database connections in use | gauge | connections | Pool saturation |

## Business metrics

| Metric | Type | Unit | Owner | Why it matters |
|---|---|---|---|---|
| {{pending: e.g. orders completed}} | counter | {{pending: unit}} | {{pending: role}} | {{pending: link to a goal}} |
| {{pending: e.g. sign-ups}} | counter | {{pending: unit}} | {{pending: role}} | {{pending: link to a goal}} |

## Change process

1. Add or rename a metric here in the same pull request that changes the code.
2. Update any dashboard, alert or SLI that uses it.
3. Keep a deprecated name for {{pending: period}} before removing it.

## Related

- [SLIs, SLOs and SLAs](slis-slos-slas.md)
- [Dashboard map](dashboard-map.md)
- [Alerting rules](alerting-rules.md)
- [Engineering metrics](../11-quality/engineering-metrics.md)
