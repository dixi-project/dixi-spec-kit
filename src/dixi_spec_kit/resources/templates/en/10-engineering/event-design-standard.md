# Event design standard

## Purpose

Make asynchronous events of the platform consistent, versioned and safe to consume, so producers
and consumers can evolve independently.

Messaging technology: {{pending: broker or event bus chosen, recorded in an ADR}}

## Naming

- Events describe **facts in the past**: `order.created`, `payment.failed`.
- Format: `<domain>.<entity>.<past_verb>` or `<entity>.<past_verb>`.
  {{pending: naming convention and registry location}}
- Commands (requests to do something) are not events and use a different channel.

## Envelope

Every event uses the same envelope, as in [the event template](templates/event-template.json):

| Field | Description |
|---|---|
| `id` | Unique ID of this event, used for deduplication |
| `type` | Event name |
| `version` | Schema version of `data` |
| `occurred_at` | When the fact happened, UTC ISO 8601 |
| `source` | Producing service |
| `correlation_id` | Propagated from the request that caused it |
| `data` | Payload, described by a versioned schema |

## Rules

1. **Schema per event and version**, stored in the repository and validated by producer and
   consumer tests.
2. **Additive evolution.** New optional fields keep the version; removing or changing a field
   creates a new version, and producers publish both during the migration window.
3. **At-least-once delivery is the default.** Consumers are idempotent: they deduplicate by `id`
   or make the effect naturally idempotent.
4. **No ordering assumptions** unless the channel guarantees it per key and the key is documented.
5. **Minimal payloads.** Include what consumers need to act; do not leak personal data that is
   not required. {{pending: personal data allowed in events}}
6. **Failures go to a dead-letter destination** after bounded retries, with an alert and a
   runbook to replay.
7. **Outbox or equivalent** when an event must be published together with a state change, so the
   two cannot diverge. {{pending: consistency mechanism}}
8. **Every event has an owner** (producing module) and a list of known consumers.

## Review checklist

- [ ] Name is a past-tense fact; envelope fields are complete.
- [ ] Schema and version are committed; compatibility is tested.
- [ ] Consumers are idempotent and have a dead-letter path.
- [ ] Event is listed in the producing module's spec.

## Related

- [Event template](templates/event-template.json)
- [Error handling standard](error-handling-standard.md)
- [Flow template](templates/flow-template.md)
- [Runbook template](templates/runbook-template.md)
