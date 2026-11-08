# STRIDE threat model — Claude Code adapter B3

## Purpose

Identify the threats specific to installing agent commands before implementing them. Extends the [B1 model](local-core-threat-model.md); filesystem threats are inherited.

## Assets and trust boundaries

Assets: user files, Claude Code configuration, frozen tests, Git history and local secrets. The text the person writes (`$ARGUMENTS`) and the project documents are untrusted data for the agent. The CLI does not run the agent; the main risk lies in what the commands instruct.

## Threats and mitigations

| ID / STRIDE | Threat | Mitigation | Test |
|---|---|---|---|
| A01 / Elevation | Installing permissions, hooks or MCP that broaden what the agent can do without the person's decision. | Only `CLAUDE.md` and `.claude/commands/dixi.*.md`; no `allowed-tools`. | `test_installs_only_commands` |
| A02 / Tampering | Overwriting existing `.claude/` commands or configuration. | Mandatory empty destination and exclusive creation (B1). | `test_existing_claude_dir_untouched` |
| A03 / Tampering | A command instructs modifying frozen tests to make them pass. | Explicit common limit in each command; human review of the PR. | `test_commands_declare_limits` |
| A04 / Repudiation | The agent signs, approves, integrates or pushes on the person's behalf. | Common limit; no command contains `git push` or `--no-verify`. | `test_commands_declare_limits`, `test_commands_avoid_dangerous_operations` |
| A05 / Information disclosure | Instruction injection in specs or arguments to read secrets. | Instruction to treat inputs as data; `dixi` denies sensitive paths. Residual risk: there is no enforcement in the agent. | `test_commands_declare_limits` |
| A06 / Spoofing | Metadata declaring a false agent or inventory to pass `check`. | Agent from a closed list and complete inventory required. | `test_unknown_agent_metadata`, `test_incomplete_adapter_inventory` |
| A07 / Information disclosure | Commands that reference private or missing resources. | Only existing `dixi` operations and packaged procedures. | `test_commands_reference_existing_operations` |

## Residual risk

Instructions in Markdown depend on the model and are not controls. Effective protection against unreviewed changes lies in branch protection and human review of the project's repository, which the kit documents but does not configure.

## Related

- [B3 contract](../07-contracts/commands/claude-code-adapter-contract.md)
- [Feature](../05-features/claude-code-adapter/feature-spec.md)
- [B1 model](local-core-threat-model.md)
