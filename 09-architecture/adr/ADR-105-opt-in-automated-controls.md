# ADR-105 — Opt-in automated controls for agents

## Purpose

Decide whether and how DIXI Spec Kit installs automatic controls (agent hooks) that enforce the rules its commands only state today: frozen tests, no secrets, no signing or attestation, safety in production mode and no "done" with verification in red.

## Status

Accepted on 2026-11-08 by the responsible person, including exit 2 for `--agent codex --controls` when Codex has no project hooks. Implementation in [TASK-010](../../tasks/backlog/TASK-010-automated-controls.md).

## Context

- The [Claude Code adapter contract](../../07-contracts/commands/claude-code-adapter-contract.md) installs no hooks, settings or permissions, and the support matrix says plainly that the rules are instructions, not controls.
- Dixi's private ecosystem enforces the same rules with five Claude Code hooks (`PreToolUse`, `Stop`, `SubagentStop`). They have caught real mistakes, but they are Bash scripts tied to its layout and policies.
- A hook runs code on the person's machine on every tool call. Installing one without consent would surprise users and could break their workflow.
- Codex hook support for project-level configuration has not been verified in Codex CLI 0.167.0.

## Decision

1. **Opt-in only.** `dixi init --controls` installs the controls; without the flag, adapters install exactly what they install today. `--controls` requires `--agent claude` or `--agent codex`.
2. **Standalone Python, standard library only.** Each control is a self-contained Python 3.11+ script in `.dixi/hooks/` that does not import `dixi`, needs no network and reads only the hook input and the project. Projects work even where `dixi` is not installed.
3. **Claude Code:** `.claude/settings.json` with a `hooks` section only (no permissions, no `allowed-tools`, no MCP).
4. **Codex:** implementation starts with a verification of hook support in the then-current Codex CLI. If project hooks are supported, the same scripts are wired through Codex's configuration. If not, `--agent codex --controls` exits 2 without writing and the support matrix states it; the instructions in the skills remain.
5. **Fail-safe semantics.** Controls that protect people (secrets, attestation, frozen tests, production mode) block when they cannot parse their input. The verification control never traps the agent in a loop: after one forced continuation it lets the agent stop and tells the person.
6. **Human escape hatches.** `DIXI_ALLOW_TEST_EDITS=1`, set by the person when launching the agent, allows editing committed tests. No variable allows signing or reading secrets.
7. **Two read-only CLI helpers.** `dixi placeholders` and `dixi pr-size` join the CLI. `pr-size` is the first subcommand that runs an external tool (`git diff --numstat`, read-only, no network); every other subcommand keeps the B1 rule of not running Git, Make or hooks.

## Alternatives considered

- **Install controls by default.** Rejected: a behavior change on every tool call for every user, and a surprise for people who did not ask for it.
- **Implement controls as `dixi hook <name>`.** Rejected: the project would depend on the installed `dixi` version on every collaborator's machine.
- **Git hooks instead of agent hooks.** Rejected as the main mechanism: Git cannot tell an agent's commit from a person's, so it cannot enforce "the agent does not sign". Branch protection and DCO stay the server-side layer.

## Consequences

- The support matrix gains a column: instruction only, or enforced when `--controls` is installed.
- A hook is evadable (for example, through a tool it does not inspect); it is a second layer, never the last one. Human review and branch protection remain the effective protection.
- Tests must exercise every control with real hook input samples, including malformed input.

## Related

- [ADR-104](ADR-104-project-profiles-and-content.md)
- [Automated controls contract](../../07-contracts/commands/automated-controls-contract.md)
- [Support matrix](../../docs/support-matrix.md)
