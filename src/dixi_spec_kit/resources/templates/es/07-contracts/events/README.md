# Contratos de eventos

## Propósito

Guardar los contratos de los eventos que publican módulos y productos. Un evento enuncia un hecho que
ya ocurrió («pedido realizado»); el productor no conoce ni espera a sus consumidores. Como los
consumidores están desacoplados, el contrato del evento es lo único que los mantiene alineados:
nombre, contenido, garantías de orden y versionado deben ser explícitos.

## Estructura

```text
07-contracts/events/
  <dominio>.<entidad>.<hecho>.v<N>.json    Un contrato por evento y versión mayor
```

- Parte de la [plantilla de evento](../../10-engineering/templates/event-template.json).
- Sigue el [estándar de diseño de eventos](../../10-engineering/event-design-standard.md).
- Nombra los eventos en pasado con el lenguaje ubicuo, p. ej. `billing.invoice.issued`.

## Qué debe definir cada contrato de evento

- Nombre, versión, módulo productor y los IDs de funcionalidad que lo justifican.
- Envoltorio: ID del evento, tipo, momento en que ocurrió, productor, inquilino, ID de correlación.
- Contenido: solo los datos que necesitan los consumidores; prefiere IDs a copias de objetos grandes.
- Datos personales del contenido, señalados y minimizados.
- Garantía de entrega asumida: {{pending: al menos una vez, como máximo una vez}}.
- Garantía de orden y la clave a la que aplica, si la hay.
- Consumidores conocidos y qué hace cada uno con el evento.

## Reglas para consumidores

- Los consumidores son idempotentes: procesar el mismo evento dos veces no tiene efecto adicional.
- Toleran campos desconocidos y eventos que llegan fuera de orden.
- Los eventos fallidos pasan a una ruta de reintento y luego a un área de mensajes fallidos que
  alguien vigila.

## Índice de eventos

| Evento | Versión | Productor | Consumidores | Estado |
|---|---|---|---|---|
| {{pending: nombre del evento}} | {{pending: versión}} | {{pending: módulo}} | {{pending: módulos}} | {{pending: borrador o publicado}} |

## Versionado

- Añadir campos opcionales mantiene la versión; eliminar o cambiar el significado crea una nueva.
- Las versiones antigua y nueva se publican en paralelo durante {{pending: duración}}.

## Relacionados

- [Comandos](../commands/README.md)
- [Estándar de diseño de eventos](../../10-engineering/event-design-standard.md)
- [Arquitectura de eventos](../../09-architecture/event-architecture.md)
- [Esquemas](../schemas/README.md)
