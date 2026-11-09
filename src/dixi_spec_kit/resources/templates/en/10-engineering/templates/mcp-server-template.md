# MCP server template

## Purpose

Specify a Model Context Protocol (MCP) server that exposes tools, resources or prompts of the
platform to AI agents: what each one does, who may call it and how it is secured and tested. Copy
the structure below for each server.

## Template

```markdown
# MCP server: <server name>

ID: {{pending: server ID}}
Version: 0.1.0
Owner: {{pending: team responsible}}
Transport: {{pending: local process or remote over HTTP}}

## Purpose

Which capability of the platform this server exposes and which agents use it.

## Tools

### Tool: <tool_name>

- Description (written for the model, precise and short):
- Input schema: (JSON schema with types, limits and required fields)
- Output: (structure, and what an error looks like)
- Side effects: none | writes ... | irreversible ...
- Authorization: which identities may call it
- Requires human confirmation: yes | no

## Resources

### Resource: <uri template>

- Content and format:
- Access rules:

## Prompts (optional)

- Name, arguments and purpose.

## Security

- Authentication of the client: {{pending: mechanism}}
- Least privilege: each tool has only the permissions it needs.
- Inputs validated; outputs never include secrets.
- Content returned to agents is treated as untrusted by them.
- Rate limits and audit log of every call.

## Dependencies

| System | Used by | Failure behavior |
|---|---|---|

## Testing

- Unit tests per tool, including invalid input and permission denied.
- Contract test of the schemas listed to clients.

## Operation

- Deployment, configuration and runbook location.
```

## Related

- [Agent specification template](agent-spec-template.md)
- [External integration template](external-integration-template.md)
- [Secure coding standard](../secure-coding-standard.md)
