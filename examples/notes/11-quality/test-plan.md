# TEST-001 — Plan de pruebas

## Propósito

Relacionar cada criterio con sus pruebas ejecutables; `make verify` ejecuta `dixi check` y la suite.

| Criterio | Prueba |
|---|---|
| FEATURE-001 · 1–3 | `tests/test_notes.py`: `test_add_assigns_increasing_ids`, `test_invalid_text_leaves_store_untouched`, `test_missing_store_is_empty` |
| FEATURE-001 · 4 | `test_search_is_case_insensitive` |
| FEATURE-001 · 5 | `test_cli_round_trip`, `test_cli_invalid_input_exit_code` |
| FEATURE-002 · 1–4 | `tests/test_tags.py` |

## Relacionados

- [Contrato](../07-contracts/example.md)
