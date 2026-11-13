# TASK-026 — The README version badge shows the current version after a release (v1.11.1)

## Purpose

Hours after v1.11.0 was on PyPI, the "pypi" badge of the README still said v1.10.0. PyPI already returned 1.11.0; the badge is served with a six-hour cache lifetime and GitHub shows README images through its own image cache. A reader cannot tell a stale badge from a failed release.

## Record

- Type: docs; priority P3; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Observed on 2026-11-12 after publishing v1.10.0 and v1.11.0 one hour apart. The Python badge had a different problem, fixed in pull request #62.

## Story

As a person who opens the repository after a release
I want the version shown at the top to be the current one
so that I trust what I am about to install.

## Acceptance criteria

1. Verify, the day after the release, what the README shows for the version badge and record it in this task: if it shows 1.11.0, the delay is only the cache and is documented; if it still shows an older version, find the cause.
2. Decide with the owner between keeping the PyPI badge with its delay, replacing it with a badge of the latest GitHub release, or showing both; apply the decision in `README.md` and `README.es.md`.
3. `docs/pypi-publishing.md` says how long the badge can take to change after a release and how to check the real version (`https://pypi.org/project/dixi-spec-kit/`).
4. A test keeps both READMEs on the chosen badge.

## Done when

1. Tests were committed red before the change, if the badge changes.
2. `make verify` passes and CI is green.

## Related

- [Tasks](../TASKS.md)
- [PyPI publishing](../../docs/pypi-publishing.md)
