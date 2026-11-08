# Contract — specialized commands (block C)

## Purpose

Specify the nine specialized operations of [TASK-007](../../tasks/backlog/TASK-007-specialized-commands.md). The common command contract and limits of the [Claude Code adapter](claude-code-adapter-contract.md) apply; Codex skills are derived from the same text ([Codex adapter](codex-adapter-contract.md)).

## Operations

| Operation | Writes | Never does |
|---|---|---|
| `data` | `08-data/`: data model, classification of personal data, retention and migration plan | Run migrations or touch databases |
| `quality` | `11-quality/`: test strategy, budgets, verification matrix (including i18n and accessibility when in scope) | Lower coverage or quality gates to make work pass |
| `ai` | `21-ai/`: use cases, evaluation plan, data, cost assumptions, agent/MCP design under the project's provider policy | Pick a model provider or call a model |
| `release` | `docs/releases/<version>.md`: readiness evidence, changelog proposal, rollback plan | Tag, publish, approve a gate or deploy |
| `promote` | `docs/promotion/<date>-prod.md`: checklist for `MODE=prod` with missing evidence | Edit `MODE`; only the person changes it |
| `operate` | `15-operations/`: SLOs, observability, runbooks, incident preparation | Operate production or run commands against it |
| `finops` | `22-finops/`: estimates with stated assumptions, sources and budgets | Invent consumption or present estimates as real costs |
| `compliance` | `23-compliance/`: obligations map and pending evidence | Declare a certification or legal conformity |
| `duediligence` | `28-due-diligence/<type>.md`: report backed by project artifacts, with gaps | Fill gaps with assumptions presented as facts |

Each operation reads `AGENTS.md`, `00-master-spec.md`, `MODE` and the relevant specs; asks when a required decision is missing; registers new documents in `.dixi/traceability.json` only when they fit an existing kind; and closes with `dixi check` and a summary of evidence and gaps.

## Compatibility

Inventory requirements do not change: the nine operations are optional, so projects from v1.0–v1.2 keep passing `check` and see them as `new` in `dixi upgrade --dry-run`. `doctor` reports installed of available (25).

## Related

- [TASK-007](../../tasks/backlog/TASK-007-specialized-commands.md)
- [Block A contract](block-a-contract.md)
