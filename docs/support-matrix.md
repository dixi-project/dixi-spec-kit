# Matriz de soporte v1.0.0 / Support matrix

## Propósito

Declarar qué soporta DIXI Spec Kit v1.0.0, con qué evidencia y qué controles son automáticos o solo instrucciones. Nada fuera de esta tabla se anuncia como soportado.

## Sistemas y Python

| Plataforma | Estado | Evidencia |
|---|---|---|
| macOS + Python 3.15 | Soportado | `make verify` local, instalación limpia desde wheel y sdist ([B3](b3-verification.md)). |
| macOS / Linux + Python 3.11 y 3.13 | Soportado al pasar la CI | Job `verify` en `ubuntu-latest` y `macos-latest` ([ADR-103](../09-architecture/adr/ADR-103-ci-publica-en-github-actions.md)). |
| Windows | No soportado | Requiere operaciones POSIX (`O_NOFOLLOW`, descriptores de directorio); `dixi` sale con código 4. |

## Integraciones

| Integración | Estado | Qué instala |
|---|---|---|
| `--agent none` | Soportada | Base documental, `AGENTS.md` y guía. Úsala con cualquier editor o agente, sin comandos instalados. |
| `--agent claude` | Soportada (Claude Code 2.1.319) | Lo anterior más `CLAUDE.md` y diez comandos `/dixi.*` en `.claude/commands/`. |
| Codex y otros | No incluidos en v1.0.0 | Previsto Codex para v1.1. Tener `AGENTS.md` no equivale a soporte. |

## Controles del adaptador Claude Code

| Control | Mecanismo | ¿Automático? |
|---|---|---|
| No sobrescribir al instalar | `dixi init` | Sí |
| Estructura, enlaces y trazabilidad | `dixi check` / `make verify` | Sí |
| Pruebas primero y congeladas | Instrucción en cada comando + revisión del PR | **No** |
| No firmar, aprobar ni integrar | Instrucción + protección de rama en tu repositorio | **No** en el agente |
| Validar decisiones estructurales | Instrucción (el comando se detiene) | **No** |
| Permisos de herramientas | Tu configuración de Claude Code; el kit no la cambia | — |
| No leer secretos | Instrucción; `dixi` rechaza rutas sensibles | Parcial |

## Capacidades

Incluidas: `init`, `doctor`, `check`, `workflow list/show/prepare`, los diez comandos `discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze`, `status`, y documentos es/en.

No incluidas en v1.0.0: `dixi upgrade`, `/dixi.handoff`, `/dixi.change`, comandos especializados (datos, calidad, IA, release, operación, FinOps, compliance, due diligence), extensiones o presets y un segundo lenguaje de ejemplo.

## English summary

Supported: macOS and Linux with Python ≥ 3.11 (local evidence on macOS/3.15; CI on Ubuntu and macOS with 3.11 and 3.13). Windows is unsupported. Integrations: `--agent none` and `--agent claude` (Claude Code 2.1.319). The Claude Code adapter installs ten commands and `CLAUDE.md`, and no hooks, permissions or MCP servers. Test-first, no-sign/approve/merge and structural-decision gates are **instructions**, not automatic controls; only install safety and `dixi check` are automated. Not in v1.0.0: upgrade, handoff, change, specialized commands, extensions, Codex, Windows.

## Relacionados

- [Contrato del adaptador](../07-contracts/commands/claude-code-adapter-contract.md)
- [ADR-102](../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md)
- [Plan](../ROADMAP.md)
