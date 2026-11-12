# TASK-015 — Local presets and extensions, and a documentation site

## Purpose

Let teams adapt DIXI without forking it, and publish the documentation as a site in English and Spanish ([ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md), phase E).

## Record

- Type: feature; priority P2; level 3 (extension mechanism needs its own ADR before code). Created 2026-11-11. Product owner: Alfredo Castillejos.
- Scope validated on 2026-11-11 with ADR-108. The site may ship before the extension mechanism.

## Story

As a team with its own conventions, and as a person evaluating DIXI
I want to override templates and add operations locally, and to read the documentation as a site
so that DIXI fits my organisation and is easy to discover.

## Acceptance criteria

1. A new ADR decides the preset and extension format, resolution order and safety rules (no network, no code execution at install, paths validated like the rest of the core) before any code.
2. Local presets override templates and operation texts with a documented precedence; `check` and `upgrade` respect them.
3. A standard-library script builds a static site in English and Spanish from the repository Markdown (navigation, search index, language switch, working relative links); a CI job builds it on every pull request.
4. A workflow publishes the site to GitHub Pages from `main` with least privilege; enabling Pages is the maintainer's action.

## Done when

1. ADR accepted and tests committed red before the implementation.
2. `make verify` passes and CI is green.
3. The site is published and linked from both READMEs.

## Progress — 2026-11-12

[ADR-109](../../09-architecture/adr/ADR-109-local-presets-and-extensions.md) accepted: local, data-only presets (override) and extensions (add `dixi-<extension>-<operation>`), validated like the core, recorded with their origin, reversible. Next: contracts, threat review and red tests.

## Related

- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [Repository settings](../../docs/repository-settings.md)
