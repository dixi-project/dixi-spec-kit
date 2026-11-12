# DIXI Spec Kit and GitHub Spec Kit

## Purpose

Help a person choose between, or combine, two specification-driven development kits, with facts and their sources. GitHub Spec Kit is a mature, widely used project; this page states where DIXI Spec Kit matches it, where it goes in a different direction and where it has gaps. It is refreshed with each DIXI release.

## Sources and date

Read on **2026-11-11**. GitHub Spec Kit **v1.4.0** (released 2026-11-10): repository https://github.com/github/spec-kit (`templates/commands/`, `CHANGELOG.md`, `docs/`, `README.md`) and its open issues. DIXI Spec Kit v1.8.0. Figures about another project (agents, extensions, stars) change quickly and are quoted as that project publishes them; verify them before reusing.

## Agent commands

| GitHub Spec Kit | DIXI Spec Kit | Notes |
|---|---|---|
| `/speckit.constitution` | `/dixi.constitution` | DIXI keeps the principles in `00-governance/principles.md`, versioned, and every operation reads them. |
| `/speckit.specify` | `/dixi.specify` | DIXI places each feature under a module and a domain, checked by `dixi check`. |
| `/speckit.clarify` | `/dixi.clarify` | |
| `/speckit.plan` | `/dixi.plan` | |
| `/speckit.checklist` | `/dixi.checklist` | Both write requirement-quality items a person ticks; DIXI's `build` stops on open items. |
| `/speckit.tasks` | `/dixi.tasks` | |
| `/speckit.analyze` | `/dixi.analyze` | Both read only and report. |
| `/speckit.implement` | `/dixi.build` | DIXI requires a failing test committed before code and treats committed tests as frozen. |
| `/speckit.converge` | `/dixi.converge` | Both append convergence tasks without editing specs or code. |
| `/speckit.github.taskstoissues` (extension) | `/dixi.issues` | DIXI uses `gh` instead of an MCP server and creates nothing before the person confirms a preview. |
| — | `/dixi.onboard`, `/dixi.bugfix` | Adopting an existing codebase as validated drafts; traced bug fixes with a failing test first. |
| — | 21 more operations | Domain, architecture, contracts, data, threat model, AI, quality, verification, review, status, handoff, change, interview, risk review, release, promotion, operation, FinOps, compliance and due diligence. |

## CLI and platform

| Area | GitHub Spec Kit | DIXI Spec Kit |
|---|---|---|
| Install | `uv tool install`, `uvx`, pipx, PyPI, air-gapped | `uv tool install`, pipx, PyPI, release wheel |
| Project checks | `specify check` (installed agent tools) | `dixi check` (structure, links and goal → domain → module → feature → contract → test traceability), `dixi doctor` |
| Upgrading a project | `specify self upgrade` upgrades the CLI; a procedure for already initialised projects is an open request (issue #1210) | `dixi upgrade --dry-run` previews kit-file changes; `dixi upgrade --apply` writes only unedited kit files, atomically |
| Workflows | Executable, resumable workflows with human review gates | `dixi workflow list/show/prepare`: deterministic context packets; the agent runs the operation |
| Extensibility | Extensions, presets, workflows, bundles and catalogs (the project lists 186 community extensions and 42 presets) | Local, data-only extensions (`dixi extension`) that add operations and presets (`dixi preset`) that override kit texts and templates; no catalogs, workflows or bundles |
| MCP | Experimental read-only server | None; the CLI needs no network |
| Agents | 41 integrations plus `generic` and `none` | Claude Code and Codex (verified), `skills` (Agent Skills in `.agents/skills/`, format compatible with Cursor, VS Code/Copilot, Gemini CLI, OpenCode, Goose and Amp, not verified per agent), plus `none` |
| Systems | Windows, macOS and Linux | macOS and Linux; Windows through WSL 2 (verified in CI) |
| Runtime dependencies | Python packages | None (standard library only) |
| Languages | README in English, Chinese, Japanese and Korean; docs in English | Documents, commands and messages in English and Spanish |

## Where DIXI takes a different direction

- **Enforced rules, opt-in.** With `--controls`, agent hooks block edits to committed tests, reading secrets, signing or merging for a person, destructive commands in production mode and finishing with `make verify` red. Without it, as in Spec Kit, rules are instructions.
- **Module-level specs.** `04-modules/` holds persistent module specs linked to domains and features; Spec Kit lists module-level persistent specs as an open request (issue #1100).
- **No imposed branch strategy.** DIXI creates no branches; in Spec Kit, issue #2047 asks to configure the branch strategy without forking.
- **Safe filesystem writes.** Every write is descriptor-relative and refuses symlinks; native Windows exits with code 4 instead of writing with weaker guarantees.
- **Beyond implementation.** Operations for release, operation, FinOps, compliance and due diligence write documents only and never deploy or claim certifications.

## Gaps DIXI has today

- Two agents instead of forty-one.
- No extension, preset or catalog mechanism.
- No executable or resumable workflows.
- No documentation site (planned).
- A much smaller community and a younger project.

## Using both

The two kits use different folders (`.specify/` and `specs/` against DIXI's numbered folders and `.dixi/`). Moving a project is a manual mapping, described in [Coming from Spec Kit](coming-from-spec-kit.md).

## Related

- [Coming from Spec Kit](coming-from-spec-kit.md)
- [ADR-108](../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [Support matrix](support-matrix.md)
- [Command catalog](command-catalog.md)
