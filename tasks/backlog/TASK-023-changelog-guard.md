# TASK-023 — `make release` warns about pull requests without a CHANGELOG entry (v1.10.0)

## Purpose

The `init --existing` entry was lost twice when merging pull requests that touched the same CHANGELOG section. Before creating a release, list the pull requests merged since the last tag and flag those not mentioned in the version's CHANGELOG section.

## Record

- Type: feature; priority P2; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Planned for the next `/loop` session, in order TASK-016 → TASK-024.

## Story

As a maintainer
I want the release to show which merged changes are missing from the notes
so that no shipped feature goes unannounced.

## Acceptance criteria

1. `scripts/release.py` lists merged pull requests since the previous tag (through `git log` merge commits) and the ones whose number or branch does not appear in the CHANGELOG section; the person confirms before continuing.
2. Documentation-only pull requests can be marked as not needing an entry.
3. Tests on the parsing and the warning.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
