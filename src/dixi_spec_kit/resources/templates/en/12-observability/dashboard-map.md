# Dashboard Map

## Purpose

List the dashboards the team relies on, who each one is for and which question it answers. A short set of well-known dashboards beats many forgotten ones.

## Rules

- Each dashboard answers one audience and a few questions; name it after them.
- Panels use metrics from the [metrics catalog](metrics-catalog.md) only.
- Show SLOs and deploy markers where they help explain changes.
- Dashboards are versioned as code when the tooling allows it: {{pending: location in the repo}}.
- Review the list {{pending: frequency}}; archive dashboards nobody opened.

## Dashboard inventory

| Dashboard | Audience | Questions it answers | Key panels | Owner | Link |
|---|---|---|---|---|---|
| Service overview | On-call engineer | Is it healthy right now? | Request rate, error rate, p95 latency, saturation | {{pending: role}} | {{pending: link}} |
| SLO status | Engineering and product | Are we within objectives? | SLI over window, remaining error budget, burn rate | {{pending: role}} | {{pending: link}} |
| Release health | Whoever is releasing | Did the last deploy make things worse? | Errors and latency by version, deploy markers | {{pending: role}} | {{pending: link}} |
| Async work | On-call engineer | Are jobs and queues keeping up? | Backlog, age of oldest message, failures, dead letters | {{pending: role}} | {{pending: link}} |
| Business | Product | {{pending: business question}} | {{pending: business metrics}} | {{pending: role}} | {{pending: link}} |

## Layout guidance

1. Top row: the few numbers that say "healthy or not".
2. Middle: breakdown by route, job or dependency.
3. Bottom: resources and capacity.
4. Every panel has a title that states what "bad" looks like.

## Access

- Viewers: {{pending: roles}}
- Editors: {{pending: roles}}
- Dashboards never display personal data or secrets.

## Related

- [Metrics catalog](metrics-catalog.md)
- [SLIs, SLOs and SLAs](slis-slos-slas.md)
- [Alerting rules](alerting-rules.md)
- [Observability strategy](observability-strategy.md)
