# Cost allocation model

## Purpose

Attribute every cost to a product, service, environment and, where relevant, a tenant, so that unit costs are known and decisions about pricing and optimisation rest on data.

Status: draft. {{pending: name the owner of the allocation model}}

## Tagging scheme

Every resource that can be tagged must carry these keys:

| Key | Example value | Required |
|-----|---------------|----------|
| `project` | {{pending: project short name}} | Yes |
| `environment` | `prod`, `staging`, `dev` | Yes |
| `service` | {{pending: service name from the service catalog}} | Yes |
| `owner` | {{pending: team or role}} | Yes |
| `tenant` | {{pending: tenant ID, when dedicated}} | When applicable |
| `cost-center` | {{pending: finance code}} | {{pending: yes / no}} |

Use lowercase keys and values from a fixed list. Untagged resources are reported every {{pending: frequency}} and fixed or removed.

## Account and environment separation

{{pending: decide whether environments live in separate accounts or projects, or only separated by tags}}

Separate accounts per environment make allocation and access control simpler; tags alone are easier to start but leak more.

## Shared costs

Some costs cannot be tagged (support plans, shared networking, observability). Allocate them by a documented rule:

| Shared cost | Allocation rule |
|-------------|-----------------|
| {{pending: e.g. shared cluster}} | {{pending: e.g. by CPU requested per service}} |
| {{pending: e.g. monitoring}} | {{pending: e.g. evenly per service}} |

## Unit costs

| Unit | Formula | Target |
|------|---------|--------|
| Cost per active user | Production cost / monthly active users | {{pending: target}} |
| Cost per tenant | Dedicated cost + share of shared cost | {{pending: target}} |
| Cost per feature | Cost of its services and AI usage | {{pending: target}} |

## Showback and chargeback

- **Showback**: each team or tenant sees its cost; no money moves. Recommended first step.
- **Chargeback**: cost is billed internally or to the customer. {{pending: decide if and when to move to chargeback}}

## Reporting

Monthly allocation results feed the cost report. Keep the queries or scripts that produce them in the repository so the numbers can be reproduced.

## Related

- [Cost strategy](cost-strategy.md)
- [Cloud cost optimisation](cloud-cost-optimization.md)
- [Cost report template](templates/cost-report-template.md)
- [Tenant onboarding](../15-operations/playbooks/tenant-onboarding.md)
- [Service catalog](../15-operations/service-catalog.md)
