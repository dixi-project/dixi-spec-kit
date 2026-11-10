# Coding standards

## Purpose

Make the code of this project read the same everywhere, fail early (in the formatter, linter or
type checker rather than in production) and be reviewable by any person or agent without learning
new conventions. This document states **what** is required; the project's verification command
states **how** it is checked.

Stack: {{pending: languages, runtimes and frameworks chosen for the project, recorded in an ADR}}

## Common rules

1. **What can be checked is checked.** Formatting, linting and type checks run in `make verify`
   and in continuous integration. A rule without a tool is only a recommendation.
2. **Strict types from the first commit.** Raising strictness later costs more than starting
   strict. Every new suppression comment is justified in the pull request.
3. **Pinned runtime version** in the repository, so local, CI and production run the same one.
4. **One language for identifiers.** {{pending: language for identifiers, commit messages and log
   messages; language for specs and documentation}}
5. **No user-facing strings in code.** Visible texts live in per-language translation catalogs.
6. **No secrets, environment URLs or account identifiers in code.** They come from configuration
   loaded at runtime from a secret store.
7. **Small, pure functions where possible.** Domain logic does not know about HTTP, the database
   or vendor SDKs; it receives them through injection so it can be tested without a network.
8. **Dates in UTC** in storage and contracts; the user's time zone only when presenting.
9. **Money as integers of the minimum unit or exact decimals**, never binary floating point.
10. **Errors and security** follow [the secure coding standard](secure-coding-standard.md).

## Per-stack table

Fill one table per language used in the project.

| Aspect | Rule |
|---|---|
| Version | {{pending: supported runtime version and upgrade policy}} |
| Formatter | {{pending: formatter and configuration}} |
| Linter | {{pending: linter, rule set and warning tolerance}} |
| Types | {{pending: type checker and strictness level}} |
| Dependencies | Manifest plus a committed lock file |
| Structure | Domain separated from infrastructure; thin entry points (controllers, handlers) |
| Tests | {{pending: test runner; property-based testing library if any}} |
| Forbidden | Dynamic code evaluation, silenced errors, string-built queries, deserializing untrusted data with unsafe formats |

## Review checklist

- [ ] Formatter, linter and type checker are green with no new suppressions.
- [ ] New behavior has a test written first, traced to a feature or contract ID.
- [ ] No hardcoded visible text, secret, URL or identifier.
- [ ] Public functions and modules have names that explain intent; comments explain *why*.
- [ ] Deviations from this standard are recorded in an ADR.

## Deviations

A project departs from these rules only through an accepted ADR that names the rule, the reason
and the compensating control. Use [the ADR template](templates/adr-template.md).

## Related

- [Secure coding standard](secure-coding-standard.md)
- [ADR template](templates/adr-template.md)
- [Test plan](../11-quality/test-plan.md)
- [Project instructions](../AGENTS.md)
