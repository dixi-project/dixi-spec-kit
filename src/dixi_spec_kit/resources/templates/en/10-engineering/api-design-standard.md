# API design standard

## Purpose

Make every API of the project consistent, contract-first and safe to evolve, so clients can rely
on it and changes do not break them silently.

API style: {{pending: REST over HTTP, RPC, GraphQL or other, recorded in an ADR}}

## Contract first

1. The contract is written and reviewed **before** the implementation, using
   [the API template](templates/api-template.yaml) or the format chosen for the project.
2. The contract lives in the repository and is the source for client types, mocks and contract
   tests. Implementation and contract are checked against each other in `make verify`.
3. Every operation traces to a feature or contract ID.

## Conventions

| Topic | Rule |
|---|---|
| Resources | Plural nouns in paths (`/orders/{order_id}`); verbs only for actions that are not CRUD |
| Naming | {{pending: case for JSON fields, e.g. snake_case or camelCase}}, used consistently |
| Methods | `GET` safe, `PUT`/`DELETE` idempotent, `POST` creates or triggers actions |
| Status codes | Follow [the error handling standard](error-handling-standard.md) |
| Dates | ISO 8601 in UTC |
| Money | Integer minor units plus currency code |
| Identifiers | Opaque strings; never expose sequential internal IDs |
| Pagination | {{pending: cursor-based or offset-based; default and maximum page size}} |
| Filtering and sorting | Explicit, documented query parameters; reject unknown ones |
| Languages | Visible texts negotiated with `Accept-Language`; codes stay language-neutral |

## Versioning and change

1. {{pending: versioning strategy, e.g. major version in the path or in a header}}
2. **Additive changes** (new optional field, new endpoint) do not need a new version.
3. **Breaking changes** (removed or renamed field, changed type or meaning, new required input)
   need a new version, a deprecation notice and a migration window.
4. Deprecated operations announce their removal date. {{pending: minimum deprecation window}}

## Security

- Authentication on every non-public operation. {{pending: authentication scheme}}
- Authorization checked per resource, not only per route.
- Input validated against the contract schema; unknown fields rejected.
- Rate limits documented per client type; responses include the retry delay.
- Idempotency keys for operations that create resources or move money.

## Review checklist

- [ ] Contract updated and reviewed before code.
- [ ] Every error response uses the shared error shape.
- [ ] Breaking changes have a new version and a deprecation plan.
- [ ] Contract tests cover success and each documented error.

## Related

- [API template](templates/api-template.yaml)
- [Error handling standard](error-handling-standard.md)
- [Secure coding standard](secure-coding-standard.md)
- [Draft contract](../07-contracts/example.md)
