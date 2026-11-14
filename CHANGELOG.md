# Changelog

## Purpose

Record changes to the public DIXI Spec Kit product. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [SemVer](https://semver.org/).

## [Unreleased]

### Added

- Documentation index and guides for what surrounds the commands (TASK-030), in English and Spanish and on the documentation site: `docs/documentation.md` lists every user document by what the person wants to do, and both READMEs link it from a Documentation section; `docs/subagents.md`, generated from the packaged subagent files by `scripts/build-subagent-reference.py`; `docs/controls.md`, what each of the five hooks of `--controls` blocks and what none covers; `docs/extensions-and-presets.md`, how to write one, with the examples `examples/extension-minimal` and `examples/preset-minimal` that a test installs; and a Spanish version of the recipes guide.

## [1.11.1] — 2026-11-13

### Changed

- The READMEs show the latest GitHub release instead of the PyPI version (TASK-026): the PyPI badge is cached for six hours and looked stale after a release. `docs/pypi-publishing.md` says how to check the real version (#64).
- The `make verify` jobs of the `verify` workflow have a limit of 30 minutes instead of 15 (TASK-027). This does not prevent the cancellation of macOS jobs that wait for a runner, as first assumed: GitHub cancels a job that no hosted runner acquires, and `timeout-minutes` does not count while it waits. `docs/repository-settings.md` explains the cause and says to re-run the failed jobs (#64, corrected in #67).
- `docs/local-development.md` describes how an agent session that works in an isolated worktree hands off to the maintainer's checkout (TASK-028, #64).

### Fixed

- The Python badge of the READMEs said "missing": it read the package's Python classifiers, which the package does not declare. It now reads `requires-python` from `pyproject.toml` and shows `>=3.11` (#62).
- Release notes lost the text of an entry that quoted the `no changelog entry` marker, as in the notes of v1.11.0 (TASK-025): `make release` now treats as a marker only a comment alone on its line (#64).

<!-- no changelog entry: #63, #65, #66, #68 -->

## [1.11.0] — 2026-11-12

### Added

- `dixi mode` (TASK-022, [contract](07-contracts/commands/automated-controls-contract.md#dixi-mode)): prints `MODE` and, for `mvp`, which of the six items `/dixi.promote` reviews (tests and budgets, threat model, data retention, runbooks and SLOs, release and rollback, owners) have no evidence yet, meaning a document without `{{pending: …}}` blanks. With `--json`. Read-only: it writes nothing and has no option to change `MODE` (#61).
- `make release` warns about unannounced changes (TASK-023): it lists the pull requests merged since the previous tag whose number or branch the CHANGELOG section of the version does not mention and asks the maintainer to type `yes` before going on. Pull requests that need no entry are marked in the section with `<!-- no changelog entry: #N -->`, which is left out of the release notes (#61).

### Changed

- `/dixi.status` resumes a session (TASK-021): besides the state and the next step, it reports what the last session did and left open from `.context/handoff.md` when it exists, lists the recent changes under `07-contracts/` from the Git history and lists the open tasks by ID. It stays read-only: no writes, commits or pushes. Same text for Claude Code, Codex and Agent Skills, in English and Spanish (#60).

## [1.10.0] — 2026-11-12

### Added

- A DIXI Spec Kit logo in `docs/assets/` (light, dark and a standalone mark, as self-contained SVG): the READMEs open with it and with PyPI, Python, verification and license badges, and the documentation site shows the mark in its header and as its icon (#52).
- The PyPI page (`packaging/README.md`) opens with the logo, loaded from an absolute URL on `main`; it shows from this version (#53).
- Command reference (TASK-016): one page per operation in `docs/commands/`, in English and Spanish, with purpose, invocation for Claude Code, Codex and Agent Skills, when to use it, steps, files read and written, stops and human gates, and next step. `scripts/build-command-reference.py` (standard library) generates the pages from the packaged command texts and the workflow graph; `--check` and a test fail when a page is missing or out of date. The documentation site gains a Commands section in both languages (#54).
- Command guide (TASK-017): `docs/command-catalog.md`, with a Spanish version in `docs/command-catalog.es.md`, is now a guide for users: the journey map, a "which command when" table of the thirty-three operations linked to their reference pages, and a walkthrough from `dixi init` to a release. The documentation site serves a document's `.es.md` version in the Spanish tree when it exists (#55).
- Command examples (TASK-018): every reference page shows a realistic example for Claude Code, Codex and Agent Skills, from `scripts/site/command-examples.json`. `README.es.md` now mentions `/dixi.interview`, `/dixi.risk-review` and the subagents, as the English README does (#56).
- CLI reference (TASK-019): `docs/cli/`, in English and Spanish, with one page per `dixi` terminal command (usage, arguments, options, subcommands) and the exit-code table. `scripts/build-cli-reference.py` generates it from the real argument parser and the message catalogs; `--check` and a test fail when a command or option is missing. The documentation site publishes it under `cli/` (#57).
- Spanish site pages (TASK-020): the migration guide has a Spanish version (`docs/coming-from-spec-kit.es.md`), so the Spanish tree shows the command guide, the command and CLI references and the migration guide in Spanish; the support matrix keeps its Spanish summary and, like every page still only in English, the notice. A test lists the pages with Spanish versions and checks that they keep the same links and that every anchor link resolves (#58).

### Changed

- The working catalog and the v1 design review moved to `docs/history/` with a note that they are historical records; they are no longer published on the documentation site. `docs/product-spec.md` no longer describes shipped commands as provisional (#55).
- The support matrix lists `--agent skills` as supported for discovery and explicit invocation in OpenCode 1.19.5, recorded in the adapter contract; other agents stay format compatible, not verified (#50).

## [1.9.0] — 2026-11-12

### Added

- `dixi init <dir> --existing` adds DIXI to a folder that already has files: creates only what is missing, never overwrites, reports the files it kept and records them with the kit hash so `upgrade --apply` never overwrites them ([contract](07-contracts/commands/local-core-contract.md#adding-dixi-to-an-existing-folder), threat T13). `--existing --controls` needs an agent with hooks, like `init`.
- Documentation site in English and Spanish ([ADR-108](09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) phase E): `scripts/build-site.py` (standard library) pre-renders the READMEs and `docs/` under `/en/` and `/es/` with `hreflang`, canonical URLs, a root redirect by browser language, a search index and interface strings in `scripts/site/<lang>.json`; `.github/workflows/pages.yml` builds it on every pull request and publishes it from `main` (enabling Pages is the maintainer's action).
- `--agent skills` ([ADR-108](09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) phase D, [contract](07-contracts/commands/agent-skills-adapter-contract.md)): the thirty-three operations as [Agent Skills](https://agentskills.io/specification) in `.agents/skills/`, derived from the Codex skills, with `disable-model-invocation: true` and neutral `dixi-<operation>` references, for Cursor, VS Code/Copilot, Gemini CLI, OpenCode and other compatible agents. Listed as format compatible, not verified per agent; `--controls` is not available for it.
- `dixi extension add|list|remove` ([ADR-109](09-architecture/adr/ADR-109-local-presets-and-extensions.md), [contract](07-contracts/commands/extensions-contract.md), threat T14): a team's own operations from a local, data-only folder, installed as `dixi-<extension>-<operation>` for Claude Code, Codex or Agent Skills; validated completely before writing, never executed, never shadowing a kit operation, recorded outside the kit inventory and removable without touching edited files.
- `dixi preset add|list|remove` ([ADR-109](09-architecture/adr/ADR-109-local-presets-and-extensions.md), [contract](07-contracts/commands/presets-contract.md), threat T15): a team's versions of kit operation texts and templates from a local, data-only folder, applied only to files still equal to the kit, behind `.dixi/overrides/` and by priority; `upgrade` never overwrites them and removal restores the kit text where unchanged.

### Fixed

- The documentation site's home page title no longer repeats the product name.
- The Spanish summary of the support matrix no longer lists applying upgrades as missing.

## [1.8.0] — 2026-11-11

### Added

- `/dixi.onboard` (draft modules and features from an existing codebase, after the person validates the split), `/dixi.bugfix` (failing test committed before the fix, traced `BUG-NNN.md`) and `/dixi.issues` (tasks to GitHub issues with `gh`, after a confirmed preview), in English and Spanish, for Claude Code and Codex, with `dixi workflow` recipes ([ADR-108](09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) phase C, [contract](07-contracts/commands/own-commands-contract.md)). Thirty-three operations in total.
- `dixi workflow show/prepare` recipes, in English and Spanish, for the nineteen operations that had none (tasks, build, verify, review, analyze, status, handoff, change, data, quality, ai, release, promote, operate, finops, compliance, duediligence, interview, risk-review), so all thirty operations have one ([ADR-108](09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) phase B, [TASK-012](tasks/backlog/TASK-012-workflow-recipes.md)); the workflow quickstart lists every operation with its target kinds, and `tests/test_workflow_coverage.py` fails if a command lacks a complete recipe.
- `dixi upgrade --apply` ([ADR-108](09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) phase C, [contract](07-contracts/commands/block-a-contract.md#dixi-upgrade---apply)): writes only `updatable` and `new` kit files, each re-checked right before writing and replaced atomically; never touches conflicts, deleted or obsolete files; idempotent, recovers after an interruption, and refuses to run twice at once (`.dixi-upgrade.lock`, exit 3). Threats T09–T12 added to the local core threat model.

### Changed

- `dixi upgrade` needs exactly one of `--dry-run` or `--apply` (exit 2 otherwise). `--dry-run` reports a symlinked or non-regular kit path as a conflict instead of failing, and a file that already has the new content as updatable (it is only recorded).

## [1.7.0] — 2026-11-11

### Added

- Spec Kit parity ([ADR-108](09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) phase A, [contract](07-contracts/commands/parity-commands-contract.md)): `/dixi.constitution` (versioned principles in `00-governance/principles.md`, read by every operation), `/dixi.checklist` (unchecked, traced requirement-quality items; `/dixi.build` stops on open items) and `/dixi.converge` (compares code with specs and appends typed, traced convergence tasks), in English and Spanish, for Claude Code and Codex, with `dixi workflow` recipes. Thirty operations in total.
- `docs/coming-from-spec-kit.md`, a command map and migration guide; `docs/spec-kit-comparison.md` rewritten as a public, dated and sourced comparison (GitHub Spec Kit v1.4.0, read on 2026-11-11), including DIXI's gaps.

### Changed

- Every operation follows `00-governance/principles.md` when it exists and reports conflicts instead of resolving them silently.
- Tests: the operation lists of `test_claude_adapter`, `test_codex_adapter`, `test_block_a` and `test_workflows` include the three operations, and the workflow catalogue size is derived from the list (both authorized by the owner on 2026-11-11, in their own commits).

### Fixed

- The support matrix says twenty-seven commands and skills (it still said twenty-five), and its Spanish summary states Windows support through WSL 2. The PyPI description (`packaging/README.md`) lists the twenty-seven commands, every CLI command, `--controls`, Codex without "preview", PyPI installation and WSL 2. `tests/test_doc_counts.py` derives the count from the packaged commands so these texts cannot drift again.

## [1.6.0] — 2026-11-10

### Added

- Windows is supported through WSL 2 with the project on the Linux filesystem ([ADR-107](09-architecture/adr/ADR-107-windows-support.md) phase 1 done): support matrix row, a Windows (WSL 2) section in `docs/local-development.md`, README notes and the recorded CI run in the local core contract. Projects under `/mnt/c` and native Windows (exit 4) stay unsupported.
- Experimental CI workflow `wsl.yml` for [ADR-107](09-architecture/adr/ADR-107-windows-support.md) phase 1: on `windows-latest` it sets up Ubuntu 24.04 in WSL 2 (`Vampire/setup-wsl`, pinned by SHA), fails unless the kernel is WSL 2 and the project is on ext4 under `~`, and runs `make verify`, `dixi init --agent claude --controls`, `check`, `upgrade --dry-run` and three blocking hooks. Not a required check; Windows stays unsupported until phase 1 is closed.

### Changed

- The READMEs install from PyPI (`uv tool install dixi-spec-kit`, `pipx install dixi-spec-kit`); Git tags and the release wheel stay as alternatives. Fixed the wheel name in the offline instructions, which still said 1.3.0.
- `examples/i18n-site` follows the Next.js 16 file convention: `middleware.ts` is now `proxy.ts` and exports `proxy` instead of `middleware`; `config.matcher` is unchanged. The example's specs, README and the comment in `lib/i18n.mjs` name `proxy.ts`. `tests/test_example_i18n_site.py` now expects `proxy.ts` (authorized one-line change) and the new `tests/test_example_next16_proxy.py` requires `export function proxy`, keeps `export const config` with its matcher and rejects `middleware.ts`.

## [1.5.0] — 2026-11-10

### Added

- Publication on PyPI through Trusted Publishing ([ADR-106](09-architecture/adr/ADR-106-pypi-trusted-publishing.md)): `.github/workflows/publish.yml` uploads the verified wheel and sdist when a release is published, with no stored token and a protected `pypi` environment. This is the first release published there.
- Windows decision ([ADR-107](09-architecture/adr/ADR-107-windows-support.md)): Windows will be supported through WSL 2; native Windows keeps exit 4. Phase 0: tests of the explicit refusal on every platform and a `windows-latest` CI job that proves `dixi` exits 4 and writes nothing.

- Second public example, `examples/i18n-site`: a Next.js (TypeScript) site in English and Spanish created with `dixi init --agent claude --profile site`, with language-prefixed routes, a root redirect by `Accept-Language`, `hreflang` and canonical URLs per language, and JSON catalogs, traced from goal to `node --test` tests. No dependencies or `npm install`; its `make verify` skips the Node tests with a message when `node` is missing.

### Changed

- `.gitattributes` forces LF and `scripts/verify-source.py` reads text as UTF-8, so checkouts and hashes are the same on every platform.
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
