# International site — DIXI Spec Kit example

## Purpose

Public, reproducible example in a second stack: a Next.js (TypeScript) site served in English and Spanish, specified with the `/dixi.*` flow and the `site` profile. It shows language-prefixed routes, a root redirect by `Accept-Language`, `hreflang` and canonical URLs per language, and one JSON catalog per language. The responsible person and the studio are fictitious.

The i18n logic is plain ES modules in `lib/` with no dependencies; `app/[lang]/` and `proxy.ts` (the Next.js 16 name for the former `middleware.ts`) are an illustrative Next.js skeleton that imports it. `make verify` runs `dixi check` and, when `node` is installed, `node --test` on the modules; without `node` it says so and skips the application tests. No `npm install`, deployment or provider is needed.

The other templates added by `--profile site` are left as generated, with their `{{pending: …}}` blanks; only the documents this example uses are filled in.

## Related

- [Step-by-step walkthrough](docs/walkthrough.md)
- [Guide](docs/guide.md)
- [Project](00-master-spec.md)
- [Goal](01-business/vision.md)
