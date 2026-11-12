# TASK-022 — Read-only `dixi mode` (v1.10.0)

## Purpose

Approved in principle by the owner on 2026-11-12; confirm the design at the start of the session. `dixi mode` shows the project's `MODE` and what is still missing for `prod`, and never changes it (ADR-105: only a person changes `MODE`).

## Record

- Type: feature; priority P3; level 2. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Planned for the next `/loop` session, in order TASK-016 → TASK-024.

## Story

As a person deciding a promotion
I want to see the current mode and the missing evidence
so that the decision is informed.

## Acceptance criteria

1. `dixi mode` prints `MODE` and, for `mvp`, the checklist items without evidence (the same items `/dixi.promote` reviews); JSON output.
2. It never writes; there is no option to change `MODE`.
3. Tests first; messages in `locales/`.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
