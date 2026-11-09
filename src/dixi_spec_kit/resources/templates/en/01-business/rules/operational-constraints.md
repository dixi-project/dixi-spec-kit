# Operational constraints

## Purpose

Record the real-world limits under which the product must operate: schedules, capacity, locations,
connectivity, staffing and dependencies. These constraints shape non-functional requirements and
architecture decisions, and they are often discovered too late if nobody writes them down.

## Constraint catalog

| ID | Constraint | Category | Impact on the product | Source | Owner |
|---|---|---|---|---|---|
| OC-001 | {{pending: constraint}} | {{pending: category}} | {{pending: impact}} | {{pending: source}} | {{pending: role}} |
| OC-002 | {{pending: constraint}} | {{pending: category}} | {{pending: impact}} | {{pending: source}} | {{pending: role}} |

## Categories to review

- Time: business hours, time zones, peak seasons, maintenance windows.
- Volume: expected users, transactions per period, growth rate, data size.
- Geography: countries, languages, currencies, local holidays and formats.
- Connectivity: offline or low-bandwidth use, device types, field conditions.
- People: support hours, on-call availability, required training.
- Dependencies: partner availability, batch windows, manual steps that cannot be automated yet.

## Operating hours and support

- Hours of operation: {{pending: e.g. 24x7 or business hours in a given time zone}}
- Support coverage: {{pending: hours and channels}}
- Acceptable maintenance windows: {{pending: when planned downtime is allowed}}

## Capacity assumptions

| Metric | Expected now | Expected in 12 months | Peak factor |
|---|---|---|---|
| {{pending: e.g. active users}} | {{pending: value}} | {{pending: value}} | {{pending: multiplier}} |

Mark each figure as measured or estimated; revisit estimates once real data exists.

## Consequences

- Requirements derived from these constraints: {{pending: links to non-functional requirements}}
- Constraints the team cannot meet today: {{pending: gaps and mitigation}}

## Related

- [Business rules](business-rules.md)
- [Non-functional requirements](../../11-quality/non-functional-requirements.md)
- [Deployment architecture](../../09-architecture/deployment-architecture.md)
