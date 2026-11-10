# Risk-based review

## Purpose

Match the depth of human review to the risk of each change, so that reviewers spend their attention where a mistake would cost the most.

Status: draft. {{pending: agree on risk levels and required reviewers}}

## Risk levels

| Level | Typical changes | Required review |
|-------|-----------------|-----------------|
| Low | Copy, styling, documentation, isolated refactors with tests green | One reviewer reads the diff and the `make verify` result |
| Medium | New feature behind existing interfaces, new tests, dependency updates | One reviewer checks spec, tests and behaviour |
| High | Data model, contracts, authentication, permissions, payments, personal data, infrastructure | {{pending: number and role of reviewers}}; structural decisions validated before building |

{{pending: adjust the examples to this project's real risk areas}}

## Signals that raise risk

- Changes to contracts or schemas consumed by others.
- Code touching secrets, access control or personal data.
- Large diffs, generated code with little test coverage, or edits to test files.
- Irreversible operations (data migrations, deletions).
- Areas with past incidents.

## Reviewer checklist

- Does the change match the spec and its acceptance criteria?
- Were tests written first, and were committed tests left unchanged?
- Did `make verify` run, and is the real output included?
- Are failure paths and edge cases handled?
- Is anything claimed as verified that was not actually run?
- Were any thresholds, budgets or rules loosened? If so, is there a recorded human decision?

## Agents and review

Agents can prepare evidence and point out risk, for example with `/dixi.quality` or `$dixi-quality`, but they never approve or merge. The final decision is always a person's.

## Related

- [Quality strategy](quality-strategy.md)
- [Verification ladder](verification-ladder.md)
- [Non-functional requirements](non-functional-requirements.md)
- [Test plan](test-plan.md)
- [Project instructions](../AGENTS.md)
