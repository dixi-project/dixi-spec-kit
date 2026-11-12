# Contract — local presets (`dixi preset`)

## Purpose

Specify how a team replaces kit operation texts and templates in a project without forking the kit ([ADR-109](../../09-architecture/adr/ADR-109-local-presets-and-extensions.md), [TASK-015](../../tasks/backlog/TASK-015-extensibility-and-site.md)). Extensions, which add operations, are in the [extensions contract](extensions-contract.md).

## Interface

```text
dixi [--lang es|en] [--json] preset add <folder>
dixi [--lang es|en] [--json] preset list
dixi [--lang es|en] [--json] preset remove <id>
```

## Preset folder

```text
<folder>/
├── preset.json                       {"id": "team", "version": "1.0.0", "priority": 50}
├── operations/{en,es}/<operation>.md   replaces a kit operation (frontmatter description, argument-hint)
└── templates/{en,es}/<path>            replaces a kit template (base or profile), same path
```

- Only these entries; no links or other files. `id` matches `[a-z0-9]+(-[a-z0-9]+)*` and is not `dixi`; `priority` is an integer from 0 to 100; operations must be kit operations; templates must be kit template paths; English and Spanish override the same files; 1 to 300 files, operation texts at most 64 KiB, templates at most 256 KiB, UTF-8. Otherwise exit 2 (`invalid_preset`) and nothing is written.

## Applying

For the project's language and agent, each override maps to a project file: the template path itself, `.claude/commands/dixi.<op>.md` for Claude Code, or `.agents/skills/dixi-<op>/SKILL.md` for Codex and Agent Skills (converted as kit skills are). A project file is replaced only when:

1. it is a kit file installed in this project;
2. there is no `.dixi/overrides/<same operations/... or templates/... path>` (the project's own override always wins);
3. it still equals the kit version, or it holds the text of a lower-priority preset unchanged (which then loses that file).

Otherwise it is kept and listed (`preset.kept`). A copy of the folder goes to `.dixi/presets/<id>/`; an id already installed or an existing copy exits 3 (`preset_conflict`).

## Record, upgrade and removal

`.dixi/project.json` gains `presets: {<id>: {version, priority, files: {path: sha256}, copy: {path: sha256}}}`, validated on every read. `managed_files` keeps the **kit** hashes, so `dixi upgrade` sees a preset file as unchanged while the kit file does not change, and as a conflict (never overwritten) when it does. `remove` restores the kit text for files whose content is still the preset's, keeps the rest, deletes the unchanged copy and drops the record.

## Related

- [ADR-109](../../09-architecture/adr/ADR-109-local-presets-and-extensions.md)
- [Extensions contract](extensions-contract.md)
- [Local core threat model](../../13-security/local-core-threat-model.md) (T15)
