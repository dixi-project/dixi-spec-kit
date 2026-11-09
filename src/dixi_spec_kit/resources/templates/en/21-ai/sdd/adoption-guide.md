# SDD adoption guide

## Purpose

Help a team start using spec-driven development, either on a new project or on an existing codebase, without documenting everything up front.

## New project

Recommended order:

1. Fill `00-master-spec.md` with problem, scope and known constraints.
2. Write the business goal in `01-business/vision.md`.
3. Describe one domain and one module, keeping the example IDs or renaming them consistently.
4. Specify the first feature with observable criteria.
5. Write its contract and planned tests; validate structural decisions with a person.
6. Choose the stack and connect real tests to `make verify`.

## Existing project

Document as you go instead of stopping development:

1. Start with the master spec and project instructions describing what exists today.
2. Specify only the features you are actively changing.
3. Add contracts for the most used interfaces first.
4. Record important past decisions retroactively when they are questioned.
5. Use the traceability matrix to decide which gaps matter next.

Avoid: empty specs created only to complete the structure, duplicating documentation that already lives elsewhere, and freezing work until everything is written.

## Minimum levels

| Level | Contents | Typical use |
| --- | --- | --- |
| Navigable | Master spec, goal, project instructions | Prototypes, exploration |
| Governable | Plus domains, modules and key decisions | Shared codebases |
| Traceable | Plus contracts and tests linked for every feature | Production and regulated work |

Target level for this project: {{pending: navigable, governable or traceable}}

## With agents

- Ask the agent to prepare context with `dixi workflow prepare` before drafting.
- Review every draft; agents fill gaps with assumptions, which must become explicit pending markers.
- Keep the human gates described in the guardrails and human-in-the-loop documents.

## Related

- [Methodology](methodology.md)
- [Traceability matrix](traceability-matrix.md)
- [Guardrails](../agents/guardrails.md)
- [Human in the loop](../agents/human-in-the-loop.md)
- [Project guide](../../docs/guide.md)
