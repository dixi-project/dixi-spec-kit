# Demo scenarios

## Purpose

Define curated, repeatable demo stories built on synthetic data. A scenario lets anyone show the product the same way every time, without improvising data or exposing real information.

Status: draft. {{pending: choose the first scenarios and who maintains the demo environment}}

## Why curated scenarios

- Demos are consistent and can be rehearsed.
- The data tells a clear story instead of random records.
- Real customer or personal data is never shown.
- Scenarios double as end-to-end acceptance checks when automated.

## Scenario catalog

| ID | Name | Audience | Story | Languages | Duration |
|----|------|----------|-------|-----------|----------|
| DEMO-001 | First-time user | New users | Sign up, complete setup, reach first value | ES, EN | {{pending}} |
| DEMO-002 | Everyday use | Existing users | Complete the core task end to end | ES, EN | {{pending}} |
| DEMO-003 | Multi-language | International audience | Same journey in two languages, with language-prefixed URLs | ES, EN | {{pending}} |
| DEMO-004 | Administration | Administrators | Manage users, roles and settings | {{pending}} | {{pending}} |
| DEMO-005 | {{pending: scenario}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |

## Scenario template

For each scenario, document:

1. Goal: what the audience should understand at the end.
2. Starting state: datasets and named records loaded.
3. Steps: numbered actions and the expected result of each.
4. Talking points: the value shown at each step, without unverified claims.
5. Reset: how to return the environment to the starting state.
6. Known limits: what not to show yet.

## Demo environment

- Separate from production, with its own configuration and no production data.
- Loaded by one command from the demo fixtures; reset by one command.
- Access is limited and credentials are managed as secrets, not written here.

{{pending: define how often the demo environment is refreshed and checked}}

## Adding a scenario

1. Write the scenario with the template above.
2. Add or reuse records from the sample data catalog.
3. Rehearse it in every listed language.
4. Optionally automate it as an end-to-end test.

## Related

- [Fixtures strategy](fixtures-strategy.md)
- [Sample data catalog](sample-data-catalog.md)
- [Environments](../14-delivery/environments.md)
- [Acceptance strategy](../11-quality/acceptance-strategy.md)
- [Personas](../01-business/actors/personas.md)
