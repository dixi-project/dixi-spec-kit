# Web vitals budgets

## Purpose

Set user-centred performance budgets for web pages, so that regressions in loading, interactivity and visual stability are caught before users notice them.

Status: draft. {{pending: decide the budgets and how they are measured}}

## Metrics

| Metric | What it measures | Budget | Measured at |
|--------|------------------|--------|-------------|
| Largest contentful paint | Time until the main content is visible | {{pending: budget}} | {{pending: percentile, for example 75th}} |
| Interaction to next paint | Responsiveness to user input | {{pending: budget}} | {{pending: percentile}} |
| Cumulative layout shift | Visual stability while loading | {{pending: budget}} | {{pending: percentile}} |
| Time to first byte | Server response time | {{pending: budget}} | {{pending: percentile}} |
| Page weight | Total transferred size of a page | {{pending: budget}} | Per page type |

Example only, not a recommendation: some teams start from widely published "good" thresholds and tighten them over time.

## Pages in scope

| Page type | Example URL | Notes |
|-----------|-------------|-------|
| {{pending: page type}} | {{pending: URL with language prefix}} | {{pending: notes}} |

Measure each supported language version, since translated content can change size and layout.

## Measurement

- **Lab:** controlled runs during development or CI to catch regressions early. {{pending: when lab checks run}}
- **Field:** real-user data, if collected, to confirm the experience. {{pending: whether field data is collected, respecting privacy}}
- Record device and network conditions so results are comparable.

## When a budget is exceeded

Treat it as a failing check: find the cause and fix it. A budget is never raised to make a change pass without a recorded decision by the responsible person.

## Related

- [Non-functional requirements](../non-functional-requirements.md)
- [Quality strategy](../quality-strategy.md)
- [Verification ladder](../verification-ladder.md)
- [Project](../../00-master-spec.md)
