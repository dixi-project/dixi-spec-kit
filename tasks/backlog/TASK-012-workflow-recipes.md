# TASK-012 — `dixi workflow` recipes for every operation (v1.8.0)

## Purpose

Give every operation a deterministic `dixi workflow show/prepare` recipe, not only the eight definition and design operations ([ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md), phase B).

## Record

- Type: feature; priority P2; level 2 (new packaged data; no change to file-writing code). Created 2026-11-11. Product owner: Alfredo Castillejos.
- Scope validated on 2026-11-11 with ADR-108.

## Story

As a person who works without an agent, or with one DIXI does not install
I want to prepare the context of any operation from the terminal
so that the whole method is reachable, not only its first steps.

## Acceptance criteria

1. `dixi workflow list` shows every operation installed by the adapters; `show` and `prepare` work for each, in English and Spanish, with human and JSON output.
2. Each recipe names its inputs, outputs, stop conditions and human gates, consistent with the operation's adapter text; a test fails if an operation has no recipe.
3. `prepare` stays read-only outside the declared packet and refuses targets outside the project, as today.
4. The workflow quickstart documents the full list.

## Done when

1. Tests were committed red before the recipes.
2. `make verify` passes and CI is green.

## Closed — 2026-11-11

Released in v1.8.0, together with phase C (owner's decision: one release for both phases).

## Related

- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [Workflow preparation contract](../../07-contracts/commands/workflow-preparation-contract.md)
- [Workflow quickstart](../../docs/workflow-quickstart.md)
