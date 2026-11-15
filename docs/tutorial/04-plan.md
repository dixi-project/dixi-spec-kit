# 4. Plan it

## Purpose

Decide how the feature will be built before writing code: the contract, the test plan and the structural decisions that a person must validate.

## What you do

Run [`/dixi.plan`](../commands/plan.md) with the ID of your feature:

```text
/dixi.plan FEATURE-002
```

With Codex, `$dixi-plan FEATURE-002`; with an Agent Skills agent, `@dixi-plan FEATURE-002`. Use the ID that the previous step reported if it is not `FEATURE-002`.

If the project does not record a technology stack yet, the agent asks you to choose one instead of guessing. For this example, a small Python package with the standard library is enough.

## What you should see

- A contract in `07-contracts/` and a test plan in `11-quality/`, both registered in `.dixi/traceability.json` under your feature.
- One ADR in `09-architecture/adr/` for each structural decision, for example where the notes are stored, with status "Proposed".

A proposed ADR blocks the work until you validate it: read it, and change its status to "Accepted" if you agree, or ask the agent to change the approach. This is the cheapest moment to change your mind.

## Next

[5. Split it into tasks](05-tasks.md).

## Related

- [Tutorial](index.md)
- [Command reference](../commands/index.md)
