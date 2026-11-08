# Evidencia B3 y v1.0.0

## Propósito

Registrar la verificación técnica del adaptador de Claude Code (TASK-003) y de la versión 1.0.0, y sus límites. Fecha: 2026-11-08. Entorno: macOS, Python 3.15.2, Claude Code 2.1.319, Setuptools 84.2.1 fijado por hash.

## Pruebas primero

| Bloque | Commit en rojo | Resultado previo |
|---|---|---|
| Adaptador Claude Code | `[11-quality] test: acceptance in red for Claude Code adapter B3` | 18 fallos esperados; la regresión de `--agent none` pasa |
| Exportador público | `[11-quality] test: acceptance in red for public release export` | 3 fallos esperados |
| Compatibilidad 1.x | `[11-quality] test: accept same-major kit versions in red` | 8 fallos esperados |

Dos pruebas congeladas cambiaron con autorización explícita de la persona responsable, cada una en su propio commit: el entrecomillado del intérprete en el shim del ejemplo (rutas con espacios) y la versión esperada (`1.0.0.dev0` → `1.0.0`).

## Resultados

- `make verify` en el repositorio: sintaxis, paridad es/en de catálogos y recursos, licencia y **93 pruebas** en verde, incluida la instalación limpia desde wheel y desde sdist reconstruido.
- Árbol público exportado (`scripts/export-release.py`, 145 archivos): `make verify` en verde con 89 pruebas (el exportador y su prueba no se distribuyen). Instalación desde el código fuente en un entorno nuevo, seguida de `dixi --version` → `dixi 1.0.0`, `init --agent claude`, `doctor` y `check` con código 0.
- `examples/notes`: `dixi check` y 12 pruebas de aplicación en verde.
- Gitleaks 8.30.1: sin hallazgos en el árbol público ni en los 64 commits del historial local.
- Enlaces relativos de los Markdown del árbol público: sin enlaces rotos.
- Nombre `dixi-spec-kit` libre en PyPI el 2026-11-08 (HTTP 404). Existe otro proyecto llamado `dixi` en PyPI; no hay conflicto de paquete, pero el ejecutable `dixi` podría coincidir si alguien instala ambos.

| Artefacto | Bytes | SHA-256 |
|---|---|---|
| `dixi_spec_kit-1.0.0-py3-none-any.whl` | 53 422 | `51e5a3424c6e1067b6bf2ba27e28d26228438390e46a44ae487c7a6c4f233a5e` |
| `dixi_spec_kit-1.0.0.tar.gz` | 33 545 | `ad736aa7096f977cf77af465e85afc757b790ca331dd5813455088be8ad35acf` |

Los hashes identifican este build local; no se promete reproducción bit a bit. La release debe adjuntar los artefactos que construya la persona desde el commit publicado.

## Recorrido en el agente

El ejemplo se produjo siguiendo los pasos de cada comando en una sesión de Claude Code 2.1.319, incluida la evolución con análisis de impacto y pruebas en rojo antes del código ([recorrido](../examples/notes/docs/walkthrough.md)). **No** es una evaluación independiente: falta que una persona invoque los diez comandos `/dixi.*` instalados en una sesión nueva y confirme que se comportan según el [contrato](../07-contracts/commands/claude-code-adapter-contract.md).

## Pendiente

- Primera ejecución de la CI en GitHub (Linux y macOS, Python 3.11 y 3.13).
- Evaluación manual de los comandos en una sesión nueva de Claude Code.

## Relacionados

- [Matriz de soporte](support-matrix.md)
- [Puerta de publicación](publication-readiness.md)
- [TASK-003](../tasks/backlog/TASK-003-adaptador-claude-code.md)
