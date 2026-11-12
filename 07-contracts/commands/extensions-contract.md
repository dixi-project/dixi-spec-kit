# Contract — local extensions (`dixi extension`)

## Purpose

Specify how a team adds its own operations to a DIXI project without forking the kit ([ADR-109](../../09-architecture/adr/ADR-109-local-presets-and-extensions.md), [TASK-015](../../tasks/backlog/TASK-015-extensibility-and-site.md)). Presets, which override kit texts, are specified separately.

## Interface

```text
dixi [--lang es|en] [--json] extension add <folder>
dixi [--lang es|en] [--json] extension list
dixi [--lang es|en] [--json] extension remove <id>
```

Run from the project root. No network, no execution of anything inside the extension.

## Extension folder

```text
<folder>/
├── extension.json            {"id": "acme", "version": "1.0.0", "operations": ["deploy-check"]}
└── operations/
    ├── en/deploy-check.md    frontmatter: description, argument-hint; body uses `$ARGUMENTS`
    └── es/deploy-check.md
```

- Nothing else is accepted: any other file, a symlink, a device or a missing language refuses the whole folder (exit 2, `invalid_extension`, nothing written).
- `id` and operation names match `[a-z0-9]+(-[a-z0-9]+)*`; `id` is not `dixi`; `dixi-<id>-<operation>` is at most 64 characters (the Agent Skills name limit); 1 to 50 operations; each text at most 64 KiB, UTF-8, with `description` (quoted, at most 1022 characters) and `argument-hint` frontmatter. `requires` is accepted and recorded for a later version check.

## Installation

- Claude Code: `.claude/commands/dixi-<id>-<operation>.md`, the text in the project's language as written.
- Codex and Agent Skills: `.agents/skills/dixi-<id>-<operation>/SKILL.md` with `name` equal to the folder, the quoted `description`, `$ARGUMENTS` replaced as in kit skills, and `/dixi.<op>` or `/dixi-<op>` references rewritten (`$dixi-<op>` for Codex, `dixi-<op>` for Agent Skills, which also get `disable-model-invocation: true`); plus `agents/openai.yaml`.
- A copy of the folder goes to `.dixi/extensions/<id>/` so the extension can be inspected and removed.
- The `dixi-<id>-` prefix means an extension can never shadow a kit operation. If any target file already exists, or the id is already installed, nothing is written (exit 3, `extension_conflict`). A project created with `--agent none` is refused (exit 2). Extensions never add hooks or change `--controls`.

## Record and removal

`.dixi/project.json` gains `extensions: {<id>: {version, files: {path: sha256}}}`, validated on every read like the kit inventory but kept outside `managed_files`, so `dixi check` and `dixi upgrade` treat extension files as the person's. `remove` deletes only recorded files whose content is unchanged, reports edited ones as kept (JSON `extension.kept`), removes empty folders it created and drops the record.

## Related

- [ADR-109](../../09-architecture/adr/ADR-109-local-presets-and-extensions.md)
- [Local core threat model](../../13-security/local-core-threat-model.md) (T14)
- [Agent Skills adapter](agent-skills-adapter-contract.md)
