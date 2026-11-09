# Performance Architecture

## Purpose

Define the performance and capacity goals of the system and the architectural tactics used to reach them: caching, asynchronous work, data access patterns and scaling. Numbers here are budgets to design against until they are measured.

## Budgets

| Metric | Budget | Scope |
|---|---|---|
| Server response time (p95) | {{pending: milliseconds}} | Main read operations |
| Server response time (p95) | {{pending: milliseconds}} | Main write operations |
| Page load (largest content) | {{pending: seconds}} | Key pages on a mid-range device |
| Throughput | {{pending: requests per second}} | Expected peak |
| Background job latency | {{pending: duration}} | From enqueue to completion |

## Expected load

- Users and growth: {{pending: current and 12-month estimate}}
- Peak patterns: {{pending: daily, seasonal or event-driven peaks}}
- Data volume: {{pending: records and growth rate}}

## Tactics

- **Caching**: {{pending: what is cached, where, and how it is invalidated}}.
- **Asynchronous processing**: move slow or non-critical work to background jobs.
- **Data access**: index for the main queries, paginate lists, avoid N+1 patterns.
- **Payload size**: compress responses, send only required fields, optimise media.
- **Scaling**: {{pending: horizontal, vertical or automatic, and the trigger}}.
- **Static delivery**: serve static assets from an edge cache.

## Hot paths

| Path | Why it matters | Current design | Risk |
|---|---|---|---|
| {{pending: operation}} | {{pending: user impact}} | {{pending: approach}} | {{pending: risk}} |

## Measuring

- Tools and environment for load tests: {{pending: tool and target environment}}
- When performance is checked: {{pending: per release, nightly, before launch}}
- Regression rule: {{pending: what blocks a release}}

## Related

- [Resilience architecture](resilience-architecture.md)
- [Container diagram](container-diagram.md)
- [Deployment architecture](deployment-architecture.md)
- [Test plan](../11-quality/test-plan.md)
- [Architecture decisions](adr/README.md)
