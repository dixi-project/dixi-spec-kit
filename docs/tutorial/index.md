# Start here: your first feature

## Purpose

Take one small feature from an empty folder to a verified build, one step per page, so that you learn the order of DIXI's steps by doing them. Each step says what you do, what you should see and what comes next, and links to the reference of every command it uses.

## What you will build

A command-line tool that keeps short notes with tags, the same example as the [command guide](../command-catalog.md). The repository has a finished version of it in [`examples/notes`](../../examples/notes): open it whenever you want to compare your result.

## Before you start

- Python 3.11 or later, on macOS or Linux. On Windows, use WSL 2 with the project under `~` ([support matrix](../support-matrix.md)).
- One of the agents DIXI supports, or none: the commands below are shown for Claude Code, and each step says how to run them with the other adapters.
- Git, to commit your work. The agent never signs, pushes or merges for you.

| Adapter | Agent | How you run an operation |
|---|---|---|
| `--agent claude` | Claude Code | `/dixi.specify add a note with tags` |
| `--agent codex` | Codex CLI | `$dixi-specify add a note with tags` |
| `--agent skills` | OpenCode, and other agents that read Agent Skills (not verified) | `@dixi-specify add a note with tags` |
| `--agent none` | Any agent or editor | `dixi workflow prepare` prints the procedure, and you give it to your agent |

## Steps

1. [Install the kit](01-install.md): install `dixi` and check its version.
2. [Create the project](02-init.md): the documentary baseline and the agent's commands.
3. [Specify the feature](03-specify.md): a story and numbered acceptance criteria with an ID.
4. [Plan it](04-plan.md): the contract, the test plan and the decisions to validate.
5. [Split it into tasks](05-tasks.md): small tasks linked to the criteria they cover.
6. [Build one task](06-build.md): failing tests first, then the code, then `make verify`.
7. [Verify the feature](07-verify.md): every criterion mapped to the test that covers it.

It takes about an hour with an agent. You can stop after any step and resume later: `/dixi.status` says where you left off.

## Related

- [Documentation index](../documentation.md)
- [Command guide](../command-catalog.md)
- [Command reference](../commands/index.md)
- [CLI reference](../cli/index.md)
