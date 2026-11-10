# Environments

## Purpose

List the environments the project uses, what each one is for, what data it holds and how a change moves between them. Fewer environments that are kept faithful beat many that drift.

## Environment catalog

| Environment | Purpose | Data | Access | Deploys | Lifetime |
|---|---|---|---|---|---|
| local | Development and fast feedback | Synthetic fixtures | Developer | Developer | Ephemeral |
| preview | {{pending: per pull request, optional}} | Synthetic | Team | Automatic on pull request | Deleted on merge |
| staging | Pre-release validation, as close to production as practical | {{pending: synthetic or anonymised}} | Team | {{pending: automatic after merge or manual}} | Permanent |
| production | Real users | Real | {{pending: restricted roles}} | After human approval | Permanent |

## Parity rules

- Same artifact, same configuration keys, different values per environment.
- Differences from production in staging are listed here with the reason: {{pending: list known differences}}.
- Production data never goes to non-production environments unless it is irreversibly anonymised and the decision is recorded.

## Configuration

| Setting | local | staging | production |
|---|---|---|---|
| Log level | debug | info | info |
| External integrations | Stubs | {{pending: sandbox or stubs}} | Real |
| Outgoing e-mail | Captured locally | {{pending: captured or allow-listed}} | Real |
| Feature flags | All on | {{pending: per flag}} | {{pending: per flag}} |

Test e-mail addresses use the `@example.com` domain.

## Access and isolation

- Credentials are separate per environment; a staging credential never works in production.
- Who has write access to production: {{pending: roles}}
- How access is reviewed: {{pending: frequency and owner}}

## Promotion

A change reaches production only after passing through staging with the same commit identifier and an explicit human approval.

## Related

- [CI/CD overview](ci-cd-overview.md)
- [Deployment strategy](deployment-strategy.md)
- [Deployment architecture](../09-architecture/deployment-architecture.md)
- [Secret management](../13-security/secret-management.md)
