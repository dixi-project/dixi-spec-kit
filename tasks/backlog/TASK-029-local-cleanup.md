# TASK-029 — Local cleanup after v1.10.0 and v1.11.0 (v1.11.1)

## Purpose

The work of v1.10.0 and v1.11.0 left a worktree and a dozen local branches in the maintainer's clone. All of them are merged; leaving them makes it easy to resume work on a stale branch.

## Record

- Type: chore; priority P3; level 1. Created 2026-11-12. Product owner: Alfredo Castillejos.
- Nothing in this task changes the repository on GitHub: the remote branches of merged pull requests are already deleted.

## Story

As a maintainer
I want my clone to hold only `main` and the work in progress
so that I do not continue from a branch that is already merged.

## Acceptance criteria

1. Before deleting, each local branch is compared with `public/main`. Branches signed off with `git rebase --signoff` have other commit hashes and look unmerged to Git: the comparison is of content, with `git diff`, not of ancestry.
2. The worktree `.claude/worktrees/task-016` is removed, and with it the link to the virtual environment it holds; the virtual environment of the main checkout is not touched.
3. The merged local branches are deleted: `docs/command-reference`, `docs/command-guide`, `docs/command-examples`, `docs/cli-reference`, `docs/spanish-site`, `docs/python-badge`, `feat/status-resume`, `feat/mode-read-only`, `chore/changelog-guard`, `release/v1.10.0`, `release/v1.11.0` and `worktree-task-016`.
4. Deleting is confirmed by the maintainer; nothing is removed that is not in `public/main`.

## Done when

1. `git worktree list` shows only the main checkout and `git branch` no merged work branch.
2. `git status` on `main` is clean and equal to `public/main`.

## Related

- [Tasks](../TASKS.md)
