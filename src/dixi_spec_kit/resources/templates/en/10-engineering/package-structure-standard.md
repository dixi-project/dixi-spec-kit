# Package structure standard

## Purpose

Make any person or agent find the same things in the same place across the repository, and keep
dependencies pointing in one direction so modules can change independently.

## Repository layout

{{pending: monorepo or several repositories, and the reason, recorded in an ADR}}

Suggested layout for a monorepo (adapt names to the chosen stack):

```text
/                      SDD documentation (00- to 13-) and project files
apps/ or services/     deployable units (web, API, worker)
packages/              shared code used by more than one deployable unit
infra/                 infrastructure as code
tests/                 cross-cutting tests (end-to-end, contract), if the stack needs it
Makefile               `make verify` runs every check of the repository
```

## Rules

1. **Organize by domain module, not by technical layer.** Each module in `04-modules/` maps to a
   code folder that holds its domain, application and infrastructure parts.
2. **Dependencies point toward the domain.** Infrastructure depends on the domain, never the other
   way around. The domain has no imports from frameworks, databases or vendor SDKs.
3. **Modules talk through public interfaces** (a package entry point, an API or an event), never
   by importing each other's internals or sharing tables.
4. **Shared packages are small and stable.** If only one module uses it, it is not shared.
5. **Tests next to the code or in a mirror tree**, following the stack convention.
   {{pending: test location convention}}
6. **Generated code** is clearly separated and never edited by hand.
7. **One verification entry point**: `make verify` at the root runs format, lint, types and tests
   for the whole repository.
8. **Configuration per environment** comes from the runtime, not from files committed per
   environment.

## Module folder

```text
<module>/
  domain/          entities, value objects, domain errors, pure rules
  application/     use cases that orchestrate the domain
  infrastructure/  adapters: persistence, HTTP clients, queues
  interface/       entry points: routes, handlers, consumers
```

Naming: {{pending: folder and package naming convention}}

## Related

- [Coding standards](coding-standards.md)
- [Module template](templates/module-template.md)
- [Domain template](templates/domain-template.md)
- [Example module](../04-modules/example/module-spec.md)
