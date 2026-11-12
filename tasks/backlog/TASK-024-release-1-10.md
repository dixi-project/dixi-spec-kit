# TASK-024 — Release v1.10.0 (v1.10.0)

## Purpose

Release the documentation and continuity work of TASK-016 to TASK-023 with `make release`.

## Record

- Type: docs; priority P2; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Planned for the next `/loop` session, in order TASK-016 → TASK-024.

## Story

As a user
I want the new reference, guide and commands on PyPI and on the site
so that I can use them.

## Acceptance criteria

1. Version bump with the owner's authorization for the `--version` test; CHANGELOG checked with TASK-023; `make release VERSION=1.10.0`; PyPI approval; clean-environment install.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
