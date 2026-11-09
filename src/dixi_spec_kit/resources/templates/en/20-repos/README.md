# Repositories

## Purpose

Describe how the project's code is split into repositories and how each repository stays linked to the specs that justify it. The rule of thumb is one repository per deployable piece: something that is built, versioned and released on its own.

Status: draft. {{pending: decide the repository layout (one per deployable piece, a monorepo, or a mix)}}

## Repository inventory

| Repository | Kind | Owner | Specs it implements | Status |
|------------|------|-------|---------------------|--------|
| {{pending: name}} | Backend service | {{pending: owner}} | {{pending: MODULE-/FEATURE- IDs}} | Planned |
| {{pending: name}} | Frontend app | {{pending: owner}} | {{pending: IDs}} | Planned |

Other kinds may apply depending on the profile: background worker, mobile app or MCP server. Add a row for each one you adopt and follow its stack guide in this folder.

## One repository per deployable piece

- A repository has one build, one version number and one release pipeline.
- Shared code goes into a versioned library, not into copies across repositories.
- Splitting or merging repositories is a structural decision: record it as an ADR.
- If you choose a monorepo instead, keep one folder per deployable piece with the same rules.

## Linking code to specs

1. This spec repository is the source of truth; code repositories do not redefine requirements.
2. Each code repository has a README section listing the spec IDs it implements and a link back here.
3. Branches, commits and pull requests mention the spec ID they change, for example `FEATURE-001`.
4. Tests name or tag the criterion they cover, so the path goal → feature → contract → test can be followed.
5. Record the code location of each item in `.dixi/traceability.json` and the traceability matrix.
6. A change to behaviour starts with a spec change, then tests, then code.

## Common conventions

Every code repository should provide:

- `README.md` with purpose, how to run it locally and the specs it implements.
- `AGENTS.md` with rules for AI agents, consistent with the root [AGENTS.md](../AGENTS.md).
- A single verification command (for example `make verify`) that runs the real checks.
- An `.env.example` with variable names only; real secrets never enter the repository.
- User-facing text in translation catalogs per language, never hardcoded.

{{pending: list the conventions that are mandatory for every repository and who reviews them}}

## Creating a new repository

1. Confirm the deployable piece is justified by a module or feature spec.
2. Pick the stack guide that fits and resolve its `{{pending}}` decisions.
3. Record the stack choice as an ADR.
4. Add the repository to the inventory above and to the traceability records.

## Related

- [Backend service](backend-service.md)
- [Frontend app](frontend-app.md)
- [Traceability matrix](../21-ai/sdd/traceability-matrix.md)
- [ADR index](../09-architecture/adr/README.md)
- [Coding standards](../10-engineering/coding-standards.md)
- [Project](../00-master-spec.md)
