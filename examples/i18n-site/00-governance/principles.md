# Principles

## Purpose

State the few principles that guide product, architecture and engineering decisions in this project, so that people and agents can resolve trade-offs consistently and explain why a choice was made.

Status: draft. {{pending: confirm the principles with the responsible person}}

## How to use them

- Cite a principle by its ID (for example `P-03`) in specs, ADRs and reviews.
- When a decision goes against a principle, record why in an ADR.
- Keep the list short. A principle nobody applies should be removed.

## Vision principles

| ID | Principle | What it means in practice |
|----|-----------|---------------------------|
| P-01 | Specs lead | No implementation starts without a feature spec and observable criteria. |
| P-02 | A person is accountable | Every change has a named human owner who reviews and merges it. |
| P-03 | Evidence over claims | "Done" means a real, reported check result, not a statement. |
| P-04 | International by default | Content, routes and formats are designed for more than one language from day one. |
| P-05 | {{pending: product-specific principle}} | {{pending: practical consequence}} |

## Architecture principles

| ID | Principle | What it means in practice |
|----|-----------|---------------------------|
| A-01 | Boundaries follow domains | Modules map to domains; cross-domain access goes through contracts. |
| A-02 | Contracts are the source of truth | Interfaces are specified before code and versioned. |
| A-03 | Simple first | Start with the simplest structure that meets the criteria; split only with evidence. |
| A-04 | Secure by default | Deny by default, least privilege, no secrets in code. |
| A-05 | Observable from the start | Logs, metrics and traces are part of the feature, not an afterthought. |
| A-06 | {{pending: architecture principle, for example cost as a requirement}} | {{pending: practical consequence}} |

## Engineering principles

| ID | Principle | What it means in practice |
|----|-----------|---------------------------|
| E-01 | Tests first | A failing test exists before the code that makes it pass. |
| E-02 | Frozen tests | Committed tests are not edited to make code pass. |
| E-03 | Small, reversible changes | Prefer short-lived branches and changes that can be rolled back. |
| E-04 | Agents assist, people decide | Agents never sign, approve or merge. |
| E-05 | Debt only goes down | New work must not lower an existing quality threshold. |

## When principles conflict

1. Safety and security of users and data come first.
2. Then correctness against the spec.
3. Then delivery speed and convenience.

{{pending: confirm or adjust this precedence order}}

## Changing a principle

- Propose the change in an ADR with context and consequences.
- The responsible person approves it: {{pending: who approves principle changes}}
- Update every document that cites the changed principle.

## Related

- [Project](../00-master-spec.md)
- [Business goal](../01-business/vision.md)
- [Engineering standards](engineering-standards.md)
- [AI governance](ai-governance.md)
- [ADR index](../09-architecture/adr/README.md)
