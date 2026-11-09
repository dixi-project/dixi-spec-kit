# ADR template

## Purpose

Record an architecture decision so that anyone can later understand what was decided, why, which
alternatives were rejected and what it costs. Copy the structure below into a new file.

## How to use

- One decision per ADR. Number them sequentially and never reuse a number.
  {{pending: ADR folder and numbering scheme}}
- A **structural decision** (stack, data model, boundaries between modules, security model,
  external providers) stays **Proposed** until a responsible person validates it. Agents may draft
  an ADR but never move it to Accepted.
- An accepted ADR is not edited to change its decision: write a new ADR that supersedes it.

## Template

```markdown
# ADR-NNN — <short decision title>

Status: Proposed | Accepted | Superseded by ADR-NNN | Rejected
Date: YYYY-MM-DD
Deciders: {{pending: people who validate this decision}}
Related IDs: {{pending: goal, feature or contract IDs affected}}

## Context

What problem or force requires a decision now. Facts, constraints and assumptions,
without proposing the answer yet.

## Decision

What we will do, stated in one or two firm sentences, followed by the details needed
to apply it.

## Alternatives considered

| Option | Pros | Cons | Why not chosen |
|---|---|---|---|
| A | | | |
| B | | | |

## Consequences

- Positive: what becomes easier.
- Negative: what becomes harder, costs, risks and debt accepted.
- Follow-up: tasks, tests or ADRs this decision requires.

## Validation

- [ ] Reviewed by the deciders.
- [ ] Impacted specs and tests updated.
```

## Status values

| Status | Meaning |
|---|---|
| Proposed | Drafted, under discussion; not binding yet |
| Accepted | Validated by the deciders; binding |
| Superseded | Replaced by a newer ADR, which is linked |
| Rejected | Discussed and not adopted; kept for history |

## Related

- [Coding standards](../coding-standards.md)
- [Project](../../00-master-spec.md)
- [Project instructions](../../AGENTS.md)
