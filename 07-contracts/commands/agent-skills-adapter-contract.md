# Contract — Agent Skills adapter (`--agent skills`)

## Purpose

Specify what `dixi init --agent skills` installs for agents that read the open [Agent Skills](https://agentskills.io/specification) format, beyond Claude Code and Codex. Implements [TASK-014](../../tasks/backlog/TASK-014-agent-skills-adapter.md) ([ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) phase D, design approved by the owner on 2026-11-11).

## Specification read

Read on 2026-11-11: https://agentskills.io/specification (repository `agentskills/agentskills`; a living document without version numbers or tags; last specification changes on 2026-08-04 and 2026-05-16). Required frontmatter: `name` (1–64 characters, `a-z`, `0-9` and `-`, no leading, trailing or double hyphen, equal to the parent folder) and `description` (1–1024 characters). The specification fixes no discovery path; its client guide recommends `<project>/.agents/skills/`.

## What it installs

Baseline documents and `AGENTS.md`, plus, for each of the thirty-three operations:

- `.agents/skills/dixi-<operation>/SKILL.md`: derived at install time from the Codex skill text, with `name`, `description` and `disable-model-invocation: true`; the Codex-only `$dixi-<operation>` syntax becomes the neutral skill name `dixi-<operation>`.
- `.agents/skills/dixi-<operation>/agents/openai.yaml`: the Codex policy disabling implicit invocation.

No `.claude/`, `.codex/`, `.cursor/`, `.github/`, `.gemini/` or `.opencode/` folder, settings, permissions, MCP servers or hooks. `--controls` exits 2 without writing: hooks exist only for Claude Code and Codex.

## Implicit invocation

`disable-model-invocation` is not a field of the specification. It is honoured by Claude Code, VS Code/Copilot, Cursor and OpenCode, according to their documentation; Codex uses `agents/openai.yaml`; Gemini CLI can only disable a skill entirely. A validator that rejects fields outside the specification may reject it; the owner chose to keep it so DIXI operations do not start by themselves.

## Discovery by agent

| Agent | Reads `.agents/skills/` | Source (read 2026-11-11) |
|---|---|---|
| OpenAI Codex | Yes | learn.chatgpt.com/docs/build-skills |
| Cursor | Yes | cursor.com/docs/skills |
| VS Code / GitHub Copilot | Yes (depending on the surface) | code.visualstudio.com/docs/copilot/customization/agent-skills |
| Gemini CLI | Yes (alias of `.gemini/skills`) | geminicli.com/docs/cli/skills |
| OpenCode | Yes | opencode.ai/docs/skills |
| Goose, Amp | Yes, according to search results only | goose-docs.ai, ampcode.com |
| Claude Code | No (only `.claude/skills/`; issue #31005 open) | code.claude.com/docs/en/skills |

The support matrix lists the adapter as "format compatible, not verified per agent". An agent moves to Supported only after a recorded run, as for Claude Code and Codex.

## Manual runs

- 2026-11-11, OpenCode 1.19.5, in a project created with `dixi init --agent skills` from this branch: `opencode debug skill` listed all thirty-three `dixi-<operation>` skills with their location in `.agents/skills/`, each `name` equal to its folder. The listing does not show whether `disable-model-invocation` is honoured. Running an operation with the configured local model (`qwen3.5:9b`) did not answer within five minutes; execution is not yet verified.

## Compatibility

`doctor` reports installed of available skills (`agent_skills`); `check` requires the core skills like Codex; `upgrade` treats the skills as kit files.

## Related

- [Codex adapter contract](codex-adapter-contract.md)
- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [Support matrix](../../docs/support-matrix.md)
