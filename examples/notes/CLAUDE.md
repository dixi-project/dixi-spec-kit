# Claude Code instructions

@AGENTS.md

## DIXI Spec Kit commands

This project includes commands in `.claude/commands/`:

`/dixi.discover` → `/dixi.specify` → `/dixi.clarify` → `/dixi.plan` → `/dixi.tasks` → `/dixi.build` → `/dixi.verify` → `/dixi.review`, plus `/dixi.analyze` and `/dixi.status` at any time.

Design: `/dixi.domain`, `/dixi.architecture`, `/dixi.contract`, `/dixi.threat-model`. Continuity and change: `/dixi.handoff` (writes `.context/handoff.md`, ignored by Git) and `/dixi.change`.

Specialized: `/dixi.data`, `/dixi.quality`, `/dixi.ai`, `/dixi.release`, `/dixi.promote`, `/dixi.operate`, `/dixi.finops`, `/dixi.compliance`, `/dixi.duediligence`. They write documents only; they never run migrations, deploy, change `MODE` or claim certifications.

In the terminal: `dixi check`, `dixi doctor`, `dixi workflow list` and `dixi upgrade --dry-run` (preview what a newer kit version would change, without writing).

## What this adapter does not do

It installs no hooks, permissions or MCP servers. The rules in `AGENTS.md` and in each command are instructions, not automatic controls: effective protection comes from human review and branch protection in the repository. The agent does not sign, approve, merge or deploy.
