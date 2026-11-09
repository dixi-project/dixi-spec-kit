# Agent architecture

## Purpose

Describe which AI agents take part in this project, what each one is responsible for, how they hand work to each other and to people, and where they run. Keep it provider-neutral: roles and boundaries matter more than the tool used.

## Roles

| Role | Responsibility | Typical outputs | Must not |
| --- | --- | --- | --- |
| Specifier | Turn a need into goal, domain, module and feature drafts | Spec drafts with pending markers | Approve its own specs |
| Contract writer | Derive contracts from approved features | Contract drafts | Change approved contracts silently |
| Test writer | Write failing tests from contracts | Test files | Edit frozen tests |
| Builder | Implement until tests pass | Code changes | Weaken tests or checks |
| Reviewer | Read diffs against specs and report risks | Review comments | Approve or merge |

Roles may be played by one agent in different modes or by separate agents: {{pending: one agent with modes or separate agents}}

## Flow

```text
need → specifier → [person validates] → contract writer → test writer
     → builder → reviewer → [person reviews, approves, merges]
```

Each arrow passes artifacts in the repository, not hidden state. Use `dixi workflow prepare <name>` to give each step the same context manifest.

## Execution modes

| Mode | Person at the keyboard? | Allowed actions |
| --- | --- | --- |
| Interactive | Yes | Read and write in the working copy; commands need confirmation |
| Unattended | No | {{pending: allowed actions, for example read-only review comments}} |

Unattended agents should process untrusted content without secrets and produce comments or artifacts, never deployments.

## Context and permissions

- Each role receives only the files it needs (see the context strategy).
- Each role has the smallest tool set that fits its task (see the capability matrix).

## Project decisions

- Agent integrations in use: {{pending: none, or the integrations chosen}}
- Where unattended agents run: {{pending: environment and isolation}}

## Related

- [Capability matrix](capability-matrix.md)
- [Guardrails](guardrails.md)
- [Human in the loop](human-in-the-loop.md)
- [Context strategy](../llm/context-strategy.md)
- [Methodology](../sdd/methodology.md)
