# TASK-021 — `/dixi.status` resumes a session like the ecosystem's `/open` (v1.10.0)

## Purpose

Approved in principle by the owner on 2026-11-12; confirm the design at the start of the session. `/dixi.status` also reads the last handoff, recent contract changes and open tasks, and recommends the next step; it never commits or pushes.

## Record

- Type: feature; priority P2; level 2. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Planned for the next `/loop` session, in order TASK-016 → TASK-024.

## Story

As a person coming back to a project
I want one command that tells me where I left off
so that I can resume without rereading everything.

## Acceptance criteria

1. Reads `.context/handoff.md` when it exists, the recent changes under `07-contracts/` and the open tasks, and reports them with the next recommended command.
2. Remains read-only: no writes, commits or pushes.
3. Both languages and adapters; tests on the command text.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
