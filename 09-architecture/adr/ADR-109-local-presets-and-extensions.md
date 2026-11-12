# ADR-109 — Local presets and extensions

## Purpose

Decide how a team adapts DIXI Spec Kit without forking it: overriding templates and operation texts (presets) and adding its own operations (extensions), safely and without network access ([ADR-108](ADR-108-spec-kit-parity-and-beyond.md) phase E, [TASK-015](../../tasks/backlog/TASK-015-extensibility-and-site.md)).

## Status

Accepted on 2026-11-12 by the responsible person ("Apruebo tal cual"). Proposed the same day.

## Context

- GitHub Spec Kit offers extensions, presets, workflows, bundles and network catalogs; its own documentation warns that community catalogs are not audits and asks people to review the source ([comparison](../../docs/spec-kit-comparison.md)).
- DIXI's core writes only through descriptor-relative, no-follow operations, never runs project code and needs no network ([ADR-101](ADR-101-nucleo-sdd-portable-e-integraciones.md), [ADR-107](ADR-107-windows-support.md)). Hooks are the only executable resources, and they ship with the kit.
- `dixi upgrade --apply` already distinguishes kit files from the person's edits through the inventory in `.dixi/project.json`.

## Decision

1. **Local only, data only.** Presets and extensions are folders of Markdown and JSON added from the local disk (`dixi preset add <folder>`, `dixi extension add <folder>`). No network catalog in this version, no scripts, no hooks, no executable files: anything else is refused.
2. **Presets override, they do not add.** A preset holds `preset.json` (`id`, `version`, `priority`, `requires` with a kit version range) and replacement files for kit templates and operation texts in both languages. Resolution order, highest first: `.dixi/overrides/` (the project's own), presets by priority, the kit. `upgrade` never overwrites a resolved override; a kit change under an override is reported as a conflict.
3. **Extensions add operations.** An extension holds `extension.json` (`id`, `version`, `requires`, `operations`) and, per operation, English and Spanish texts with the same frontmatter and limits as kit operations. They are installed for the project's adapter (Claude Code command, Codex skill or Agent Skill) under the name `dixi-<extension>-<operation>`, so they can never shadow a kit operation. Extensions cannot add hooks or change `--controls`.
4. **Validated like the core.** IDs match `[a-z0-9]+(-[a-z0-9]+)*`; every path passes `safe_path`; size and count limits; every installed file is recorded in the inventory with its origin (`kit`, `preset:<id>`, `extension:<id>`), so `check`, `doctor` and `upgrade` can explain where each file comes from.
5. **Reversible.** `dixi preset remove <id>` and `dixi extension remove <id>` remove only unedited files they installed and report the rest, as `upgrade --apply` does.

## Alternatives considered

- **Network catalogs from the start.** Rejected for now: they need network access, trust decisions and supply-chain review; local folders cover team needs first. A later ADR can add catalogs on top of the same format.
- **Executable extensions (scripts, hooks).** Rejected: they would break the guarantee that DIXI never runs third-party code; hooks stay kit-owned and reviewed.
- **Letting extensions replace kit operations.** Rejected: replacing belongs to presets, where it is explicit, prioritised and reported by `upgrade`.

## Consequences

- New commands `dixi preset add|list|remove` and `dixi extension add|list|remove`, with contracts, threat review (tampering through crafted folders, path escapes, name shadowing) and tests first.
- The inventory gains an origin per file; projects from earlier versions read as all-`kit`.
- The comparison with Spec Kit can state local extensibility, and keep catalogs, workflows and bundles as gaps.

## Related

- [ADR-108](ADR-108-spec-kit-parity-and-beyond.md)
- [TASK-015](../../tasks/backlog/TASK-015-extensibility-and-site.md)
- [Local core threat model](../../13-security/local-core-threat-model.md)
