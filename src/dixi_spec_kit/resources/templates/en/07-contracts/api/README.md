# API contracts

## Purpose

Store the contracts of the synchronous APIs that the project exposes or consumes. A contract is the
agreement between producer and consumer: endpoints, inputs, outputs, errors, authentication and
versioning. Write the contract before the implementation, review it with the consumers and derive
contract tests from it, so that both sides can evolve independently.

## Layout

```text
07-contracts/api/
  <service>-api.yaml      Machine-readable contract (for example, OpenAPI)
  <service>-api.md        Optional human notes: scope, decisions, examples
```

- Start from the [API template](../../10-engineering/templates/api-template.yaml).
- Follow the [API design standard](../../10-engineering/api-design-standard.md).
- Use `/dixi.contract` (or `$dixi-contract`) to draft a contract from a feature spec.

## What every contract must define

- Base path, version and the feature IDs it serves.
- Each operation: method, path, parameters, request body, responses and error codes.
- Authentication and the permissions required per operation.
- Tenant context, if the platform is multi-tenant.
- Pagination, filtering and sorting conventions for collections.
- Idempotency for operations that create or change state.
- Examples for success and for the most common errors.

## Contract index

| ID | Contract | Producer | Consumers | Version | Status |
|---|---|---|---|---|---|
| CONTRACT-001 | [Example](../example.md) | {{pending: producer}} | {{pending: consumers}} | {{pending: version}} | draft |
| {{pending: CONTRACT ID}} | {{pending: file}} | {{pending: producer}} | {{pending: consumers}} | {{pending: version}} | {{pending: status}} |

Register each contract in `.dixi/traceability.json` with `kind: contract` and the feature as
parent, then run `dixi check`.

## Versioning and change

- Versioning scheme: {{pending: path, header or media type}}
- Additive changes (new optional fields, new operations) keep the version.
- Breaking changes create a new version and a deprecation period of {{pending: duration}}.

## Related

- [Contract example](../example.md)
- [API design standard](../../10-engineering/api-design-standard.md)
- [Schemas](../schemas/README.md)
- [Error handling standard](../../10-engineering/error-handling-standard.md)
