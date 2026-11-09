# Command contracts

## Purpose

Store the contracts of the commands that one module sends to another to ask for an action ("issue
invoice"). Unlike an event, a command has exactly one intended handler and may be rejected. The
contract defines what is requested, who may request it, what the handler validates and how the
sender learns the outcome.

## Commands versus events

| Aspect | Command | Event |
|---|---|---|
| Meaning | A request to do something | A fact that already happened |
| Tense | Imperative: `IssueInvoice` | Past: `InvoiceIssued` |
| Handlers | Exactly one | Zero or many |
| Can be rejected | Yes | No, it already happened |

## Layout

```text
07-contracts/commands/
  <domain>.<action>.v<N>.json    One contract per command and major version
```

## What every command contract must define

- Name, version, handling module, allowed senders and the feature IDs that need it.
- Payload with required and optional fields, reusing shared schemas.
- Validation rules and the business rules (`BR-NNN`) the handler enforces.
- Idempotency key, so that a retried command is not executed twice.
- Outcomes: accepted, rejected with reason codes, or failed; and how the sender is told
  (synchronous reply, result event, or status query).
- Authorization: which identity and tenant context must accompany the command.
- Timeout expected by the sender and the behavior after it.

## Command index

| Command | Version | Handler | Senders | Result channel | Status |
|---|---|---|---|---|---|
| {{pending: command name}} | {{pending: version}} | {{pending: module}} | {{pending: modules}} | {{pending: reply or event}} | {{pending: status}} |

## Versioning

- Same rules as events: additive changes keep the version, breaking changes create a new one.
- The handler accepts the previous version for {{pending: duration}} after a new one is published.

## Related

- [Event contracts](../events/README.md)
- [Event design standard](../../10-engineering/event-design-standard.md)
- [Schemas](../schemas/README.md)
- [Business rules](../../01-business/rules/business-rules.md)
