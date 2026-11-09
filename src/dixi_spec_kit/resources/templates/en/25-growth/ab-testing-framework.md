# A/B testing framework

## Purpose

Define when to run controlled experiments, how to design them so the result can be trusted, and how to record decisions. An experiment is a way to reduce uncertainty, not a way to avoid making a decision.

Status: draft. {{pending: decide the minimum traffic, significance level and who approves experiments}}

## When to experiment

Experiment when:

- The change is reversible and the outcome is genuinely uncertain.
- There is enough traffic in the segment to detect the expected effect in a reasonable time.
- The metric can be measured reliably.

Decide without an experiment when:

- The change fixes a defect, an accessibility problem or a legal requirement.
- Traffic is too low to reach a conclusion.
- The change is required by a spec regardless of the result.

## Experiment design

| Field | Content |
|-------|---------|
| ID and owner | {{pending}} |
| Hypothesis | If we change X for segment Y, metric Z will move by N because ... |
| Primary metric | One metric that decides the result |
| Guardrail metrics | Metrics that must not get worse (errors, performance, complaints) |
| Segment and languages | {{pending}} |
| Sample size and duration | Calculated before starting |
| Stop conditions | When to stop early for harm |

## Rules for trustworthy results

- Fix the sample size and duration before starting; do not stop when the result looks good.
- Run for whole weekly cycles to avoid day-of-week effects.
- Check that variants received the expected share of traffic before reading results.
- Analyse languages and markets separately when they behave differently.
- Avoid overlapping experiments on the same page or metric unless designed for it.
- Variants in every language are complete translations; a missing translation invalidates the test.
- Server-rendered variants must not show crawlers different content than people would see.

## Decision

| Outcome | Action |
|---------|--------|
| Primary metric improves, guardrails stable | Ship and record |
| No significant difference | Choose the simpler option and record |
| Guardrail gets worse | Do not ship; investigate |

## Result record

Record each experiment: hypothesis, dates, segments, results with uncertainty, decision and the person who made it. Keep failed experiments too.

## Related

- [Conversion funnel](conversion-funnel.md)
- [Growth strategy](growth-strategy.md)
- [Landing pages catalog](landing-pages-catalog.md)
- [Decision log](../18-knowledge-base/decision-log.md)
- [PII classification](../08-data/pii-classification.md)
