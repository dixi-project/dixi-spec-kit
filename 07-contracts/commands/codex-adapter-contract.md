# Contract — Codex adapter (block B)

## Purpose

Specify what `dixi init --agent codex` installs and how the DIXI operations behave inside OpenAI Codex. Implements [TASK-006](../../tasks/backlog/TASK-006-codex-adapter.md).

## Checked versions and syntax

- Codex CLI **0.167.0** (macOS), checked on 2026-11-08 with `codex --version`.
- Project skills: `.agents/skills/<name>/SKILL.md`, scanned from the working directory up to the repository root ([Codex skills documentation](https://learn.chatgpt.com/docs/build-skills)). Custom prompts are deprecated and user-level only, so they are not used.
- Frontmatter per the [Agent Skills specification](https://agentskills.io/specification): `name` 1–64 characters, lowercase `a-z`, `0-9` and single hyphens, equal to the parent directory; `description` 1–1024 characters.
- Optional `agents/openai.yaml` per skill: `policy.allow_implicit_invocation: false` disables implicit invocation; explicit `$name` keeps working.
- Codex reads `AGENTS.md` from the repository root automatically.

## CLI

```text
dixi [--lang es|en] [--json] init <directory> [--agent none|claude|codex]
```

Same destination guarantees as v1.0: new or empty directory, no symlinks, exclusive creation.

## Installed files

| Path | Content |
|---|---|
| `.agents/skills/dixi-<operation>/SKILL.md` | One per operation: `discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze`, `status`, `domain`, `architecture`, `contract`, `threat-model`, `handoff`, `change`. |
| `.agents/skills/dixi-<operation>/agents/openai.yaml` | `policy: {allow_implicit_invocation: false}` |

No `.codex/` directory, configuration, hooks, MCP servers or permission grants. `.dixi/project.json` records `"agent": "codex"` and the hash of every installed file; `check` requires the ten v1.0 operations (both files each), the six newer ones are optional for future compatibility.

## Skill body

Same goal, steps, gates, common limits and closing as the [Claude Code commands](claude-code-adapter-contract.md), with two substitutions: "the person's request (the text written with the skill mention)" replaces `$ARGUMENTS`, and `$dixi-<operation>` replaces `/dixi.<operation>`. If the request is empty when one is required, the skill asks and stops.

## Controls matrix

| Control | Mechanism in v1.2.0 |
|---|---|
| No overwrite on install | Automated by `dixi init` (tests). |
| Structure and traceability | Automated by `dixi check` / `make verify` (tests). |
| No implicit start of a DIXI skill | `allow_implicit_invocation: false` (Codex setting; checked statically by tests). |
| Tests first and frozen; no sign, approve or merge; structural decisions validated by a person | Instruction in every skill + human review and branch protection. **Not enforced in Codex.** |
| Sandbox and approvals | The person's Codex configuration; the kit does not change it. |

## Errors

Same exit codes as v1.0. An unknown `--agent` value exits 2 without writing.

## Related

- [TASK-006](../../tasks/backlog/TASK-006-codex-adapter.md)
- [Block A contract](block-a-contract.md)
- [Support matrix](../../docs/support-matrix.md)
