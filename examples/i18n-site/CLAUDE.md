# Claude Code instructions

@AGENTS.md

## DIXI Spec Kit commands

This project includes commands in `.claude/commands/`:

`/dixi.discover` → `/dixi.specify` → `/dixi.clarify` → `/dixi.plan` → `/dixi.tasks` → `/dixi.build` → `/dixi.verify` → `/dixi.review`, plus `/dixi.analyze` and `/dixi.status` at any time.

Design: `/dixi.domain`, `/dixi.architecture`, `/dixi.contract`, `/dixi.threat-model`. Continuity and change: `/dixi.handoff` (writes `.context/handoff.md`, ignored by Git) and `/dixi.change`.

Specialized: `/dixi.data`, `/dixi.quality`, `/dixi.ai`, `/dixi.release`, `/dixi.promote`, `/dixi.operate`, `/dixi.finops`, `/dixi.compliance`, `/dixi.duediligence`. They write documents only; they never run migrations, deploy, change `MODE` or claim certifications.

Guided and review: `/dixi.interview` fills the `{{pending: …}}` blanks one question at a time; `/dixi.risk-review` prepares a risk-based review for a person. Subagents in `.claude/agents/`: `dixi-architect`, `dixi-tester`, `dixi-developer`, `dixi-reviewer`.

In the terminal: `dixi check`, `dixi doctor`, `dixi workflow list`, `dixi placeholders`, `dixi pr-size` and `dixi upgrade --dry-run` (preview what a newer kit version would change, without writing).

## What this adapter does not do

It installs no permissions or MCP servers, and no hooks unless the project was created with `--controls` (then `.claude/settings.json` runs the scripts in `.dixi/hooks/`: a second layer, not the last one). Without them, the rules in `AGENTS.md` and in each command are instructions, not automatic controls: effective protection comes from human review and branch protection in the repository. The agent does not sign, approve, merge or deploy.
