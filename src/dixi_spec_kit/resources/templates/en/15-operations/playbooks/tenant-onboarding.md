# Tenant onboarding

## Purpose

Create a new tenant (customer organisation) in a multi-tenant platform in a repeatable way, with isolation, configuration and monitoring in place from day one, and remove it cleanly when it leaves.

Status: draft. {{pending: name the owner of this playbook}}

## Two paths

| Path | When | Who runs it |
|------|------|-------------|
| Self-service | Standard plans, signup flow | The product, automatically |
| Assisted | Custom contracts, data migration, dedicated resources | Operations with the account owner |

{{pending: decide which plans use which path}}

## Before creating the tenant

- Signed agreement or accepted terms, and the plan recorded.
- Data residency requirement known. {{pending: list allowed regions}}
- A named contact on the customer side, using an address such as `admin@example.com` in examples.
- Isolation model confirmed: shared, schema per tenant or dedicated. {{pending: choose the default isolation model}}

## Steps (assisted path)

1. Create the tenant record with a unique, immutable tenant ID.
2. Provision resources according to the isolation model, using the reviewed script or pipeline, not manual console clicks.
3. Apply plan limits: users, storage, rate limits, AI usage quotas.
4. Configure identity: first admin user, single sign-on if contracted.
5. Load initial data if agreed, after validating format and consent.
6. Tag every resource with the tenant ID so cost can be allocated.
7. Enable monitoring: per-tenant error rate and usage dashboards.
8. Send the welcome message with access instructions and support channels.

An AI agent may prepare the configuration and check it against this list; a person runs steps 2 to 5 in production.

## Close criteria

- Tenant admin signed in successfully.
- Isolation tested: a test user of another tenant cannot see this tenant's data.
- Usage and cost appear under the tenant ID.

## Offboarding

1. Confirm the end date and the data export the customer needs.
2. Provide the export and get confirmation.
3. Disable access, then delete or anonymise data after {{pending: retention period}}.
4. Remove resources and tags; keep only what the law or contract requires.

## Related

- [Service catalog](../service-catalog.md)
- [Support model](../support-model.md)
- [Cost allocation model](../../22-finops/cost-allocation-model.md)
- [SLA matrix](../vendor-management/sla-matrix.md)
