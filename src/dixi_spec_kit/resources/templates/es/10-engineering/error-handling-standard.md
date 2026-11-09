# Estándar de manejo de errores

## Propósito

Que los errores sean predecibles para usuarios, clientes y operadores: cada fallo tiene un código
estable, un mensaje seguro, contexto suficiente para diagnosticarlo y un responsable claro. Aplica
a servicios, APIs y workers.

## Categorías de error

| Categoría | Significado | Estado HTTP típico | ¿Reintentar? |
|---|---|---|---|
| Validación | La entrada no cumple el contrato | 400 / 422 | No, corregir la entrada |
| Autenticación | Identidad ausente o inválida | 401 | Tras volver a autenticarse |
| Autorización | La identidad no tiene permiso | 403 (o 404 para ocultar existencia) | No |
| No encontrado | El recurso no existe para quien llama | 404 | No |
| Conflicto | Estado o versión no coinciden | 409 | Tras refrescar el estado |
| Límite de uso | Se excedió una cuota | 429 | Sí, tras la espera indicada |
| Dependencia | Falló un sistema externo | 502 / 503 / 504 | Sí, con backoff |
| Interno | Defecto inesperado | 500 | Quizá; es un bug |

## Reglas

1. **Los errores de dominio son tipos explícitos**, no excepciones genéricas con texto libre. El
   dominio los lanza; el borde (controlador, handler, consumidor) los traduce al transporte.
2. **Códigos de error estables y documentados**, como `ORDER_NOT_FOUND`. El cliente decide por el
   código, nunca por el mensaje. {{pending: convención de nombres y ubicación del registro de códigos}}
3. **Una sola forma de respuesta para todo error.** {{pending: formato del cuerpo de error, p. ej.
   RFC 9457 problem details o un sobre propio}} Incluye código, mensaje seguro e ID de correlación.
4. **Mensajes seguros.** Sin trazas, consultas, hosts internos ni datos personales en respuestas.
   Los mensajes visibles salen de los catálogos de traducción.
5. **Nunca tragarse errores.** Capturar solo lo que se puede manejar; lo demás se propaga al borde,
   que lo registra una vez con contexto.
6. **Registrar una vez, en el borde**, con el ID de correlación, según
   [el estándar de logging](logging-standard.md).
7. **Reintentos acotados** (intentos, tiempo total) con backoff exponencial y jitter, y solo en
   operaciones idempotentes o protegidas con clave de idempotencia.
8. **Timeout en toda llamada externa.** {{pending: timeouts por defecto por tipo de dependencia}}
9. **Fallar cerrado en controles de seguridad**: si no se puede evaluar la autorización, se niega.
10. **Cada código de error tiene una prueba** que demuestra su estado, forma y clave de mensaje.

## Ejemplo de respuesta

```json
{
  "code": "ORDER_NOT_FOUND",
  "message_key": "errors.order_not_found",
  "correlation_id": "{{pending: formato del ID de correlación}}"
}
```

## Relacionados

- [Estándar de logging](logging-standard.md)
- [Estándar de diseño de APIs](api-design-standard.md)
- [Estándar de código seguro](secure-coding-standard.md)
- [Estándares de código](coding-standards.md)
