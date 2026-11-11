# DIXI Spec Kit

## Purpose / Propósito

Specification-driven development (SDD) kit by Dixi Project: traceable specs, tests first, verified code and human review. Ships the `dixi` CLI (standard library only, no network, no AI calls) and optional commands for Claude Code and Codex.

Kit de desarrollo guiado por especificaciones de Dixi Project: specs trazables, pruebas primero, código verificado y revisión humana.

## Install

```text
uv tool install dixi-spec-kit   # or: pipx install dixi-spec-kit
```

Requirements: Python 3.11+, macOS or Linux. On Windows, use WSL 2 with the project under `~`, not `/mnt/c`; native Windows exits with code 4.

## Quickstart

```text
dixi init my-project --agent claude   # or --agent codex, or --agent none
cd my-project
dixi doctor
dixi check
make verify
```

Optional: `--profile site|app|platform` (and `--regulated`) for fuller templates, `--controls` (with `--agent claude` or `codex`) for hooks that enforce frozen tests, no secrets, no signing or merging, production-mode safety and verification before stopping. Without `--controls`, these rules are instructions; hooks are a second layer, not the last one.

In Claude Code, twenty-seven commands: `/dixi.discover`, `/dixi.interview`, `/dixi.specify`, `/dixi.clarify`, `/dixi.domain`, `/dixi.architecture`, `/dixi.contract`, `/dixi.data`, `/dixi.threat-model`, `/dixi.ai`, `/dixi.plan`, `/dixi.tasks`, `/dixi.build`, `/dixi.verify`, `/dixi.review`, `/dixi.analyze`, `/dixi.quality`, `/dixi.status`, `/dixi.handoff`, `/dixi.change`, `/dixi.release`, `/dixi.promote`, `/dixi.operate`, `/dixi.finops`, `/dixi.compliance`, `/dixi.duediligence`, `/dixi.risk-review`, plus four subagents.

In Codex, `--agent codex` installs the same operations as skills, invoked as `$dixi-specify`, `$dixi-plan`, etc., with implicit invocation disabled.

Terminal: `dixi init`, `dixi doctor`, `dixi check`, `dixi workflow list|show|prepare`, `dixi upgrade --dry-run` (preview what a newer kit version would change, without writing), `dixi placeholders`, `dixi pr-size`. Global options `--lang es|en` and `--json` go before the command. Exit codes: 0 success, 1 invalid content, 2 usage, 3 occupied or unsafe destination, 4 unsupported version or platform, 5 I/O.

`dixi check` and the generated `make verify` check documentary structure and traceability; connect your application's real tests to `make verify`.

## Related / Relacionados

Source, documentation, support matrix and contribution guide: https://github.com/dixi-project/dixi-spec-kit. License: MIT.
