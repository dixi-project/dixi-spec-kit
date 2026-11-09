# Sample data catalog

## Purpose

List the canonical synthetic datasets the project uses, what each one contains, which states it covers and where it is used. Everyone uses the same named records, so tests, demos and bug reports can refer to them without ambiguity.

Status: draft. {{pending: confirm the first datasets based on the domain model}}

## Datasets

| Dataset | Purpose | Records | States covered | Languages | Used by |
|---------|---------|---------|----------------|-----------|---------|
| Users | Accounts with different roles | {{pending}} | Active, invited, suspended, deleted | ES, EN | Tests, seed, demo |
| Organisations | Tenants or customer accounts, if applicable | {{pending}} | Trial, active, cancelled | ES, EN | Tests, seed, demo |
| Plans | Product plans or tiers, if applicable | {{pending}} | Current and retired | ES, EN | Tests, seed |
| {{pending: core domain entity}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |
| Support requests | Requests of every severity | {{pending}} | Open, waiting, resolved | ES, EN | Demo |

## Named records

Give a few records stable names and documented traits, so people can say "log in as the admin of the trial organisation".

| Key | Description | Language | Example contact |
|-----|-------------|----------|-----------------|
| `user.admin` | Administrator with full permissions | EN | `admin.demo@example.com` |
| `user.member_es` | Regular member using Spanish | ES | `miembro.demo@example.com` |
| `user.suspended` | Suspended account to test access rules | EN | `suspended.demo@example.com` |
| `org.trial` | Organisation on a trial | {{pending}} | n/a |

Passwords or tokens for these accounts are generated per environment and never written in this catalog.

## Schema and format

- Each dataset has a documented schema aligned with the canonical data model.
- {{pending: choose the file format for fixtures and where schemas live}}
- Every record includes the audit fields required by the data standards, with synthetic values.

## Edge cases to include

- Empty and maximum-length fields.
- Characters with accents, symbols and mixed scripts.
- Dates near boundaries: end of month, leap day, time zone changes.
- Amounts in several currencies and with zero or negative values where valid.
- Records in each lifecycle state, including deleted or archived.

## Ownership

| Dataset | Owner | Last reviewed |
|---------|-------|---------------|
| {{pending}} | {{pending}} | {{pending}} |

## Related

- [Fixtures strategy](fixtures-strategy.md)
- [Demo scenarios](demo-scenarios.md)
- [PII classification](../08-data/pii-classification.md)
- [Personas](../01-business/actors/personas.md)
- [Test plan](../11-quality/test-plan.md)
