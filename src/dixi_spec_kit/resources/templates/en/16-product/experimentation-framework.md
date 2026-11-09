# Experimentation framework

## Purpose

Define how the project runs controlled experiments, such as A/B tests, so that product decisions rest on results that are statistically sound, ethical and reproducible, and so that no experiment harms users or skews metrics.

Status: draft. {{pending: decide whether the project runs experiments at all and who approves each one}}

## When to experiment

Run an experiment when:

- There is a clear hypothesis and a metric that can move within a reasonable time.
- Traffic is large enough to reach the required sample size.
- The change can be safely shown to only part of the users.

Do not experiment on security, legal notices, accessibility features or pricing shown to protected groups. Ship those as normal decisions.

## Hypothesis template

```text
We believe that <change>
for <audience, including locale>
will cause <expected effect>
measured by <primary metric>.
We will know it worked if <metric> changes by at least <minimum detectable effect>
within <duration>, without degrading <guardrail metrics>.
```

## Experiment register

| ID | Hypothesis | Primary metric | Guardrails | Locales | Sample size | Start | End | Result | Decision |
|----|------------|----------------|------------|---------|-------------|-------|-----|--------|----------|
| EXP-001 | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | — | — | — | — |

## Design rules

- Pre-register the hypothesis, metrics, sample size and duration before starting; do not change them mid-run.
- Assign users randomly and consistently; a user sees the same variant across sessions.
- Run for full weekly cycles to avoid day-of-week bias.
- Analyze locales separately when behaviour may differ by language or market.
- Every variant meets the same accessibility and translation standard as production.
- Define a stop condition for harm, for example a guardrail metric degrading beyond a threshold.

{{pending: set the significance level, statistical power and minimum detectable effect}}

## Ethics and privacy

- Experiments use only events listed in the analytics catalog.
- Users are not deceived about prices, terms or data use.
- {{pending: decide whether users are told about experiments and how they can opt out}}

## Closing an experiment

1. Stop at the planned end or at a stop condition, not when results look good.
2. Record the result, including inconclusive and negative ones.
3. Decide: ship, iterate or discard; remove the losing code and flags.
4. Link the result from the related feature spec.

## Related

- [Analytics events catalog](analytics-events-catalog.md)
- [Feature lifecycle](feature-lifecycle.md)
- [Prioritization framework](prioritization-framework.md)
- [Accessibility standard](../17-ux/accessibility-standard.md)
- [PII classification](../08-data/pii-classification.md)
