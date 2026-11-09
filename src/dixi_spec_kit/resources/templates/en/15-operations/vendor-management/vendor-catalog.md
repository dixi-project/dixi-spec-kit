# Vendor catalog

## Purpose

Keep one list of the external services the project depends on, what data they receive, who owns the relationship and how critical they are.

Status: draft. {{pending: name the owner of the catalog}}

## Catalog

| Vendor | Category | Used for | Data shared | Criticality | Owner | Contract or plan | Renewal | Exit plan |
|--------|----------|----------|-------------|-------------|-------|------------------|---------|-----------|
| {{pending: vendor name}} | {{pending: e.g. hosting, e-mail, payments, AI model, analytics}} | {{pending: purpose}} | {{pending: none / metadata / personal data}} | {{pending: critical / high / normal}} | {{pending: role}} | {{pending: plan}} | {{pending: date}} | {{pending: yes / no / link}} |

Record facts, not opinions. Do not store contracts, credentials or account numbers here; link to where they are kept.

## Categories

{{pending: adjust the category list to the project}}

- Hosting and infrastructure
- Data storage and backups
- Identity and authentication
- Payments and billing
- Messaging (e-mail, SMS, push)
- AI models and APIs
- Monitoring and logging
- Developer tooling

## Criticality

| Level | Meaning |
|-------|---------|
| Critical | Its failure stops a critical service |
| High | Its failure degrades the product, a workaround exists |
| Normal | Internal or easily replaceable |

## Adding a vendor

1. Check whether an existing vendor already covers the need.
2. Record the row above before production use.
3. Confirm what data it receives and whether a data processing agreement is needed.
4. For critical vendors, write an exit plan: how to export data and what could replace it.

## Review

Review every {{pending: frequency}}: still used, owner still correct, renewal date, price changes.

## Related

- [Service catalog](../service-catalog.md)
- [RACI matrix](../team/raci-matrix.md)
- [Cost strategy](../../22-finops/cost-strategy.md)
