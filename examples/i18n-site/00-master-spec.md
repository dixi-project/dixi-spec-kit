# Project — International site

## Purpose

Public DIXI Spec Kit example: the marketing site of a fictitious studio, built with Next.js and served in English and Spanish. It shows the flow idea → specs → tests → verified code for international SEO. The responsible person is fictitious; their decisions are marked as "Decision (example owner)".

## Problem and scope

- Problem: a site that switches language only in the browser is indexed in one language and shows every visitor the same content first.
- Scope: language-prefixed routes (`/en`, `/es`), redirect of unprefixed paths by `Accept-Language`, canonical and `hreflang` alternates per language, one JSON catalog per language (FEATURE-001).
- Out of scope: content management, pages other than the home page, languages other than `en` and `es`, analytics, deployment.
- Stack: Next.js App Router with TypeScript; routing logic in dependency-free ES modules tested with `node --test`. Decision (example owner, 2026-11-10), see [ADR-001](09-architecture/adr/ADR-001-i18n-logic-in-plain-modules.md).
- Constraints: no runtime dependencies for the logic, no hardcoded user-facing text, content rendered on the server.

## Related

- [Goal](01-business/vision.md)
- [Guide](docs/guide.md)
- [Example walkthrough](docs/walkthrough.md)
- [i18n policy](00-governance/policies/i18n-policy.md)
