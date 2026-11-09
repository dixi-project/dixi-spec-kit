# Contratos de API

## Propósito

Guardar los contratos de las API síncronas que el proyecto expone o consume. Un contrato es el
acuerdo entre productor y consumidor: operaciones, entradas, salidas, errores, autenticación y
versionado. Escribe el contrato antes de la implementación, revísalo con los consumidores y deriva
de él pruebas de contrato, para que ambos lados evolucionen de forma independiente.

## Estructura

```text
07-contracts/api/
  <servicio>-api.yaml      Contrato legible por máquinas (por ejemplo, OpenAPI)
  <servicio>-api.md        Notas opcionales: alcance, decisiones, ejemplos
```

- Parte de la [plantilla de API](../../10-engineering/templates/api-template.yaml).
- Sigue el [estándar de diseño de API](../../10-engineering/api-design-standard.md).
- Usa `/dixi.contract` (o `$dixi-contract`) para redactar un contrato a partir de una funcionalidad.

## Qué debe definir cada contrato

- Ruta base, versión y los IDs de funcionalidad a los que sirve.
- Cada operación: método, ruta, parámetros, cuerpo de la petición, respuestas y códigos de error.
- Autenticación y permisos requeridos por operación.
- Contexto de tenencia, si la plataforma es multiinquilino.
- Convenciones de paginación, filtrado y ordenación para colecciones.
- Idempotencia en las operaciones que crean o cambian estado.
- Ejemplos de éxito y de los errores más comunes.

## Índice de contratos

| ID | Contrato | Productor | Consumidores | Versión | Estado |
|---|---|---|---|---|---|
| CONTRACT-001 | [Ejemplo](../example.md) | {{pending: productor}} | {{pending: consumidores}} | {{pending: versión}} | borrador |
| {{pending: ID de CONTRACT}} | {{pending: archivo}} | {{pending: productor}} | {{pending: consumidores}} | {{pending: versión}} | {{pending: estado}} |

Registra cada contrato en `.dixi/traceability.json` con `kind: contract` y la funcionalidad como
padre, y ejecuta `dixi check`.

## Versionado y cambios

- Esquema de versionado: {{pending: en la ruta, en una cabecera o en el tipo de contenido}}
- Los cambios aditivos (campos opcionales nuevos, operaciones nuevas) mantienen la versión.
- Los cambios incompatibles crean una versión nueva y un periodo de retirada de {{pending: duración}}.

## Relacionados

- [Ejemplo de contrato](../example.md)
- [Estándar de diseño de API](../../10-engineering/api-design-standard.md)
- [Esquemas](../schemas/README.md)
- [Estándar de gestión de errores](../../10-engineering/error-handling-standard.md)
