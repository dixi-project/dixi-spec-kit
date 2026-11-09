# Estándar de diseño de APIs

## Propósito

Que toda API del proyecto sea consistente, se diseñe primero como contrato y pueda evolucionar sin
romper en silencio a quienes la usan.

Estilo de API: {{pending: REST sobre HTTP, RPC, GraphQL u otro, registrado en un ADR}}

## Contrato primero

1. El contrato se escribe y revisa **antes** de la implementación, con
   [la plantilla de API](templates/api-template.yaml) o el formato elegido por el proyecto.
2. El contrato vive en el repositorio y es la fuente de los tipos del cliente, los mocks y las
   pruebas de contrato. Implementación y contrato se contrastan en `make verify`.
3. Cada operación se traza a un ID de feature o de contrato.

## Convenciones

| Tema | Regla |
|---|---|
| Recursos | Sustantivos en plural en las rutas (`/orders/{order_id}`); verbos solo para acciones que no son CRUD |
| Nombres | {{pending: estilo de campos JSON, p. ej. snake_case o camelCase}}, usado de forma consistente |
| Métodos | `GET` seguro, `PUT`/`DELETE` idempotentes, `POST` crea o dispara acciones |
| Códigos de estado | Según [el estándar de manejo de errores](error-handling-standard.md) |
| Fechas | ISO 8601 en UTC |
| Dinero | Enteros de la unidad mínima más código de moneda |
| Identificadores | Cadenas opacas; nunca exponer IDs internos secuenciales |
| Paginación | {{pending: por cursor o por offset; tamaño de página por defecto y máximo}} |
| Filtros y orden | Parámetros explícitos y documentados; se rechazan los desconocidos |
| Idiomas | Textos visibles negociados con `Accept-Language`; los códigos no dependen del idioma |

## Versionado y cambios

1. {{pending: estrategia de versionado, p. ej. versión mayor en la ruta o en un header}}
2. **Cambios aditivos** (campo opcional nuevo, endpoint nuevo) no requieren versión nueva.
3. **Cambios incompatibles** (campo eliminado o renombrado, tipo o significado distinto, entrada
   obligatoria nueva) requieren versión nueva, aviso de deprecación y ventana de migración.
4. Las operaciones deprecadas anuncian su fecha de retiro. {{pending: ventana mínima de deprecación}}

## Seguridad

- Autenticación en toda operación no pública. {{pending: esquema de autenticación}}
- Autorización comprobada por recurso, no solo por ruta.
- Entrada validada contra el esquema del contrato; campos desconocidos rechazados.
- Límites de uso documentados por tipo de cliente; las respuestas indican la espera para reintentar.
- Claves de idempotencia en operaciones que crean recursos o mueven dinero.

## Lista de revisión

- [ ] Contrato actualizado y revisado antes del código.
- [ ] Toda respuesta de error usa la forma compartida.
- [ ] Los cambios incompatibles tienen versión nueva y plan de deprecación.
- [ ] Las pruebas de contrato cubren el éxito y cada error documentado.

## Relacionados

- [Plantilla de API](templates/api-template.yaml)
- [Estándar de manejo de errores](error-handling-standard.md)
- [Estándar de código seguro](secure-coding-standard.md)
- [Contrato borrador](../07-contracts/example.md)
