# Logging standard

## Purpose

Give the project a single logging convention so that any event can be found, correlated across
services and read by people and tools without exposing sensitive data.

## Format

1. **Structured logs**, one event per line, in a machine-readable format.
   {{pending: log format, e.g. JSON lines}}
2. **Mandatory fields** on every event:

| Field | Description |
|---|---|
| `timestamp` | UTC, ISO 8601 with milliseconds |
| `level` | `debug`, `info`, `warning`, `error` |
| `service` | Name of the emitting component |
| `environment` | e.g. `dev`, `staging`, `prod` |
| `message` | Short, constant text describing the event |
| `correlation_id` | Propagated across calls, queues and jobs |
| `tenant_id` | When the system is multi-tenant; omit otherwise |

3. **Context in fields, not in the message.** Write `message="order created"` with
   `order_id=...`, not an interpolated sentence. Constant messages are searchable.

## Levels

- `error`: requires action by someone; usually linked to an alert.
- `warning`: unexpected but handled; worth reviewing.
- `info`: a business or lifecycle event happened (request served, job finished).
- `debug`: diagnostic detail; disabled in production by default.

## What is never logged

- Secrets, tokens, passwords, session cookies, API keys, private keys.
- Personal data without masking (names, e-mails, phone numbers, document IDs, addresses).
- Full request or response bodies of sensitive endpoints.
- Payment data.

Masking rule: {{pending: masking or hashing rule for identifiers that must remain correlatable}}

## Retention and access

- Retention: {{pending: retention period per environment and legal requirement}}
- Access: {{pending: roles allowed to read production logs}}
- Logs are not a database: business facts that must be queried belong in storage or events.

## Errors

Log each error once, at the boundary, with its code and correlation ID, as described in
[the error handling standard](error-handling-standard.md).

## Related

- [Error handling standard](error-handling-standard.md)
- [Secure coding standard](secure-coding-standard.md)
- [Coding standards](coding-standards.md)
- [Runbook template](templates/runbook-template.md)
