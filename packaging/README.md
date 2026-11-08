# DIXI Spec Kit

## Purpose / Propósito

Specification-driven development (SDD) kit by Dixi Project: traceable specs, tests first, verified code and human review. Ships the `dixi` CLI (standard library only, no network, no AI calls) and optional Claude Code commands.

Kit de desarrollo guiado por especificaciones de Dixi Project: specs trazables, pruebas primero, código verificado y revisión humana.

## Quickstart

```text
dixi --lang en init my-project --agent claude   # or --agent none
cd my-project
dixi doctor
dixi check
make verify
```

In Claude Code: `/dixi.discover`, `/dixi.specify`, `/dixi.clarify`, `/dixi.plan`, `/dixi.tasks`, `/dixi.build`, `/dixi.verify`, `/dixi.review`, `/dixi.analyze`, `/dixi.status`.

Terminal: `dixi init`, `dixi doctor`, `dixi check`, `dixi workflow list|show|prepare`. Global options `--lang es|en` and `--json` go before the command. Exit codes: 0 success, 1 invalid content, 2 usage, 3 occupied or unsafe destination, 4 unsupported version or platform, 5 I/O.

`dixi check` and the generated `make verify` check documentary structure and traceability; connect your application's real tests to `make verify`. The Claude Code adapter installs commands and instructions, not hooks or permissions.

Requirements: Python 3.11+, macOS or Linux. Windows is not supported.

## Related / Relacionados

Source, documentation, support matrix and contribution guide: https://github.com/dixi-project/dixi-spec-kit. License: MIT.
