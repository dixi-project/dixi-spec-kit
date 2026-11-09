# Memory architecture

## Purpose

Define what agents and AI features remember across steps and sessions, where that memory lives, who can read it and when it is deleted. The repository remains the source of truth; memory never replaces specs.

## Layers

| Layer | Content | Lifetime | Location |
| --- | --- | --- | --- |
| Working | Current task context | One request or session | In the agent process |
| Session notes | Decisions and open questions of a session | Days | Private, untracked folder (for example `.context/`) |
| Project knowledge | Specs, contracts, decisions, tests | Life of the project | Repository, versioned |
| Derived index | Search index or graph built from the repository | Rebuilt on change | {{pending: whether an index is used and where}} |
| Product memory | Per-user state used by AI features | {{pending: retention}} | {{pending: storage}} |

## Rules

- If information can live in the repository documentation, put it there instead of agent memory.
- Memory is never a place for secrets or credentials.
- A derived index is disposable: it can be rebuilt from the repository at any time.
- Session notes are private and not committed; promote decisions into specs before ending the session.

## Product memory

If a product feature remembers user information:

- What is stored and why: {{pending: data stored and purpose}}
- User visibility and deletion: users can see and delete what is remembered.
- Isolation: one user's memory is never retrieved for another user; a test proves it.
- Retention and deletion requests follow the project's data policy.

## Access

| Layer | Readers | Writers |
| --- | --- | --- |
| Session notes | The person and their agents | Same |
| Project knowledge | Everyone with repository access | Through reviewed pull requests |
| Product memory | {{pending: services and roles}} | {{pending: services and roles}} |

## Exposure through tools

If memory is exposed to agents through MCP resources, register each resource in the tool catalogue with its sensitivity.

## Related

- [MCP architecture](../mcp/mcp-architecture.md)
- [Tool catalogue](../mcp/tool-catalog.md)
- [Context strategy](../llm/context-strategy.md)
- [Responsible AI](../governance/responsible-ai.md)
