# Feature — Claude Code adapter B3

## Purpose

Install the ten `/dixi.*` commands in a new project so that a person can walk through the method inside Claude Code, with traceability and human gates. Makes [TASK-003](../../tasks/backlog/TASK-003-adaptador-claude-code.md) concrete.

## Story and criteria

As a person who uses Claude Code I want to install the DIXI Spec Kit commands in my project to walk through discovery, specification, plan, tasks, build, verification and review without losing traceability or human control.

- CC-01: `init --agent claude` creates the B1 baseline, `CLAUDE.md` and exactly ten commands in `.claude/commands/`, with no hooks, settings, MCP or permissions; no network. The `init` help announces `claude`.
- CC-02: an occupied destination (including a pre-existing `.claude/`) is rejected without changes.
- CC-03: each command has frontmatter with `description` and `argument-hint`, uses `$ARGUMENTS`, declares the common limits (frozen tests; do not sign, approve or integrate) and only invokes existing `dixi` operations and procedures. It does not contain `git push`, `--no-verify` or absolute paths.
- CC-04: `doctor` reports the integration and the number of commands; `check` fails if an installed command is missing or if the metadata declares an unknown agent or an incomplete inventory.
- CC-05: the adapter resources ship in wheel/sdist and have es/en parity.
- CC-06: the public example `examples/notes` passes `dixi check` and its `make verify` runs real application tests.

## Verification

`tests/test_claude_adapter.py` covers CC-01 to CC-06 deterministically. The walkthrough of the example inside Claude Code is recorded in [the B3 evidence](../../docs/b3-verification.md); it does not require literal equality of the generated text.

## Related

- [Parent module](../../04-modules/command-workflow/module-spec.md)
- [B3 contract](../../07-contracts/commands/claude-code-adapter-contract.md)
- [Scenarios](scenarios.feature)
- [Acceptance](acceptance.yaml)
- [Threats](../../13-security/claude-code-adapter-threat-model.md)
