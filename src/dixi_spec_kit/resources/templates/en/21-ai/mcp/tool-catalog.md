# Tool catalogue

## Purpose

List every tool and resource that agents or product features can call through MCP or similar integrations, with its risk and the controls around it. A tool that is not in this catalogue must not be enabled.

## Risk levels

| Level | Description | Required control |
| --- | --- | --- |
| Read | Returns data, no side effects | Access check per caller |
| Write | Changes state, reversible | Access check, audit log |
| Destructive | Irreversible or external effect | Access check, audit log, human confirmation |

## Catalogue

| Tool | Server | Description | Inputs | Risk | Roles allowed | Tests |
| --- | --- | --- | --- | --- | --- | --- |
| {{pending: tool name}} | {{pending: define}} | {{pending: define}} | {{pending: schema reference}} | {{pending: read / write / destructive}} | {{pending: define}} | {{pending: test reference}} |

## Resources

| Resource | Server | Content | Sensitivity | Roles allowed |
| --- | --- | --- | --- | --- |
| {{pending: resource name}} | {{pending: define}} | {{pending: define}} | {{pending: public / internal / confidential}} | {{pending: define}} |

## Entry checklist

- [ ] Contract with input and output schema exists.
- [ ] Risk level assigned and matching controls implemented.
- [ ] Tests cover permission denial and invalid input.
- [ ] Roles allowed are reflected in the capability matrix.
- [ ] Third-party tools reviewed, with version pinned.

## Retiring a tool

Disable it in the server first, then remove it from this catalogue and from the capability matrix in the same change.

## Related

- [MCP architecture](mcp-architecture.md)
- [Capability matrix](../agents/capability-matrix.md)
- [Human in the loop](../agents/human-in-the-loop.md)
- [AI audit trail](../governance/ai-audit-trail.md)
