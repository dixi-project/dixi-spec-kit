# Threat model — Preparación de procedimientos B2a

## Propósito

Extender el análisis de B1 a solicitudes, selección de contexto y recetas compartidas, antes de implementar TASK-002. Sin agentes ejecutados ni archivos escritos.

## Amenazas y cobertura

| Amenaza / STRIDE | Control | Evidencia prevista |
|---|---|---|
| Suplantar un objetivo o tipo | ID exacto, tipos por operación, grafo validado | Objetivos ausentes/incompatibles, padres inválidos y duplicados. |
| Alterar o fabricar evidencia | Hash de bytes actuales, estado prepared, sin aprobación implícita | Repetición idéntica y cambio de hash al editar. |
| Leer fuera del alcance / divulgación | Raíz confinada B1; selección de ancestros; sin cuerpos ni enlaces seguidos; solo campos conocidos del objetivo | Symlinks/FIFO, traversal, nombres sensibles, rama ajena no leída y `test_target_excludes_unknown_fields`. |
| Agotar memoria o bloquear lectura | 1 MiB/archivo, 64 fuentes, 2 MiB total, solicitud 4 096 caracteres | Casos de cada límite y archivos especiales. |
| Ejecutar texto malicioso / elevación | Solicitud como dato, sin subprocess/red; recetas con guardas | Solicitud shell no ejecutada, sockets bloqueados, snapshot sin cambios. |
| Ocultar falta de controles / repudio | Estado y alcance explícitos; gates comunes y específicos | Recetas completas, estado prepared y sin cuerpos del proyecto. |
| Perder recursos en distribución | Allowlist y carga desde importlib.resources | Recorrido en wheel y wheel reconstruido desde sdist. |

## Riesgo residual

El manifiesto no es snapshot ni firma; un consumidor debe revalidar hashes. La CLI no interpreta si una instrucción del proyecto es segura ni impone guardas a un agente externo. No detecta secretos con nombres arbitrarios: no se deben registrar archivos secretos como specs. Un paquete preparado no certifica completitud, consentimiento o calidad del diseño. Evaluaciones de inyección/gates en cada adaptador quedan pendientes antes de anunciarlo.

## Relacionados

- [Contrato](../07-contracts/commands/workflow-preparation-contract.md)
- [Amenazas B1](local-core-threat-model.md)
- [Feature](../05-features/workflow-preparation/feature-spec.md)
