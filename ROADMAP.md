# DIXI Spec Kit roadmap

## Purpose

Show what each public release includes and what comes next. Only what has tests and evidence is announced as available.

## v1.0.0 — first public release (2026-11-08)

`dixi` CLI (`init`, `doctor`, `check`, `workflow`), no-agent mode, Claude Code adapter with ten commands, Spanish/English documentation, the `examples/notes` example, public CI and MIT license. Scope set in [ADR-102](09-architecture/adr/ADR-102-recorte-de-alcance-v1.md).

## v1.1.0 — English first and design, continuity and change commands (2026-11-08)

- English as the repository's primary language and the CLI default (`--lang es` remains available).
- Agent commands `/dixi.domain`, `/dixi.architecture`, `/dixi.contract`, `/dixi.threat-model`, `/dixi.handoff` and `/dixi.change`.
- `dixi upgrade --dry-run`: compare the project with its original inventory and list updatable files and conflicts without writing.

## v1.2.0 — Codex adapter (in progress)

Codex integration evaluated against its own capability and control matrix.

## v1.3.0 — specialized commands

`/dixi.data`, `quality`, `ai`, `release`, `promote`, `operate`, `finops`, `compliance` and `duediligence`, each with an explicit contract and limits.

## Later

PyPI publication (requires its own ADR), a second example language and Windows support if safe filesystem operations can be guaranteed.

## Related

- [Support matrix](docs/support-matrix.md)
- [Changelog](CHANGELOG.md)
