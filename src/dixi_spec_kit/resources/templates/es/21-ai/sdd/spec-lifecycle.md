# Ciclo de vida de specs

## Propósito

Definir los estados por los que pasa una especificación, qué debe cumplirse para avanzar y cómo se detecta la deriva entre spec y código. Los estados describen documentos; nunca afirman que se ejecutaron pruebas o revisiones si no hay evidencia.

## Estados

| Estado | Significado | Quién puede avanzarla |
| --- | --- | --- |
| Borrador | En redacción; puede contener marcas `{{pending: ...}}` | Autor |
| Revisión | Lo bastante completa para leerse y cuestionarse | El autor la pide, quien revisa la lee |
| Aprobada | Aceptada como referencia para pruebas y código | Una persona responsable |
| Implementada | Existen código y pruebas que pasan y coinciden con la spec | Persona, con evidencia |
| Obsoleta | Se conserva como historia; reemplazada o retirada | Una persona responsable |

## Criterios de salida

### Borrador → Revisión

- [ ] Empieza con un título y una sección de propósito.
- [ ] Nombra su spec padre y conserva su ID.
- [ ] Los enlaces locales resuelven (`dixi check` reporta estructura rota).

### Revisión → Aprobada

- [ ] Sin marcas pendientes en campos que bloquean pruebas (criterios, entradas, errores).
- [ ] Coherente con su padre; los términos coinciden con el glosario del dominio.
- [ ] Registrada en `.dixi/traceability.json`.
- [ ] Revisada por una persona; la revisión de un agente sola no basta.

### Aprobada → Implementada

- [ ] Existen pruebas derivadas del contrato que primero se vieron fallar.
- [ ] Las comprobaciones reales del proyecto pasan y el resultado se reporta tal como se observó.
- [ ] No hay deriva conocida entre spec y comportamiento.

## Versionado

- Las specs viven en control de versiones; el historial de pull requests es el registro de cambios.
- Un cambio incompatible en un contrato aprobado crea una nueva versión o un nuevo ID de contrato: {{pending: convención de versionado de contratos}}

## Deriva

Hay deriva cuando el código ya no hace lo que dice la spec. Señales: pruebas editadas sin cambio en la spec, comportamiento presente en el código pero en ninguna spec, o specs que mencionan funciones eliminadas. Al detectarla, actualiza la spec o el código en el mismo cambio y registra el motivo.

- Frecuencia de revisión de deriva: {{pending: cadencia de revisión}}

## Relacionados

- [Metodología](methodology.md)
- [Reglas de validación](validation-rules.md)
- [Matriz de trazabilidad](traceability-matrix.md)
- [Plan de pruebas](../../11-quality/test-plan.md)
