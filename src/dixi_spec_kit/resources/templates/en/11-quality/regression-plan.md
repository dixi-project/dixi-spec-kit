# Regression plan

## Purpose

Make sure that behaviour which already works keeps working as the project changes, by defining which tests guard it, when they run and what happens when one fails.

Status: draft. {{pending: confirm the regression suite and its schedule}}

## Regression suite

The regression suite is the set of committed, frozen tests that protect delivered behaviour.

| Suite | Contents | Runs | Time budget |
|-------|----------|------|-------------|
| Fast | Unit and integration tests | Every change, inside `make verify` | {{pending: budget}} |
| Full | Fast suite plus contract and end-to-end tests | {{pending: for example every pull request}} | {{pending: budget}} |
| Extended | Performance, security and long-running tests | {{pending: schedule}} | {{pending: budget}} |

## Adding to the suite

- Every fixed defect gets a test that reproduces it first (red), then the fix (green).
- Every accepted feature adds its tests to the suite.
- Tests are never removed to speed up the suite without a recorded decision; move them to a slower tier instead.

## Selecting tests for a change

{{pending: decide whether to run the full suite always or select tests by changed areas, and how to avoid missing dependencies}}

## Failures

1. A failing regression test blocks the merge.
2. Find whether the code, the environment or the test is wrong.
3. If the test is wrong, stop and ask for a human decision; do not edit a frozen test to make it pass.
4. Flaky tests are quarantined with an owner and a deadline, and fixed.

## Release checks

Before a release, record:

- Real results of the full suite.
- Known failures and their accepted risk, with the person who accepted it.
- Manual regression checks performed, if any.

## Related

- [Quality strategy](quality-strategy.md)
- [Verification ladder](verification-ladder.md)
- [Test pyramid](test-pyramid.md)
- [Risk-based review](risk-based-review.md)
- [Test plan](test-plan.md)
