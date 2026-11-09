# Lista 06 — Procesos

> **Regla de evidencia.** Puntúa solo lo que prueba un artefacto. Un artefacto ausente se anota como «sin evidencia» y vale 0; nunca se rellena con un supuesto presentado como hecho.

## Propósito

Evaluar cómo avanza el trabajo desde la idea hasta producción y de vuelta: planificación, especificación, revisión, publicación, marcha atrás, gestión de incidentes y aprendizaje. Los procesos cuentan solo cuando los registros muestran que se siguen.

Estado: borrador. {{pending: decidir el periodo de muestra de los registros de proceso}}

## Insumos

- [Hoja de ruta](../../16-product/roadmap.md) y [Ciclo de vida de funcionalidades](../../16-product/feature-lifecycle.md)
- [Escalera de verificación](../../11-quality/verification-ladder.md)
- [Visión general de CI/CD](../../14-delivery/ci-cd-overview.md), [Estrategia de despliegue](../../14-delivery/deployment-strategy.md), [Estrategia de marcha atrás](../../14-delivery/rollback-strategy.md)
- [Niveles de incidente](../../15-operations/incident-levels.md) y [Matriz de escalado](../../15-operations/escalation-matrix.md)
- [Plantilla de postmortem](../../10-engineering/templates/postmortem-template.md)
- [Registro de decisiones](../../18-knowledge-base/decision-log.md)

## Elementos

| ID | Pregunta | Evidencia (artefacto) | Puntuación 0–5 | Hallazgo |
|----|----------|-----------------------|----------------|----------|
| PRO-01 | ¿El trabajo se planifica y prioriza en un backlog visible? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| PRO-02 | ¿Las funcionalidades se especifican con criterios de aceptación antes de construir? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| PRO-03 | ¿Cada cambio es trazable desde el requisito hasta el test y la publicación? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| PRO-04 | ¿Las publicaciones son automáticas, frecuentes y reversibles? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| PRO-05 | ¿Hay un proceso de incidentes con niveles de gravedad y guardias? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| PRO-06 | ¿Se escriben postmortems y se cierran sus acciones? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| PRO-07 | ¿Las decisiones quedan registradas donde el equipo las encuentra? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| PRO-08 | ¿Se siguen métricas de entrega (tiempo de entrega, tasa de fallos en cambios, tiempo de recuperación)? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| PRO-09 | ¿El uso de agentes de IA en el desarrollo se rige por reglas documentadas? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |

## Señales de alarma

- Las publicaciones dependen de que una persona ejecute pasos manuales.
- Los incidentes se arreglan pero nunca se revisan.
- Ningún registro une los cambios publicados con su revisión.

## Resultado

- Puntuación del área: {{pending: puntuación y método}}
- Hallazgos trasladados al [Informe de DD](../dd-report-template.md).

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Lista 05 — Gestión de datos](05-data-management.md)
- [Lista 07 — Equipo](07-team.md)
- [Lista final](11-final-report.md)
