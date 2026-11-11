# TASK-014 — Generic Agent Skills adapter (v1.9.0)

## Purpose

Reach more agents with one standard format instead of one adapter per tool ([ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md), phase D).

## Record

- Type: feature; priority P2; level 3 (new adapter; changes the support matrix). Created 2026-11-11. Product owner: Alfredo Castillejos.
- Scope validated on 2026-11-11 with ADR-108.

## Story

As a person who uses an agent other than Claude Code or Codex
I want DIXI's operations installed in a format my agent reads
so that I can use the method without waiting for a dedicated adapter.

## Acceptance criteria

1. A new `--agent` value installs every operation as an Agent Skill in the standard layout, in English and Spanish, without permissions, MCP servers or settings.
2. The format is checked against the published Agent Skills specification at the time of implementation, and the version read is recorded.
3. The support matrix lists an agent as supported only after a recorded run; others appear as "format compatible, not verified".
4. `doctor`, `check` and `upgrade --dry-run` recognise the new adapter's files.

## Done when

1. Tests were committed red before the adapter.
2. `make verify` passes and CI is green.
3. At least one agent other than Claude Code and Codex ran an operation and the run is recorded.

## Related

- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [Codex adapter contract](../../07-contracts/commands/codex-adapter-contract.md)
