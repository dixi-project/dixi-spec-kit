# FEATURE-001 — Capture, list and search notes

## Purpose

First feature of the example, produced with `/dixi.specify`.

## Story

As a terminal user
I want to add notes and search them by text
so that I can retrieve ideas without leaving the console.

## Acceptance criteria

1. `add` saves a note with trimmed text and returns its ID; IDs increase from 1.
2. Empty text or text longer than 1,000 characters is rejected without modifying the store.
3. `list` returns the notes in creation order; a nonexistent store is equivalent to an empty one.
4. `search` returns the notes whose text contains the term, case-insensitively.
5. The CLI exits with code 0 on completion and 2 on invalid input.

## Business rules

1. Notes are not edited or deleted in this version.

## Related

- [Module](../../04-modules/example/module-spec.md)
- [Contract](../../07-contracts/example.md)
- [Tasks](tasks.md)
