# GOAL-001 — Reach visitors in their own language

## Purpose

Serve every public page in English and Spanish, each language with its own indexable URL, so that search engines list the right language and visitors land on it without having to choose.

## Actors

- Visitor (browser with a language preference).
- Search engine crawler (does not run scripts).
- Content editor (maintains the catalogs).

## Success metrics

- A visitor whose browser prefers Spanish lands on `/es` from `/`.
- Each language URL declares itself as canonical and lists every language version.
- Adding a language means adding a catalog and a code to the list, without touching pages.

## Open questions

- Translated slugs (`/es/contacto`)? Pending: out of this version; slugs are shared.

## Related

- [Domain](../03-domains/example/domain-spec.md)
