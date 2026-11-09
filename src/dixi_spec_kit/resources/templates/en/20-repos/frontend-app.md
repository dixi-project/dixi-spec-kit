# Frontend app

## Purpose

Describe the expected structure and conventions of a web frontend repository. The app must be international from the start: language-prefixed routes, server-rendered content and correct SEO signals per language. This guide does not choose a framework.

Status: draft. {{pending: choose the frontend framework and rendering strategy}}

## Stack decisions

| Decision | Choice | ADR |
|----------|--------|-----|
| Framework | {{pending}} | {{pending}} |
| Rendering (server-side, pre-rendered or hybrid) | {{pending}} | {{pending}} |
| Styling approach | {{pending}} | {{pending}} |
| Unit and end-to-end test tools | {{pending}} | {{pending}} |
| Supported languages | ES, EN, {{pending: others}} | {{pending}} |

## Suggested folder layout

```text
<app>/
├── README.md
├── AGENTS.md
├── src/
│   ├── routes/[lang]/   # every public page lives under a language prefix
│   ├── components/      # presentational pieces, no hardcoded text
│   ├── features/        # screens grouped by feature spec
│   ├── services/        # API clients generated or written from contracts
│   └── i18n/            # locale detection and helpers
├── locales/
│   ├── en.json
│   └── es.json
├── public/
└── tests/
    ├── unit/
    └── e2e/
```

## Internationalization rules

- Public URLs carry the language: `/en/...`, `/es/...`. Never switch language only on the client.
- The root `/` redirects to the best match for the browser language, with a default.
- Every page emits a canonical URL for its own language and `hreflang` alternates for all languages, plus `x-default`.
- Content is rendered on the server or pre-rendered, so crawlers see translated text without running scripts.
- All visible strings come from the JSON catalogs; missing keys fail the build or the tests.
- Dates, numbers and currencies are formatted by locale.

## Conventions

- Pages follow the page template and the accessibility standard.
- Performance budgets are checked for key pages.
- No secrets in client code; only public configuration reaches the browser.

{{pending: define which pages are public and indexable and which require sign-in}}

## Related

- [Repositories](README.md)
- [Backend service](backend-service.md)
- [i18n policy](../00-governance/policies/i18n-policy.md)
- [Page template](../10-engineering/templates/page-template.md)
- [Accessibility standard](../17-ux/accessibility-standard.md)
- [Web vitals budgets](../11-quality/performance-budgets/web-vitals-budgets.md)
