# v1.0.0 support matrix

## Purpose

Declare what DIXI Spec Kit v1.0.0 supports, with what evidence, and which controls are automatic or only instructions. Nothing outside this table is announced as supported.

## Systems and Python

| Platform | Status | Evidence |
|---|---|---|
| macOS + Python 3.15 | Supported | Local `make verify`, clean install from wheel and sdist ([B3](b3-verification.md)). |
| macOS / Linux + Python 3.11 and 3.13 | Supported when CI passes | `verify` job on `ubuntu-latest` and `macos-latest` ([ADR-103](../09-architecture/adr/ADR-103-ci-publica-en-github-actions.md)). |
| Windows | Not supported | Requires POSIX operations (`O_NOFOLLOW`, directory descriptors); `dixi` exits with code 4. |

## Integrations

| Integration | Status | What it installs |
|---|---|---|
| `--agent none` | Supported | Documentary base, `AGENTS.md` and guide. Use it with any editor or agent, without installed commands. |
| `--agent claude` | Supported (Claude Code 2.1.319) | All of the above plus `CLAUDE.md` and twenty-five `/dixi.*` commands in `.claude/commands/` (fewer in projects created with earlier versions; see `dixi upgrade --dry-run`). |
| `--agent codex` | Preview (Codex CLI 0.167.0); supported once a manual run is recorded | Baseline plus twenty-five skills in `.agents/skills/dixi-<operation>/SKILL.md`, each with `agents/openai.yaml` disabling implicit invocation. Invoke them as `$dixi-<operation>`. Codex reads `AGENTS.md` itself. |
| Others | Not included | Having `AGENTS.md` does not amount to support. |

## Claude Code adapter controls

| Control | Mechanism | Automatic? |
|---|---|---|
| Do not overwrite on install | `dixi init` | Yes |
| Structure, links and traceability | `dixi check` / `make verify` | Yes |
| Tests first and frozen | Instruction in each command + PR review | **No** |
| Do not sign, approve or merge | Instruction + branch protection in your repository | **No** in the agent |
| Validate structural decisions | Instruction (the command stops) | **No** |
| Tool permissions | Your Claude Code configuration; the kit does not change it | — |
| Do not read secrets | Instruction; `dixi` rejects sensitive paths | Partial |

## Codex adapter controls

| Control | Mechanism | Automatic? |
|---|---|---|
| No overwrite on install | `dixi init` | Yes |
| Structure, links and traceability | `dixi check` / `make verify` | Yes |
| No implicit start of a DIXI skill | `allow_implicit_invocation: false` per skill | Yes (Codex setting) |
| Tests first and frozen; no sign, approve or merge; validate structural decisions | Instruction in every skill + human review and branch protection | **No** |
| Sandbox and approvals | Your Codex configuration; the kit does not change it | — |

## Capabilities

Included: `init`, `doctor`, `check`, `workflow list/show/prepare`, `upgrade --dry-run`, the twenty-five operations `discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze`, `status`, `domain`, `architecture`, `contract`, `threat-model`, `handoff`, `change`, `data`, `quality`, `ai`, `release`, `promote`, `operate`, `finops`, `compliance`, `duediligence`, and es/en documents.

Not included yet: applying upgrades, extensions or presets, and a second example language.

## Related

- [Adapter contract](../07-contracts/commands/claude-code-adapter-contract.md)
- [ADR-102](../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md)
- [Roadmap](../ROADMAP.md)

## Resumen en español

Soportado: macOS y Linux con Python ≥ 3.11 (evidencia local en macOS/3.15; CI en Ubuntu y macOS con 3.11 y 3.13). Windows no está soportado. Integraciones: `--agent none`, `--agent claude` (Claude Code 2.1.319) y `--agent codex` en vista previa (Codex CLI 0.167.0, veinticinco skills con invocación implícita desactivada). El adaptador de Claude Code instala veinticinco comandos y `CLAUDE.md`, sin hooks, permisos ni servidores MCP. Las reglas de pruebas primero, no firmar/aprobar/integrar y validar decisiones estructurales son **instrucciones**, no controles automáticos; solo la instalación segura y `dixi check` están automatizados. Aún no incluidos: aplicar upgrades, extensiones y Windows.
