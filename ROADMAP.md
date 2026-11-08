# DIXI Spec Kit roadmap

## Purpose

Show what each public release includes and what comes next. Only what has tests and evidence is announced as available.

## v1.0.0 — first public release (2026-11-08)

`dixi` CLI (`init`, `doctor`, `check`, `workflow`), no-agent mode, Claude Code adapter with ten commands, Spanish/English documentation, the `examples/notes` example, public CI and MIT license. Scope set in [ADR-102](09-architecture/adr/ADR-102-recorte-de-alcance-v1.md).

## v1.1.0 — English first and design, continuity and change commands (2026-11-08)

- English as the repository's primary language and the CLI default (`--lang es` remains available).
- Agent commands `/dixi.domain`, `/dixi.architecture`, `/dixi.contract`, `/dixi.threat-model`, `/dixi.handoff` and `/dixi.change`.
- `dixi upgrade --dry-run`: compare the project with its original inventory and list updatable files and conflicts without writing.

## v1.2.0 — Codex adapter (2026-11-08, shipped in 1.3.0)

Codex integration evaluated against its own capability and control matrix.

## v1.3.0 — specialized commands (2026-11-08)

`/dixi.data`, `quality`, `ai`, `release`, `promote`, `operate`, `finops`, `compliance` and `duediligence`, each with an explicit contract and limits.

## v1.4.0 — project profiles and core templates

`dixi init --profile site|app|platform [--regulated]` with generic templates for data, architecture, engineering, quality, security and AI ([ADR-104](09-architecture/adr/ADR-104-project-profiles-and-content.md)). Without `--profile`, nothing changes.

## v1.5.0 — remaining content areas

Templates for governance, business, platform, observability, delivery, operations, product, UX, FinOps, compliance, due diligence and the other method areas, assigned to profiles.

## v1.6.0 — opt-in automated controls

`dixi init --controls`: agent hooks for frozen tests, secrets, signing and approval, production mode and verification before stopping ([ADR-105](09-architecture/adr/ADR-105-opt-in-automated-controls.md)); Claude Code subagents; `interview` and `risk-review` operations; `dixi placeholders` and `dixi pr-size`.

## Later

PyPI publication (requires its own ADR), a second example language and Windows support if safe filesystem operations can be guaranteed.

## Related

- [Support matrix](docs/support-matrix.md)
- [Changelog](CHANGELOG.md)
