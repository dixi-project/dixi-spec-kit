# Strategic goals

## Purpose

Turn the business goal into a small set of measurable objectives for a defined period. Strategic
goals are the top of the traceability chain: each one should have an ID that domains and features
cite as a parent in `.dixi/traceability.json`, so that every piece of work can answer "which goal
does this serve?".

## How to define goals

- Write outcomes, not outputs: "reduce onboarding time" instead of "build an onboarding wizard".
- Give each goal a baseline, a target and a date. Without a baseline the target is a guess.
- Limit the set to three to five goals per period.
- Assign an owner who can decide trade-offs for the goal.
- Review the goals at the end of each period and record what was learned.

## Period

- Time frame: {{pending: quarter, half-year or year}}
- Approved by: {{pending: person or role who validates the goals}}

## Goals

| ID | Goal (outcome) | Metric | Baseline | Target | Date | Owner |
|---|---|---|---|---|---|---|
| GOAL-001 | {{pending: outcome}} | {{pending: metric}} | {{pending: current value}} | {{pending: target}} | {{pending: date}} | {{pending: owner}} |
| GOAL-002 | {{pending: outcome}} | {{pending: metric}} | {{pending: current value}} | {{pending: target}} | {{pending: date}} | {{pending: owner}} |

`GOAL-001` matches the baseline goal in `vision.md`. Add new IDs to `.dixi/traceability.json`
with `kind: goal` and no parents, then run `dixi check`.

## Guardrail metrics

Metrics that must not degrade while pursuing the goals (for example, error rate, accessibility or
support load):

| Metric | Acceptable limit | Why it matters |
|---|---|---|
| {{pending: guardrail}} | {{pending: limit}} | {{pending: reason}} |

## Non-goals for this period

- {{pending: what the team explicitly will not pursue now}}

## Review log

| Date | Goal | Result | Decision |
|---|---|---|---|
| {{pending: date}} | {{pending: goal ID}} | {{pending: measured result}} | {{pending: keep, adjust or drop}} |

## Related

- [Business goal](vision.md)
- [Value proposition](value-proposition.md)
- [Business capabilities](domains/business-capabilities.md)
- [Project](../00-master-spec.md)
