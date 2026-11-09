# External partners

## Purpose

Identify the organizations and systems outside the team that the product depends on or serves:
suppliers, integrators, resellers, regulators or data providers. For each one, record what is
exchanged, who owns the relationship and what happens if the partner becomes unavailable. Use
generic labels until a partner is contractually confirmed.

## Partner catalog

| ID | Partner type | What they provide or receive | Criticality | Relationship owner |
|---|---|---|---|---|
| EXT-001 | {{pending: e.g. payment processor}} | {{pending: exchange}} | {{pending: high, medium or low}} | {{pending: role}} |
| EXT-002 | {{pending: e.g. messaging provider}} | {{pending: exchange}} | {{pending: high, medium or low}} | {{pending: role}} |

Choosing a concrete provider is a project decision: record it in an ADR, not here.

## Integration points

| Partner | Direction | Channel | Contract |
|---|---|---|---|
| {{pending: partner ID}} | {{pending: inbound, outbound or both}} | {{pending: API, file, webhook, manual}} | {{pending: link to the contract in 07-contracts/external}} |

## Dependency risks

For each critical partner, answer:

- What fails for users if the partner is down? {{pending: impact}}
- Is there a fallback or degraded mode? {{pending: fallback}}
- Which data do we share and under which agreement? {{pending: data and agreement}}
- How do we leave the partner if needed? {{pending: exit plan}}

## Obligations

- Service levels we depend on: {{pending: availability, response time, support hours}}
- Service levels we offer to partners: {{pending: commitments, if any}}

## Related

- [Internal roles](internal-roles.md)
- [External integration template](../../10-engineering/templates/external-integration-template.md)
- [External contracts](../../07-contracts/external/README.md)
- [Integration architecture](../../09-architecture/integration-architecture.md)
