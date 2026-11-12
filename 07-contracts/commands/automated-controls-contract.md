# Contract — automated controls, subagents and new operations (block F)

## Purpose

Specify the opt-in controls of [ADR-105](../../09-architecture/adr/ADR-105-opt-in-automated-controls.md), the Claude Code subagents, two new agent operations and two read-only CLI helpers. Implements [TASK-010](../../tasks/backlog/TASK-010-automated-controls.md).

## CLI

```text
dixi [--lang es|en] [--json] init <directory> [--agent none|claude|codex] [--profile …] [--regulated] [--controls]
dixi [--lang es|en] [--json] placeholders [--strict]
dixi [--lang es|en] [--json] pr-size [--base <ref>] [--max <lines>]
```

- `--controls` with `--agent none` exits 2 without writing. `--agent claude` and `--agent codex` are supported (see wiring below).
- `.dixi/project.json` records `"controls": true|false`; absent means false.

## Controls

Each control is a standalone Python 3.11+ script using only the standard library, installed in `.dixi/hooks/`. It reads the hook event as JSON on standard input, writes its reason on standard error and exits 0 (allow) or 2 (block).

| Control | Event (Claude Code) | Blocks |
|---|---|---|
| `protect_tests.py` | `PreToolUse` on `Edit`, `Write`, `MultiEdit`, `NotebookEdit` and `Bash` | Changes to a test file that exists in `HEAD`, through the edit tools or a shell command that writes, moves or deletes it: output redirections, `sed`/`perl -i`, `tee`, `cp`, `mv`, `install`, `ln`, `rsync`, `rm`, `unlink`, `shred`, `truncate`, `dd of=`, `git rm`/`git mv`, also inside `env`, `sudo`, `bash -c`, `eval`, command chains and after `cd`; a folder counts when it contains committed tests. Tests not yet committed can be written (tests first). Allowed when the person launched the agent with `DIXI_ALLOW_TEST_EDITS=1`. |
| `guard_secrets.py` | `PreToolUse` on `Bash`, `Read`, `Grep` | Reading `.env*` (except `.env.example`, `.env.sample`, `.env.template`), keys (`*.pem`, `*.key`, `id_rsa`, `id_ed25519`), `.aws/`, `.ssh/` and credential files, also through shell commands such as `cat`, `grep`, `head`, `source`. |
| `guard_attestation.py` | `PreToolUse` on `Bash` | Adding `Signed-off-by` (`commit -s`, `--signoff`, `--trailer`, a trailer in `-m` or `-F`, `rebase`/`am`/`cherry-pick`/`revert` with `--signoff`); `gh pr review --approve`; `gh pr merge`; ticking an attestation checkbox through `gh pr create/edit` or `gh api`. Also when wrapped in `env`, `bash -c`, `sh -c`, `eval` or a pipeline. |
| `mode_gate.py` | `PreToolUse` on `Bash` | With `MODE` = `prod`: `rm -rf` outside the project's temporary folders, `git push --force`, `git reset --hard` on a shared branch, infrastructure apply/destroy commands (`terraform`, `tofu`, `pulumi`, `cdk`), `kubectl delete`/`apply` against a cluster, and SQL `DROP`/`TRUNCATE` through database clients. With `mvp`, it allows them. |
| `verify_on_stop.py` | `Stop`, `SubagentStop` | Ending the turn when the working tree changed and `make verify` fails. After one forced continuation (`stop_hook_active`), it allows the stop and tells the person. No `verify` target, or no changes: allow. Timeout `DIXI_VERIFY_TIMEOUT` (default 240 s). |

Common rules:

1. `protect_tests`, `guard_secrets`, `guard_attestation` and `mode_gate` block when the input is not valid JSON or lacks the expected fields. `verify_on_stop` allows in that case, so that a broken hook never traps the agent.
2. No control writes files, uses the network or reads secrets to decide.
3. What counts as a test file: paths under `tests/`, `test/`, `__tests__/`, `spec/`, or names matching `test_*`, `*_test.*`, `*.test.*`, `*.spec.*`, `*.feature`.

Inline interpreter code (`python -c`, a heredoc fed to `python3 -`, `node -e`, `ruby -e`, `perl -e`, `php -r`, also `deno` and `bun`) is blocked when it contains a write, move or delete operation and names a committed test (or a folder that contains one) in quotes.

Known limit: `protect_tests` does not see files written by a script run from a file, or through paths built at run time or held in shell variables. The instruction in `AGENTS.md` still applies. Hooks are a second layer, never the last one.

### Claude Code wiring

`.claude/settings.json` contains only a `hooks` object that runs each script with `python3 "$CLAUDE_PROJECT_DIR/.dixi/hooks/<script>"`. No permissions, `allowed-tools`, environment variables or MCP servers.

Manual run on 2026-11-09 with Claude Code 2.1.319, in a project created with `dixi init demo-controls --agent claude --controls` (kit from this branch) with a committed `tests/test_ok.py`:

- Asked to change the test with the `Edit` tool, the agent was stopped by `PreToolUse:Edit hook error: [python3 "$CLAUDE_PROJECT_DIR/.dixi/hooks/protect_tests.py"]: DIXI protect_tests: tests/test_ok.py is a committed test. …`; the file did not change.
- Asked to run `git commit --allow-empty -s -m prueba-firma`, the agent was stopped by `PreToolUse:Bash hook error: [python3 "$CLAUDE_PROJECT_DIR/.dixi/hooks/guard_attestation.py"]: DIXI guard_attestation: git commit with a sign-off is reserved to a person. …`; no commit was created.
- `verify_on_stop` ran at the end of every turn without blocking (clean tree, or `make verify` green).

