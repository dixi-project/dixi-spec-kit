# TASK-017 — Public command guide replacing the internal catalog (v1.10.0)

## Purpose

Replace the internal, outdated `docs/command-catalog.md` with a guide for users: the journey, which command to use when, and a full walkthrough.

## Record

- Type: docs; priority P1; level 2. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Planned for the next `/loop` session, in order TASK-016 → TASK-024.

## Story

As a new user
I want a map of the method and a table of which command to use at each moment
so that I know where to start and what comes next.

## Acceptance criteria

1. A journey map (discover → specify → clarify → plan → tasks → build → verify → review → release) with the design, quality, continuity and specialized operations around it.
2. A "which command when" table covering all thirty-three operations, linking to their reference pages (TASK-016).
3. The old working catalog moves to `docs/history/` with a note; no public page says "proposed", "pending" or "deferred" for shipped commands.
4. A walkthrough from `dixi init` to a release on a small example, in English and Spanish.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
