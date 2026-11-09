# Analytics events catalog

## Purpose

Keep a single list of the product events the project records, what each one means and which data it carries, so that metrics are trustworthy, privacy is respected and nobody invents a duplicate event.

Status: draft. {{pending: choose the analytics tool or storage and the person who approves new events}}

## Naming convention

- Format: `object_action` in lowercase with underscores, past tense, for example `report_exported`.
- One event per meaningful user action or system outcome; avoid events for every click.
- Properties use lowercase with underscores and stable value sets.
- Event names and property keys never change meaning; a new meaning needs a new event.

{{pending: confirm the naming format if the chosen tool imposes another}}

## Privacy rules

- Do not put personal data (names, e-mails, free text, precise location) in event properties.
- Use a pseudonymous identifier; classify every property against the PII classification.
- Respect the user's consent choice before sending any non-essential event.
- State the retention period for raw events.

{{pending: decide the consent model and retention period for analytics data}}

## Standard properties

Sent with every event when available:

| Property | Type | Example | Notes |
|----------|------|---------|-------|
| `event_version` | integer | `1` | Increments when properties change |
| `locale` | string | `es-MX` | Interface language and region |
| `platform` | string | `web` | {{pending: allowed values}} |
| `app_version` | string | `1.4.0` | Product release |

## Event list

| Event | Trigger | Properties | Owner | Feature | Status |
|-------|---------|------------|-------|---------|--------|
| `account_created` | User finishes sign-up | `method` | {{pending}} | {{pending: feature ID}} | Proposed |
| `onboarding_completed` | Last setup step done | `steps_skipped` | {{pending}} | {{pending}} | Proposed |
| `report_exported` | Export succeeds | `format` | {{pending}} | {{pending}} | Proposed |

Status values: Proposed, Implemented, Deprecated, Removed.

## Adding an event

1. Check this catalog for an existing event that already answers the question.
2. Write the question the event answers and the metric it feeds.
3. Classify every property for personal data.
4. Add the row with status Proposed and get approval.
5. Implement it with a test that asserts the event and its properties.
6. Change status to Implemented once released.

## Quality checks

- Events in code that are not in this catalog are defects.
- Events in this catalog that are not sent for a whole review period are investigated.

## Related

- [Feature lifecycle](feature-lifecycle.md)
- [Prioritization framework](prioritization-framework.md)
- [PII classification](../08-data/pii-classification.md)
- [Retention policy](../08-data/retention-policy.md)
- [Example feature spec](../05-features/example/feature-spec.md)
