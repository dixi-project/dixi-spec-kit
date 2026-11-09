# Catálogo de servicios

## Propósito

Mantener una sola lista de los servicios que opera el proyecto, con su responsable, criticidad y dependencias, para que operaciones, soporte y respuesta a incidentes hablen de lo mismo.

Estado: borrador. {{pending: nombrar al responsable del catálogo}}

## Catálogo

| Servicio | Qué hace | Responsable | Criticidad | Depende de | Runbook | Estado |
|----------|----------|-------------|------------|------------|---------|--------|
| {{pending: p. ej. aplicación web}} | {{pending: descripción}} | {{pending: equipo o rol}} | {{pending: crítica / alta / normal}} | {{pending: servicios y proveedores}} | {{pending: enlace}} | {{pending: activo / obsoleto}} |

Añade una fila por unidad desplegable o capacidad visible para el usuario. {{pending: decidir la granularidad: unidad desplegable o capacidad de negocio}}

## Criticidad

| Nivel | Significado | Nivel mínimo de incidente |
|-------|-------------|---------------------------|
| Crítica | Los usuarios no pueden hacer su tarea principal sin él | SEV2 o mayor cuando falla |
| Alta | Importante, pero hay alternativa | SEV3 o mayor |
| Normal | Interno o secundario | SEV4 o mayor |

Mantén la lista de servicios críticos alineada con los flujos críticos de [niveles de incidente](incident-levels.md).

## Obligatorio por servicio

- Un responsable con nombre (equipo o rol, no una sola persona que podría irse).
- Señales de salud y alertas que avisan a la rotación de guardia.
- Un runbook para los fallos más comunes.
- Los proveedores de los que depende, listados en el [catálogo de proveedores](vendor-management/vendor-catalog.md).
- Sus objetivos, si los hay: disponibilidad, latencia, tiempo de recuperación. {{pending: fijar objetivos por servicio crítico}}

## Ciclo de vida

- **Servicio nuevo**: se añade aquí antes de llegar a producción.
- **Obsoleto**: se marca, con fecha de fin y una ruta de migración para los usuarios.
- **Retirado**: se elimina cuando sus datos, alertas y accesos se han limpiado.

## Revisión

Revisa el catálogo cada {{pending: frecuencia}} y tras cada cambio de arquitectura.

## Relacionados

- [Modelo de soporte](support-model.md)
- [Niveles de incidente](incident-levels.md)
- [Rotación de guardia](team/on-call-rotation.md)
- [Catálogo de proveedores](vendor-management/vendor-catalog.md)
- [Política de ventanas de mantenimiento](maintenance-window-policy.md)
