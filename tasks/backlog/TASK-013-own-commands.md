# TASK-013 — DIXI's own commands: onboard, bugfix, issues and `upgrade --apply` (v1.9.0)

## Purpose

Go beyond Spec Kit where DIXI's method is broader: adopting existing projects, traced bug fixes, tasks as GitHub issues and applying kit upgrades safely ([ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md), phase C).

## Record

- Type: feature; priority P1; level 3 (`upgrade --apply` is the first command that rewrites files in an existing project). Created 2026-11-11. Product owner: Alfredo Castillejos.
- Scope validated on 2026-11-11 with ADR-108; `upgrade --apply` needs its own contract and threat review before code.

## Story

As a team with an existing codebase and a living project
I want to bring it under DIXI, fix bugs with traceability, publish tasks as issues and take kit upgrades
so that the method fits real projects, not only new ones.

## Acceptance criteria

1. `onboard` reads an existing codebase and proposes modules, specs and traceability as drafts with `{{pending: …}}` where evidence is missing; it writes only documentation and asks the person to validate the module split.
2. `bugfix` takes a bug from report to fix: reproduction, a failing test committed first, the fix, the spec or contract updated when behaviour changes, and a traced change record.
3. `issues` previews the issues it would create from a feature's tasks and creates them with `gh` only after the person confirms; it never closes or edits existing issues and needs no MCP server.
4. `dixi upgrade --apply` writes only kit-owned files whose content still matches the version that installed them, never files the person edited, reports every skipped file, and is idempotent; `--dry-run` shows exactly what `--apply` would do.
5. Both languages and both adapters; inventory, catalog, READMEs, support matrix and PyPI description updated (thirty-three operations).

## Done when

1. Contract, threat review for `upgrade --apply` and tests were committed red before the implementation.
2. `make verify` passes and CI is green.
3. A person ran `onboard` on an existing repository and `upgrade --apply` on a project created with v1.6.0, and both runs are recorded.

## Related

- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [Local core threat model](../../13-security/local-core-threat-model.md)
