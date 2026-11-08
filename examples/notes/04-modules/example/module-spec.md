# MODULE-001 — `notes` package

## Purpose

Implement the notes domain as the Python package `notes` with an API (`NoteStore`) and a CLI (`python3 -m notes`).

## Responsibilities

- Validate text and tags before saving.
- Persist atomically (temporary write and replace).
- CLI messages in the catalogs `notes/locales/es.json` and `en.json`.

## Related

- [Domain](../../03-domains/example/domain-spec.md)
- [Feature: capture and search](../../05-features/example/feature-spec.md)
- [Feature: tags](../../05-features/tags/feature-spec.md)
