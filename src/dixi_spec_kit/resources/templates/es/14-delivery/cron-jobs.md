# Tareas programadas

## Propósito

Listar cada tarea programada, cuándo corre, qué hace y qué pasa cuando falla. Las tareas que corren en silencio y fallan en silencio son una fuente habitual de incidentes.

## Reglas

- Los horarios se declaran en configuración versionada, nunca solo en un servidor.
- Las horas están en UTC; anota al lado la hora local de negocio si importa.
- Toda tarea es idempotente: ejecutarla dos veces produce el mismo resultado.
- Solo corre una instancia a la vez salvo que la tarea esté diseñada para paralelismo (usa un bloqueo).
- Toda tarea emite métricas de duración y fallos, y logs con su nombre.
- Una tarea que no termina bien dentro de su intervalo esperado genera una alerta.

## Inventario de tareas

| Tarea | Horario (UTC) | Qué hace | Duración máxima | Idempotente | Si falla | Responsable |
|---|---|---|---|---|---|---|
| {{pending: p. ej. cleanup-expired-sessions}} | {{pending: expresión cron}} | {{pending: descripción}} | {{pending: minutos}} | Sí | {{pending: reintento, alerta}} | {{pending: rol}} |
| {{pending: p. ej. nightly-report}} | {{pending: expresión cron}} | {{pending: descripción}} | {{pending: minutos}} | {{pending: sí o no}} | {{pending: acción}} | {{pending: rol}} |

## Manejo de fallos

- Reintentos: {{pending: número y espera progresiva}}.
- Tras los reintentos: alerta a {{pending: canal}} y registro del fallo.
- Ejecuciones perdidas (sistema caído a la hora programada): {{pending: ejecutar al recuperarse u omitir}}.

## Despliegue

- Las tareas usan el mismo artefacto y configuración que el servicio al que pertenecen.
- Durante un despliegue, las tareas en curso terminan o se detienen de forma segura: {{pending: comportamiento}}.
- Una tarea nueva se prueba en staging antes de activarse en producción.

## Monitoreo

| Señal | Fuente |
|---|---|
| Duración por ejecución | `job.run.duration` en el catálogo de métricas |
| Fallos por ejecución | `job.run.failures` en el catálogo de métricas |
| Hora del último éxito | {{pending: métrica o consulta de logs}} |

## Relacionados

- [Workers y colas](workers-and-queues.md)
- [Catálogo de métricas](../12-observability/metrics-catalog.md)
- [Reglas de alertas](../12-observability/alerting-rules.md)
- [Estrategia de trazas](../12-observability/tracing-strategy.md)
