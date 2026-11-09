# Infrastructure Modules

## Purpose

Explain how infrastructure is declared as code: which tool, how modules are organised, how changes are reviewed and applied. This document holds rules and decisions; the infrastructure code itself lives wherever the project decides, not in this area.

## Decisions

- Infrastructure as code tool: {{pending: choose with a selection matrix and record in an ADR}}
- Location in the repository: {{pending: path}}
- State or stack storage: {{pending: where, how it is locked and who can read it}}

## Selection criteria

| Criterion | Weight | Option A | Option B |
|---|---|---|---|
| Team familiarity | {{pending: weight}} | {{pending: score}} | {{pending: score}} |
| Support for the chosen hosting | {{pending: weight}} | {{pending: score}} | {{pending: score}} |
| Plan or preview before applying | {{pending: weight}} | {{pending: score}} | {{pending: score}} |
| Licence and long-term maintenance | {{pending: weight}} | {{pending: score}} | {{pending: score}} |

## Module structure

- One module per reusable building block (network, database, service, static site).
- One composition per environment that wires modules together with environment values.
- Modules take inputs and expose outputs; no hidden global values.
- Tool and module versions are pinned.

## Naming and tagging

Every resource carries: project, environment, component, owner. Pattern: {{pending: naming convention}}.

## Safety rules

- Resources that hold data are protected against accidental destruction.
- No secrets in code or in state files that are not encrypted.
- Least privilege: the role that applies changes in an environment cannot touch another environment.
- Changes are never applied from a personal machine to production.

## Change flow

1. Open a pull request with the infrastructure change.
2. CI runs `make verify`, formatting, static checks and produces a plan or preview.
3. A reviewer reads the plan, not only the code.
4. After merge, the plan is applied to staging, then to production after human approval.

## Drift

- Detect differences between code and reality {{pending: frequency}}.
- Fix drift through code, never by editing resources by hand.

## Related

- [Environments](environments.md)
- [CI/CD overview](ci-cd-overview.md)
- [Deployment architecture](../09-architecture/deployment-architecture.md)
- [Secret management](../13-security/secret-management.md)
