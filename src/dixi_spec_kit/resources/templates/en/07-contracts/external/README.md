# External contracts

## Purpose

Document the contracts with systems the project does not control: third-party APIs, partner
webhooks, file exchanges and public data sources. External contracts change on someone else's
schedule, so record exactly what the project relies on, how it is isolated and what happens when
the other side fails or changes.

## Layout

```text
07-contracts/external/
  <partner-or-system>.md        One file per external system
  <partner-or-system>/          Optional: copies of schemas or samples, without secrets
```

Start each file from the [external integration template](../../10-engineering/templates/external-integration-template.md).
Use generic names until the provider is chosen in an ADR.

## What every external contract must record

- The capability needed and the feature IDs that depend on it.
- The subset of the external interface actually used (operations, fields, events).
- Authentication method and where credentials live (never the credentials themselves).
- Limits: rate limits, quotas, payload sizes, availability commitments.
- Timeouts, retries, circuit breaking and the degraded behavior for users.
- Data shared with the external party, flagged for personal data and agreements.
- How the integration is isolated (an adapter or anti-corruption layer) so it can be replaced.
- How it is tested without calling the real system (stubs, recorded samples, sandbox).

## Integration index

| System | Capability | Direction | Criticality | Adapter owner | Status |
|---|---|---|---|---|---|
| {{pending: generic system name}} | {{pending: capability}} | {{pending: inbound, outbound or both}} | {{pending: criticality}} | {{pending: role}} | {{pending: status}} |

## Change monitoring

- How the team learns about changes on the external side: {{pending: changelog, notices, contact}}
- Who reviews deprecation notices: {{pending: role}}

## Related

- [External integration template](../../10-engineering/templates/external-integration-template.md)
- [Integration architecture](../../09-architecture/integration-architecture.md)
- [External partners](../../01-business/actors/external-partners.md)
- [Schemas](../schemas/README.md)
