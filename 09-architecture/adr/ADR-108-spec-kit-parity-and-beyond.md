# ADR-108 — Spec Kit parity and DIXI's own extensions

## Purpose

Decide which commands, CLI features and documentation DIXI Spec Kit adds to compete fairly with GitHub Spec Kit, in what order, and where DIXI goes further instead of copying.

## Status

Accepted on 2026-11-11 by the responsible person: phases A→E in this order; all four extras of phase C; a documentation site on GitHub Pages built with the standard library; a generic Agent Skills adapter for more agents.

## Context

GitHub Spec Kit v1.4.0 (2026-11-10, read from `github/spec-kit` on 2026-11-11) installs nine agent commands: `constitution`, `specify`, `clarify`, `plan`, `checklist`, `tasks`, `analyze`, `implement` and `converge`; `taskstoissues` moved to its `github` extension in 1.3.0. Its CLI adds `integration`, `extension`, `preset`, `workflow` (executable, resumable), `bundle`, catalogs, `self upgrade` and an experimental read-only MCP server. It supports 41 agents plus `generic` and `none`, and documents itself on a DocFX site.

DIXI Spec Kit v1.6.0 installs twenty-seven operations for Claude Code and Codex, six of which cover Spec Kit's `specify`, `clarify`, `plan`, `tasks`, `analyze` and `implement` (`build`); the other twenty-one (domain, architecture, contracts, data, threats, AI, quality, review, release, operation, FinOps, compliance, due diligence…) have no Spec Kit counterpart. DIXI lacks `constitution`, `checklist` and `converge`; only eight of its operations have `dixi workflow` recipes; it supports two agents and has no extension mechanism.

Several limits Spec Kit acknowledges in its own issues are DIXI strengths: module-level persistent specs (#1100; DIXI has `04-modules/` checked by `dixi check`), upgrading initialised projects (#1210; DIXI has `upgrade --dry-run`), a fixed branch strategy (#2047; DIXI imposes none). DIXI also enforces its rules with opt-in hooks, runs without network or runtime dependencies, and ships English and Spanish.

## Decision

Competing fairly means: matching what users expect from Spec Kit, going further where the method is broader, and stating gaps honestly with dated sources. No disparagement, no unverifiable claims.

1. **Phase A — parity (v1.7.0, [TASK-011](../../tasks/backlog/TASK-011-parity-commands.md)).** `constitution` (versioned project principles that every other operation reads), `checklist` (requirement-quality checks, written as unchecked items; a person ticks them) and `converge` (compares code with specs, plan and tasks and appends traced convergence tasks; never edits specs or code). Both languages, both adapters, with templates and `workflow` recipes. Public documentation: an honest, dated comparison and a "Coming from Spec Kit" migration guide with a command mapping.
2. **Phase B — complete DIXI (v1.8.0, [TASK-012](../../tasks/backlog/TASK-012-workflow-recipes.md)).** `dixi workflow` recipes for every operation that lacks one.
3. **Phase C — DIXI's own commands (v1.9.0, [TASK-013](../../tasks/backlog/TASK-013-own-commands.md)).** `onboard` (existing projects: derive modules, specs and traceability from the code, marked as drafts for human validation), `bugfix` (reproduction, red test, fix, spec update, traced), `issues` (tasks to GitHub Issues through `gh`, previewed and confirmed by the person; no MCP, no new dependency) and `dixi upgrade --apply` (applies only kit-owned files that the person has not edited; never overwrites local edits).
4. **Phase D — more agents (v1.10.0, [TASK-014](../../tasks/backlog/TASK-014-agent-skills-adapter.md)).** A generic adapter in the Agent Skills format. An agent is announced as supported only with a recorded run, as for Claude Code and Codex.
5. **Phase E — extensibility and documentation site ([TASK-015](../../tasks/backlog/TASK-015-extensibility-and-site.md)).** Local presets and extensions (no network catalog in the first version), decided in its own ADR before code. A static documentation site in English and Spanish built from the repository Markdown by a standard-library script and published with GitHub Pages; enabling Pages is the maintainer's action.

Constraints that hold in every phase: tests first in new modules (existing tests change only with explicit authorization, in their own commit); no runtime dependencies; messages in `locales/`; every resource declared in `pyproject.toml`, `MANIFEST.in` and `scripts/build-local.py`; a release per phase through Trusted Publishing.

## Alternatives considered

- **Copy Spec Kit's command set and names.** Rejected: DIXI's method is broader, and `implement` is already `build`. The migration guide maps names instead.
- **Network catalogs and an MCP server now.** Rejected for now: they need network access and, for MCP, a long-running server; Spec Kit itself marks MCP experimental. Local presets come first.
- **One adapter per agent before a generic one.** Rejected as the first step: more code to maintain for the same reach; specific adapters stay possible when a generic one is not enough.
- **A documentation site with MkDocs or DocFX.** Rejected: adds a build dependency; the standard library is enough for static HTML.

## Consequences

- The operation count grows from twenty-seven to thirty-three (phases A and C); `tests/test_doc_counts.py` keeps public texts in step.
- `docs/spec-kit-comparison.md` is replaced by a dated public comparison that is refreshed with each DIXI release.
- `upgrade --apply` is the first command that rewrites files in an existing project; it needs its own contract and threat review in phase C.
- The support matrix only lists agents with recorded evidence; the Agent Skills adapter may work with more agents than the matrix announces.

## Related

- [ADR-100](ADR-100-distribucion-publica-v1.md)
- [ADR-104](ADR-104-project-profiles-and-content.md)
- [ADR-105](ADR-105-opt-in-automated-controls.md)
- [Command catalog](../../docs/command-catalog.md)
- [Spec Kit comparison](../../docs/spec-kit-comparison.md)
