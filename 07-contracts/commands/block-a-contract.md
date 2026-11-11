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
| `updatable` | Kit changed it and the local file still equals the recorded original, or the local file already equals the new kit version (an interrupted apply) | `--apply` replaces it, or only records it |
| `conflict` | Kit changed it and the local file differs from the original, a new kit file collides with an existing untracked file, or the local path is a symlink or not a regular file | Manual merge needed; never written |
| `new` | Kit adds it and no local file exists | `--apply` creates it |
| `missing` | Recorded in the inventory but deleted locally | Reported; never recreated silently |
| `obsolete` | Recorded in the inventory but no longer shipped by the kit | Kept; the person decides |

Exit codes: 0 plan produced (even with conflicts), 2 neither or both of `--dry-run` and `--apply`, or no project, 4 project from a newer kit (`kit_version` greater than installed) or another major version, 1 invalid metadata. JSON adds `upgrade: {from, to, files: {status: [paths]}}` with sorted paths.

## `dixi upgrade --apply`

```text
dixi [--lang es|en] [--json] upgrade --apply
```

Accepted on 2026-11-11 ([ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) phase C, [TASK-013](../../tasks/backlog/TASK-013-own-commands.md)). Computes the same plan as `--dry-run` and then writes only `updatable` and `new` files; `conflict`, `missing` and `obsolete` files are never written, recreated or deleted, and are listed for the person.

1. **Exclusive.** Creates `.dixi-upgrade.lock` with exclusive creation before writing; if it exists, exits 3 and writes nothing. It is removed at the end; after an interruption the person checks the project and removes it.
2. **Re-checked per file.** Right before writing, the local file is read again: an `updatable` file must still equal its recorded original, a `new` file must still be absent. Otherwise, or if the path became a symlink or a non-regular file, the file is skipped and reported as a conflict.
3. **Atomic per file.** The new content goes to a temporary file created exclusively, without following links, in the same directory, and is renamed over the target relative to the directory descriptor. A file is never left half written.
4. **Idempotent.** A file that already has the new content is only recorded. Running `--apply` again after success applies nothing; after an interruption it finishes the work.
5. **Metadata last.** `.dixi/project.json` is rewritten atomically at the end with the installed `kit_version` and the hashes of the applied files; skipped files keep their recorded hashes.
6. No network, no execution of project code. The plan printed by `--dry-run` is exactly what `--apply` writes, unless a file changes in between (then it is skipped).

Exit codes: 0 applied (even with conflicts left), 2 usage or no project, 3 another upgrade running or interrupted (lock present), 4 project from a newer kit, 1 invalid metadata, 5 I/O error. JSON adds `upgrade.applied` (sorted paths written or recorded) and `upgrade.skipped` (paths that changed before writing). Multi-file atomicity is not guaranteed: each file is atomic, the set is not ([threat model](../../13-security/local-core-threat-model.md), T09–T12).

Recorded run on 2026-11-11 with this branch against projects created by `dixi 1.6.0` installed from PyPI:

- `dixi init --agent claude --controls`, then a line appended to `README.md`: `--dry-run` planned 1.6.0 → 1.7.0 with 24 unchanged, 28 updatable and 3 new files; `--apply` reported "31 files applied; 0 left for you to review", installed thirty commands, kept the `README.md` edit (unchanged by the kit), left no lock, and a new `--dry-run` showed 55 unchanged; `dixi check` passed.
- `dixi init --agent claude`, then a line appended to `.claude/commands/dixi.build.md` (changed by the kit in 1.7.0): `--apply` applied 30 files and reported `dixi.build.md` as the only conflict; the file stayed byte for byte as the person left it.

## Related

- [Claude Code adapter contract](claude-code-adapter-contract.md)
- [Local core contract](local-core-contract.md)
- [TASK-005](../../tasks/backlog/TASK-005-design-continuity-change-upgrade.md)
