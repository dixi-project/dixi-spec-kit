# Block A contract — design, continuity and change commands + upgrade plan

## Purpose

Specify the six agent commands and `dixi upgrade --dry-run` of [TASK-005](../../tasks/backlog/TASK-005-design-continuity-change-upgrade.md). Extends the [Claude Code adapter contract](claude-code-adapter-contract.md); its common command contract and limits apply unchanged.

## New agent commands

| Command | Starts from | Writes | Specific gate |
|---|---|---|---|
| `/dixi.domain` | `dixi workflow prepare domain` | `03-domains/<slug>/domain-spec.md`, trace items | Bounded contexts and ubiquitous language confirmed by the person |
| `/dixi.architecture` | `dixi workflow prepare architecture` | `09-architecture/adr/ADR-NNN-<slug>.md` (Proposed), design notes | No ADR becomes Accepted without human validation |
| `/dixi.contract` | `dixi workflow prepare contract` | `07-contracts/<slug>.md`, trace items | Breaking changes flagged with consumers listed |
| `/dixi.threat-model` | `dixi workflow prepare threat-model` | `13-security/<slug>-threat-model.md` | Each threat has a mitigation and a planned test |
| `/dixi.handoff` | `dixi doctor`, `dixi check` | `.context/handoff.md` (Git-ignored) | Reports unverified work as pending, never as done |
| `/dixi.change` | `/dixi.analyze` logic | `05-features/<slug>/changes/CHANGE-NNN.md` | Never edits frozen tests; existing specs change only after the person accepts the proposal |

## Inventory compatibility

`.dixi/project.json` stays at `schema_version: 1`. For `agent: claude`, `check` requires `CLAUDE.md` and the ten v1.0.0 commands in the inventory; the six new commands are optional so v1.0.0 projects keep passing. `doctor` reports `installed of available` commands.

## `dixi upgrade --dry-run`

```text
dixi [--lang es|en] [--json] upgrade --dry-run
```

Run from the project root. Reads `.dixi/project.json` and the project files; compares with the resources of the installed kit for the same language and agent. Writes nothing, uses no network.

| Status | Condition | Meaning |
|---|---|---|
| `unchanged` | Kit resource identical to the recorded original | Nothing to do |
| `updatable` | Kit changed it and the local file still equals the recorded original | A future apply could replace it safely |
| `conflict` | Kit changed it and the local file differs from the original, or a new kit file collides with an existing untracked file | Manual merge needed |
| `new` | Kit adds it and no local file exists | A future apply could create it |
| `missing` | Recorded in the inventory but deleted locally | Reported; never recreated silently |
| `obsolete` | Recorded in the inventory but no longer shipped by the kit | Kept; the person decides |

Exit codes: 0 plan produced (even with conflicts), 2 missing `--dry-run` or project, 4 project from a newer kit (`kit_version` greater than installed) or another major version, 1 invalid metadata. JSON adds `upgrade: {from, to, files: {status: [paths]}}` with sorted paths.

## Related

- [Claude Code adapter contract](claude-code-adapter-contract.md)
- [Local core contract](local-core-contract.md)
- [TASK-005](../../tasks/backlog/TASK-005-design-continuity-change-upgrade.md)
