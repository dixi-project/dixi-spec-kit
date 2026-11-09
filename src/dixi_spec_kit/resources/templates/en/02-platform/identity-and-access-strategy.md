# Identity and access strategy

## Purpose

Define how people, services and agents are identified across the platform and how access is granted,
checked and revoked. A consistent strategy prevents each product from inventing its own login and
permission model, which leads to gaps, duplicated accounts and inconsistent audit trails.

## Identity types

| Identity | Examples | How it authenticates | Lifetime |
|---|---|---|---|
| End user | {{pending: personas}} | {{pending: method}} | {{pending: session duration}} |
| Internal staff | {{pending: internal roles}} | {{pending: method, including second factor}} | {{pending: duration}} |
| Service | Product backends, jobs | {{pending: short-lived credentials or workload identity}} | {{pending: rotation period}} |
| AI agent | Assistants acting for a person or a service | {{pending: delegated, scoped credential}} | {{pending: duration}} |

Choosing an identity provider is a project decision recorded in an ADR, not here.

## Principles

- One identity per person across products; products do not keep their own passwords.
- Least privilege by default; access is granted to roles, not to individuals.
- Every request carries identity and tenant context, and every service verifies them.
- Agents act with the permissions of the person or service they represent, never more.
- Access changes are logged and reviewable.

## Authorization model

- Model: {{pending: role-based, attribute-based or a combination}}
- Where decisions are made: {{pending: central service, each product, or both}}
- Scope of a role: {{pending: global, per tenant or per resource}}

| Role | Products | Scope | Granted by |
|---|---|---|---|
| {{pending: role}} | {{pending: products}} | {{pending: scope}} | {{pending: approver}} |

## Lifecycle

- Provisioning: {{pending: how accounts are created and roles assigned}}
- Periodic review: {{pending: cadence for reviewing who has access}}
- Deprovisioning: {{pending: maximum time to revoke access after a role change}}
- Emergency access: {{pending: break-glass procedure and who approves it}}

## Related

- [Tenant strategy](tenant-strategy.md)
- [Authentication and authorization model](../13-security/authn-authz-model.md)
- [Internal roles](../01-business/actors/internal-roles.md)
- [Shared services map](shared-services-map.md)
