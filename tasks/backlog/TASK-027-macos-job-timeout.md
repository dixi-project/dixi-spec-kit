# TASK-027 — macOS verification jobs survive a slow runner queue (v1.11.1)

## Purpose

On 2026-11-12 the job `make verify (macos-latest, Python 3.13)` was cancelled twice, in a pull request and on `main`, without running a single step: it waited for a macOS runner until its `timeout-minutes: 15` ran out. A required check then shows as failed, the pull request cannot be merged and a person has to re-run the job by hand.

## Record

- Type: ci; priority P3; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Evidence: runs of the `verify` workflow for pull request #53 and for the merge of #53 on `main`; the same job passed in about two minutes when re-run. The Linux and WSL 2 jobs were not affected.

## Story

As a maintainer
I want a slow runner queue not to fail a required check
so that a green change is not blocked by infrastructure.

## Acceptance criteria

1. The timeout of the `make verify` matrix job in `.github/workflows/verify.yml` leaves room for the queue seen on macOS, without removing the limit: a hung job must still be cancelled.
2. The change keeps the workflow rules already tested: pinned actions, least privilege and no secrets.
3. A test fixes the new limit and that every job of the workflow still has one.
4. `docs/repository-settings.md` or the workflow itself says what to do when the job is cancelled while waiting: re-run the failed jobs.

## Done when

1. Tests were committed red before the change.
2. `make verify` passes and CI is green, including the macOS jobs.

## Correction

Added on 2026-11-13. The diagnosis in Purpose was wrong. The limit went from 15 to 30 minutes in pull request #64, and on the same day two macOS jobs of pull request #66 were cancelled again after fifteen minutes without a runner. GitHub's annotation names the cause: "The job was not acquired by Runner of type hosted even after multiple attempts", with a notice about capacity constraints of the macOS arm64 runners. `timeout-minutes` does not count while a job waits for a runner, so the workflow cannot prevent the cancellation.

What stays from this task: the documented response, re-running the failed jobs, and a limit that still cancels a job that hangs. The story is not met by the workflow change; if the cancellations become frequent, the option left is not to require the macOS checks in the ruleset, which the maintainers decide.

## Related

- [Tasks](../TASKS.md)
- [Repository settings](../../docs/repository-settings.md)
