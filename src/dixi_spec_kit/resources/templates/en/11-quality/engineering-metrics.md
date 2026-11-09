# Engineering metrics

## Purpose

Choose a small set of metrics that show whether the delivery process is healthy, and use them to improve the process, never to rank people.

Status: draft. {{pending: choose the metrics this project will track}}

## Candidate metrics

| Metric | What it shows | How measured | Target |
|--------|---------------|--------------|--------|
| Lead time for changes | Time from commit to production | {{pending: source}} | {{pending: target}} |
| Deployment frequency | How often changes reach users | {{pending: source}} | {{pending: target}} |
| Change failure rate | Share of changes that cause a failure | {{pending: source}} | {{pending: target}} |
| Time to restore | Time to recover from a failure | {{pending: source}} | {{pending: target}} |
| Verification time | Duration of `make verify` and CI | {{pending: source}} | {{pending: target}} |
| Flaky test count | Tests quarantined for instability | {{pending: source}} | {{pending: target}} |
| Escaped defects | Defects found after release | {{pending: source}} | {{pending: target}} |

Pick only the metrics someone will review and act on.

## Rules

- Metrics describe the system, not individuals.
- A metric used as a target loses meaning; watch for gaming (smaller commits only to raise frequency, deleted tests to speed up CI).
- Do not lower quality gates to improve a metric.
- Agent-generated changes are measured like any other change.

## Review

- {{pending: how often metrics are reviewed and by whom}}
- Each review ends with at most a few improvement actions, each with an owner.

## Data

{{pending: where metric data comes from and how long it is kept}}

Collect only what is needed; avoid personal data.

## Related

- [Quality strategy](quality-strategy.md)
- [Regression plan](regression-plan.md)
- [Verification ladder](verification-ladder.md)
- [Risk-based review](risk-based-review.md)
