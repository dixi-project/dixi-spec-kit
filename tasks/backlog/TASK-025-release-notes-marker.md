# TASK-025 — Release notes keep the text that quotes the no-entry marker (v1.11.1)

## Purpose

The notes of the v1.11.0 release say "marked in the section with ``": the example of the marker is gone. `scripts/release.py` removes every `<!-- no changelog entry: … -->` from the notes, including one quoted inside an entry. Remove only real markers and repair the published notes.

## Record

- Type: fix; priority P2; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Found when publishing v1.11.0, the first release that ran the check of TASK-023. `CHANGELOG.md` in the repository is correct; only the notes of the GitHub release are affected.

## Story

As a person reading the release notes
I want every entry to be complete
so that I can follow the instructions it gives.

## Acceptance criteria

1. `scripts/release.py` treats as a marker only a `<!-- no changelog entry: … -->` that is alone on its line; a marker quoted inside an entry, for example in a code span, stays in the notes and exempts no pull request.
2. A test builds the notes of a section whose entry quotes the marker and checks that the text is intact, and that a real marker on its own line is still removed and still exempts its pull requests.
3. The notes of the v1.11.0 release on GitHub show the complete entry of TASK-023. Editing a published release is the maintainer's action.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.
3. The maintainer confirmed the edited notes of v1.11.0.

## Related

- [Tasks](../TASKS.md)
- [TASK-023](TASK-023-changelog-guard.md)
- [PyPI publishing](../../docs/pypi-publishing.md)
