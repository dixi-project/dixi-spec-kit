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
- Same day, second attempt with a fifteen-minute limit: `opencode run "Use the dixi-status skill…"` loaded the skill explicitly (`Skill "dixi-status"`, base directory `.agents/skills/dixi-status`), followed its steps (ran `dixi doctor` and `dixi check`, read `00-master-spec.md` and `docs/guide.md`), reported the project as an unstarted draft and changed no file. `dixi doctor` and `check` answered "invalid metadata" because the `dixi` on that machine's PATH was an installed release that does not know `skills` yet; the run ended with an OpenCode internal server error after the answer. Discovery and explicit invocation are verified for OpenCode; a full run with a released `dixi` that knows the adapter is pending.

- 2026-11-12, released `dixi 1.9.0` installed from PyPI: `dixi init --agent skills` installed 33 of 33 skills, `dixi check` passed and `doctor` reported the adapter. Two OpenCode 1.19.5 runs of `dixi-status` with the configured local model (`ollama/qwen3.5:9b` on a 16 GB machine): the first could not reach the model server (`ECONNREFUSED`); the second reached it but did not finish within fifteen minutes (the model only started a subagent to load the skill). No file changed in either run.
- **Accepted by the owner on 2026-11-12** as evidence for OpenCode: discovery of all thirty-three skills and explicit loading and following of a skill are verified; the speed and quality of a full answer depend on the model the person configures, which is outside the adapter.

## Compatibility

`doctor` reports installed of available skills (`agent_skills`); `check` requires the core skills like Codex; `upgrade` treats the skills as kit files.

## Related

- [Codex adapter contract](codex-adapter-contract.md)
- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [Support matrix](../../docs/support-matrix.md)
