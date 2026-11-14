# Automatic controls

## Purpose

Explain what `--controls` installs, what each control blocks and what none of them covers. Without controls, the rules of DIXI are instructions that the agent is asked to follow. With them, five small scripts run inside the agent and stop it before it breaks one of those rules.

## Turning them on

Controls are optional and exist for the two agents that can run hooks:

```sh
dixi init my-project --agent claude --controls
dixi init my-project --agent codex --controls
```

For a project that already exists, `dixi upgrade --dry-run --controls` shows what would be added and `dixi upgrade --apply --controls` adds it. They are not available with `--agent skills` or `--agent none`: those agents have no hooks that DIXI can install, and `dixi init` refuses the combination instead of installing something that would not run.

What gets installed:

- The five scripts, in `.dixi/hooks/`. Each is standard-library Python, reads the agent's event, and answers allow or block with the reason.
- For Claude Code, `.claude/settings.json` with only a `hooks` section that calls them. No permissions, tools or servers are added.
- For Codex, `.codex/hooks.json`. Codex loads project hooks only when you trust the project, and runs each new or changed hook only after you approve it with its `/hooks` command.

## What each control blocks

| Control | What it blocks | When it runs |
|---|---|---|
| `protect_tests.py` | Changing, moving or deleting a test that is already committed, through the edit tools or a shell command. Tests that are not committed yet can be written: that is how tests come first. | Before every edit and every shell command |
| `guard_secrets.py` | Reading `.env*` files, private keys, `.aws/`, `.ssh/` and credential files, directly or through a shell command. Example files such as `.env.example` are allowed. | Before every read, search and shell command |
| `guard_attestation.py` | Signing off a commit, approving or merging a pull request, and ticking an attestation checkbox. The agent may commit without a sign-off; the person signs. | Before every shell command |
| `mode_gate.py` | With `MODE` set to `prod`: recursive deletes outside temporary folders, forced pushes, hard resets of a shared branch, infrastructure apply and destroy, cluster deletes and SQL `DROP` or `TRUNCATE`. With `mvp` it allows them. | Before every shell command |
| `verify_on_stop.py` | Ending the turn when files changed and `make verify` fails. After one forced continuation it lets the agent stop and tells you, so the agent is never trapped in a loop. | When the agent, or a subagent, is about to stop |

Two of them have a setting, read from the environment in which you start the agent:

- `DIXI_ALLOW_TEST_EDITS=1` lets the agent edit committed tests for that session. Use it when you have decided that a test is wrong; the decision is yours, not the agent's.
- `DIXI_VERIFY_TIMEOUT` is the number of seconds `verify_on_stop.py` waits for `make verify`; the default is 240.

## How to see that they are active

1. `dixi doctor` reports whether the project was created with controls.
2. The files are there: `.dixi/hooks/` with the five scripts, and `.claude/settings.json` or `.codex/hooks.json`.
3. Ask the agent for something a control blocks, for example to change a committed test. It is stopped with a message that starts with the name of the control, such as `DIXI protect_tests`, and the file does not change.

In Codex, also check that the project is trusted and that the hooks are approved; until then they do not run.

## What the controls do not cover

A control is a second layer, never the last one.

- A hook can be evaded. `protect_tests.py` does not see a file written by a script that is run from a file, or reached through a path built at run time or held in a shell variable. The written rule in `AGENTS.md` still applies in those cases.
- They check commands, not intentions: they do not judge whether a change is correct, complete or safe.
- They act only inside the agent. A person, another tool or a continuous integration job is not affected.
- They do not replace your review or the protection of the main branch. The effective protection is still that a person reads the change and that the repository requires it.
- `mode_gate.py` reads `MODE`; it never changes it. `dixi mode` shows what is missing before a person changes it.

## Related

- [Documentation index](documentation.md)
- [Subagents](subagents.md)
- [Support matrix](support-matrix.md)
- [CLI reference](cli/index.md)
- [Controls contract](../07-contracts/commands/automated-controls-contract.md)
