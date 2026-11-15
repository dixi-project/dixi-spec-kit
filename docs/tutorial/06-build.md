# 6. Build one task

## Purpose

Build one task with tests first: the tests are written and shown failing before any code, and once committed they are frozen.

## What you do

Run [`/dixi.build`](../commands/build.md) with the first task:

```text
/dixi.build T-001
```

With Codex, `$dixi-build T-001`; with an Agent Skills agent, `@dixi-build T-001`.

The agent works in this order:

1. It writes the tests for the task's criteria and runs them, to show that they fail for the expected reason. No failing test, no code.
2. It proposes committing those tests on their own. Review them and commit them: from then on they are frozen, and nobody edits them to make code pass.
3. It writes the minimal code to make them pass.
4. It runs `make verify` and shows the real result.

Then review the change and commit it yourself:

```bash
make verify
git add .
git commit -m "T-001 save a note with tags"
```

The agent does not sign, push or merge for you. Repeat this step for `T-002` and the rest of the tasks, one at a time.

## What you should see

- The tests in your project's test folder, first red and then green.
- `make verify` passing. In a new project it runs [`dixi check`](../cli/check.md); add your test command to the `Makefile` so that it runs your tests too.
- The task marked as done in `tasks.md` and the tests registered in `.dixi/traceability.json`.

If a frozen test looks wrong, the agent stops and explains instead of changing it. If you created the project with [`dixi init`](../cli/init.md) and `--controls`, Claude Code and Codex hooks enforce this rule ([automatic controls](../controls.md)).

## Next

[7. Verify the feature](07-verify.md).

## Related

- [Tutorial](index.md)
- [Command reference](../commands/index.md)
- [Subagents](../subagents.md)
