# Internal roles

## Purpose

List the roles inside the organization that operate, support or govern the product, with their
responsibilities and the permissions they need. This page feeds the authorization model, the
escalation paths and the human review gates of the SDD workflow. Describe roles, not individuals.

## Role catalog

| ID | Role | Responsibilities | Uses the product for | Decision rights |
|---|---|---|---|---|
| ROLE-001 | {{pending: e.g. product owner}} | {{pending: responsibilities}} | {{pending: tasks}} | {{pending: what this role approves}} |
| ROLE-002 | {{pending: e.g. support agent}} | {{pending: responsibilities}} | {{pending: tasks}} | {{pending: what this role approves}} |
| ROLE-003 | {{pending: e.g. operator or administrator}} | {{pending: responsibilities}} | {{pending: tasks}} | {{pending: what this role approves}} |

## Access needs

Apply least privilege: start from no access and add only what each task requires.

| Role | Data it may read | Actions it may perform | Actions that need a second person |
|---|---|---|---|
| {{pending: role}} | {{pending: data scope}} | {{pending: actions}} | {{pending: sensitive actions}} |

## Human review gates

Who validates each kind of change before it is built or merged:

| Change type | Validating role |
|---|---|
| Structural decisions (domains, contracts, architecture) | {{pending: role}} |
| Business rules and pricing | {{pending: role}} |
| Security and privacy impact | {{pending: role}} |

AI agents can draft and propose, but never take the place of the validating role.

## Segregation of duties

- {{pending: pairs of actions that the same role must not perform alone}}

## Related

- [Personas](personas.md)
- [External partners](external-partners.md)
- [Authentication and authorization model](../../13-security/authn-authz-model.md)
- [Agent instructions](../../AGENTS.md)
