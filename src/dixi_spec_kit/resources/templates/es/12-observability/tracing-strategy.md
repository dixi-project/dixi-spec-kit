# Estrategia de trazas

## Propósito

Definir cómo se sigue una petición o un mensaje a través de servicios, colas y tareas programadas, para que el equipo encuentre dónde ocurren el tiempo y los errores en un sistema distribuido.

## Decisiones

- Formato de propagación de contexto: {{pending: un estándar abierto como W3C Trace Context; registrar en un ADR}}
- Enfoque de instrumentación: {{pending: automática, manual o mixta por stack}}
- Topología del colector o agente: {{pending: sidecar, por host o central}}
- Backend de trazas: {{pending: decidir y registrar en un ADR}}

## Propagación

- HTTP entrante: lee el contexto recibido; inicia una traza nueva solo si no existe o si quien llama no es de confianza.
- HTTP saliente: inyecta el contexto en cada llamada a servicios internos.
- Colas y eventos: escribe el contexto en las cabeceras del mensaje al publicar y continúalo al consumir, como enlace o span hijo.
- Tareas programadas: inicia una traza nueva por ejecución y registra el nombre de la tarea.
- Nunca propagues contexto a terceros salvo acuerdo; puede filtrar identificadores internos.

## Convenciones de spans

| Span | Patrón de nombre | Atributos obligatorios |
|---|---|---|
| Servidor HTTP | `MÉTODO /plantilla/de/ruta` | ruta, código de estado |
| Cliente HTTP | `MÉTODO host` | servicio destino, código de estado |
| Base de datos | operación y tabla | sistema, operación (sin sentencias completas con valores) |
| Publicar o consumir mensaje | `queue publish` / `queue process` | nombre de cola, ID de mensaje |

No pongas datos personales, secretos ni cargas completas en los atributos de un span.

## Muestreo

- Tasa por defecto: {{pending: porcentaje de trazas que se conserva}}
- Conservar siempre: errores, peticiones lentas por encima de {{pending: umbral}} y trazas de chequeos sintéticos.
- Punto de decisión: {{pending: al inicio, al final o ambos}}

## Correlación

- Los logs incluyen el identificador de traza para que una traza enlace con sus líneas de log.
- Las métricas pueden llevar ejemplares que apunten a una traza de muestra, si el backend lo admite.

## Verificación

- [ ] Una traza de punta a punta cruza web, servicio, cola y worker sin romperse
- [ ] El muestreo conserva los errores aunque la tasa por defecto sea baja
- [ ] No hay datos personales en una muestra de atributos de spans

## Relacionados

- [Estrategia de observabilidad](observability-strategy.md)
- [Mapa de logs](logging-map.md)
- [Arquitectura de eventos](../09-architecture/event-architecture.md)
- [Workers y colas](../14-delivery/workers-and-queues.md)
