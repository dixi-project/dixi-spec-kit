# TASK-028 — The handoff of an isolated session reaches the maintainer's checkout (v1.11.1)

## Purpose

The maintainers' handoff lives in `.context/`, which Git ignores, so it exists only in the main checkout. An agent session that works in an isolated worktree cannot write there: the handoff of the session of 2026-11-12 was left in a temporary folder for the maintainer to copy, and it is lost if that folder is removed first.

## Record

- Type: chore; priority P2; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- The handoff itself is private and is not part of this repository; this task only tracks that it is saved and how.

## Story

As a maintainer who works with agent sessions
I want the handoff of each session to end up where the next session reads it
so that no session starts without the state of the previous one.

## Acceptance criteria

1. The handoff of the session of 2026-11-12 (logo, v1.10.0 and v1.11.0) is in `.context/` of the maintainer's checkout. This is the maintainer's action.
2. `docs/local-development.md` says, in a short section, how an isolated session hands off: it writes the handoff outside the repository and gives the maintainer the exact command to copy it into `.context/`.
3. No private content is added to the repository: the section describes the procedure, not the handoff.

## Done when

1. The maintainer confirmed that the handoff is in place.
2. `make verify` passes and CI is green for the documentation change.

## Related

- [Tasks](../TASKS.md)
- [Local development](../../docs/local-development.md)
