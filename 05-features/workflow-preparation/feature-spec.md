# Feature — Preparar definición y diseño sin acoplar un agente

## Propósito

Entregar B2a sobre el módulo command-workflow: consultar ocho procedimientos compartidos y preparar contexto explícito verificable. Una persona o un adaptador posterior usa el mismo contrato para producir artefactos.

## Aceptación

- WP-01: catálogo y recetas es/en completos, disponibles sin proyecto.
- WP-02: objetivo explícito del tipo admitido y solicitud válida; sin selección automática.
- WP-03: manifiesto mínimo de fuentes y ancestros, hashes actuales, límites y lectura confinada.
- WP-04: resultado preparado, repetible y sin efectos externos, claramente distinto de ejecución semántica.
- WP-05: disponibilidad del recorrido en wheel y sdist limpios; regresión B1 en verde.

La historia y sus criterios detallados viven en TASK-002. Esto no acredita generación asistida de specs, cumplimiento semántico, adaptadores verificados ni el recorrido completo B2.

## Verificación

Pruebas deterministas nuevas en `tests/test_workflows.py` y `tests/test_workflow_distribution.py`, congeladas antes de implementación. `tests/test_workflow_edges.py` añade regresiones de salida y contexto compartido. Los escenarios BDD enlazan el comportamiento; no se requiere runner Gherkin. La rúbrica posterior deberá evaluar los artefactos producidos por cada integración, incluidas decisiones faltantes y gates. [Evidencia B2a](../../docs/b2-verification.md).

## Relacionados

- [Módulo padre](../../04-modules/command-workflow/module-spec.md)
- [Contrato](../../07-contracts/commands/workflow-preparation-contract.md)
- [Tarea](../../tasks/backlog/TASK-002-operaciones-compartidas-b2.md)
- [Escenarios](scenarios.feature)
- [Aceptación](acceptance.yaml)
