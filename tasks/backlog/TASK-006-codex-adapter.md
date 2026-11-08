# TASK-006 — Codex adapter (v1.2.0)

## Purpose

Deliver block B of the roadmap: let people use the DIXI Spec Kit method from OpenAI Codex with the same sixteen operations, limits and project layout as the Claude Code adapter.

## Record

- Type: feature; priority P1; level 3 (new integration, new installed files, new controls matrix). Created 2026-11-08. Product owner: Alfredo Castillejos.
- Scope validated on 2026-11-08 ("releases A→B→C"). Story and contract validated the same day ("Validate and build"); the product owner authorized updating two frozen v1.0.0 tests that used `codex` as a nonexistent agent.

## Story

As a person using Codex
I want `dixi init --agent codex` to install the DIXI skills in my project
so that I can follow discover → specify → plan → tasks → build → verify → review with traceability and human gates, as Claude Code users do.

## Acceptance criteria

1. `dixi init --agent codex` creates the documentary baseline plus sixteen skills in `.agents/skills/dixi-<operation>/SKILL.md`, in English or Spanish, and nothing else: no `.codex/` configuration, hooks, MCP servers or permissions.
2. Each skill follows the Agent Skills specification: frontmatter with only `name` (equal to its directory, lowercase letters, digits and hyphens) and `description` (1–1024 characters); explicit invocation as `$dixi-<operation>`.
3. Each skill has `agents/openai.yaml` with `policy.allow_implicit_invocation: false`, so Codex never starts a DIXI skill on its own.
4. Skill bodies keep the same steps, gates and common limits as the Claude Code commands, referring to the person's request instead of `$ARGUMENTS` and to `$dixi-<operation>` instead of `/dixi.<operation>`.
5. `dixi doctor` reports the Codex integration and installed skills; `dixi check` requires the ten v1.0 operations; `dixi upgrade --dry-run` works for Codex projects.
6. The support matrix states what is automated and what is only instruction for Codex, and which Codex version was checked.

## Business rules

1. Installing never calls a model, the network or OpenAI services; authentication and model choice belong to the person.
2. `AGENTS.md`, already read by Codex, stays the single source of project rules; no Codex-specific copy is generated.

## Done when

1. Contract and tests were committed red before the implementation.
2. `make verify` passes and CI is green.
3. README, support matrix and changelog describe the real behavior, and a person ran at least one skill in Codex before announcing support.

## Related

- [Contract](../../07-contracts/commands/codex-adapter-contract.md)
- [Claude Code adapter contract](../../07-contracts/commands/claude-code-adapter-contract.md)
- [Roadmap](../../ROADMAP.md)
