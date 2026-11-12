# TASK-019 — CLI reference generated from the help (v1.10.0)

## Purpose

One page per `dixi` command (init, doctor, check, workflow, upgrade, extension, preset, placeholders, pr-size) with options and exit codes, generated from the CLI help in both languages.

## Record

- Type: docs; priority P2; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Planned for the next `/loop` session, in order TASK-016 → TASK-024.

## Story

As a person scripting DIXI
I want every option and exit code documented
so that I can automate it safely.

## Acceptance criteria

1. A script renders the argparse help of every command and subcommand in English and Spanish into `docs/cli/`, plus the exit-code table.
2. The site links the CLI reference; a test fails when a command or option is missing from it.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
