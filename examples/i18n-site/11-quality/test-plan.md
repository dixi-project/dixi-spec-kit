# TEST-001 — Test plan

## Purpose

Map each criterion to its executable tests; `make verify` runs `dixi check` and, when `node` is installed, `node --test` on `tests/*.test.mjs`.

| Criterion | Test |
|---|---|
| FEATURE-001 · 1 | `tests/i18n.test.mjs`: `splits the locale prefix from the path`, `builds language-prefixed paths and rejects unsupported locales` |
| FEATURE-001 · 2 | `parses ranges by quality, then by position`, `ignores malformed entries and oversized headers`, `negotiates exact tag, then primary subtag`, `falls back to the default language`, `never chooses a language refused with q=0`, `redirects unprefixed paths by Accept-Language and leaves prefixed ones`, `redirect targets stay on the same site` |
| FEATURE-001 · 3–4 | `declares canonical and reciprocal hreflang alternates per language`, `rejects origins that are not bare http(s) origins` |
| FEATURE-001 · 5 | `tests/catalog.test.mjs` |

Not covered by automated tests: the Next.js skeleton itself (`middleware.ts`, `app/[lang]/`), which needs `npm install next react react-dom` to run. Its HTTP status and headers are checked by hand when the skeleton is run.

## Related

- [Contract](../07-contracts/example.md)
