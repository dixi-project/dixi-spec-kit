# Quality strategy

## Purpose

Describe how this project decides that a change is good enough to merge. The strategy connects specs, tests written first, automated checks and human review into one path that every change follows.

Status: draft. {{pending: confirm the strategy with the person responsible for quality}}

## Principles

- **Specs before code.** Every behaviour change starts from a feature spec and observable acceptance criteria.
- **Tests first (red → green).** A failing test is committed before the code that makes it pass.
- **Frozen tests.** Once committed, a test is not edited to make code pass. If a test looks wrong, stop, explain and get a human decision.
- **Machines check what machines can.** Format, types, unit and integration tests run automatically; people review intent, risk and business fit.
- **Evidence, not claims.** "Verified" means a check ran and its real output was recorded.

## Scope

| Area | In scope | Owner |
|------|----------|-------|
| Functional behaviour | {{pending: list the features covered}} | {{pending: owner}} |
| Non-functional requirements | See [non-functional requirements](non-functional-requirements.md) | {{pending: owner}} |
| Performance | See [web vitals budgets](performance-budgets/web-vitals-budgets.md) | {{pending: owner}} |
| Out of scope | {{pending: what this strategy does not cover and why}} | — |

## Quality gates

1. Spec and acceptance criteria exist and are traceable (`dixi check`).
2. Tests were written first and are linked from the [test plan](test-plan.md).
3. `make verify` passes locally, following the [verification ladder](verification-ladder.md).
4. Review depth matches the change risk, per the [risk-based review](risk-based-review.md).
5. A person approves and merges. Agents never approve or merge.

{{pending: decide which gates block a merge and which only warn}}

## When a gate fails

Fix the code or the spec, never the threshold. Lowering a coverage target, a budget or a strictness level to make a change pass requires an explicit, recorded decision by the responsible person, and it is never done by an agent.

## Review cadence

{{pending: how often this strategy is reviewed and who signs off}}

## Related

- [Verification ladder](verification-ladder.md)
- [Test pyramid](test-pyramid.md)
- [TDD guide](tdd-guide.md)
- [Acceptance strategy](acceptance-strategy.md)
- [Test plan](test-plan.md)
- [Project](../00-master-spec.md)
