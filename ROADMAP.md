# Plan de DIXI Spec Kit

## Propósito

Mostrar qué incluye cada versión pública y qué viene después. Solo se anuncia como disponible lo que tiene pruebas y evidencia.

## v1.0.0 — primera versión pública

CLI `dixi` (`init`, `doctor`, `check`, `workflow`), modo sin agente, adaptador de Claude Code con diez comandos, documentación es/en, ejemplo `examples/notes`, CI pública y licencia MIT. Alcance fijado en [ADR-102](09-architecture/adr/ADR-102-recorte-de-alcance-v1.md).

## v1.1 — previsto

- `dixi upgrade --dry-run`: comparar el proyecto con el inventario original y listar archivos actualizables y conflictos sin escribir.
- Adaptador de Codex, evaluado con su propia matriz de controles.
- `/dixi.handoff` y `/dixi.change`.
- Ejemplo en un segundo lenguaje.
- Publicación en PyPI (requiere ADR propio).

## Después

Comandos especializados (datos, calidad, IA, release, operación, FinOps, compliance, due diligence) según demanda, y soporte de Windows si se resuelven las operaciones seguras de filesystem.

## Relacionados

- [Matriz de soporte](docs/support-matrix.md)
- [Historia de lanzamiento](tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Changelog](CHANGELOG.md)
