# TASK-020 — Spanish versions of the key site pages (v1.10.0)

## Purpose

The `/es/` site shows Spanish content for the guide, the command and CLI references, the migration guide and the support matrix summary.

## Record

- Type: docs; priority P2; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Planned for the next `/loop` session, in order TASK-016 → TASK-024.

## Story

As a Spanish-speaking user
I want the main documentation in Spanish
so that I do not depend on English to adopt DIXI.

## Acceptance criteria

1. Spanish sources for the pages above, built into `/es/` with the same links and anchors.
2. Pages still only in English keep the notice; a test lists which pages have Spanish versions.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
