# Testing policy

## Purpose

Set the non-negotiable testing rules for this project. How to apply them day to day is explained in the TDD guide; this policy says what must always hold.

Status: draft. {{pending: confirm this policy with the responsible person}}

## Scope

All production code, scripts that change data or infrastructure, and contracts. Throwaway spikes are out of scope only if they never merge.

## Rules

| ID | Rule |
|----|------|
| T-1 | **Tests first.** A failing test is committed before the code that makes it pass. |
| T-2 | **Frozen tests.** Nobody, person or agent, edits a committed test to make code pass. Changing a test requires a spec change and human approval. |
| T-3 | **No green, no done.** Nothing is reported as done while `make verify` fails. Report the real result. |
| T-4 | **Criteria are covered.** Every acceptance criterion has at least one test, linked in the test plan. |
| T-5 | **Bugs bring their test.** Each fix includes a test that reproduced the bug first. |
| T-6 | **No silent skips.** A skipped test references an open issue and an owner. |
| T-7 | **Thresholds by risk.** Higher-risk code has stricter coverage and review. |
| T-8 | **Deterministic and fast.** Tests do not depend on time, order, network or shared state. |

## Thresholds by risk

| Risk | Example | Minimum |
|------|---------|---------|
| High | Payments, permissions, personal data | {{pending: threshold, e.g. coverage or mutation score}} |
| Medium | Core business logic | {{pending: threshold}} |
| Low | Presentation, glue code | {{pending: threshold}} |

Thresholds only go up. A change must not lower an existing threshold.

## Definition of done (quality)

- [ ] Tests for every criterion exist and pass.
- [ ] `dixi check` and `make verify` pass and the output is reported.
- [ ] No new skipped tests without an issue.
- [ ] A person reviewed the tests, not only the code.

## How it is enforced

{{pending: list the checks that enforce each rule and which ones are still review-only}}

## Related

- [TDD guide](../../11-quality/tdd-guide.md)
- [Test pyramid](../../11-quality/test-pyramid.md)
- [Test plan](../../11-quality/test-plan.md)
- [Branching strategy](branching-strategy.md)
