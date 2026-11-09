# Contract testing guide

## Purpose

Explain how this project checks that producers and consumers of an interface (HTTP APIs, events, messages) keep agreeing, so that one side cannot break the other unnoticed.

Status: draft. {{pending: decide the contract testing approach for each interface}}

## When contract tests help

- Several services or teams depend on the same interface.
- Producer and consumer are released independently.
- Messages travel through a queue or event bus where failures surface late.

## Approaches

| Approach | How it works | Fits when |
|----------|--------------|-----------|
| Consumer-driven | Consumers publish expectations; the producer verifies them | Few known consumers |
| Schema-based | Both sides validate against a shared, versioned schema | Many or unknown consumers |
| Provider snapshot | Producer records responses; changes are reviewed | Simple, single-team interfaces |

{{pending: choose an approach per interface and record why}}

## Rules

- The written contract in `07-contracts/` is the source of truth; tests check code against it.
- Contract changes follow the spec first: update the contract, get it reviewed, then write the failing test.
- Breaking changes need a new version or a migration plan agreed with consumers.
- Contract tests are frozen like any other test.

## What to test

- Required fields, types and formats.
- Error responses and their shape.
- Optional fields being truly optional.
- Unknown fields being tolerated if the contract says so.
- Message headers, keys and ordering assumptions for events.

## In the verification ladder

Contract tests run after integration tests and before end-to-end tests. {{pending: where contract verification runs, locally or in CI}}

## Related

- [Contract](../07-contracts/example.md)
- [Verification ladder](verification-ladder.md)
- [Test pyramid](test-pyramid.md)
- [API latency budgets](performance-budgets/api-latency-budgets.md)
- [Regression plan](regression-plan.md)
