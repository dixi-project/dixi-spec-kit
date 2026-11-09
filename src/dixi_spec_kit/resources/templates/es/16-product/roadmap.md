# Hoja de ruta del producto

## Propósito

Mostrar hacia dónde va el producto y por qué, en términos de resultados y no de fechas prometidas al día. La hoja de ruta conecta el objetivo de negocio con las funcionalidades que se especificarán, para que cada elemento pueda rastrearse y cuestionarse.

Estado: borrador. {{pending: nombrar a la persona que mantiene y publica la hoja de ruta}}

## Horizontes

Usa horizontes de tiempo en lugar de fechas fijas de entrega. Cuanto más lejano es un elemento, menos detalle y certeza tiene.

| Horizonte | Significado | Detalle esperado |
|-----------|-------------|------------------|
| Ahora | En especificación o construcción | Especificación de funcionalidad con criterios de aceptación |
| Después | Dirección comprometida, sin empezar | Problema, resultado buscado, tamaño aproximado |
| Más adelante | Ideas que vale la pena explorar | Una línea y la evidencia que la originó |

{{pending: confirmar la duración de cada horizonte, por ejemplo uno, tres y seis meses}}

## Elementos

| ID | Resultado buscado | Horizonte | Evidencia | Especificación | Estado |
|----|-------------------|-----------|-----------|----------------|--------|
| RM-001 | {{pending: resultado medible, por ejemplo «los usuarios nuevos terminan la configuración sin ayuda»}} | Ahora | {{pending: nota de investigación o métrica}} | [FEATURE-001](../05-features/example/feature-spec.md) | Borrador |
| RM-002 | {{pending: resultado}} | Después | {{pending: evidencia}} | — | Idea |

Reglas:

- Cada elemento expresa un resultado que notaría un usuario o el negocio, no una tarea.
- Los elementos en «Ahora» deben apuntar a una especificación de funcionalidad; si no la tienen, se quedan en «Después».
- Los elementos entran y cambian de horizonte mediante el [marco de priorización](prioritization-framework.md).
- Cada elemento indica a qué idiomas y mercados se dirige; si sale en un solo idioma, lo dice de forma explícita.

## Temas

Agrupa los elementos en pocos temas que salgan del [objetivo de negocio](../01-business/vision.md).

- {{pending: tema 1, por ejemplo incorporación de usuarios}}
- {{pending: tema 2}}
- {{pending: tema 3}}

## Cadencia de revisión

- Revisa la hoja de ruta a intervalos fijos y después de cualquier hallazgo de investigación relevante.
- Registra cada revisión: qué se movió, qué se descartó y por qué.
- Comunica los cambios a quienes dependen de la hoja de ruta antes de publicarlos.

{{pending: decidir el intervalo de revisión y quién debe asistir}}

## Lo que la hoja de ruta no es

- No es un compromiso de entrega: las fechas pertenecen a los planes de versión.
- No es un backlog: las tareas detalladas viven en las especificaciones y en el gestor de trabajo.
- No es una lista de peticiones: cada elemento necesita evidencia, no solo alguien que lo pida.

## Relacionados

- [Marco de priorización](prioritization-framework.md)
- [Ciclo de vida de funcionalidades](feature-lifecycle.md)
- [Notas de versión](release-notes.md)
- [Propuesta de valor](../01-business/value-proposition.md)
- [Objetivo de negocio](../01-business/vision.md)
- [Estrategia de descubrimiento](../24-research/discovery-strategy.md)
