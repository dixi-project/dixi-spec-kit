# Contract — automated controls, subagents and new operations (block F)

## Purpose

Specify the opt-in controls of [ADR-105](../../09-architecture/adr/ADR-105-opt-in-automated-controls.md), the Claude Code subagents, two new agent operations and two read-only CLI helpers. Implements [TASK-010](../../tasks/backlog/TASK-010-automated-controls.md).

## CLI

```text
dixi [--lang es|en] [--json] init <directory> [--agent none|claude|codex] [--profile …] [--regulated] [--controls]
dixi [--lang es|en] [--json] placeholders [--strict]
dixi [--lang es|en] [--json] pr-size [--base <ref>] [--max <lines>]
```

- `--controls` with `--agent none` exits 2 without writing. With `--agent codex` it exits 2 unless Codex project hooks were verified (see below).
- `.dixi/project.json` records `"controls": true|false`; absent means false.

## Controls

Each control is a standalone Python 3.11+ script using only the standard library, installed in `.dixi/hooks/`. It reads the hook event as JSON on standard input, writes its reason on standard error and exits 0 (allow) or 2 (block).

| Control | Event (Claude Code) | Blocks |
|---|---|---|
| `protect_tests.py` | `PreToolUse` on `Edit`, `Write`, `MultiEdit`, `NotebookEdit` | Changes to a test file that exists in `HEAD`. Tests not yet committed can be written (tests first). Allowed when the person launched the agent with `DIXI_ALLOW_TEST_EDITS=1`. |
| `guard_secrets.py` | `PreToolUse` on `Bash`, `Read`, `Grep` | Reading `.env*` (except `.env.example`, `.env.sample`, `.env.template`), keys (`*.pem`, `*.key`, `id_rsa`, `id_ed25519`), `.aws/`, `.ssh/` and credential files, also through shell commands such as `cat`, `grep`, `head`, `source`. |
| `guard_attestation.py` | `PreToolUse` on `Bash` | Adding `Signed-off-by` (`commit -s`, `--signoff`, `--trailer`, a trailer in `-m` or `-F`, `rebase`/`am`/`cherry-pick`/`revert` with `--signoff`); `gh pr review --approve`; `gh pr merge`; ticking an attestation checkbox through `gh pr create/edit` or `gh api`. Also when wrapped in `env`, `bash -c`, `sh -c`, `eval` or a pipeline. |
| `mode_gate.py` | `PreToolUse` on `Bash` | With `MODE` = `prod`: `rm -rf` outside the project's temporary folders, `git push --force`, `git reset --hard` on a shared branch, infrastructure apply/destroy commands (`terraform`, `tofu`, `pulumi`, `cdk`), `kubectl delete`/`apply` against a cluster, and SQL `DROP`/`TRUNCATE` through database clients. With `mvp`, it allows them. |
| `verify_on_stop.py` | `Stop`, `SubagentStop` | Ending the turn when the working tree changed and `make verify` fails. After one forced continuation (`stop_hook_active`), it allows the stop and tells the person. No `verify` target, or no changes: allow. Timeout `DIXI_VERIFY_TIMEOUT` (default 240 s). |

Common rules:

1. `protect_tests`, `guard_secrets`, `guard_attestation` and `mode_gate` block when the input is not valid JSON or lacks the expected fields. `verify_on_stop` allows in that case, so that a broken hook never traps the agent.
2. No control writes files, uses the network or reads secrets to decide.
3. What counts as a test file: paths under `tests/`, `test/`, `__tests__/`, `spec/`, or names matching `test_*`, `*_test.*`, `*.test.*`, `*.spec.*`, `*.feature`.

### Claude Code wiring

`.claude/settings.json` contains only a `hooks` object that runs each script with `python3 "$CLAUDE_PROJECT_DIR/.dixi/hooks/<script>"`. No permissions, `allowed-tools`, environment variables or MCP servers.

### Codex wiring

TASK-010 starts by verifying, with the Codex CLI available at that time, whether project-level hooks exist and which events they expose. The result is recorded in this contract with the version and date. If hooks exist, the same scripts are wired through Codex's project configuration, covering the events Codex offers; the support matrix lists any control Codex cannot run. If they do not exist, `--agent codex --controls` exits 2 and the skills keep the rules as instructions.

## Claude Code subagents

With `--agent claude`, four subagents are installed in `.claude/agents/`: `dixi-architect`, `dixi-tester`, `dixi-developer` and `dixi-reviewer`, in English and Spanish. Each has a narrow role (design and ADRs; red tests; code to green without touching committed tests; review report without approving) and the common limits of the adapter. They are optional in the inventory, like the operations added after v1.0. Codex has no project subagent format verified; nothing is installed for it.

## New operations

| Operation | Writes | Never does |
|---|---|---|
| `interview` | Fills `{{pending: …}}` slots in the project's documents through a guided conversation, one question at a time, area by area following the project's profile | Answer for the person, or edit rules and policies marked as norms |
| `risk-review` | A risk review report for a person: risk level (low, medium, high), the diff explained against the spec, edge cases, assumptions not in the spec, what could break elsewhere, and where to look first | Approve, merge or lower the risk the author declared |

Both are installed for Claude Code (`/dixi.interview`, `/dixi.risk-review`) and Codex (`$dixi-interview`, `$dixi-risk-review`), are optional in the inventory and bring the available total to 27.

Changing `MODE` stays a manual action of the person: `status` shows the mode and `promote` prepares the evidence. There is no `mode` operation.

## CLI helpers

### `dixi placeholders`

Read-only. Lists the `{{pending: …}}` markers in the project's managed Markdown files, grouped by file, ignoring fenced code blocks and inline code. Exit 0; with `--strict`, exit 1 if any marker remains. JSON output: `{"placeholders": {"<file>": <count>}, "total": <n>}`.

### `dixi pr-size`

Read-only. Runs `git diff --numstat <base>...HEAD` (default base `main`) inside the project and reports added plus deleted lines. Documentation (`*.md`, `docs/`), lockfiles, minified or generated files and tests are not counted; tests are reported separately. Exit 1 when the count exceeds `--max` (default 1 500), 2 when Git is missing or the base does not exist. It is the only subcommand that runs an external program; it never fetches, writes or changes the repository.

## Work-in-progress limit

The project's `AGENTS.md` template gains a `wip_limit` line (default 3). `/dixi.build` and `$dixi-build` read it and, when `gh` is available and authenticated, stop before starting new work if the person already has that many open pull requests. This is an instruction, not a control.

## Upgrade and compatibility

Projects without `controls` keep their current inventory. `dixi upgrade --dry-run --controls` lists the control files as `new`. Subagents and the two operations appear as `new` for existing Claude Code and Codex projects.

## Related

- [ADR-105](../../09-architecture/adr/ADR-105-opt-in-automated-controls.md)
- [TASK-010](../../tasks/backlog/TASK-010-automated-controls.md)
- [Claude Code adapter contract](claude-code-adapter-contract.md)
- [Codex adapter contract](codex-adapter-contract.md)
