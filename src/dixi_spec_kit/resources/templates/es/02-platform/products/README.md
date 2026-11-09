# Productos

## Propósito

Contener una carpeta por cada producto de la plataforma. Cada carpeta describe qué hace el producto,
dónde están sus límites y de qué depende, para que equipos y agentes trabajen en un producto sin
romper otro. Este README explica cómo añadir la carpeta de un producto; no define ningún producto.

## Añadir un producto

1. Registra el producto en el [mapa de productos](../product-map.md) con un ID `PROD-NNN`.
2. Crea una carpeta `products/<slug-del-producto>/` con palabras en minúsculas separadas por guiones.
3. Empieza la especificación del producto con la [plantilla de producto](../../10-engineering/templates/product-template.md).
4. Añade los archivos de abajo y completa cada marcador `{{pending: ...}}` con la persona responsable.
5. Registra los dominios del producto en `.dixi/traceability.json` y ejecuta `dixi check`.

## Estructura de carpeta sugerida

```text
products/<slug-del-producto>/
  product-spec.md          Propósito, segmento, objetivos a los que sirve, responsable, etapa
  capabilities.md          Capacidades de negocio que el producto posee o usa
  context-boundaries.md    Contextos delimitados, datos propios, lo que queda fuera
  dependencies.md          Servicios compartidos, otros productos y sistemas externos
```

## Qué debe responder cada archivo

- `capabilities.md`: qué `CAP-NNN` posee el producto, cuáles consume de otros y a qué objetivo
  estratégico sirve cada una.
- `context-boundaries.md`: los contextos y dominios dentro del producto, las entidades de las que es
  dueño, el lenguaje que usa y la lista explícita de responsabilidades que no asume.
- `dependencies.md`: cada dependencia con su dirección, ruta del contrato, criticidad y alternativa
  cuando no está disponible.

## Lista de comprobación antes de dar un producto por definido

- Responsable y etapa registrados: {{pending: responsable y etapa de cada producto}}
- Las capacidades no se solapan con otro producto sin una decisión escrita.
- Cada dependencia apunta a un contrato de `07-contracts/`.
- Tenencia e identidad siguen las estrategias de la plataforma.

## Relacionados

- [Mapa de productos](../product-map.md)
- [Visión general de la plataforma](../platform-overview.md)
- [Integraciones entre productos](../cross-product-integrations.md)
- [Plantilla de producto](../../10-engineering/templates/product-template.md)
