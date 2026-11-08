# CONTRACT-001 — API y CLI de notas

## Propósito

Contrato de `notes` producido con `/dixi.plan`; actualizado por FEATURE-002 (ver [impacto](../05-features/tags/impact.md)).

## API

- `NoteStore(path)`: almacén en `path`; no crea el archivo hasta el primer `add`.
- `add(text, tags=()) -> Note`: valida y guarda. Lanza `NoteError` si el texto o una etiqueta son inválidos.
- `list(tag=None) -> list[Note]`: orden de creación; con `tag`, solo las notas que la contienen (FEATURE-002).
- `search(term) -> list[Note]`: coincidencia de subcadena sin distinguir mayúsculas.
- `Note(id: int, text: str, tags: tuple[str, ...])`.

## Etiquetas (v2 del contrato, FEATURE-002)

Se recortan, pasan a minúsculas y se eliminan duplicados conservando el primer orden. Válidas: 1 a 32 caracteres de `a-z`, `0-9`, `-` o `_`. Los datos guardados con la v1 se normalizan al leer.

## CLI

```text
python3 -m notes [--file notes.json] [--lang es|en] add <texto> [--tag <t>]...
python3 -m notes [--file notes.json] [--lang es|en] list [--tag <t>]
python3 -m notes [--file notes.json] [--lang es|en] search <término>
```

Salida: una línea por nota `#<id> <texto> [etiquetas]`. Códigos: 0 completado, 2 entrada inválida.

## Persistencia

JSON `{"schema_version": 1, "notes": [...]}` escrito en un archivo temporal y reemplazado atómicamente.

## Relacionados

- [Funcionalidad: capturar y buscar](../05-features/example/feature-spec.md)
- [Funcionalidad: etiquetas](../05-features/tags/feature-spec.md)
- [Plan de pruebas](../11-quality/test-plan.md)
- [ADR-001](../09-architecture/adr/ADR-001-almacen-json-local.md)
