# ADR-102 — Scope reduction proposal for v1.0.0

## Purpose

Record a proposal to reduce the minimum scope of v1.0.0 to a competitive and verifiable level, after comparing progress with GitHub Spec Kit ([comparison](../../docs/spec-kit-comparison.md)).

## Status

**Accepted** on 2026-11-08 by the responsible person (Alfredo Castillejos) in a joint validation of story, ADR and assumptions: "Validate reduction", "MIT + DCO" and "Defer to v1.1" for `upgrade --dry-run`. [TASK-001](../../tasks/backlog/TASK-001-lanzamiento-v1.md) is updated accordingly. Acceptance does not by itself accredit adapter support: it is announced only with the evidence from [TASK-003](../../tasks/backlog/TASK-003-adaptador-claude-code.md).

## Context

B1 and B2a deliver a verifiable local core (CLI, no-agent mode, diagnostics, structural checking and preparation of eight procedures), but no command installable inside an agent. The comparison with GitHub Spec Kit shows that its value proposition is precisely installing commands in the agent the person already uses. Without an adapter, v1.0.0 would be a documentary template with validators.

TASK-001 currently requires two adapters evaluated against two languages, `upgrade --dry-run` and 16 commands. That scope delays first contact with external users.

## Proposal

1. **One adapter in v1.0.0: Claude Code**, with real evaluation of its capabilities and controls. Codex moves to v1.1. ADR-101 does not change: the core remains agent-independent and no provider is assumed.
2. **Ten agent commands:** `discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze` and `status`. The design ones (`domain`, `architecture`, `contract`, `threat-model`) remain available through `dixi workflow prepare`. Deferred to v1.1: `handoff`, `change` and the nine specialized entries.
3. **`--agent none` is kept** as the documentary mode.
4. **One public example** from idea to verified code, with one evolution and its impact analysis. The second language moves to v1.1.
5. **Systems:** macOS and Linux with real evidence. Windows declared as unsupported.
6. **`upgrade --dry-run`:** deferred to v1.1 (the person's decision, 2026-11-08). Documentation cannot promise upgrades in the meantime; the hashed inventory in `.dixi/project.json` is kept as the basis for that version.
7. **No extensions, presets or catalogs** in v1.0.0.

## What does not change

Human accountability (ADR-010), tests first and frozen, gates, structural checks, `make verify`, pending license, clean history and the [publication](../../docs/publication-readiness.md) gate. No deferred capability is announced as available.

## Decisions resolved on 2026-11-08

- **License: MIT** for the product's code, resources and documentation, with **DCO** (`Signed-off-by`) for contributions, consistent with ADR-010. The distributed resources were written for this product; no proprietary EIS-IA material is included.
- **Repository model:** `main` public and downloadable by anyone; contributions only via fork and PR; only Dixi maintainers merge, with mandatory review and checks; no direct push, force push or deletion of `main`.

## Decisions that remain with the person

- **License.** Technical recommendation: MIT for the product, with DCO (ADR-010's `Signed-off-by`) instead of a CLA for contributions; Apache-2.0 if an explicit patent grant and trademark clause are desired. This is not legal advice. It must first be confirmed that Dixi holds the rights to the selected EIS-IA materials; the references in `19-references/` keep their original license and are not distributed under MIT.
- Availability of the names `dixi` and `dixi-spec-kit` in the registry and on GitHub.
- Creation of `main` on the remote and every merge.

## Consequences

If validated, v1.0.0 arrives sooner and with less surface to test, and adoption can be measured before expanding. In exchange, it ships with fewer capabilities than designed and with a single adapter, which must be made explicit in the README and support matrix. If rejected, TASK-001 and ADR-101 remain the scope.

## Related

- [Comparison with GitHub Spec Kit](../../docs/spec-kit-comparison.md)
- [ADR-100](ADR-100-distribucion-publica-v1.md)
- [ADR-101](ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [TASK-001](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [TASK-003](../../tasks/backlog/TASK-003-adaptador-claude-code.md)
- [Command catalog](../../docs/command-catalog.md)
- [Publication](../../docs/publication-readiness.md)
