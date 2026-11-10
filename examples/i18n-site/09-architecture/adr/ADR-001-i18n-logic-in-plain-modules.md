# ADR-001 — i18n logic in plain ES modules, no i18n library

## Purpose

Decide where the language rules of the site live and how they are tested.

## Status

Accepted. Decision (example owner, 2026-11-10), proposed by `/dixi.plan`.

## Context

The site needs locale negotiation, prefixed routes, alternates and catalogs. Next.js offers the routing primitives but no negotiation; libraries such as `next-intl` or `negotiator` cover it, at the cost of dependencies and of tests that need `npm install` and a Next.js build.

## Options

1. An i18n library: complete, but adds dependencies and hides the rules this example wants to show.
2. Logic inside `middleware.ts` and the pages: no dependencies, but only testable through Next.js.
3. Plain ES modules (`lib/*.mjs`) imported by Next.js and tested with `node --test`.

## Decision

Option 3. The modules have no dependencies; Next.js files only adapt their results (redirect response, `Metadata`, JSX).

## Consequences

Tests run with Node alone, in milliseconds. Plural rules, translated slugs and locale-aware formats are not covered and would need `Intl` or a library later. The Next.js skeleton is not exercised by `make verify`.

## Related

- [Contract](../../07-contracts/example.md)
- [ADR index](README.md)