### Codex wiring

Verified on 2026-11-08 with Codex CLI 0.167.0 (feature `hooks`: stable, enabled), against the official hooks documentation and the `rust-v0.167.0` source:

- Project hooks live in `.codex/hooks.json` (events → groups with a regular-expression `matcher` → `command` handlers). Codex loads them only when the project is trusted and runs each new or changed hook only after the person approves it with `/hooks`.
- Events used: `PreToolUse` (tools `Bash`, with the command in `tool_input.command`, and `apply_patch`, with the patch text in `tool_input.command`), `Stop` and `SubagentStop` (with `stop_hook_active`). A hook blocks by exiting 2 with the reason on standard error.
- There is no project-directory variable: commands locate the scripts with `git rev-parse --show-toplevel`, falling back to the current directory.

`--agent codex --controls` therefore installs `.codex/hooks.json` with hooks only: `mode_gate`, `guard_secrets`, `guard_attestation` and `protect_tests` on `Bash`; `protect_tests` also on `apply_patch`, which reads the paths from the patch headers (`*** Add File:`, `*** Update File:`, `*** Delete File:`, `*** Move to:`); `verify_on_stop` on `Stop` and `SubagentStop`. Codex has no separate read tool, so `guard_secrets` covers reads through `Bash`. The README states that the person must trust the project and approve the hooks for them to run.

## Claude Code subagents

With `--agent claude`, four subagents are installed in `.claude/agents/`: `dixi-architect`, `dixi-tester`, `dixi-developer` and `dixi-reviewer`, in English and Spanish. Each has a narrow role (design and ADRs; red tests; code to green without touching committed tests; review report without approving) and the common limits of the adapter. They are optional in the inventory, like the operations added after v1.0. Codex has no project subagent format verified; nothing is installed for it.

## New operations

| Operation | Writes | Never does |
|---|---|---|
| `interview` | Fills `{{pending: …}}` slots in the project's documents through a guided conversation, one question at a time, area by area following the project's profile | Answer for the person, or edit rules and policies marked as norms |
| `risk-review` | A risk review report for a person: risk level (low, medium, high), the diff explained against the spec, edge cases, assumptions not in the spec, what could break elsewhere, and where to look first | Approve, merge or lower the risk the author declared |

Both are installed for Claude Code (`/dixi.interview`, `/dixi.risk-review`) and Codex (`$dixi-interview`, `$dixi-risk-review`), are optional in the inventory and bring the available total to 27.

Changing `MODE` stays a manual action of the person: `status` shows the mode and `promote` prepares the evidence. No operation and no terminal command changes it; `dixi mode` (below) only reads it.

## CLI helpers

### `dixi placeholders`

Read-only. Lists the `{{pending: …}}` markers in the project's managed Markdown files, grouped by file, ignoring fenced code blocks and inline code. Exit 0; with `--strict`, exit 1 if any marker remains. JSON output: `{"placeholders": {"<file>": <count>}, "total": <n>}`.

### `dixi pr-size`

Read-only. Runs `git diff --numstat <base>...HEAD` (default base `main`) inside the project and reports added plus deleted lines. Documentation (`*.md`, `docs/`), lockfiles, minified or generated files and tests are not counted; tests are reported separately. Exit 1 when the count exceeds `--max` (default 1 500), 2 when Git is missing or the base does not exist. It is the only subcommand that runs an external program; it never fetches, writes or changes the repository.

### `dixi mode`

Read-only. Prints the content of `MODE` (`mvp` or `prod`; any other value is invalid content, exit 1). For `mvp` it lists which of the six items `/dixi.promote` reviews have no evidence yet. Evidence is a non-empty document without `{{pending: …}}` blanks outside code, read without following symbolic links:

| Item | Evidence looked for |
|---|---|
| `tests` (tests and budgets) | `11-quality/strategy.md` |
| `threats` (threat model) | a `*threat-model*.md` file in `13-security/` |
| `data` (data retention) | a Markdown file in `08-data/`, other than `README.md` |
| `operations` (runbooks and SLOs) | a Markdown file in `15-operations/`, other than `README.md` |
| `release` (release and rollback process) | a Markdown file in `docs/releases/`, other than `README.md` |
| `owners` | a non-empty `CODEOWNERS` in the root, `.github/` or `docs/` |

It checks that the document exists and is filled in, not that its content is sufficient: the judgement stays with the person and with `/dixi.promote`. Exit 0 whether or not items are missing, 1 for an invalid or absent `MODE`, 2 outside a project or with any argument: there is no option to change `MODE`. JSON output: `{"mode": {"mode": "mvp", "evidence": [{"item": "<item>", "status": "present|missing", "expected": "<path>", "found": ["<file>"]}], "missing": <n>}}`; for `prod`, `evidence` is empty. It writes nothing.

## Work-in-progress limit

The project's `AGENTS.md` template gains a `wip_limit` line (default 3). `/dixi.build` and `$dixi-build` read it and, when `gh` is available and authenticated, stop before starting new work if the person already has that many open pull requests. This is an instruction, not a control.

## Upgrade and compatibility

Projects without `controls` keep their current inventory. `dixi upgrade --dry-run --controls` lists the control files as `new`. Subagents and the two operations appear as `new` for existing Claude Code and Codex projects.

## Related

- [ADR-105](../../09-architecture/adr/ADR-105-opt-in-automated-controls.md)
- [TASK-010](../../tasks/backlog/TASK-010-automated-controls.md)
- [Claude Code adapter contract](claude-code-adapter-contract.md)
- [Codex adapter contract](codex-adapter-contract.md)
