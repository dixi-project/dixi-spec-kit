# TDD guide

## Purpose

Explain how this project writes tests before code (red → green → refactor) and keeps committed tests frozen, so that tests express the spec instead of describing whatever the code happens to do.

Status: draft. {{pending: confirm the TDD workflow with the team}}

## Cycle

1. **Read the spec.** Start from the feature spec and its acceptance criteria.
2. **Red.** Write the smallest test that expresses one criterion. Run it and confirm it fails for the expected reason.
3. **Commit the red test.** The commit contains the test only, for example `[11-quality] test: <behaviour> (red)`.
4. **Green.** Write the minimum code that makes the test pass. Do not touch the test.
5. **Refactor.** Improve the code with all tests green.
6. **Verify.** Run `make verify` and record the real result.

## Frozen tests

- A committed test is a contract with the spec. Do not edit it to make code pass.
- If a test seems wrong, stop. Explain why, point to the spec, and ask the responsible person to decide.
- Changing a frozen test requires a spec change first and a human approval. {{pending: who approves changes to frozen tests}}
- Agents follow the same rule as people; see [project instructions](../AGENTS.md).

## Writing good first tests

- Name the test after the behaviour, not the implementation.
- One observable behaviour per test.
- Cover boundaries: empty, zero, one, maximum, invalid input.
- Prefer real values over mocks; mock only true external boundaries.
- A test that cannot fail is not a test. Confirm the red state before writing code.

## Traceability

Link each test to its criterion in the [test plan](test-plan.md) and keep IDs in `.dixi/traceability.json` so `dixi check` can follow the chain from goal to test.

## Exceptions

{{pending: list the cases where tests may follow code, for example throwaway spikes, and how they are removed or covered before merge}}

## Related

- [Quality strategy](quality-strategy.md)
- [Test pyramid](test-pyramid.md)
- [Acceptance strategy](acceptance-strategy.md)
- [Verification ladder](verification-ladder.md)
- [Test plan](test-plan.md)
