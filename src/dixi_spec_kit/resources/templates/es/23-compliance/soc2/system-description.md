# Descripción del sistema (SOC 2)

> **Ayuda de trabajo; no es asesoría legal.** Este esquema reúne los hechos que suele requerir la descripción del sistema que acompaña a un informe SOC 2. La dirección es responsable de la descripción final y el auditor la evalúa; ninguna plantilla certifica conformidad.

## Propósito

Describir el sistema en alcance con exactitud y de forma completa: qué servicio presta, qué componentes y personas lo sostienen, cómo fluyen los datos y qué compromisos y controles aplican. Cada afirmación debe coincidir con el funcionamiento real del sistema.

Estado: borrador. {{pending: nombrar al autor y al aprobador de la descripción del sistema}}

## 1. Servicios prestados

- Servicio y usuarios principales: {{pending: describir}}
- Compromisos principales con los clientes (p. ej. disponibilidad, confidencialidad): {{pending: enumerar, vinculados a contratos o SLA}}
- Requisitos del sistema derivados de esos compromisos: {{pending: enumerar}}

## 2. Componentes del sistema

| Componente | Descripción | Artefacto de origen |
|------------|-------------|---------------------|
| Infraestructura | Entornos, redes, regiones de alojamiento | [Arquitectura de despliegue](../../09-architecture/deployment-architecture.md) |
| Software | Aplicaciones, servicios, bases de datos | [Contexto del sistema](../../09-architecture/system-context.md) |
| Personas | Roles que operan, desarrollan y dan soporte | [Matriz RACI](../../15-operations/team/raci-matrix.md) |
| Procedimientos | Cambios, accesos, incidentes, copias | {{pending: enlaces}} |
| Datos | Tipos de datos, clasificación, retención | [Clasificación de PII](../../08-data/pii-classification.md) |

## 3. Límites

- En alcance: {{pending: sistemas, ubicaciones, equipos}}
- Fuera de alcance, con motivo: {{pending: enumerar}}
- Organizaciones de subservicio y su tratamiento (excluidas o incluidas): {{pending: enumerar categorías}}

## 4. Flujos de datos

Describe cómo entran, se procesan, se almacenan y salen los datos de clientes. {{pending: enlazar un diagrama de 09-architecture}}

## 5. Resumen de controles

Remite a la [Matriz de controles](soc2-controls-matrix.md); no la dupliques aquí.

## 6. Controles complementarios

- Controles que se esperan de los clientes: {{pending: enumerar, p. ej. gestionar sus propias cuentas de usuario}}
- Controles que se esperan de las organizaciones de subservicio: {{pending: enumerar}}

## 7. Cambios significativos durante el periodo

| Fecha | Cambio | Impacto en los controles |
|-------|--------|--------------------------|
| {{pending: fecha}} | {{pending: cambio}} | {{pending: impacto}} |

## Relacionados

- [Preparación para SOC 2](soc2-readiness.md)
- [Matriz de controles SOC 2](soc2-controls-matrix.md)
- [Contexto del sistema](../../09-architecture/system-context.md)
- [Panorama de cumplimiento](../compliance-overview.md)
