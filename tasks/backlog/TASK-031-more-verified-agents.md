# TASK-031 — More agents verified with the Agent Skills adapter (v1.13.0)

## Purpose

`--agent skills` installs the thirty-three operations in a format that Cursor, VS Code/Copilot, Gemini CLI, OpenCode, Goose and Amp read according to their documentation, but only OpenCode has a recorded run, and only for discovery and explicit invocation ([contract](../../07-contracts/commands/agent-skills-adapter-contract.md#manual-runs)). A person using any other agent reads "format compatible, not verified" and cannot tell whether DIXI works there. This task turns documentation claims into recorded evidence, agent by agent, without changing the adapter unless a run shows that it must change.

## Record

- Type: feature (evidence and docs); priority P2; level 2 (changes the support matrix; the adapter changes only if a run finds a defect). Created 2026-11-14. Product owner: Alfredo Castillejos.
- Scope chosen by the owner on 2026-11-14: "more supported agents" for v1.13.0.
- Audit of 2026-11-14 on the maintainer's machine: installed and reading `.agents/skills/` according to the contract, Cursor 3.29.9 and VS Code 1.145.2 (whether Copilot agent mode is enabled is to be checked by the owner); OpenCode 1.19.5 is installed and has partial evidence. Gemini CLI, Goose and Amp are not installed. Claude Code does not read `.agents/skills/` and keeps its own adapter; Codex keeps `--agent codex`.
- Out of scope: new adapters or folders per agent (`.cursor/`, `.github/`, `.gemini/`), hooks for `--agent skills`, and agents that are not installed unless the owner installs them during the task.

## Story

As a person who uses Cursor, VS Code/Copilot or OpenCode
I want to know whether DIXI's operations actually run in my agent
so that I can adopt the method without testing the adapter myself.

## Acceptance criteria

1. Recorded run per agent: for Cursor and VS Code/Copilot, and a full run for OpenCode, the contract gains an entry under "Manual runs" with the date, the agent version, the released `dixi` version installed from PyPI, the project created with `dixi init --agent skills`, and four observations: (a) the agent lists or discovers all thirty-three `dixi-<operation>` skills; (b) it loads and follows `dixi-status` when asked explicitly; (c) it does not start a DIXI skill by itself in a prompt that does not name one (`disable-model-invocation`); (d) the files changed by the run. A failed or partial run is recorded as such.
2. Support matrix: an agent moves to Supported, with its version and a link to its run, only when (a) and (b) hold; (c) is reported as observed or not observed. Agents without a run stay "format compatible, not verified". The Spanish summary of the matrix says the same.
3. The discovery table of the contract is re-read from each agent's documentation and dated; any agent whose documentation no longer reads `.agents/skills/` is corrected.
4. A test fails when the support matrix names an agent as supported for `--agent skills` and the contract has no manual-run entry for that agent and version.
5. If a run shows that the adapter must change (for example, a frontmatter field rejected by an agent), the change follows tests first and is recorded in the contract; otherwise `src/` does not change.
6. No page, in English or Spanish, describes an agent as supported unless the support matrix does.

## Done when

1. Tests were committed red before the documentation changes.
2. `make verify` passes and CI is green.
3. The owner ran each agent, or recorded why an agent could not be run, and accepted the evidence.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
- [TASK-014](TASK-014-agent-skills-adapter.md)
- [Agent Skills adapter contract](../../07-contracts/commands/agent-skills-adapter-contract.md)
- [Support matrix](../../docs/support-matrix.md)
