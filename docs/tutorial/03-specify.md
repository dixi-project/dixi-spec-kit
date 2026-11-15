# 3. Specify the feature

## Purpose

Turn the idea into a specification: a story, numbered acceptance criteria that can be checked from outside, and an ID that links the feature to its module.

## What you do

Open your agent in the `notes` folder and run [`/dixi.specify`](../commands/specify.md) with the feature in your own words:

```text
/dixi.specify add a note with tags
```

With Codex, write `$dixi-specify add a note with tags`; with an Agent Skills agent, `@dixi-specify add a note with tags`. With `--agent none`, [`dixi workflow`](../cli/workflow.md) prints the same procedure for any agent:

```bash
dixi workflow prepare specify --target MODULE-001 --request "Add a note with tags"
```

The agent asks which module the feature belongs to when it is not clear, and asks about anything the request leaves open. Answer in plain language. If doubts remain after the spec is written, [`/dixi.clarify`](../commands/clarify.md) asks about them one by one and records the answers.

## What you should see

- A new file `05-features/<slug>/feature-spec.md` with the story (As / I want / So that), numbered acceptance criteria such as "a note without text is rejected", and the assumptions marked as such.
- The feature registered in `.dixi/traceability.json` with a new ID, usually `FEATURE-002` (the kit's example is `FEATURE-001`), and `MODULE-001` as its parent.

Read the criteria now: each one becomes at least one test later. Change them while it is cheap. Compare with [`examples/notes`](../../examples/notes), whose criteria are in `05-features/`.

## Next

[4. Plan it](04-plan.md).

## Related

- [Tutorial](index.md)
- [Command reference](../commands/index.md)
