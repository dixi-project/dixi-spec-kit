# FEATURE-001 — Language-prefixed pages with SEO alternates

## Purpose

First feature of the example, produced with `/dixi.specify`.

## Story

As a visitor
I want to land on the site in my browser's language, at a URL of its own
so that I read it in my language and search engines index each language.

## Acceptance criteria

1. Public pages live under `/en` or `/es`; any other first segment is not a locale.
2. An unprefixed path redirects (307, `Vary: Accept-Language`) to the same path under the negotiated locale: exact tag, then primary subtag, then `en`. A language refused with `q=0` is never chosen, and the target always stays on the site.
3. Each page declares its canonical URL in its own language, never in another language.
4. Each page lists one `hreflang` alternate per supported locale plus `x-default` (`en`); alternates are reciprocal.
5. Every user-facing string comes from `locales/<locale>.json`; catalogs have the same keys, and a missing key fails instead of showing the raw key.

## Business rules

1. Content is rendered on the server per locale; the language is never switched only in the browser.

## Related

- [Module](../../04-modules/example/module-spec.md)
- [Contract](../../07-contracts/example.md)
- [Tasks](tasks.md)
