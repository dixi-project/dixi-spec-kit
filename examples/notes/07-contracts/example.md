# CONTRACT-001 — Notes API and CLI

## Purpose

Contract of `notes` produced with `/dixi.plan`; updated by FEATURE-002 (see [impact](../05-features/tags/impact.md)).

## API

- `NoteStore(path)`: store at `path`; does not create the file until the first `add`.
- `add(text, tags=()) -> Note`: validates and saves. Raises `NoteError` if the text or a tag is invalid.
- `list(tag=None) -> list[Note]`: creation order; with `tag`, only the notes that contain it (FEATURE-002).
- `search(term) -> list[Note]`: case-insensitive substring match.
- `Note(id: int, text: str, tags: tuple[str, ...])`.

## Tags (contract v2, FEATURE-002)

They are trimmed, lowercased and duplicates are removed, keeping the first-occurrence order. Valid: 1 to 32 characters from `a-z`, `0-9`, `-` or `_`. Data saved with v1 is normalized on read.

## CLI

```text
python3 -m notes [--file notes.json] [--lang es|en] add <text> [--tag <t>]...
python3 -m notes [--file notes.json] [--lang es|en] list [--tag <t>]
python3 -m notes [--file notes.json] [--lang es|en] search <term>
```

Output: one line per note `#<id> <text> [tags]`. Codes: 0 completed, 2 invalid input.

## Persistence

JSON `{"schema_version": 1, "notes": [...]}` written to a temporary file and replaced atomically.

## Related

- [Feature: capture and search](../05-features/example/feature-spec.md)
- [Feature: tags](../05-features/tags/feature-spec.md)
- [Test plan](../11-quality/test-plan.md)
- [ADR-001](../09-architecture/adr/ADR-001-almacen-json-local.md)
