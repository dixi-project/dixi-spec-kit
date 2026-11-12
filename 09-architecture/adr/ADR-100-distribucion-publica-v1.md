# ADR-100 — DIXI Spec Kit as an independent public distribution

## Purpose

Propose the architecture and boundaries of the first public distribution, without changing the rules of the private repository.

## Status

Accepted for incremental local execution on 2026-11-06. After clarifying the approach open to any agent and language, the user stated "ok, then let's go ahead with it" and authorized the first functional block: Python package/CLI, no-agent mode, help, diagnostics, checking and tests first. This validates the direction and the start of TASK-001; it does not confirm the license, rights, adapter support or availability of the later commands.

## Context

EIS-IA contains method, scripts and internal configuration. Changing its visibility would expose a history and an operation that are not part of the public product. The user has an empty folder dedicated to DIXI Spec Kit and asked for the public repository to be created when it is ready.

## Decision and execution scope

1. Keep the private EIS-IA repository private and create an independent public distribution with a new history and an explicit selection of materials.
2. Start the public numbering at v1.0.0, without inheriting EIS-IA's numbering.
3. Python package, `dixi` executable and resources included in the artifact; no private credentials needed to generate projects.
4. Define an SDD core independent of agent and stack, separate from adapters, stack profiles and policy sets. ADR-101 specifies the openness direction set by the user and proposes the exception for external project providers; integrations are not announced without evidence and inherited rules are not changed silently.
5. MIT license for the public product, with DCO for contributions (the person's decision, 2026-11-08). Only materials written for this product are distributed; the proprietary EIS-IA license does not change. Generated projects belong to whoever creates them; the initial files produced by `dixi init` may be used without attribution, as the license states.
6. Reserve write access to Dixi maintainers and allow forks. `main` is public and anyone can download or install it; nobody outside the maintainers can modify it. Contributions arrive from forks via PR and are merged only after review and with checks green (confirmed by the person on 2026-11-08).
7. Once extracted, the public core is the official source of the shared materials; the private operation consumes versions of that core and keeps its own extensions. Do not create two manually edited copies of the same core.
8. Distribute a command-based workflow: deterministic CLI, shared contracts and templates, validators and the agent adapter. The catalog covers Dixi's own capabilities; guided steps and direct invocations reuse the same contract to avoid divergence. Every distributed command needs tests and evaluation in the supported agent.
9. The initial plan specifies 16 agent commands and four CLI operations, with upgrade limited to a local preview. The nine specialized entries remain to be prioritized; the rules they cover remain in force within the main journey. The B1 contract specifies only help/version, `init --agent none`, `doctor` and `check`; the rest needs detailed contracts and evidence in their blocks.

## Consequences

Extraction and initial support take additional work, but do not expose the internal history. The product needs its own tests, documentation, releases and security controls. The CLI interface will be a published contract and later changes to it must respect compatibility or be versioned.

## Pending decisions

Resolved on 2026-11-08 by [ADR-102](ADR-102-recorte-de-alcance-v1.md): license (MIT + DCO), catalog scope (ten commands), one adapter (Claude Code) and upgrade deferred to v1.1. Still open: the product's build and CI platform in line with inherited rules. The proposed exception for public project providers is reviewed in ADR-101, without automatically affecting the operation of this repository.

## Related

- [Story](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-101: portable core](ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Specification](../../docs/product-spec.md)
- [Proposed catalog](../../docs/command-catalog.md)
- [Joint review](../../docs/history/v1-design-review.md)
- [Proposed contract](../../07-contracts/commands/command-contract.md)
- [Allowlist exporter](../../docs/repository-settings.md)
