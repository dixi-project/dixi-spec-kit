# Impact — normalize tags (FEATURE-002)

## Purpose

`/dixi.analyze` report on the change "normalize tags and filter by tag", before specifying it.

## Affected artifacts

| Artifact | Impact | Action |
|---|---|---|
| CONTRACT-001 | `add` validates tags and `list` accepts `tag`: compatible change in the API and stricter on input | Contract v2 with a tags section |
| Existing data | Tags saved with uppercase or duplicates | Normalize on read (criterion 4), without destructive migration |
| `tests/test_notes.py` | Frozen test of FEATURE-001; not modified | New tests in `tests/test_tags.py` |
| CLI | New `list --tag`; `add --tag` validates | `invalid_tag` message in es/en |
| TEST-001 | Add FEATURE-002 row | Update plan |

## Compatibility

An invalid tag that was previously accepted is now rejected when adding. Those already saved remain readable. No ADR is needed: it changes neither persistence nor architecture.

## Related

- [Feature](feature-spec.md)
- [Contract](../../07-contracts/example.md)
