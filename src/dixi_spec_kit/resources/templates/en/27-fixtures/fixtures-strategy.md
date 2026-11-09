# Fixtures strategy

## Purpose

Define how the project creates and uses sample data for development, tests and demos. All sample data is synthetic: it never contains real or personal data copied from production or from real people, and it is safe to commit, share and show.

Status: draft. {{pending: decide where fixtures live and who maintains them}}

## Levels of fixtures

| Level | Used for | Size | Determinism | Lives in |
|-------|----------|------|-------------|----------|
| Unit | Single test cases | Minimal, inline | Fully fixed | Next to the test |
| Integration | Tests across components | Small sets | Fixed seed | Test folder of each repository |
| Development seed | Local environments | Medium | Fixed seed | {{pending}} |
| Demo | Curated stories for presentations | Small, hand-picked | Fixed | {{pending}} |
| Load | Performance tests | Large, generated | Seeded generator | Generated on demand, not committed |

## Synthetic data rules

- Never copy production data into fixtures, not even anonymised dumps, unless a recorded decision approves a specific technique.
- Names, organisations and addresses are clearly fictional.
- E-mail addresses use reserved example domains, for example `ana.demo@example.com`.
- Phone numbers use ranges reserved for fiction or documentation where available.
- Payment details use only test values meant for testing; never real card or account numbers.
- Identifiers look realistic in format but are generated.
- Free-text fields contain neutral text, without offensive or misleading content.

## Internationalisation

- Fixtures include names, addresses, currencies, dates and text in every supported language.
- Include tricky cases: accents, long strings, right-to-left text if relevant, different date and number formats.

## Generation

- Generators use a fixed seed so the same command produces the same data.
- Generated data respects the canonical data model and its constraints.
- Fixtures are versioned with the schema; a schema change updates fixtures in the same change.

{{pending: decide the generation approach and the command that loads each level}}

## Safety checks

- A check scans fixtures for real-looking e-mail domains, secrets and personal data patterns.
- Demo and seed data are never loaded into production.

## Related

- [Sample data catalog](sample-data-catalog.md)
- [Demo scenarios](demo-scenarios.md)
- [PII classification](../08-data/pii-classification.md)
- [Environments](../14-delivery/environments.md)
- [Test pyramid](../11-quality/test-pyramid.md)
- [Test plan](../11-quality/test-plan.md)
