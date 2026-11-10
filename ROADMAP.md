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

## v1.4.0 — profiles, full content and opt-in controls (2026-11-09)

Released together; originally planned as v1.4.0 to v1.6.0.

- `dixi init --profile site|app|platform [--regulated]` with generic templates for every method area: up to 273 per language ([ADR-104](09-architecture/adr/ADR-104-project-profiles-and-content.md)). Without `--profile`, nothing changes.
- `dixi init --controls`: agent hooks for frozen tests (edit tools and shell), secrets, signing and approval, production mode and verification before stopping, for Claude Code and Codex ([ADR-105](09-architecture/adr/ADR-105-opt-in-automated-controls.md)).
- Claude Code subagents, `interview` and `risk-review` operations, `dixi placeholders` and `dixi pr-size`.

## v1.5.0 — PyPI, second example and the Windows decision (2026-11-10)

- First release on PyPI, published by CI through Trusted Publishing ([ADR-106](09-architecture/adr/ADR-106-pypi-trusted-publishing.md)).
- `examples/i18n-site`: a Next.js site in English and Spanish, traced from goal to tests.
- `protect_tests` also stops inline interpreter code that rewrites committed tests.
- Windows through WSL 2 accepted ([ADR-107](09-architecture/adr/ADR-107-windows-support.md)); phase 0 verifies the native refusal in CI.

## Later

- Windows through WSL 2, phase 1: a recorded manual run and the support matrix row ([ADR-107](09-architecture/adr/ADR-107-windows-support.md)).
- A native Windows backend only with real demand and a new validation.

## Related

- [Support matrix](docs/support-matrix.md)
- [Changelog](CHANGELOG.md)
