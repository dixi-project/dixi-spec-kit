# Logging Map

## Purpose

Show which component writes which logs, in what format, where they go and how long they are kept. The coding rules for writing a log line live in the logging standard; this map covers the operational side.

## Format

- Structured, one JSON object per line, written to standard output unless decided otherwise.
- Required fields: `timestamp` (UTC, ISO 8601), `level`, `service.name`, `service.version`, `deployment.environment`, `message`, and a correlation or trace identifier.
- Optional fields: `event` (a stable name), `duration_ms`, `error.type`.

## Levels

| Level | Use | Enabled in production |
|---|---|---|
| error | A request or job failed and needs attention | Yes |
| warn | Unexpected but handled; may need attention if repeated | Yes |
| info | Business-relevant events and lifecycle | Yes |
| debug | Diagnostic detail | {{pending: only on demand, for a limited time}} |

## Map

| Component | Log stream | Key events | Destination | Retention | Contains personal data |
|---|---|---|---|---|---|
| Web or API | {{pending: name}} | request completed, auth failure | {{pending: destination}} | {{pending: days}} | No (masked) |
| Workers | {{pending: name}} | job started, job failed, retry | {{pending: destination}} | {{pending: days}} | No (masked) |
| Audit | {{pending: name}} | privileged action, permission change | {{pending: destination}} | {{pending: per retention policy}} | {{pending: yes or no}} |

## Never log

- Passwords, tokens, API keys, session cookies or full authorization headers.
- Payment data, full identity documents or health data.
- Full request bodies by default; log identifiers instead.

## Access

- Who can read production logs: {{pending: roles}}
- How access is granted and reviewed: {{pending: process}}
- Audit logs are append-only and separated from application logs.

## Related

- [Logging standard](../10-engineering/logging-standard.md)
- [Observability strategy](observability-strategy.md)
- [Data retention policy](../08-data/retention-policy.md)
- [PII classification](../08-data/pii-classification.md)
