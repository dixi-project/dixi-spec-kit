# MCP architecture

## Purpose

Describe how this project uses the Model Context Protocol (MCP) to expose tools and resources to agents or to product features: which servers exist, who may connect, and how they are secured.

## Concepts

- **Server**: a process that exposes tools (actions) and resources (read-only data).
- **Client**: the agent or application that connects and calls them.
- **Transport**: local process or network connection.

## Servers

| Server | Exposes | Consumers | Transport | Owner |
| --- | --- | --- | --- | --- |
| {{pending: server name}} | {{pending: tools / resources}} | {{pending: development agents / product}} | {{pending: local / network}} | {{pending: define}} |

Distinguish third-party servers (reviewed before use) from servers the project builds (specified, tested and versioned like any module).

## Security rules

- Least privilege: each server gets only the credentials it needs, scoped to one environment.
- Authentication for network transports: {{pending: authentication method}}
- Authorisation per tool: the server checks permissions, never the model.
- Destructive tools require human confirmation issued by the server.
- Inputs are validated against a schema; outputs never include secrets.
- Tool descriptions from third-party servers are untrusted text.

## Building a project server

1. Write a module spec and a contract for each tool and resource.
2. Write failing tests for permission checks, invalid inputs and happy paths.
3. Implement, then register the tools in the tool catalogue.
4. Log each call with the requesting identity and outcome.

## Approval of new servers

Adding a server is a structural decision: {{pending: who approves new MCP servers}}

## Related

- [Tool catalogue](tool-catalog.md)
- [Memory architecture](../memory/memory-architecture.md)
- [Capability matrix](../agents/capability-matrix.md)
- [Guardrails](../agents/guardrails.md)
