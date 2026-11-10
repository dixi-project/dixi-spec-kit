# Changelog

## Purpose

Record changes to the public DIXI Spec Kit product. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [SemVer](https://semver.org/).

## [Unreleased]

### Added

- Second public example, `examples/i18n-site`: a Next.js (TypeScript) site in English and Spanish created with `dixi init --agent claude --profile site`, with language-prefixed routes, a root redirect by `Accept-Language`, `hreflang` and canonical URLs per language, and JSON catalogs, traced from goal to `node --test` tests. No dependencies or `npm install`; its `make verify` skips the Node tests with a message when `node` is missing.

### Changed

- `protect_tests` also blocks inline interpreter code (`python -c`, heredocs, `node -e`, `ruby`/`perl -e`, `php -r`) that writes, moves or deletes a committed test named in quotes.

## [1.4.0] — 2026-11-09

### Added

- Project profiles: `dixi init --profile minimal|site|app|platform [--regulated]`. `minimal` (the default) is the unchanged baseline; the other profiles add generic templates in English and Spanish. `.dixi/project.json` records `profile` and `regulated`; `doctor` reports them.
- `dixi upgrade --dry-run --profile <name> [--regulated]` shows the files another profile would add.
- Templates for the remaining method areas (block E): governance, business, platform, flows, contracts, observability, delivery, operations, product, UX, knowledge base, references, stack layouts, FinOps, compliance, research, growth, customer success, fixtures and due diligence. Profile totals: `site` 77, `app` 190, `platform` 241; with `--regulated` 94, 226 and 273. Compliance templates state they are not legal advice.
- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1) and `SUPPORT.md` in the repository.
- Opt-in automated controls: `dixi init --agent claude|codex --controls` installs five standalone hooks in `.dixi/hooks/` (`protect_tests`, `guard_secrets`, `guard_attestation`, `mode_gate`, `verify_on_stop`), wired through `.claude/settings.json` or `.codex/hooks.json` with hooks only. Without `--controls`, nothing changes. `.dixi/project.json` records `controls`; `doctor` reports it; `upgrade --dry-run --controls` lists the files. `protect_tests` covers the edit tools and shell commands that write, move or delete a committed test.
- Operations `/dixi.interview` (`$dixi-interview`) and `/dixi.risk-review` (`$dixi-risk-review`), and four Claude Code subagents (`dixi-architect`, `dixi-tester`, `dixi-developer`, `dixi-reviewer`), optional for existing projects.
- `dixi placeholders [--strict]` and `dixi pr-size [--base] [--max]` (read-only; `pr-size` is the only subcommand that runs Git).
- `AGENTS.md` declares `wip_limit: 3`; `/dixi.build` stops when the person already has that many open pull requests.

### Changed

- Profile templates are optional after creation: deleting one does not fail `dixi check`; `upgrade --dry-run` lists it as missing.
- The project inventory accepts up to 1 000 managed files (was 500).

### Known limitations

- Hooks are a second layer, not the last one: `protect_tests` does not see files written by an interpreter's own code (`python -c`, `node -e`) or through shell variables. In Codex, hooks run only in a trusted project after the person approves them with `/hooks`.
- Windows unsupported; not on PyPI.

## [1.3.0] — 2026-11-08

### Added

- Nine specialized operations for Claude Code (`/dixi.<operation>`) and Codex (`$dixi-<operation>`), in English and Spanish: `data`, `quality`, `ai`, `release`, `promote`, `operate`, `finops`, `compliance`, `duediligence`. Each writes documents in its area only and never runs migrations, deploys, edits `MODE`, queries billing or claims certifications. Optional for projects from earlier versions (`dixi upgrade --dry-run` lists them as new).
- `dixi init .` initializes the current directory when it is empty.

### Changed

- An unsafe `init` destination now reports how to choose a valid one instead of a generic unsafe-path message.

## [1.2.0] — 2026-11-08 (released as part of 1.3.0)

### Added

- Codex adapter: `dixi init --agent codex` installs sixteen Agent Skills in `.agents/skills/dixi-<operation>/`, invoked as `$dixi-<operation>`, with implicit invocation disabled. Same steps and limits as the Claude Code commands; `doctor`, `check` and `upgrade --dry-run` support it.

### Fixed

- Claude Code command frontmatter values are now double-quoted, valid YAML: the `build` description contained `: ` and several argument hints were bracketed (parsed as lists by strict YAML parsers). Existing projects see these files as updatable in `dixi upgrade --dry-run`.

## [1.1.0] — 2026-11-08

### Changed

- English is the repository's primary language; README, contributing guide, policies, specs and ADRs are in English, with a Spanish README (`README.es.md`).
- **Behavior change:** the CLI and new projects default to English. Use `dixi --lang es …` for Spanish. Inside an existing project, messages follow the project's language when `--lang` is not given.

### Added

- Six Claude Code commands in English and Spanish: `/dixi.domain`, `/dixi.architecture`, `/dixi.contract`, `/dixi.threat-model`, `/dixi.handoff` (writes `.context/handoff.md`) and `/dixi.change` (change proposal with impact).
- `dixi upgrade --dry-run`: read-only plan classifying files as unchanged, updatable, conflict, new, missing or obsolete; human and JSON output. Applying upgrades is not available yet.
- `dixi doctor` reports installed versus available commands and suggests the upgrade plan.

### Compatibility

- Projects created with v1.0.0 keep passing `dixi check`: the six new commands are optional in their inventory.

## [1.0.0] — 2026-11-08 — first public release

### Added

- `dixi` CLI with no runtime dependencies: `init`, `doctor`, `check`, `workflow list/show/prepare`, `--help`, `--version`, `--lang es|en`, `--json`.
- `dixi init --agent none|claude`: traceable documentary baseline that never overwrites and rejects symlinks and unsafe paths.
- Claude Code adapter: `CLAUDE.md` and ten commands `/dixi.discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze`, `status` in Spanish and English; no hooks or permissions.
- `dixi check`: structure, local Markdown links and the goal → domain → module → feature → contract → test graph.
- Eight shared procedures with context preparation and a source manifest with hashes.
- Public example `examples/notes` with an evolution and impact analysis.
- Spanish/English documentation, support matrix, CONTRIBUTING with DCO, SECURITY and credential-free public CI.
- MIT license.

### Known limitations

- No `dixi upgrade`; Windows unsupported; a single adapter (Claude Code). See the [support matrix](docs/support-matrix.md).
- Renaming or deleting files generated by `init` makes `dixi check` fail, because they are part of the project inventory.

## Related

- [Roadmap](ROADMAP.md)
- [Support matrix](docs/support-matrix.md)
