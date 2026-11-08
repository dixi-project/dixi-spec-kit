# FEATURE-002 — Normalized tags and filtering by tag

## Purpose

Evolution of the example: it changes the tags contract of FEATURE-001. Before specifying it, `/dixi.analyze` was run ([impact](impact.md)).

## Story

As a terminal user
I want to tag notes without worrying about capitalization or duplicates and filter them by tag
so that I can group related ideas.

## Acceptance criteria

1. Tags are trimmed, lowercased and deduplicated, keeping the first-occurrence order.
2. A tag that is empty, longer than 32 characters or with characters outside `a-z 0-9 - _` is rejected without modifying the store.
3. `list --tag X` returns only the notes with the normalized tag of X.
4. Notes saved with tags in the previous format are normalized on read, without rewriting the file.

## Related

- [Module](../../04-modules/example/module-spec.md)
- [Contract](../../07-contracts/example.md)
- [Impact](impact.md)
- [Tasks](tasks.md)
