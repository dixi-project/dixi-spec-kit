# TASK-016 — Generated command reference (v1.10.0)

## Purpose

Give every operation its own reference page, generated from the command texts themselves so the reference never drifts.

## Record

- Type: docs; priority P1; level 2. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Planned for the next `/loop` session, in order TASK-016 → TASK-024.

## Story

As a person evaluating or using DIXI
I want one page per command that says what it does, when to use it, what it reads and writes and where it stops
so that I can choose and run commands without opening the packaged files.

## Acceptance criteria

1. A standard-library script generates `docs/commands/<operation>.md` in English and Spanish from the packaged Claude Code command texts: purpose, when to use it, arguments, files read and written, stops and human gates, next step, and the invocation for Claude Code (`/dixi.<op>`), Codex (`$dixi-<op>`) and Agent Skills (`dixi-<op>`).
2. The documentation site gains a Commands section with the thirty-three pages in both languages.
3. A test fails when an operation has no page or a page is out of date with its command text.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
