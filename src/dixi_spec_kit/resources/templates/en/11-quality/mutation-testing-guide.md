# Mutation testing guide

## Purpose

Explain how mutation testing measures whether tests actually detect wrong code, by introducing small changes (mutants) and checking that some test fails for each one.

Status: draft. {{pending: decide where and how often mutation testing runs}}

## How it works

1. A tool changes the code slightly, for example `>` to `>=` or `+` to `-`.
2. The test suite runs against each mutant.
3. If a test fails, the mutant is **killed** (good). If all tests pass, it **survived**: no test checks that behaviour.

The mutation score is the share of mutants killed.

## When to use it

- Critical logic: money, permissions, rules with boundaries.
- Code mostly generated or heavily refactored, to check the tests are meaningful.
- On changed files in a pull request, and on the whole code base on a schedule.

## Working with survivors

- Read each surviving mutant: it points to a missing or weak test.
- Add a test that kills it, written from the spec, not from the mutant.
- Some mutants are equivalent (behaviour does not change); mark them with a reason.
- Never weaken the mutation set or exclude files only to raise the score.

## Targets

| Scope | Minimum score | Runs |
|-------|---------------|------|
| Changed code in a pull request | {{pending: target}} | {{pending: when}} |
| Critical modules | {{pending: target}} | {{pending: when}} |
| Whole code base | {{pending: target or "tracked only"}} | {{pending: schedule}} |

Example only: some teams start by tracking the score without blocking, then set a floor once it is stable.

## Cost

Mutation testing is slow. Limit it to changed or critical code in pull requests and run full analysis on a schedule.

## Tooling

{{pending: choose a mutation testing tool for the stack}}

## Related

- [Property-based testing guide](property-based-testing-guide.md)
- [TDD guide](tdd-guide.md)
- [Verification ladder](verification-ladder.md)
- [Engineering metrics](engineering-metrics.md)
