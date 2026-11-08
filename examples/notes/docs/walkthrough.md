# Example walkthrough

## Purpose

Record how this example was built with DIXI Spec Kit and Claude Code, step by step, so that you can repeat it. The responsible person is fictitious.

The example was produced by following each command's steps in a Claude Code 2.1.319 session. If you repeat it, the generated wording will vary; what must hold is the structure, the traceability and `make verify` green.

## Steps

| Step | Command | Result in this repository |
|---|---|---|
| 1 | `dixi init notes --agent claude` | Documentation base, `CLAUDE.md` and ten `/dixi.*` commands. |
| 2 | `/dixi.discover A library and CLI to store local notes with tags` | `00-master-spec.md` and `01-business/vision.md` (GOAL-001). |
| 3 | `/dixi.specify Capture, list and search notes` | Domain, module and FEATURE-001 with verifiable criteria. |
| 4 | `/dixi.plan FEATURE-001` | CONTRACT-001, test plan TEST-001 and ADR-001 (accepted by the person). |
| 5 | `/dixi.tasks FEATURE-001` | `05-features/example/tasks.md` (T-001 to T-003). |
| 6 | `/dixi.build T-001` … `T-003` | `tests/test_notes.py` red first; then `notes/` until green. |
| 7 | `/dixi.verify` | `make verify`: `dixi check` and 7 tests green. |
| 8 | `/dixi.analyze normalize tags and filter by tag` | [Impact report](../05-features/tags/impact.md): contract v2, old data and frozen test untouched. |
| 9 | `/dixi.specify` + `/dixi.tasks` | FEATURE-002 and T-004 to T-006. |
| 10 | `/dixi.build T-004` … `T-006` | `tests/test_tags.py` red (5 failures); then green without touching `tests/test_notes.py`. |
| 11 | `/dixi.verify` and `/dixi.review` | `make verify` with 12 tests green; [prepared review](review-feature-002.md) for a person. |

## Repeat it

```sh
cd examples/notes
make verify
python3 -m notes --file /tmp/my-notes.json add "Read about DDD" --tag Books
python3 -m notes --file /tmp/my-notes.json list --tag books
```

Requires `dixi` installed and Python 3.11 or later.

## Related

- [Project](../00-master-spec.md)
- [Test plan](../11-quality/test-plan.md)
