# Event contracts

## Purpose

Store the contracts of the events that modules and products publish. An event states a fact that
already happened ("order placed"); the producer does not know or wait for its consumers. Because
consumers are decoupled, the event contract is the only thing that keeps them aligned: name,
payload, ordering guarantees and versioning must be explicit.

## Layout

```text
07-contracts/events/
  <domain>.<entity>.<fact>.v<N>.json    One contract per event and major version
```

- Start from the [event template](../../10-engineering/templates/event-template.json).
- Follow the [event design standard](../../10-engineering/event-design-standard.md).
- Name events in the past tense using the ubiquitous language, e.g. `billing.invoice.issued`.

## What every event contract must define

- Name, version, producing module and the feature IDs that justify it.
- Envelope: event ID, type, occurrence time, producer, tenant, correlation ID.
- Payload: only the data consumers need; prefer IDs over copies of large objects.
- Personal data in the payload, flagged and minimized.
- Delivery guarantee assumed: {{pending: at least once, at most once}}.
- Ordering guarantee and the key it applies to, if any.
- Known consumers and what each does with the event.

## Consumer rules

- Consumers are idempotent: processing the same event twice has no extra effect.
- Consumers tolerate unknown fields and events that arrive out of order.
- Failed events go to a retry path and then to a dead-letter area that someone monitors.

## Event index

| Event | Version | Producer | Consumers | Status |
|---|---|---|---|---|
| {{pending: event name}} | {{pending: version}} | {{pending: module}} | {{pending: modules}} | {{pending: draft or published}} |

## Versioning

- Adding optional fields keeps the version; removing or changing meaning creates a new one.
- Old and new versions are published in parallel for {{pending: duration}}.

## Related

- [Commands](../commands/README.md)
- [Event design standard](../../10-engineering/event-design-standard.md)
- [Event architecture](../../09-architecture/event-architecture.md)
- [Schemas](../schemas/README.md)
