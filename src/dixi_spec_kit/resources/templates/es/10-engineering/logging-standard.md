# Estándar de logging

## Propósito

Dar al proyecto una sola convención de logging para que cualquier evento se pueda encontrar,
correlacionar entre servicios y leer por personas y herramientas sin exponer datos sensibles.

## Formato

1. **Logs estructurados**, un evento por línea, en un formato legible por máquina.
   {{pending: formato de log, p. ej. líneas JSON}}
2. **Campos obligatorios** en cada evento:

| Campo | Descripción |
|---|---|
| `timestamp` | UTC, ISO 8601 con milisegundos |
| `level` | `debug`, `info`, `warning`, `error` |
| `service` | Nombre del componente que emite |
| `environment` | p. ej. `dev`, `staging`, `prod` |
| `message` | Texto corto y constante que describe el evento |
| `correlation_id` | Se propaga entre llamadas, colas y jobs |
| `tenant_id` | Cuando el sistema es multi-tenant; si no, se omite |

3. **El contexto va en campos, no en el mensaje.** Escribe `message="order created"` con
   `order_id=...`, no una frase interpolada. Los mensajes constantes se pueden buscar.

## Niveles

- `error`: alguien debe actuar; suele ir ligado a una alerta.
- `warning`: inesperado pero manejado; conviene revisarlo.
- `info`: ocurrió un evento de negocio o de ciclo de vida (petición atendida, job terminado).
- `debug`: detalle de diagnóstico; desactivado en producción por defecto.

## Lo que nunca se registra

- Secretos, tokens, contraseñas, cookies de sesión, API keys, llaves privadas.
- Datos personales sin enmascarar (nombres, correos, teléfonos, documentos, direcciones).
- Cuerpos completos de petición o respuesta de endpoints sensibles.
- Datos de pago.

Regla de enmascarado: {{pending: regla de enmascarado o hash para identificadores que deben seguir siendo correlacionables}}

## Retención y acceso

- Retención: {{pending: periodo de retención por entorno y requisito legal}}
- Acceso: {{pending: roles autorizados a leer logs de producción}}
- Los logs no son una base de datos: los hechos de negocio que se consultan van en almacenamiento o eventos.

## Errores

Registra cada error una sola vez, en el borde, con su código e ID de correlación, como describe
[el estándar de manejo de errores](error-handling-standard.md).

## Relacionados

- [Estándar de manejo de errores](error-handling-standard.md)
- [Estándar de código seguro](secure-coding-standard.md)
- [Estándares de código](coding-standards.md)
- [Plantilla de runbook](templates/runbook-template.md)
