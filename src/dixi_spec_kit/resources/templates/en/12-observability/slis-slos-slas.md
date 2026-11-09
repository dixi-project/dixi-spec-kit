# SLIs, SLOs and SLAs

## Purpose

Turn "the system must be reliable" into measurable indicators, internal objectives and, only when the business decides it, external commitments. The numbers here are decisions of the project, not defaults.

## Definitions

- **SLI** (indicator): a ratio of good events to valid events, measured from the user's point of view.
- **SLO** (objective): the target for an SLI over a window, for example "99.x % of requests succeed over 28 days".
- **Error budget**: `1 - SLO`; the amount of failure the team accepts before it stops shipping features to fix reliability.
- **SLA** (agreement): a contractual promise with consequences. It must always be looser than the SLO.

## Indicator catalog

| ID | User journey | Good event | Valid event | Measured at | Source |
|---|---|---|---|---|---|
| SLI-001 | {{pending: main journey}} | Response without server error | All requests except health checks | {{pending: edge or service}} | {{pending: metric name}} |
| SLI-002 | {{pending: main journey}} | Response faster than {{pending: threshold}} | Same as above | {{pending: edge or service}} | {{pending: metric name}} |
| SLI-003 | {{pending: async job, if any}} | Processed within {{pending: time}} | All accepted jobs | Worker | {{pending: metric name}} |

## Objectives

| SLI | SLO | Window | Error budget | Owner |
|---|---|---|---|---|
| SLI-001 | {{pending: target}} | {{pending: e.g. 28 days rolling}} | {{pending: computed}} | {{pending: role}} |
| SLI-002 | {{pending: target}} | {{pending: window}} | {{pending: computed}} | {{pending: role}} |

Example only, not a recommendation: an SLO of 99.5 % over 28 days allows about 3.4 hours of failure in that window.

## Error budget policy

- Budget healthy: normal delivery.
- Budget below {{pending: percentage}}: prioritize reliability work in the next iteration.
- Budget exhausted: {{pending: freeze non-urgent releases, who can grant exceptions}}.

## External commitments

- SLA offered: {{pending: none yet, or the agreed target and its consequences}}
- Exclusions (planned maintenance, client-side failures): {{pending: list}}

## Review

Review indicators and objectives {{pending: frequency}} with product and engineering. Change an SLO only with a written reason.

## Related

- [Non-functional requirements](../11-quality/non-functional-requirements.md)
- [Metrics catalog](metrics-catalog.md)
- [Alerting rules](alerting-rules.md)
- [Observability strategy](observability-strategy.md)
- [Goal](../01-business/vision.md)
