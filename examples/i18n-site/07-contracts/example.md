# CONTRACT-001 — i18n routing and catalog API

## Purpose

Contract of `lib/i18n.mjs` and `lib/catalog.mjs`, produced with `/dixi.plan`. Next.js code imports only these functions; it holds no language rules of its own.

## `lib/i18n.mjs`

- `LOCALES = ["en", "es"]`, `DEFAULT_LOCALE = "en"`; `isLocale(value) -> boolean`.
- `parseAcceptLanguage(header) -> {range, q}[]`: lowercase ranges ordered by `q` (default 1), then by position. Malformed entries are dropped; headers over 4,096 characters or not strings give `[]`.
- `negotiateLocale(header) -> locale`: first range with `q > 0` that matches a locale exactly or by primary subtag (`es-MX` → `es`); `*` gives the default unless refused; otherwise `DEFAULT_LOCALE`. A locale refused with `q=0` is not chosen.
- `splitLocale(pathname) -> {locale, rest}`: `"/es/about"` → `{locale: "es", rest: "/about"}`; `locale` is `null` without a supported prefix.
- `localizedPath(locale, path = "/") -> string`: `"/es"`, `"/es/contact"`. Leading slashes collapse to one. Throws `RangeError` for an unsupported locale or a path not starting with `/`.
- `redirectTarget(pathname, acceptLanguage) -> string | null`: `null` when the path already has a locale prefix; otherwise `localizedPath(negotiateLocale(...), pathname)`.
- `pageAlternates(origin, locale, path = "/") -> {canonical, languages}`: absolute URLs; `languages` has every locale and `x-default` (the default locale). Same shape as Next.js `Metadata["alternates"]`. Throws `RangeError` unless `origin` is a bare `http(s)` origin.

## `lib/catalog.mjs`

- `getCatalog(locale) -> object`: contents of `locales/<locale>.json`; throws `RangeError` for an unsupported locale.
- `translate(catalog, key) -> string`: throws `Error("Missing translation: <key>")` when the key is absent or empty.

## Catalogs

`locales/en.json` and `locales/es.json`: flat objects, identical keys, non-empty strings. Keys: `meta.title`, `meta.description`, `home.heading`, `home.intro`, `nav.languages`, `language.<locale>`.

## Next.js usage (illustrative)

- `middleware.ts`: answers `redirectTarget(...)` with a 307 redirect, `Vary: Accept-Language` and `Cache-Control: private, no-store`.
- `app/[lang]/layout.tsx`: `<html lang>` from the prefix; unknown locales give 404 (`dynamicParams = false`).
- `app/[lang]/page.tsx`: `generateMetadata` returns `alternates: pageAlternates(...)`; visible text comes from `translate`.

## Related

- [Feature](../05-features/example/feature-spec.md)
- [Test plan](../11-quality/test-plan.md)
- [ADR-001](../09-architecture/adr/ADR-001-i18n-logic-in-plain-modules.md)
