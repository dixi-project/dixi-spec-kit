# Revisión preparada — FEATURE-002

## Propósito

Informe de `/dixi.review` para la persona revisora del cambio de etiquetas. No aprueba nada.

## Riesgo

Bajo: cambia validación de entrada y lectura de datos locales; no toca persistencia, red ni permisos.

## Criterio → cambio → prueba

| Criterio | Cambio | Prueba |
|---|---|---|
| 1 Normalizar | `normalize_tags` en `notes/store.py` | `test_tags_are_normalized` |
| 2 Rechazar inválidas | `TAG` y `NoteError("invalid_tag")` | `test_invalid_tags_rejected_without_writing` |
| 3 Filtrar | `NoteStore.list(tag)` y `list --tag` | `test_filter_by_tag`, `test_cli_filter_and_invalid_tag` |
| 4 Datos antiguos | `normalize_tags(..., strict=False)` al leer | `test_legacy_tags_normalized_on_read` |

## Hallazgos

- Ninguno bloqueante. `tests/test_notes.py` (congelada) no cambió.
- Observación: una etiqueta antigua inválida se descarta al leer en lugar de fallar; coherente con el criterio 4, conviene confirmarlo con la persona.

## Para la persona revisora

- [ ] Los criterios de FEATURE-002 reflejan lo pedido.
- [ ] `make verify` en verde en tu entorno.
- [ ] La observación sobre etiquetas antiguas inválidas es aceptable.

## Relacionados

- [Funcionalidad](../05-features/tags/feature-spec.md)
- [Impacto](../05-features/tags/impact.md)
