# TASK-010 — Opt-in automated controls, subagents and new operations (v1.6.0)

## Purpose

Deliver block F: opt-in agent hooks that enforce frozen tests, no secrets, no signing or approval, production-mode safety and verification before stopping; Claude Code subagents; the `interview` and `risk-review` operations; and the `placeholders` and `pr-size` CLI helpers.

## Record

- Type: feature; priority P1; level 3 (code that runs on every agent tool call; changes the adapter contract). Created 2026-11-08. Product owner: Alfredo Castillejos.
- Contract and [ADR-105](../../09-architecture/adr/ADR-105-opt-in-automated-controls.md) validated on 2026-11-08 ("Approve the three" deviations: `14-delivery`, no `mode` operation, opt-in controls). Independent of TASK-008 and TASK-009 except for the `interview` operation, which follows the project's profile.

## Story

As a person who works with an AI agent
I want the kit's rules enforced by the agent's hooks when I ask for it
so that a forgotten instruction does not end in an edited test, a leaked secret or a commit signed in my name.

## Acceptance criteria

1. Without `--controls`, every adapter installs exactly what v1.5 installs.
2. `dixi init --agent claude --controls` installs the five scripts in `.dixi/hooks/` and `.claude/settings.json` with hooks only; `--agent none --controls` exits 2 without writing.
3. Each control blocks and allows exactly the cases in the [contract](../../07-contracts/commands/automated-controls-contract.md), verified with recorded hook inputs, including malformed input and wrapped commands.
4. Codex hook support is verified and recorded with version and date before wiring; if unsupported, `--agent codex --controls` exits 2.
5. Four Claude Code subagents and the `interview` and `risk-review` operations are installed in both languages (operations for both adapters), optional in the inventory.
6. `dixi placeholders` and `dixi pr-size` behave as specified, read-only, with human and JSON output.
7. The support matrix distinguishes instruction-only rules from rules enforced with `--controls`, and states that hooks are a second layer, not the last one.

## Done when

1. Contract and tests were committed red before the implementation.
2. `make verify` passes and CI is green.
3. A person ran Claude Code with `--controls` and recorded at least one blocked edit of a committed test and one blocked `--signoff`.

## Related

- [Contract](../../07-contracts/commands/automated-controls-contract.md)
- [ADR-105](../../09-architecture/adr/ADR-105-opt-in-automated-controls.md)
