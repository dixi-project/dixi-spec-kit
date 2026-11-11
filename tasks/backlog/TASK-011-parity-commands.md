# TASK-011 — Spec Kit parity: constitution, checklist, converge and comparison docs (v1.7.0)

## Purpose

Close the visible gap with GitHub Spec Kit: add the three agent operations DIXI lacks and publish an honest comparison and a migration guide ([ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md), phase A).

## Record

- Type: feature; priority P1; level 3 (new operations in both adapters; changes the adapter contract and public claims). Created 2026-11-11. Product owner: Alfredo Castillejos.
- Scope validated on 2026-11-11 with ADR-108.

## Story

As a person who knows GitHub Spec Kit
I want the same core steps in DIXI, plus its broader method
so that I can switch without losing `constitution`, `checklist` or `converge`.

## Acceptance criteria

1. `constitution` creates or amends the project's principles in one versioned document (semantic version, dated change log, impact on other documents listed); it changes no code. Every other operation names the constitution as an input when it exists.
2. `checklist` writes requirement-quality items for a named feature and domain as unchecked boxes with stable identifiers, traced to the spec; it never ticks or deletes items. `build` stops and asks when a checklist of the feature has open items.
3. `converge` compares the code with the feature's spec, plan, tasks and constitution and appends a convergence section to the tasks, each item traced to its source and typed (missing, partial, contradicts, unrequested); it never edits specs or code, and leaves the tasks unchanged and says so when nothing is missing.
4. The three operations are installed in English and Spanish for Claude Code (`/dixi.*`) and Codex (`$dixi-*`, implicit invocation disabled), with templates where they write documents, `dixi workflow` recipes, and inventory entries so `upgrade --dry-run` reports them as new.
5. `docs/spec-kit-comparison.md` becomes a public, dated comparison (sources and date of reading, no unverifiable claims) and a "Coming from Spec Kit" guide maps every Spec Kit command to DIXI.
6. Command catalog, READMEs, support matrix and PyPI description state thirty operations.

## Done when

1. Contract changes and tests were committed red before the implementation.
2. `make verify` passes and CI is green.
3. A person ran the three operations in Claude Code on a sample project and the run is recorded in the contract.

## Progress — 2026-11-11

With the owner's authorization, the operation lists of four frozen tests gained the three names and `test_workflows.py:71` derives the catalogue size from the list, each in its own commit; new red tests in `tests/test_parity_operations.py`. `constitution`, `checklist` and `converge` are installed in both languages and both adapters (Codex skills generated with `scripts/generate-codex-skills.py`), with `dixi workflow` recipes; every operation follows `00-governance/principles.md`, and `build` stops on open checklist items. Public comparison, migration guide, contract, catalog, READMEs, support matrix and PyPI description updated; `make verify` green with 209 tests. A Claude Code 2.1.322 run on a sample project exercised the three operations and the `build` stop, recorded in the [contract](../../07-contracts/commands/parity-commands-contract.md#manual-run). Pending: release v1.7.0.

## Related

- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [Adapter contract](../../07-contracts/commands/claude-code-adapter-contract.md)
- [Command catalog](../../docs/command-catalog.md)
