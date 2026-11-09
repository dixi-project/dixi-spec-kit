# Licensing policy

## Purpose

State the license under which the project is distributed and the rules for accepting third-party code, so that every dependency, snippet or generated artifact is compatible with that choice.

Status: draft. {{pending: name the person who approves licensing decisions}}

## Project license

- License of this project: {{pending: choose the outbound license}}
- Where it is declared: `LICENSE` file and package metadata.
- Contributions are accepted under: {{pending: same license, contributor agreement or other}}

## Rules for third-party code

1. Every dependency must have a known license; "no license" means "all rights reserved".
2. Licenses on the approved list may be used without further review.
3. Licenses marked "review" need a recorded decision before use.
4. Licenses marked "not allowed" are rejected unless the policy owner records an exception.
5. Copied snippets (from documentation, forums or AI output) follow the same rules as dependencies.
6. Keep required notices and attributions in the distributed product.

## Distribution model

How the project is delivered changes which obligations apply. {{pending: describe it, e.g. hosted service, distributed binary, library, mobile app}}

## AI-generated code

- Treat generated code as untrusted input for licensing: review long or distinctive snippets.
- Do not paste proprietary code from other projects into prompts.
- {{pending: decide whether provenance of generated code must be recorded}}

## Checks

- License detection runs together with dependency scanning.
- New dependencies with an unknown or non-approved license block the merge until reviewed.

## Exceptions

| Component | License | Reason | Approved by | Review date |
|-----------|---------|--------|-------------|-------------|
| {{pending: component}} | {{pending: license}} | {{pending: reason}} | {{pending: person}} | {{pending: date}} |

## Related

- [Approved licenses](approved-licenses.md)
- [Dependency scanning](../dependency-scanning.md)
- [Project](../../00-master-spec.md)
