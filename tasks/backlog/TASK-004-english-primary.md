# TASK-004 — English as the primary language (v1.1.0)

## Purpose

Make English the repository's primary language and the CLI default, keeping Spanish available.

## Record

- Type: change; priority P1; level 2. Created 2026-11-08. Product owner: Alfredo Castillejos.
- Validation: on 2026-11-08 the product owner chose "English primary + Spanish" and "default `en`" for the CLI and new projects.

## Story

As the product owner
I want DIXI Spec Kit documented in English and defaulting to English
so that an international audience can adopt it without translating.

## Acceptance criteria

1. README, contributing guide, security policy, agent instructions, roadmap, changelog, docs, specs, ADRs, tasks and the example are in English; `README.es.md` and Spanish summaries remain.
2. Without `--lang`, help, errors and new projects are in English.
3. Inside an existing project and without `--lang`, messages follow the project language; unreadable metadata falls back to English.
4. `--lang es` keeps producing Spanish output and documents.
5. The changelog announces the default-language change.

## Done when

1. `tests/test_default_language.py` was committed red before the implementation and is green.
2. `make verify` passes and the CI is green on the pull request.

## Closed — 2026-11-09

Released in [v1.1.0](https://github.com/dixi-project/dixi-spec-kit/releases/tag/v1.1.0).

## Related

- [Board](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
