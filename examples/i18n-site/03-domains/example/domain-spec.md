# DOMAIN-001 — Localized delivery

## Purpose

Define the language of serving content per language.

## Ubiquitous language

- **Locale:** supported language code: `en` (default) or `es`.
- **Prefix:** first path segment that names the locale (`/es/contact`).
- **Negotiation:** choosing a locale from the `Accept-Language` header: exact tag, then primary subtag, then the default.
- **Alternates:** the canonical URL of a page in its own locale plus one URL per locale and `x-default`.
- **Catalog:** JSON file with every user-facing string of one locale, keyed by stable names such as `home.heading`.

## Related

- [Goal](../../01-business/vision.md)
- [Module](../../04-modules/example/module-spec.md)
