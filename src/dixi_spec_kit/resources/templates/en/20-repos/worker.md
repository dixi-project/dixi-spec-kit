# Worker

## Purpose

Describe the expected structure and conventions of a background worker repository: a process that consumes messages or scheduled jobs and does work outside the request path. This guide does not choose a language or a messaging technology.

Status: draft. {{pending: choose the language, runtime and messaging or scheduling technology for workers}}

## Stack decisions

| Decision | Choice | ADR |
|----------|--------|-----|
| Language and runtime | {{pending}} | {{pending}} |
| Message broker or queue | {{pending}} | {{pending}} |
| Scheduler for periodic jobs | {{pending}} | {{pending}} |
| Test runner | {{pending}} | {{pending}} |

## Suggested folder layout

```text
<worker>/
├── README.md          # purpose, consumed and produced events, spec IDs
├── AGENTS.md
├── src/
│   ├── consumers/     # one handler per message type
│   ├── jobs/          # scheduled tasks
│   ├── domain/        # business rules shared with no transport code
│   └── adapters/      # broker, storage, external services
├── tests/
│   ├── unit/
│   └── integration/
└── .env.example
```

## Conventions

- Every handler is idempotent: processing the same message twice has the same effect as once.
- Messages follow the event contracts; a schema change is versioned and backwards compatible.
- Retries use backoff and a limit; messages that keep failing go to a dead-letter destination.
- Each message carries a correlation ID that reaches the logs and any produced messages.
- Long jobs report progress and can be stopped safely.
- Concurrency limits are explicit and documented.

## Operations

| Item | Value |
|------|-------|
| Messages consumed | {{pending}} |
| Messages produced | {{pending}} |
| Maximum retries | {{pending}} |
| Dead-letter handling owner | {{pending}} |
| Alert on queue depth | {{pending}} |

## Verification

- Tests cover the happy path, duplicates, malformed messages and retry exhaustion.
- `make verify` runs the worker's real checks.

## Related

- [Repositories](README.md)
- [Backend service](backend-service.md)
- [Alerting rules](../12-observability/alerting-rules.md)
- [Coding standards](../10-engineering/coding-standards.md)
- [Restore service playbook](../15-operations/playbooks/restore-service.md)
