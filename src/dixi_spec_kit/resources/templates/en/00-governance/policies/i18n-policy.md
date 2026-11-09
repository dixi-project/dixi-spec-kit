# Internationalization policy

## Purpose

Make sure the product is designed for more than one language and region from the start, so that adding a language is a translation task and not a rewrite, and so that each language can be found by search engines.

Status: draft. {{pending: confirm supported languages and markets}}

## Supported languages

| Language | Code | Status | Owner of translations |
|----------|------|--------|-----------------------|
| English | `en` | Required | {{pending: owner}} |
| Spanish | `es` | Required | {{pending: owner}} |
| {{pending: e.g. Portuguese}} | {{pending: code}} | Planned | {{pending: owner}} |

Default language: {{pending: default language}}

## Rules

1. **No hardcoded user-facing text.** All strings live in one catalog per language, for example `locales/en.json`.
2. **Language in the URL.** Public pages use a language prefix (`/en/`, `/es/`). Language is never switched only on the client.
3. **Root redirect.** `/` redirects to the best match for the visitor's preferred language, with the default as fallback.
4. **Alternate links.** Every public page declares `<link rel="alternate" hreflang="...">` for each language and an `x-default`.
5. **Canonical URL per language.** Each translated page is its own indexable URL.
6. **Server-side translation.** Translated content is rendered on the server or pre-rendered so crawlers see it without running scripts.
7. **Locale-aware formats.** Dates, numbers, currencies and units use locale formatting, never string concatenation.
8. **Text expansion.** Layouts tolerate text that is 30–40% longer than English.

## Catalog rules

- Keys are stable and semantic: `checkout.summary.total`.
- Missing keys fail tests in development; they never show raw keys to users.
- Plurals and gender use the catalog's plural rules, not code branches.
- Translators get context: a description or screenshot per key.

## Content and documentation

- Product messages and documentation exist in every required language.
- Legal and policy texts are reviewed per market by a qualified person.

## Checklist for a new screen or page

- [ ] All strings come from the catalogs.
- [ ] Route has a language prefix and alternate links.
- [ ] Dates, numbers and currencies are locale-formatted.
- [ ] Layout checked with the longest language.
- [ ] Tests cover at least two languages.

## Related

- [Naming conventions](naming-conventions.md)
- [Documentation policy](documentation-policy.md)
- [Principles](../principles.md)
