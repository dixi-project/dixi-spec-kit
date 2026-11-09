# Verification ladder

## Purpose

Order every automated check from cheapest to most expensive so that machines catch what they can before a person spends attention on a change. Each rung catches a different class of defect; none replaces the next one.

Status: draft. {{pending: map each rung to a real command of the chosen stack}}

## The ladder

```
cheap / fast                                                  expensive / slow
1 format/lint -> 2 types -> 3 unit -> 4 integration -> 5 contract -> 6 end-to-end -> person
```

| Rung | Catches | Does not catch | Command |
|------|---------|----------------|---------|
| 1. Format and lint | Noisy diffs, unused imports, dead code, risky patterns | Wrong business logic | {{pending: command}} |
| 2. Types | Mismatched types, unhandled null, invented signatures | Wrong value of the right type | {{pending: command}} |
| 3. Unit tests | Wrong logic inside one unit, edge cases | Wiring between components | {{pending: command}} |
| 4. Integration tests | Broken wiring, persistence, configuration | Drift from external consumers | {{pending: command}} |
| 5. Contract tests | Interface drift between producer and consumer | Full user journeys | {{pending: command}} |
| 6. End-to-end tests | Broken critical user journeys | Rare edge cases (too slow to cover) | {{pending: command}} |

## `make verify`

The project defines `make verify` as the single entry point for local verification. The baseline only runs `dixi check`, which checks document structure, not application behaviour.

- Add each rung to `make verify` as soon as the stack provides it.
- Keep the local run fast enough to execute on every change. {{pending: local time budget, for example a few minutes}}
- Slower rungs (full end-to-end, deep security scans) may run in continuous integration instead. {{pending: which rungs run only in CI}}

## Rules

- Run the rungs in order and stop at the first failure.
- Report the real result of each rung: passed, failed or not run. Never report a rung as passed if it did not run.
- A failure is fixed in the code or the spec, never by loosening a rule, skipping a test or lowering a threshold.
- With Claude Code, `/dixi.quality` can guide this review; with Codex, `$dixi-quality`.

## Where each rung runs

| Moment | Rungs | Trigger |
|--------|-------|---------|
| Local | {{pending: rungs}} | Developer or agent before asking for review |
| Pull request | {{pending: rungs}} | Continuous integration |
| Scheduled | {{pending: rungs}} | {{pending: schedule}} |

## Related

- [Quality strategy](quality-strategy.md)
- [Test pyramid](test-pyramid.md)
- [TDD guide](tdd-guide.md)
- [Test plan](test-plan.md)
- [Guide](../docs/guide.md)
