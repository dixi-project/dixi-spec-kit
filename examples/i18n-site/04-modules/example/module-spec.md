# MODULE-001 — i18n routing and catalogs

## Purpose

Implement the localized delivery domain as dependency-free ES modules (`lib/i18n.mjs`, `lib/catalog.mjs`) that a Next.js app imports from `proxy.ts` and `app/[lang]/`.

## Responsibilities

- Negotiate the locale and compute redirect targets that never leave the site.
- Build language-prefixed paths and the canonical and `hreflang` alternates.
- Load the catalog of a locale and fail on a missing key instead of showing it.
- Keep Next.js specifics in the skeleton files, so the logic is testable with `node --test` alone.

## Related

- [Domain](../../03-domains/example/domain-spec.md)
- [Feature](../../05-features/example/feature-spec.md)
