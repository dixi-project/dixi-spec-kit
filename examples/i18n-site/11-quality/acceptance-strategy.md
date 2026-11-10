# Acceptance strategy

## Purpose

Define how acceptance criteria are written, tested and accepted, so that "done" means the observable behaviour the business asked for, confirmed by a person.

Status: draft. {{pending: decide who accepts features and how acceptance is recorded}}

## Writing criteria

Each feature spec lists criteria that are:

- **Observable:** describe what a user or system sees, not how it is built.
- **Testable:** a test can pass or fail against it.
- **Independent:** one behaviour per criterion.
- **Identified:** each criterion has a stable ID referenced by tests.

A common shape is *Given* a context, *When* an action happens, *Then* an outcome is observed. Plain sentences are fine if they stay observable.

## From criteria to tests

| Step | Output | Owner |
|------|--------|-------|
| Draft criteria | Criteria in the [feature spec](../05-features/example/feature-spec.md) | {{pending: owner}} |
| Review criteria | Ambiguities resolved, IDs assigned | {{pending: owner}} |
| Write failing tests | Tests linked from the [test plan](test-plan.md) | Developer or agent |
| Make them pass | Code, with `make verify` green | Developer or agent |
| Accept | Recorded human decision | {{pending: owner}} |

## Acceptance evidence

Record for each feature:

- Criteria IDs and the tests that cover them.
- Real result of `make verify` and any manual checks.
- Who accepted, when, and any open follow-ups.

{{pending: where acceptance evidence lives, for example the pull request description}}

## Manual checks

Some criteria cannot be automated cheaply (visual layout, copy tone). Mark them as manual, describe the steps, and record who ran them. A manual check is not reported as automated.

## Rejection

If a criterion is not met, the feature goes back to development. Criteria are not rewritten after the fact to match the delivered behaviour without a recorded decision.

## Related

- [Quality strategy](quality-strategy.md)
- [TDD guide](tdd-guide.md)
- [Test pyramid](test-pyramid.md)
- [Test plan](test-plan.md)
- [Goal](../01-business/vision.md)
