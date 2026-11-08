# Comparison with GitHub Spec Kit

## Purpose

Position DIXI Spec Kit's progress against GitHub Spec Kit in order to prioritize what is missing before publishing. This is an internal planning analysis, not marketing material: it claims neither parity nor superiority.

## Source and validity

Data on github/spec-kit taken on 2026-11-08 from its README, its releases page and its documentation site. Its Issues and CHANGELOG were not read. Figures such as version, releases or stars change quickly; verify them before quoting. DIXI's status corresponds to the working branch on that date.

## Compared status

| Area | GitHub Spec Kit | DIXI Spec Kit |
|---|---|---|
| Maturity | v1.3.2 released on Nov 6; ten releases in about three weeks | `1.0.0.dev0` local, no release |
| License | MIT | MIT proposed; rights and decision pending |
| Installation | `uv tool install`, `uvx`, pipx, pip and air-gapped wheels | Local wheel and sdist; names not verified in the registry |
| Agents | 41 integrations, plus `none` and `generic` | None; only `--agent none` |
| Commands in the agent | constitution, specify, clarify, plan, checklist, tasks, analyze, implement, converge | None installable; 16 proposed |
| CLI | init, check, version, self check, integration, extension, mcp | init, doctor, check, workflow list/show/prepare |
| Extensibility | Extensions, presets, workflows, bundles, catalogs | Does not exist |
| Community | CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT, docs site, READMEs in three languages | Not prepared |
| Systems | Linux, macOS and Windows | Only macOS tested |

## Main gap

Spec Kit's value proposition is installing commands in the agent the person already uses. DIXI today creates documents and prepares context deterministically, but does not install commands in any agent.

## Differences DIXI can sustain with its own evidence

Each one requires the executed public example before being announced.

- Mechanical checking of the business → domain → module → feature → contract → test chain through `dixi check`.
- Explicit human gates: AI does not sign, attest, approve or merge; frozen tests are not modified.
- Design of domains, architecture, contracts and threats, and impact analysis when a feature changes.
- Agent-independent core documented in ADR-101.
- CLI execution with the standard library and verification of paths, symlinks and limits with regression tests.

## What is missing to publish

Blockers: license and rights; at least one agent adapter with installed commands; verified names; installation without cloning the repository; a public example from idea to verified code; README es/en and community files; clean history and branch protection. Deferrable: `upgrade`, Linux and Windows, specialized commands, second language and second adapter, extensions. The scope proposal is in [ADR-102](../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md).

## Related

- [ADR-102](../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md)
- [Command catalog](command-catalog.md)
- [Publication](publication-readiness.md)
- [Product](product-spec.md)
- [TASK-003](../tasks/backlog/TASK-003-adaptador-claude-code.md)
