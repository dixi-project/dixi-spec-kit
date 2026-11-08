# Claude Code instructions

@AGENTS.md

## DIXI Spec Kit commands

This project includes commands in `.claude/commands/`:

`/dixi.discover` → `/dixi.specify` → `/dixi.clarify` → `/dixi.plan` → `/dixi.tasks` → `/dixi.build` → `/dixi.verify` → `/dixi.review`, plus `/dixi.analyze` and `/dixi.status` at any time.

In the terminal: `dixi check`, `dixi doctor` and `dixi workflow list` (domain, architecture, contract and threat procedures).

## What this adapter does not do

It installs no hooks, permissions or MCP servers. The rules in `AGENTS.md` and in each command are instructions, not automatic controls: effective protection comes from human review and branch protection in the repository. The agent does not sign, approve, merge or deploy.
