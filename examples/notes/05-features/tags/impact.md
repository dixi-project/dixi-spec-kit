# Impacto — normalizar etiquetas (FEATURE-002)

## Propósito

Informe de `/dixi.analyze` sobre el cambio «normalizar etiquetas y filtrar por etiqueta», antes de especificarlo.

## Artefactos afectados

| Artefacto | Impacto | Acción |
|---|---|---|
| CONTRACT-001 | `add` valida etiquetas y `list` admite `tag`: cambio compatible en la API y más restrictivo en la entrada | Contrato v2 con sección de etiquetas |
| Datos existentes | Etiquetas guardadas con mayúsculas o duplicadas | Normalizar al leer (criterio 4), sin migración destructiva |
| `tests/test_notes.py` | Prueba congelada de FEATURE-001; no se modifica | Pruebas nuevas en `tests/test_tags.py` |
| CLI | `list --tag` nuevo; `add --tag` valida | Mensaje `invalid_tag` en es/en |
| TEST-001 | Añadir fila de FEATURE-002 | Actualizar plan |

## Compatibilidad

Una etiqueta inválida que antes se aceptaba ahora se rechaza al añadir. Las ya guardadas siguen legibles. No hace falta ADR: no cambia la persistencia ni la arquitectura.

## Relacionados

- [Funcionalidad](feature-spec.md)
- [Contrato](../../07-contracts/example.md)
