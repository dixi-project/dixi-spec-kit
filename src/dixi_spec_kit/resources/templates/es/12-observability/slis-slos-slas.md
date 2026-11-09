# SLIs, SLOs y SLAs

## Propósito

Convertir «el sistema debe ser confiable» en indicadores medibles, objetivos internos y, solo cuando el negocio lo decida, compromisos externos. Los números de este documento son decisiones del proyecto, no valores por defecto.

## Definiciones

- **SLI** (indicador): proporción de eventos buenos sobre eventos válidos, medida desde el punto de vista de la persona usuaria.
- **SLO** (objetivo): la meta de un SLI en una ventana, por ejemplo «el 99,x % de las peticiones tiene éxito en 28 días».
- **Presupuesto de error**: `1 - SLO`; la cantidad de fallos que el equipo acepta antes de dejar de entregar funcionalidades para corregir la confiabilidad.
- **SLA** (acuerdo): una promesa contractual con consecuencias. Siempre debe ser más holgado que el SLO.

## Catálogo de indicadores

| ID | Recorrido de usuario | Evento bueno | Evento válido | Medido en | Fuente |
|---|---|---|---|---|---|
| SLI-001 | {{pending: recorrido principal}} | Respuesta sin error de servidor | Todas las peticiones salvo chequeos de salud | {{pending: borde o servicio}} | {{pending: nombre de métrica}} |
| SLI-002 | {{pending: recorrido principal}} | Respuesta más rápida que {{pending: umbral}} | Igual que arriba | {{pending: borde o servicio}} | {{pending: nombre de métrica}} |
| SLI-003 | {{pending: trabajo asíncrono, si existe}} | Procesado en menos de {{pending: tiempo}} | Todos los trabajos aceptados | Worker | {{pending: nombre de métrica}} |

## Objetivos

| SLI | SLO | Ventana | Presupuesto de error | Responsable |
|---|---|---|---|---|
| SLI-001 | {{pending: meta}} | {{pending: p. ej. 28 días móviles}} | {{pending: calculado}} | {{pending: rol}} |
| SLI-002 | {{pending: meta}} | {{pending: ventana}} | {{pending: calculado}} | {{pending: rol}} |

Solo como ejemplo, no como recomendación: un SLO del 99,5 % en 28 días permite unas 3,4 horas de fallo en esa ventana.

## Política de presupuesto de error

- Presupuesto sano: entrega normal.
- Presupuesto por debajo del {{pending: porcentaje}}: priorizar trabajo de confiabilidad en la siguiente iteración.
- Presupuesto agotado: {{pending: congelar versiones no urgentes, quién puede conceder excepciones}}.

## Compromisos externos

- SLA ofrecido: {{pending: ninguno todavía, o la meta acordada y sus consecuencias}}
- Exclusiones (mantenimiento planificado, fallos del lado del cliente): {{pending: lista}}

## Revisión

Revisa indicadores y objetivos {{pending: frecuencia}} con producto e ingeniería. Cambia un SLO solo con un motivo escrito.

## Relacionados

- [Requisitos no funcionales](../11-quality/non-functional-requirements.md)
- [Catálogo de métricas](metrics-catalog.md)
- [Reglas de alertas](alerting-rules.md)
- [Estrategia de observabilidad](observability-strategy.md)
- [Objetivo](../01-business/vision.md)
