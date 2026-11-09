# Products

## Purpose

Hold one folder per product on the platform. Each folder describes what the product does, where its
boundaries are and what it depends on, so that teams and agents can work on one product without
breaking another. This README explains how to add a product folder; it does not define any product.

## Adding a product

1. Register the product in the [product map](../product-map.md) with a `PROD-NNN` ID.
2. Create a folder `products/<product-slug>/` using lowercase words separated by hyphens.
3. Start the product spec from the [product template](../../10-engineering/templates/product-template.md).
4. Add the files below and fill every `{{pending: ...}}` marker with the responsible person.
5. Register the product's domains in `.dixi/traceability.json` and run `dixi check`.

## Suggested folder layout

```text
products/<product-slug>/
  product-spec.md          Purpose, segment, goals served, owner, stage
  capabilities.md          Business capabilities the product owns or uses
  context-boundaries.md    Bounded contexts, owned data, what stays outside
  dependencies.md          Shared services, other products and external systems
```

## What each file should answer

- `capabilities.md`: which `CAP-NNN` the product owns, which it consumes from others, and which
  strategic goal each one serves.
- `context-boundaries.md`: the contexts and domains inside the product, the entities it owns, the
  language it uses, and the explicit list of responsibilities it does not take.
- `dependencies.md`: each dependency with direction, contract path, criticality and fallback when
  the dependency is unavailable.

## Checklist before a product is considered defined

- Owner and stage are recorded: {{pending: owner and stage of each product}}
- Capabilities do not overlap with another product without a written decision.
- Every dependency points to a contract in `07-contracts/`.
- Tenancy and identity follow the platform strategies.

## Related

- [Product map](../product-map.md)
- [Platform overview](../platform-overview.md)
- [Cross-product integrations](../cross-product-integrations.md)
- [Product template](../../10-engineering/templates/product-template.md)
