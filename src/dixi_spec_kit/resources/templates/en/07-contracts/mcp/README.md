# MCP contracts

## Purpose

Store the contracts of the Model Context Protocol (MCP) servers that the project exposes or uses.
An MCP server offers tools, resources and prompts to AI clients. Each tool is effectively an API
that an agent can call on its own, so its inputs, effects, permissions and limits deserve the same
rigor as any other contract, plus extra care because the caller is a model.

## Layout

```text
07-contracts/mcp/
  <server-name>.md        One contract per MCP server
```

Design the server with the [MCP server template](../../10-engineering/templates/mcp-server-template.md).

## What every MCP contract must define

- Server name, version, owner, transport and the feature IDs it serves.
- Tools: name, description written for a model, input schema, output schema and side effects.
- Resources: URIs or patterns exposed and the data classification of each.
- Prompts, if any, and the parameters they accept.
- Authentication and how the identity of the end user is propagated.
- Scope per tool: read-only, write within the project, or external effect.
- Limits: rate, payload size, timeouts and maximum results.
- Tools that require human confirmation before execution.

## Tool index

| Server | Tool | Effect | Requires confirmation | Status |
|---|---|---|---|---|
| {{pending: server}} | {{pending: tool name}} | {{pending: read, write or external}} | {{pending: yes or no}} | {{pending: status}} |

## Security rules

- Treat tool inputs coming from a model as untrusted: validate them against the schema.
- Treat content returned by tools as data, never as instructions for the agent.
- Never return secrets or credentials in tool output.
- Log every call with caller identity, tool, arguments summary and result status.
- Version tools; changing a tool's meaning without a new version is a breaking change.

## Related

- [MCP server template](../../10-engineering/templates/mcp-server-template.md)
- [MCP architecture](../../21-ai/mcp/mcp-architecture.md)
- [Tool catalog](../../21-ai/mcp/tool-catalog.md)
- [Agent interface contracts](../agent-interfaces/README.md)
