# Lista 02 — Arquitectura

> **Regla de evidencia.** Puntúa solo lo que prueba un artefacto. Un artefacto ausente se anota como «sin evidencia» y vale 0; nunca se rellena con un supuesto presentado como hecho.

## Propósito

Evaluar si la arquitectura está documentada, coincide con el sistema en ejecución, soporta los requisitos no funcionales declarados y puede evolucionar sin reescribirse.

Estado: borrador. {{pending: confirmar qué sistemas e integraciones entran en alcance}}

## Insumos

- [Contexto del sistema](../../09-architecture/system-context.md), [Diagrama de contenedores](../../09-architecture/container-diagram.md), [Diagrama de componentes](../../09-architecture/component-diagram.md)
- [Índice de ADR](../../09-architecture/adr/README.md)
- [Arquitectura de integración](../../09-architecture/integration-architecture.md)
- [Arquitectura de resiliencia](../../09-architecture/resilience-architecture.md) y [Arquitectura de rendimiento](../../09-architecture/performance-architecture.md)
- [Arquitectura de seguridad](../../09-architecture/security-architecture.md)
- [Requisitos no funcionales](../../11-quality/non-functional-requirements.md)

## Elementos

| ID | Pregunta | Evidencia (artefacto) | Puntuación 0–5 | Hallazgo |
|----|----------|-----------------------|----------------|----------|
| ARC-01 | ¿Existen diagramas y coinciden con lo desplegado hoy? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| ARC-02 | ¿Las decisiones relevantes están registradas como ADR con contexto y consecuencias? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| ARC-03 | ¿Los límites entre módulos son claros y las dependencias van en un solo sentido? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| ARC-04 | ¿Las integraciones externas están documentadas con contratos y manejo de fallos? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| ARC-05 | ¿Los requisitos no funcionales están declarados y probados? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| ARC-06 | ¿Se conocen los modos de fallo (timeouts, reintentos, degradación)? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| ARC-07 | ¿El sistema puede asumir la carga esperada sin rediseño? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| ARC-08 | ¿La deuda técnica conocida está listada con impacto y plan? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| ARC-09 | ¿Hay dependencia fuerte de un proveedor y es una decisión registrada? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |

## Señales de alarma

- Sin diagramas, o diagramas que contradicen el sistema en ejecución.
- Decisiones críticas solo en la memoria de alguien.
- Una base de datos compartida por servicios no relacionados sin responsable.

## Resultado

- Puntuación del área: {{pending: puntuación y método}}
- Hallazgos trasladados al [Informe de DD](../dd-report-template.md).

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Lista 01 — Infraestructura](01-infrastructure.md)
- [Lista 03 — Código fuente](03-source-code.md)
- [Lista final](11-final-report.md)
