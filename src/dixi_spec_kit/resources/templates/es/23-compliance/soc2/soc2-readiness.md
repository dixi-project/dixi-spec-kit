# Preparación para SOC 2

> **Ayuda de trabajo; no es asesoría legal.** Este plan organiza la preparación para un examen SOC 2. Solo un auditor independiente emite un informe SOC 2; ninguna plantilla certifica conformidad ni garantiza una opinión.

## Propósito

Decidir si conviene buscar un informe SOC 2, qué alcance y criterios cubriría, y seguir las brechas entre hoy y un estado listo para auditoría, con evidencia para cada control.

Estado: borrador. {{pending: decidir si se busca un informe SOC 2 y anotar el motivo de negocio}}

## Decisiones de alcance

| Decisión | Opciones | Elección | Motivo |
|----------|----------|----------|--------|
| Criterios de servicios de confianza | Seguridad (siempre) más disponibilidad, confidencialidad, integridad del procesamiento, privacidad | {{pending: criterios en alcance}} | {{pending: motivo}} |
| Sistemas en alcance | Producto, infraestructura de soporte, herramientas internas | {{pending: lista}} | {{pending: motivo}} |
| Tipo de informe | Tipo I o Tipo II (ver [Tipo I frente a Tipo II](type-i-vs-type-ii.md)) | {{pending: tipo}} | {{pending: motivo}} |
| Organizaciones de servicio excluidas | Infraestructura y otros proveedores de los que se depende | {{pending: enumerar categorías}} | {{pending: motivo}} |
| Criterios de selección del auditor | Independencia, experiencia en el sector, coste, disponibilidad | {{pending: criterios; no nombrar firma aquí hasta elegirla}} | — |

## Fases

1. **Alcance**: responder la tabla anterior y redactar la [Descripción del sistema](system-description.md).
2. **Análisis de brechas**: completar la [Matriz de controles](soc2-controls-matrix.md); cada brecha es un ticket y, si es relevante, un riesgo.
3. **Remediación**: diseñar e implantar los controles que faltan; guardar la evidencia a medida que se genera.
4. **Revisión de preparación**: recorrer cada control con su evidencia; preevaluación opcional.
5. **Auditoría**: en un momento dado (Tipo I) o durante un periodo de observación (Tipo II).
6. **Mantenimiento**: los controles siguen operando; la evidencia se recoge de forma continua.

## Principios de evidencia

- Preferir evidencia generada por sistemas (logs, tickets, registros de pipeline) a capturas de pantalla.
- Cada evidencia tiene responsable, ubicación y frecuencia de recogida.
- Nunca antedatar ni reconstruir evidencia; un periodo sin evidencia es una brecha que se declara.

## Seguimiento de preparación

| Área | Controles | Diseñados | Operando con evidencia | Brechas abiertas |
|------|-----------|-----------|------------------------|------------------|
| {{pending: área}} | {{pending: número}} | {{pending: número}} | {{pending: número}} | {{pending: tickets}} |

## Relacionados

- [Matriz de controles SOC 2](soc2-controls-matrix.md)
- [Descripción del sistema](system-description.md)
- [Tipo I frente a Tipo II](type-i-vs-type-ii.md)
- [Solapamiento ISO 27001 y SOC 2](../iso-soc2-overlap-mapping.md)
- [Panorama de cumplimiento](../compliance-overview.md)
