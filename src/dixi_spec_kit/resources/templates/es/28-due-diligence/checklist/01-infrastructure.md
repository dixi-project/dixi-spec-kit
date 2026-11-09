# Lista 01 — Infraestructura

> **Regla de evidencia.** Puntúa solo lo que prueba un artefacto. Un artefacto ausente se anota como «sin evidencia» y vale 0; nunca se rellena con un supuesto presentado como hecho.

## Propósito

Evaluar si la infraestructura está definida, es reproducible, observable, recuperable y asumible en coste, con la escala de la [Estrategia de DD](../dd-strategy.md).

Estado: borrador. {{pending: confirmar qué entornos y cuentas de alojamiento entran en alcance}}

## Insumos

- [Arquitectura de despliegue](../../09-architecture/deployment-architecture.md)
- [Entornos](../../14-delivery/environments.md) y [Módulos de infraestructura](../../14-delivery/infra-modules.md)
- [Copias y recuperación](../../14-delivery/backup-and-recovery.md), [Estrategia de DR](../../14-delivery/disaster-recovery/dr-strategy.md), [Matriz RTO/RPO](../../14-delivery/disaster-recovery/rto-rpo-matrix.md)
- [Estrategia de observabilidad](../../12-observability/observability-strategy.md) y [SLI, SLO y SLA](../../12-observability/slis-slos-slas.md)
- [Estrategia de costes](../../22-finops/cost-strategy.md)

## Elementos

| ID | Pregunta | Evidencia (artefacto) | Puntuación 0–5 | Hallazgo |
|----|----------|-----------------------|----------------|----------|
| INF-01 | ¿Toda la infraestructura está definida como código y se revisa como el código de la aplicación? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| INF-02 | ¿Los entornos están separados y el acceso a producción restringido? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| INF-03 | ¿Se puede reconstruir un entorno solo desde el repositorio? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| INF-04 | ¿Las copias son automáticas, cifradas y con restauraciones probadas y registradas? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| INF-05 | ¿Los objetivos de recuperación están definidos y ensayados? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| INF-06 | ¿Hay métricas, logs y alertas en los caminos críticos? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| INF-07 | ¿Los objetivos de nivel de servicio están definidos y medidos? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| INF-08 | ¿La capacidad está planificada y el escalado probado? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| INF-09 | ¿El coste es visible por entorno o componente, con alertas? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| INF-10 | ¿Existe un punto único de fallo o una sola persona que tenga el acceso? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |

## Señales de alarma

- Producción modificada a mano sin registro.
- Copias que nunca se han restaurado.
- Credenciales raíz o de propietario compartidas o en manos de una sola persona.

## Resultado

- Puntuación del área: {{pending: puntuación y método}}
- Hallazgos trasladados al [Informe de DD](../dd-report-template.md).

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Lista 02 — Arquitectura](02-architecture.md)
- [Lista final](11-final-report.md)
