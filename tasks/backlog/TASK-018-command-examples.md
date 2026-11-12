# TASK-018 — Usage examples for every operation (v1.10.0)

## Purpose

Every operation has at least one invocation example, and the Spanish README lists `interview` and `risk-review`.

## Record

- Type: docs; priority P2; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Planned for the next `/loop` session, in order TASK-016 → TASK-024.

## Story

As a user
I want a concrete example of each command
so that I can copy it and adapt it.

## Acceptance criteria

1. Each reference page (TASK-016) shows at least one realistic example with its arguments for the three adapters.
2. `README.es.md` and the guide mention `/dixi.interview` and `/dixi.risk-review`.
3. A test checks that every operation has an example.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
