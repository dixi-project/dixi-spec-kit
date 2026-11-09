# v1.4.0 support matrix

## Purpose

Declare what DIXI Spec Kit v1.4.0 supports, with what evidence, and which controls are automatic or only instructions. Nothing outside this table is announced as supported.

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
| `--agent codex` | Supported (Codex CLI 0.167.0; [manual run](../07-contracts/commands/codex-adapter-contract.md#manual-run)) | Baseline plus twenty-five skills in `.agents/skills/dixi-<operation>/SKILL.md`, each with `agents/openai.yaml` disabling implicit invocation. Invoke them as `$dixi-<operation>`. Codex reads `AGENTS.md` itself. |
| Others | Not included | Having `AGENTS.md` does not amount to support. |

## Claude Code adapter controls

| Control | Mechanism | Default | With `--controls` |
|---|---|---|---|
| Do not overwrite on install | `dixi init` | Automatic | Automatic |
| Structure, links and traceability | `dixi check` / `make verify` | Automatic | Automatic |
| Frozen tests (committed tests are not edited) | Instruction + PR review; hook `protect_tests` | Instruction | Enforced by hook |
| Do not sign, attest, approve or merge | Instruction + branch protection; hook `guard_attestation` | Instruction | Enforced by hook |
| Do not read secrets | Instruction; `dixi` rejects sensitive paths; hook `guard_secrets` | Partial | Enforced by hook |
| No destructive commands in `MODE=prod` | Instruction; hook `mode_gate` | Instruction | Enforced by hook |
| No "done" with `make verify` in red | Instruction; hook `verify_on_stop` | Instruction | Enforced by hook (once, then the person decides) |
| Validate structural decisions | Instruction (the command stops) | Instruction | Instruction |
| Tool permissions | Your Claude Code configuration; the kit does not change it | — | — |

Hooks are a second layer, not the last one: an agent can reach a file through a path a hook does not inspect. Human review and branch protection remain the effective protection.

## Codex adapter controls

| Control | Mechanism | Automatic? |
|---|---|---|
| No overwrite on install | `dixi init` | Yes |
| Structure, links and traceability | `dixi check` / `make verify` | Yes |
| No implicit start of a DIXI skill | `allow_implicit_invocation: false` per skill | Yes (Codex setting) |
| Frozen tests; no sign, attest, approve or merge; no secrets; `MODE=prod` safety; no "done" in red | Instruction in every skill; with `--controls`, the same hooks through `.codex/hooks.json` (`Bash`, `apply_patch`, `Stop`, `SubagentStop`) | Instruction; enforced by hook with `--controls` once you trust the project and approve the hooks with `/hooks` |
| Validate structural decisions | Instruction in every skill + human review | **No** |
| Sandbox and approvals | Your Codex configuration; the kit does not change it | — |

## Capabilities

Included: `init` with the `minimal`, `site`, `app` and `platform` profiles and `--regulated`, `doctor`, `check`, `workflow list/show/prepare`, `upgrade --dry-run`, `placeholders`, `pr-size`, opt-in `--controls`, Claude Code subagents, the twenty-seven operations `discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze`, `status`, `domain`, `architecture`, `contract`, `threat-model`, `handoff`, `change`, `data`, `quality`, `ai`, `release`, `promote`, `operate`, `finops`, `compliance`, `duediligence`, `interview`, `risk-review`, and es/en documents.

Not included yet: applying upgrades, extensions or presets, and a second example language.

## Related

- [Adapter contract](../07-contracts/commands/claude-code-adapter-contract.md)
- [ADR-102](../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md)
- [Roadmap](../ROADMAP.md)

## Resumen en español

Soportado: macOS y Linux con Python ≥ 3.11 (evidencia local en macOS/3.15; CI en Ubuntu y macOS con 3.11 y 3.13). Windows no está soportado. Integraciones: `--agent none`, `--agent claude` (Claude Code 2.1.319) y `--agent codex` (Codex CLI 0.167.0, veinticinco skills con invocación implícita desactivada; ejecución manual registrada). El adaptador de Claude Code instala veintisiete comandos, cuatro subagentes y `CLAUDE.md`, sin permisos ni servidores MCP. Por defecto, las reglas de pruebas congeladas, no firmar/aprobar/integrar, no leer secretos y validar decisiones estructurales son **instrucciones**; con `--controls` se instalan hooks (Claude Code y Codex) que hacen cumplir todas salvo la validación de decisiones. Los hooks son una segunda capa, no la última. Aún no incluidos: aplicar upgrades, extensiones y Windows.
