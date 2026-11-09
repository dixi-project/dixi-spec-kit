# MCP server

## Purpose

Describe the expected structure and conventions of a Model Context Protocol (MCP) server repository: a service that exposes tools, resources or prompts to AI agents. This guide does not choose a language or SDK; it sets the safety and traceability rules every MCP server must follow.

Status: draft. {{pending: choose the language, SDK and transport for MCP servers}}

## Stack decisions

| Decision | Choice | ADR |
|----------|--------|-----|
| Language and SDK | {{pending}} | {{pending}} |
| Transport (local process or network) | {{pending}} | {{pending}} |
| Authentication for network transport | {{pending}} | {{pending}} |
| Test runner | {{pending}} | {{pending}} |

## Suggested folder layout

```text
<mcp-server>/
├── README.md          # purpose, exposed tools, spec IDs
├── AGENTS.md
├── src/
│   ├── tools/         # one module per tool, with its input schema
│   ├── resources/     # read-only data exposed to agents
│   ├── prompts/       # reusable prompt templates, if any
│   └── adapters/      # calls to backend services
├── tests/
└── .env.example
```

## Tool catalog

| Tool | What it does | Side effects | Needs human approval |
|------|--------------|--------------|----------------------|
| {{pending: name}} | {{pending}} | None / writes / external call | {{pending: yes or no}} |

## Conventions

- Each tool has a narrow purpose, a strict input schema and a clear description.
- Read-only tools are separated from tools that change state; write tools require explicit approval.
- Inputs are validated; outputs never include secrets or more personal data than needed.
- Content returned from external sources is treated as data, not as instructions for the agent.
- The server acts with the least privilege needed and never with a person's full credentials.
- Every tool call is logged with caller, tool, arguments summary and result status.
- Rate limits and timeouts protect the services behind the server.

## Verification

- Tests cover valid input, invalid input, permission denial and injection attempts in returned content.
- `make verify` runs the server's real checks.

## Related

- [Repositories](README.md)
- [Backend service](backend-service.md)
- [AI agent hardening](../13-security/ai-agent-hardening.md)
- [Guardrails](../21-ai/agents/guardrails.md)
- [Human in the loop](../21-ai/agents/human-in-the-loop.md)
- [AI audit trail](../21-ai/governance/ai-audit-trail.md)
