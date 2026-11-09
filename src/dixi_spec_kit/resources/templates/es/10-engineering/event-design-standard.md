# Estándar de diseño de eventos

## Propósito

Que los eventos asíncronos de la plataforma sean consistentes, versionados y seguros de consumir,
para que productores y consumidores evolucionen de forma independiente.

Tecnología de mensajería: {{pending: broker o bus de eventos elegido, registrado en un ADR}}

## Nombres

- Los eventos describen **hechos en pasado**: `order.created`, `payment.failed`.
- Formato: `<dominio>.<entidad>.<verbo_en_pasado>` o `<entidad>.<verbo_en_pasado>`.
  {{pending: convención de nombres y ubicación del registro}}
- Los comandos (peticiones de hacer algo) no son eventos y usan otro canal.

## Sobre

Todo evento usa el mismo sobre, como en [la plantilla de evento](templates/event-template.json):

| Campo | Descripción |
|---|---|
| `id` | ID único de este evento, usado para deduplicar |
| `type` | Nombre del evento |
| `version` | Versión del esquema de `data` |
| `occurred_at` | Cuándo ocurrió el hecho, UTC ISO 8601 |
| `source` | Servicio productor |
| `correlation_id` | Propagado desde la petición que lo causó |
| `data` | Contenido, descrito por un esquema versionado |

## Reglas

1. **Un esquema por evento y versión**, guardado en el repositorio y validado por pruebas del
   productor y del consumidor.
2. **Evolución aditiva.** Los campos opcionales nuevos mantienen la versión; eliminar o cambiar un
   campo crea una versión nueva, y el productor publica ambas durante la ventana de migración.
3. **La entrega al menos una vez es lo normal.** Los consumidores son idempotentes: deduplican por
   `id` o hacen que el efecto sea idempotente por naturaleza.
4. **Sin suposiciones de orden** salvo que el canal lo garantice por clave y la clave esté documentada.
5. **Contenido mínimo.** Incluir lo que el consumidor necesita para actuar; no filtrar datos
   personales innecesarios. {{pending: datos personales permitidos en eventos}}
6. **Los fallos van a un destino de mensajes muertos** tras reintentos acotados, con alerta y un
   runbook para reprocesar.
7. **Outbox o equivalente** cuando un evento debe publicarse junto con un cambio de estado, para que
   ambos no diverjan. {{pending: mecanismo de consistencia}}
8. **Cada evento tiene dueño** (módulo productor) y una lista de consumidores conocidos.

## Lista de revisión

- [ ] El nombre es un hecho en pasado; los campos del sobre están completos.
- [ ] Esquema y versión versionados; la compatibilidad está probada.
- [ ] Los consumidores son idempotentes y tienen ruta de mensajes muertos.
- [ ] El evento figura en la spec del módulo productor.

## Relacionados

- [Plantilla de evento](templates/event-template.json)
- [Estándar de manejo de errores](error-handling-standard.md)
- [Plantilla de flujo](templates/flow-template.md)
- [Plantilla de runbook](templates/runbook-template.md)
