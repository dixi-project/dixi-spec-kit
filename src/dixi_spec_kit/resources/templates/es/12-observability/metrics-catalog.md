# Catálogo de métricas

## Propósito

Listar cada métrica que emite el sistema con un nombre estable, una unidad y un responsable, para que tableros, alertas y SLIs se refieran a lo mismo. No se debe confiar en una métrica que no esté en este catálogo.

## Reglas de nombres

- Palabras en minúsculas separadas por puntos o guiones bajos, de forma consistente: {{pending: elegir una convención}}.
- Incluye la unidad en el nombre o en sus metadatos (segundos, bytes, peticiones).
- Usa contadores para lo que solo crece, gauges para valores actuales e histogramas para duraciones y tamaños.
- Mantén acotada la cardinalidad de etiquetas: nunca uses IDs de usuario, correos, URLs completas ni texto libre como etiqueta.

## Métricas base por punto de entrada

Para cada endpoint HTTP, consumidor de cola o tarea programada, registra al menos tasa, errores y duración:

| Métrica | Tipo | Unidad | Etiquetas | Propósito |
|---|---|---|---|---|
| `http.server.request.duration` | histograma | segundos | ruta, método, clase de estado | Latencia y throughput |
| `http.server.request.errors` | contador | peticiones | ruta, clase de estado | Tasa de errores |
| `job.run.duration` | histograma | segundos | tarea | Tiempo de tareas programadas |
| `job.run.failures` | contador | ejecuciones | tarea | Fallos de tareas programadas |
| `queue.messages.pending` | gauge | mensajes | cola | Acumulación |
| `queue.messages.dead_lettered` | contador | mensajes | cola | Mensajes envenenados |

## Métricas de recursos

| Métrica | Tipo | Unidad | Propósito |
|---|---|---|---|
| Uso de CPU | gauge | proporción | Capacidad |
| Uso de memoria | gauge | bytes | Capacidad y fugas |
| Conexiones de base de datos en uso | gauge | conexiones | Saturación del pool |

## Métricas de negocio

| Métrica | Tipo | Unidad | Responsable | Por qué importa |
|---|---|---|---|---|
| {{pending: p. ej. pedidos completados}} | contador | {{pending: unidad}} | {{pending: rol}} | {{pending: vínculo con un objetivo}} |
| {{pending: p. ej. registros}} | contador | {{pending: unidad}} | {{pending: rol}} | {{pending: vínculo con un objetivo}} |

## Proceso de cambio

1. Agrega o renombra una métrica aquí en el mismo pull request que cambia el código.
2. Actualiza todo tablero, alerta o SLI que la use.
3. Conserva el nombre obsoleto durante {{pending: periodo}} antes de eliminarlo.

## Relacionados

- [SLIs, SLOs y SLAs](slis-slos-slas.md)
- [Mapa de tableros](dashboard-map.md)
- [Reglas de alertas](alerting-rules.md)
- [Métricas de ingeniería](../11-quality/engineering-metrics.md)
