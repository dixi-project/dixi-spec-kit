# Tenant strategy

## Purpose

Decide how the platform separates customers (tenants) from each other: data, configuration,
capacity and billing. Tenancy is expensive to change later, so make the decision explicit early,
document the trade-offs and apply the same model in every product.

## Definitions

- Tenant: {{pending: what a tenant represents, e.g. an organization, a workspace or a household}}
- Tenant identifier: {{pending: format and where it is assigned}}
- Users per tenant: {{pending: one or many; can a user belong to several tenants?}}

## Isolation models

| Model | Description | Strengths | Costs |
|---|---|---|---|
| Shared everything | One store, rows tagged with tenant ID | Cheapest, simplest to operate | Strict filtering everywhere, noisy neighbors |
| Separate schema or partition | Shared runtime, isolated data area | Clearer isolation, easier export | More migrations to manage |
| Dedicated stack | Separate deployment per tenant | Strongest isolation | Highest cost and operational effort |

- Chosen model: {{pending: model and ADR link}}
- Exceptions: {{pending: tenants or data types that need a stronger model}}

## Rules that every product follows

- Every record that belongs to a tenant stores the tenant ID.
- Every query and every message is scoped by tenant; tests include cross-tenant access attempts.
- Caches, files and search indexes are partitioned by tenant as well.
- Logs and metrics include the tenant ID without exposing tenant data.
- Background jobs process one tenant at a time or carry tenant context explicitly.

## Tenant lifecycle

| Stage | What happens | Owner |
|---|---|---|
| Onboarding | {{pending: provisioning steps}} | {{pending: role}} |
| Configuration | {{pending: what tenants can customize}} | {{pending: role}} |
| Suspension | {{pending: what is blocked and what is kept}} | {{pending: role}} |
| Offboarding | {{pending: export, retention and deletion}} | {{pending: role}} |

## Fairness and limits

- Per-tenant quotas: {{pending: requests, storage, users}}
- Behavior when a quota is exceeded: {{pending: throttle, block or bill}}

## Related

- [Multi-tenant architecture](../09-architecture/multi-tenant-architecture.md)
- [Identity and access strategy](identity-and-access-strategy.md)
- [Platform overview](platform-overview.md)
