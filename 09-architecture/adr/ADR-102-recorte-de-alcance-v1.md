# ADR-102 — Propuesta de recorte de alcance para v1.0.0

## Propósito

Registrar una propuesta para reducir el alcance mínimo de v1.0.0 a un nivel competitivo y verificable, tras comparar el avance con GitHub Spec Kit ([comparación](../../docs/spec-kit-comparison.md)).

## Estado

**Aceptado** el 2026-11-08 por la persona responsable (Alfredo Castillejos) en validación conjunta de historia, ADR y supuestos: «Validar recorte», «MIT + DCO» y «Aplazar a v1.1» el `upgrade --dry-run`. [TASK-001](../../tasks/backlog/TASK-001-lanzamiento-v1.md) queda actualizado en consecuencia. La aceptación no acredita por sí misma el soporte del adaptador: se anuncia solo con la evidencia de [TASK-003](../../tasks/backlog/TASK-003-adaptador-claude-code.md).

## Contexto

B1 y B2a entregan un núcleo local verificable (CLI, modo sin agente, diagnóstico, comprobación estructural y preparación de ocho procedimientos), pero ningún comando instalable dentro de un agente. La comparación con GitHub Spec Kit muestra que su propuesta de valor es precisamente instalar comandos en el agente que la persona ya usa. Sin un adaptador, v1.0.0 sería una plantilla documental con validadores.

TASK-001 exige hoy dos adaptadores evaluados contra dos lenguajes, `upgrade --dry-run` y 16 comandos. Ese alcance retrasa el primer contacto con usuarios externos.

## Propuesta

1. **Un adaptador en v1.0.0: Claude Code**, con evaluación real de sus capacidades y controles. Codex pasa a v1.1. ADR-101 no cambia: el núcleo sigue siendo independiente del agente y ningún proveedor se presupone.
2. **Diez comandos del agente:** `discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze` y `status`. Los de diseño (`domain`, `architecture`, `contract`, `threat-model`) siguen disponibles mediante `dixi workflow prepare`. Quedan para v1.1: `handoff`, `change` y las nueve entradas especializadas.
3. **`--agent none` se mantiene** como modo documental.
4. **Un ejemplo público** de idea a código verificado con una evolución y su análisis de impacto. El segundo lenguaje pasa a v1.1.
5. **Sistemas:** macOS y Linux con evidencia real. Windows declarado como no soportado.
6. **`upgrade --dry-run`:** aplazado a v1.1 (decisión de la persona, 2026-11-08). La documentación no puede prometer actualización mientras tanto; el inventario con hashes de `.dixi/project.json` se conserva como base para esa versión.
7. **Sin extensiones, presets ni catálogos** en v1.0.0.

## Lo que no cambia

Responsabilidad humana (ADR-010), pruebas primero y congeladas, gates, comprobaciones estructurales, `make verify`, licencia pendiente, historial limpio y la puerta de [publicación](../../docs/publication-readiness.md). Ninguna capacidad aplazada se anuncia como disponible.

## Decisiones resueltas el 2026-11-08

- **Licencia: MIT** para el código, recursos y documentación del producto, con **DCO** (`Signed-off-by`) para contribuciones, coherente con ADR-010. Los recursos distribuidos se escribieron para este producto; no se incorpora material propietario de EIS-IA.
- **Modelo de repositorio:** `main` público y descargable por cualquiera; contribuciones solo mediante fork y PR; solo mantenedores de Dixi integran, con revisión y checks obligatorios; sin push directo, force push ni borrado de `main`.

## Decisiones que siguen siendo de la persona

- **Licencia.** Recomendación técnica: MIT para el producto, con DCO (el `Signed-off-by` de ADR-010) en lugar de CLA para contribuciones; Apache-2.0 si se desea concesión explícita de patentes y cláusula de marca. No es asesoría legal. Debe confirmarse antes que Dixi tiene los derechos sobre los materiales de EIS-IA seleccionados; las referencias de `19-references/` conservan su licencia original y no se distribuyen bajo MIT.
- Disponibilidad de los nombres `dixi` y `dixi-spec-kit` en el registro y en GitHub.
- Creación de `main` en el remoto y todo merge.

## Consecuencias

Si se valida, v1.0.0 llega antes y con menos superficie que probar, y se puede medir adopción antes de ampliar. A cambio, se publica con menos capacidades que las diseñadas y con un solo adaptador, lo que debe quedar explícito en README y matriz de soporte. Si se rechaza, TASK-001 y ADR-101 siguen siendo el alcance.

## Relacionados

- [Comparación con GitHub Spec Kit](../../docs/spec-kit-comparison.md)
- [ADR-100](ADR-100-distribucion-publica-v1.md)
- [ADR-101](ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [TASK-001](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [TASK-003](../../tasks/backlog/TASK-003-adaptador-claude-code.md)
- [Catálogo de comandos](../../docs/command-catalog.md)
- [Publicación](../../docs/publication-readiness.md)
