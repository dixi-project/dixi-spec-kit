# Mapa de logs

## Propósito

Mostrar qué componente escribe qué logs, en qué formato, a dónde van y cuánto tiempo se conservan. Las reglas de código para escribir una línea de log viven en el estándar de logging; este mapa cubre la parte operativa.

## Formato

- Estructurado, un objeto JSON por línea, escrito a la salida estándar salvo que se decida otra cosa.
- Campos obligatorios: `timestamp` (UTC, ISO 8601), `level`, `service.name`, `service.version`, `deployment.environment`, `message` y un identificador de correlación o de traza.
- Campos opcionales: `event` (un nombre estable), `duration_ms`, `error.type`.

## Niveles

| Nivel | Uso | Activo en producción |
|---|---|---|
| error | Una petición o tarea falló y requiere atención | Sí |
| warn | Inesperado pero manejado; puede requerir atención si se repite | Sí |
| info | Eventos relevantes para el negocio y ciclo de vida | Sí |
| debug | Detalle de diagnóstico | {{pending: solo bajo demanda y por tiempo limitado}} |

## Mapa

| Componente | Flujo de logs | Eventos clave | Destino | Retención | Contiene datos personales |
|---|---|---|---|---|---|
| Web o API | {{pending: nombre}} | petición completada, fallo de autenticación | {{pending: destino}} | {{pending: días}} | No (enmascarados) |
| Workers | {{pending: nombre}} | tarea iniciada, tarea fallida, reintento | {{pending: destino}} | {{pending: días}} | No (enmascarados) |
| Auditoría | {{pending: nombre}} | acción privilegiada, cambio de permisos | {{pending: destino}} | {{pending: según la política de retención}} | {{pending: sí o no}} |

## Nunca registrar

- Contraseñas, tokens, llaves de API, cookies de sesión ni cabeceras de autorización completas.
- Datos de pago, documentos de identidad completos ni datos de salud.
- Cuerpos de petición completos por defecto; registra identificadores en su lugar.

## Acceso

- Quién puede leer logs de producción: {{pending: roles}}
- Cómo se concede y revisa el acceso: {{pending: proceso}}
- Los logs de auditoría son de solo anexado y están separados de los de aplicación.

## Relacionados

- [Estándar de logging](../10-engineering/logging-standard.md)
- [Estrategia de observabilidad](observability-strategy.md)
- [Política de retención de datos](../08-data/retention-policy.md)
- [Clasificación de PII](../08-data/pii-classification.md)
