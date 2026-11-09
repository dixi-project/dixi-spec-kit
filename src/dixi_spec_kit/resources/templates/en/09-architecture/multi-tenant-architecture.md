# Multi-Tenant Architecture

## Purpose

Describe how the platform serves several tenants (organisations, workspaces or customers) from shared infrastructure while keeping their data and configuration isolated. Tenant isolation failures are among the most severe defects a platform can have, so the model must be explicit.

## Tenancy model

| Option | Isolation | Cost | Operational effort |
|---|---|---|---|
| Shared schema with tenant column | Logical | Low | Low |
| Schema or database per tenant | Stronger | Medium | Medium |
| Dedicated stack per tenant | Strongest | High | High |

Chosen model: {{pending: tenancy model, recorded in an ADR}}

## Tenant resolution

- How a request identifies its tenant: {{pending: subdomain, path, token claim or header}}
- Where the tenant context is set: {{pending: middleware or gateway}}
- What happens when it is missing or invalid: reject the request.

## Isolation rules

- Every query on tenant-owned data is scoped by tenant, enforced centrally rather than by convention: {{pending: mechanism, e.g. row-level policies or repository filter}}.
- Caches, files, search indexes and queues are keyed by tenant.
- Background jobs and events carry the tenant ID explicitly.
- Logs include the tenant ID but never another tenant's data.
- Cross-tenant operations (support, reporting) require an explicit, audited role.

## Per-tenant configuration

| Setting | Default | Who can change it |
|---|---|---|
| {{pending: feature flag or limit}} | {{pending: value}} | {{pending: role}} |

## Noisy neighbours

- Rate limits and quotas per tenant: {{pending: limits}}
- Resource isolation for heavy tenants: {{pending: strategy}}

## Lifecycle

- Onboarding: {{pending: steps to provision a tenant}}
- Offboarding and data deletion: {{pending: export, retention and deletion steps}}
- Data residency needs: {{pending: whether tenants require specific locations}}

## Verification

- Isolation tests that try to access another tenant's data must exist in the [test plan](../11-quality/test-plan.md): {{pending: test IDs}}.

## Related

- [Security architecture](security-architecture.md)
- [Container diagram](container-diagram.md)
- [Performance architecture](performance-architecture.md)
- [Architecture decisions](adr/README.md)
- [Test plan](../11-quality/test-plan.md)
