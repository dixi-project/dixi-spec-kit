# Prepared review — FEATURE-002

## Purpose

`/dixi.review` report for the reviewer of the tags change. It approves nothing.

## Risk

Low: it changes input validation and reading of local data; it does not touch persistence, network or permissions.

## Criterion → change → test

| Criterion | Change | Test |
|---|---|---|
| 1 Normalize | `normalize_tags` in `notes/store.py` | `test_tags_are_normalized` |
| 2 Reject invalid | `TAG` and `NoteError("invalid_tag")` | `test_invalid_tags_rejected_without_writing` |
| 3 Filter | `NoteStore.list(tag)` and `list --tag` | `test_filter_by_tag`, `test_cli_filter_and_invalid_tag` |
| 4 Old data | `normalize_tags(..., strict=False)` on read | `test_legacy_tags_normalized_on_read` |

## Findings

- None blocking. `tests/test_notes.py` (frozen) did not change.
- Observation: an invalid old tag is discarded on read instead of failing; consistent with criterion 4, it is worth confirming with the person.

## For the reviewer

- [ ] The criteria of FEATURE-002 reflect what was requested.
- [ ] `make verify` green in your environment.
- [ ] The observation about invalid old tags is acceptable.

## Related

- [Feature](../05-features/tags/feature-spec.md)
- [Impact](../05-features/tags/impact.md)
