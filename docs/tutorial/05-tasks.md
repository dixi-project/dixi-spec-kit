# 5. Split it into tasks

## Purpose

Split the plan into small tasks, ordered by their dependencies, each linked to the acceptance criteria it covers.

## What you do

Run [`/dixi.tasks`](../commands/tasks.md) with the ID of your feature:

```text
/dixi.tasks FEATURE-002
```

With Codex, `$dixi-tasks FEATURE-002`; with an Agent Skills agent, `@dixi-tasks FEATURE-002`.

## What you should see

A file `05-features/<slug>/tasks.md` with a list like this one:

| ID | Task | Covers | Level |
|---|---|---|---|
| `T-001` | Save a note with trimmed text and its tags | Criteria 1–2 | 1 |
| `T-002` | List notes in creation order | Criterion 3 | 1 |

Each task has an ID, the criteria it covers, its dependencies and a risk level from 0 (a fix) to 3 (structural). A level 3 task needs your validation before it is built, and the agent flags any ADR that is still "Proposed" as a blocker.

If the requirements still have open questions, [`/dixi.checklist`](../commands/checklist.md) writes them as items you tick; the build stops while any item is open.

## Next

[6. Build one task](06-build.md).

## Related

- [Tutorial](index.md)
- [Command reference](../commands/index.md)
