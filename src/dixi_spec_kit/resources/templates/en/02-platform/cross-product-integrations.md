# Cross-product integrations

## Purpose

Document every integration between products on the platform: what triggers it, which contract it
uses, who owns each side and how failures are handled. Integrations are where independent products
become coupled; making them explicit keeps that coupling deliberate and testable.

## Integration catalog

| ID | Producer | Consumer | Style | Trigger | Contract | Owner |
|---|---|---|---|---|---|---|
| INT-001 | {{pending: product}} | {{pending: product}} | {{pending: sync API, event, command or file}} | {{pending: business trigger}} | {{pending: path in 07-contracts}} | {{pending: role}} |
| INT-002 | {{pending: product}} | {{pending: product}} | {{pending: style}} | {{pending: trigger}} | {{pending: contract}} | {{pending: role}} |

## Choosing a style

| Style | Use when | Watch out for |
|---|---|---|
| Synchronous API | The caller needs an immediate answer | Cascading failures, latency budgets |
| Event | Others react to a fact; producer does not wait | Ordering, duplicates, eventual consistency |
| Command | One specific consumer must perform an action | Retries and idempotency |
| File or batch | Large volumes on a schedule | Partial failures, reprocessing |

## Per-integration detail (copy per integration)

### INT-001 — {{pending: name}}

- Business reason: {{pending: why the products need to talk}}
- Data exchanged: {{pending: entities and fields, with PII flagged}}
- Consistency expected: {{pending: immediate or eventual, and acceptable delay}}
- Failure behavior: {{pending: retry, dead letter, compensation, user message}}
- Idempotency: {{pending: key used to detect duplicates}}
- Tenant propagation: {{pending: how tenant and identity travel with the message}}
- Contract tests: {{pending: where they live and who runs them}}

## Rules

- No product reads another product's storage directly.
- Every integration has a contract and a contract test on the consumer side.
- Changing a contract follows its versioning policy and notifies all consumers.

## Related

- [Product map](product-map.md)
- [Shared services map](shared-services-map.md)
- [Event contracts](../07-contracts/events/README.md)
- [Command contracts](../07-contracts/commands/README.md)
- [Contract testing guide](../11-quality/contract-testing-guide.md)
