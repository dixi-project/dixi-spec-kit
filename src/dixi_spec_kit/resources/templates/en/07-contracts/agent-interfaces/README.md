# Agent interface contracts

## Purpose

Describe the interfaces of the AI agents that take part in the project: what each agent can do,
what it receives, what it returns, which tools it may use and which actions require a person. An
agent interface is a contract like any other; writing it down makes agent behavior reviewable,
testable and replaceable, regardless of the model or provider behind it.

## Layout

```text
07-contracts/agent-interfaces/
  <agent-name>.interface.md     Human-readable contract
  <agent-name>.interface.json   Optional machine-readable version
```

Design the agent itself with the [agent spec template](../../10-engineering/templates/agent-spec-template.md);
this folder holds only the interface other components rely on.

## What every agent interface must define

- Name, version, owner and the feature IDs it serves.
- Capabilities: each task the agent performs, with input and output formats.
- Autonomy level per capability: suggest only, act with approval, or act and report.
- Tools it may call and the scope of each (read-only, write, external effect).
- Context it receives and data it must never receive (secrets, unnecessary personal data).
- Output validation: schema checks, limits and what happens on invalid output.
- Human checkpoints: actions that always need a person to approve.
- Audit: what is recorded for each run so decisions can be reviewed later.

## Example shape

```json
{
  "agent": "spec-drafter",
  "version": "0.1.0",
  "capabilities": [
    {"name": "draft_feature_spec", "input": {"goal_id": "string"}, "output": "markdown",
     "autonomy": "suggest"}
  ],
  "tools": ["read_specs"],
  "human_approval_required": ["write_to_main_branch"]
}
```

## Agent index

| Agent | Capabilities | Autonomy | Owner | Status |
|---|---|---|---|---|
| {{pending: agent name}} | {{pending: capabilities}} | {{pending: autonomy level}} | {{pending: role}} | {{pending: status}} |

## Related

- [Agent spec template](../../10-engineering/templates/agent-spec-template.md)
- [Agent architecture](../../21-ai/agents/agent-architecture.md)
- [Human in the loop](../../21-ai/agents/human-in-the-loop.md)
- [MCP contracts](../mcp/README.md)
