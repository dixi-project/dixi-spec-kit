# Integration governance

## Purpose

Set the rules for every integration between this platform's services and with external systems, so that each integration has an owner, a contract, a security review and a known failure behaviour.

Status: draft. {{pending: name the integration governance owner}}

## Rules

1. Every integration has a written contract before it is built.
2. Contracts are versioned; breaking changes follow a deprecation period.
3. Each integration has a named owner on both sides.
4. Credentials are per integration and per environment, with least privilege.
5. Every call has a timeout, a retry policy and a defined behaviour when the other side is down.
6. External data is validated at the boundary and treated as untrusted.
7. Integrations are observable: rate, errors, latency and correlation IDs.

## Integration register

| ID | Consumer | Provider | Style | Contract | Owner | Criticality |
|----|----------|----------|-------|----------|-------|-------------|
| INT-001 | {{pending: consumer}} | {{pending: provider}} | {{pending: sync API / event / file}} | [Contract](../07-contracts/example.md) | {{pending: owner}} | {{pending: level}} |

## Choosing a style

| Need | Prefer |
|------|--------|
| Immediate answer required | Synchronous request |
| Decoupled reaction to a fact | Event |
| Large batch transfer | File or bulk transfer |

{{pending: default integration style for this platform}}

## Approval checklist for a new integration

- [ ] Contract written and reviewed.
- [ ] Data classification of exchanged fields known.
- [ ] Threat model updated.
- [ ] Failure behaviour and fallback defined.
- [ ] Contract tests planned on both sides.
- [ ] Owner and support contact recorded.

## Deprecation

- Announce at least {{pending: notice period}} before removing a version.
- Track consumers of each version before removal.

## Related

- [Integration architecture](../09-architecture/integration-architecture.md)
- [Contract testing guide](../11-quality/contract-testing-guide.md)
- [API design standard](../10-engineering/api-design-standard.md)
- [Event design standard](../10-engineering/event-design-standard.md)
- [Observability standard](observability-standard.md)
