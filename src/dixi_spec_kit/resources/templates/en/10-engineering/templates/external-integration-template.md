# External integration template

## Purpose

Document a dependency on a system the project does not control (payment, messaging, identity,
data provider, etc.): what is used, how it fails and how it is protected. Copy the structure below
for each integration.

## Template

```markdown
# Integration: <system name>

ID: {{pending: integration ID}}
Owner: {{pending: person responsible for the relationship}}
Status: evaluating | active | deprecated

## Purpose

What the project uses this system for and which features depend on it.

## Interface

- Protocol and contract: (API, webhook, file exchange, SDK)
- Contract or documentation version used:
- Environments available (sandbox, production):

## Authentication and secrets

- Method: {{pending: authentication method}}
- Secrets live in the secret store; names only, never values.
- Rotation: {{pending: rotation period and procedure}}

## Data exchanged

| Direction | Data | Personal data? | Legal basis or agreement |
|---|---|---|---|

## Limits and costs

- Rate limits and quotas:
- Pricing model and budget alert:

## Failure behavior

| Failure | Detection | Our behavior |
|---|---|---|
| Timeout | | retry with backoff, then ... |
| Error response | | |
| Unavailable for hours | | degraded mode: ... |

## Isolation

The integration is wrapped in an adapter inside the owning module; the domain does not
depend on its SDK or data shapes.

## Tests

- Contract tests against recorded responses or a sandbox.
- Failure tests for each row of the table above.

## Exit plan

How to replace this system and what would be lost.
```

## Related

- [Module template](module-template.md)
- [Error handling standard](../error-handling-standard.md)
- [Secure coding standard](../secure-coding-standard.md)
- [Runbook template](runbook-template.md)
