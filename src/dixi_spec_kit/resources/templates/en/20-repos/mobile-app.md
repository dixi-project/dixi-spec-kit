# Mobile app

## Purpose

Describe the expected structure and conventions of a mobile app repository. This guide does not choose between native or cross-platform approaches; it sets what any mobile repository must contain to stay aligned with the specs.

Status: draft. {{pending: choose native or cross-platform, the language and the minimum OS versions}}

## Stack decisions

| Decision | Choice | ADR |
|----------|--------|-----|
| Approach (native or cross-platform) | {{pending}} | {{pending}} |
| Language and UI toolkit | {{pending}} | {{pending}} |
| Minimum OS versions | {{pending}} | {{pending}} |
| Offline storage | {{pending}} | {{pending}} |
| Test tools (unit and UI) | {{pending}} | {{pending}} |

## Suggested folder layout

```text
<mobile-app>/
├── README.md
├── AGENTS.md
├── src/
│   ├── features/      # screens grouped by feature spec
│   ├── components/    # reusable UI, no hardcoded text
│   ├── services/      # API clients built from contracts
│   ├── storage/       # local persistence and sync
│   └── i18n/
├── locales/
│   ├── en.json
│   └── es.json
├── assets/
└── tests/
```

## Conventions

- All visible text comes from per-language catalogs; the app follows the device language with a manual override.
- The app tolerates old API versions for as long as old app versions remain in use.
- Sensitive data is stored only in the platform's secure storage, never in plain files.
- Offline behaviour is defined per feature: what works, what queues and what is blocked.
- Permissions are requested in context, with an explanation, and only when needed.
- Deep links map to the same language-prefixed paths as the web app when one exists.

## Releases

| Item | Value |
|------|-------|
| Release cadence | {{pending}} |
| Staged rollout percentage | {{pending}} |
| Forced update policy | {{pending}} |
| Crash-free sessions target | {{pending}} |

## Verification

- `make verify` runs unit tests and static checks; UI tests run on {{pending: devices or emulators}}.
- Accessibility is checked with screen readers and large text sizes.

## Related

- [Repositories](README.md)
- [Frontend app](frontend-app.md)
- [Backend service](backend-service.md)
- [Accessibility standard](../17-ux/accessibility-standard.md)
- [i18n policy](../00-governance/policies/i18n-policy.md)
