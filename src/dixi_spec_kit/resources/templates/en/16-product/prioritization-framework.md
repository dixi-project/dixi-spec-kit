# Prioritization framework

## Purpose

Give the team one shared, explainable way to decide what to work on next, so that priority comes from evidence and agreed criteria rather than from whoever asks loudest.

Status: draft. {{pending: choose the scoring method and the person who has the final say}}

## Inputs

An item can be scored only when it has:

- A problem statement written from the user's point of view.
- The evidence behind it (research note, metric, support trend, regulatory need).
- A rough size agreed by the people who would build it.
- The target audience, including languages and markets affected.

## Scoring method

Pick one method and use it consistently. Two common options:

| Method | Formula | Good for |
|--------|---------|----------|
| Reach, impact, confidence, effort | (reach × impact × confidence) ÷ effort | Comparing many items with some data |
| Value versus effort matrix | Place each item in a 2×2 grid | Quick sorting with little data |

{{pending: pick the method and define the scale for each factor}}

### Scale definitions

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| Reach | {{pending: for example fewer than 10% of active users}} | {{pending}} | {{pending}} |
| Impact | Small improvement | Noticeable improvement | Changes the outcome for the user |
| Confidence | Opinion only | Some evidence | Strong, repeated evidence |
| Effort | {{pending: unit, for example person-weeks}} | {{pending}} | {{pending}} |

## Items that skip the queue

Some work is not scored against features:

- Security fixes and incidents follow the security and operations process.
- Legal or contractual obligations get a deadline, not a score.
- Accessibility defects that block a user from completing a task are treated as defects, not as features.

{{pending: list any other categories that bypass scoring}}

## Decision record

For every prioritization session, record:

| Date | Items reviewed | Decision | Reason | Decided by |
|------|----------------|----------|--------|------------|
| {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |

## Anti-patterns

- Scoring after the decision has already been made.
- Treating confidence as high without evidence.
- Ignoring the cost of maintaining a feature after launch.
- Prioritizing only the primary language market and leaving translations for "later" without a date.

## Related

- [Roadmap](roadmap.md)
- [Feature lifecycle](feature-lifecycle.md)
- [Analytics events catalog](analytics-events-catalog.md)
- [Jobs to be done](../24-research/jobs-to-be-done.md)
- [Business goal](../01-business/vision.md)
