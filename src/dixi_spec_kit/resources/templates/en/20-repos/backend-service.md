# Backend service

## Purpose

Describe the expected structure and conventions of a backend service repository: the piece that exposes an API, owns business rules and persists data. This guide does not create code or choose a language; it defines what every backend repository must contain so that it stays aligned with the specs.

Status: draft. {{pending: choose the language, framework and runtime for backend services}}

## Stack decisions

| Decision | Choice | ADR |
|----------|--------|-----|
| Language and runtime | {{pending}} | {{pending}} |
| Web framework | {{pending}} | {{pending}} |
| Persistence and migrations tool | {{pending}} | {{pending}} |
| Test runner | {{pending}} | {{pending}} |
| API description format | {{pending}} | {{pending}} |

## Suggested folder layout

```text
<service>/
├── README.md          # purpose, local run, implemented spec IDs
├── AGENTS.md          # agent rules for this repository
├── src/
│   ├── api/           # transport layer: routes, request/response mapping
│   ├── domain/        # business rules, no framework or I/O imports
│   ├── application/   # use cases that orchestrate domain and adapters
│   └── adapters/      # database, queues, external services
├── migrations/        # versioned schema changes
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/      # checks against the published contracts
├── locales/           # user-facing messages per language
└── .env.example       # variable names only
```

Adapt names to the chosen stack, but keep the separation between transport, domain and adapters.

## Conventions

- The API follows the contracts in `07-contracts/`; a contract change comes first.
- Errors use one documented shape with a stable code and a translatable message key.
- Every request carries a correlation ID that reaches the logs.
- Configuration comes from the environment; secrets come from the chosen secret store.
- Messages returned to users are resolved by language, using the request's locale.
- Health and readiness endpoints exist and are cheap to call.
- Migrations are forward-only and reviewed like code.

## Verification

- `make verify` (or its equivalent) runs linting, unit, integration and contract tests.
- New behaviour starts with a failing test linked to a spec ID.

{{pending: define the minimum coverage and which checks block a merge}}

## Related

- [Repositories](README.md)
- [Frontend app](frontend-app.md)
- [Coding standards](../10-engineering/coding-standards.md)
- [Secure coding standard](../10-engineering/secure-coding-standard.md)
- [Secret management](../13-security/secret-management.md)
- [Contract example](../07-contracts/example.md)
