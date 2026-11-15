# 7. Verify the feature

## Purpose

Check that every acceptance criterion of the feature is covered by a passing test, and find the ones that are not.

## What you do

When all the tasks are built, run [`/dixi.verify`](../commands/verify.md) with the ID of your feature:

```text
/dixi.verify FEATURE-002
```

With Codex, `$dixi-verify FEATURE-002`; with an Agent Skills agent, `@dixi-verify FEATURE-002`.

You can run the same checks yourself in the terminal at any time:

```bash
make verify
dixi check
```

## What you should see

- The output of `make verify`, as it ran. The agent never reports as green anything it did not run.
- Every acceptance criterion with the tests that cover it, and a list of the criteria without a test, with skipped or failing tests.
- For each gap, a proposal to run [`/dixi.build`](../commands/build.md) again. Verification does not fix code.
- [`dixi check`](../cli/check.md) ending with exit code 0: the chain from the goal to the tests is complete.

When everything is green, [`/dixi.review`](../commands/review.md) groups the change by risk for the person who reviews the pull request. You open the pull request, and a person approves it.

## What comes after

You have taken one feature through the whole path. From here:

- Change behavior that already exists with [`/dixi.change`](../commands/change.md): it shows what the change touches before any spec or code is edited.
- Prepare a version with [`/dixi.release`](../commands/release.md): evidence, a changelog entry and a rollback plan. Tagging and publishing are yours.
- Find the right operation for any other moment in the [command guide](../command-catalog.md).

## Related

- [Tutorial](index.md)
- [Command reference](../commands/index.md)
- [Documentation index](../documentation.md)
