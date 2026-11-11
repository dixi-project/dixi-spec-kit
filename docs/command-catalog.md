# DIXI Spec Kit proposed command catalog

## Purpose

Turn EIS-IA's capabilities into operations usable by third parties: define, build, verify and maintain a product with traceability. Coverage is derived from the Dixi method and from verifiable walkthroughs, without being limited to another tool's catalog.

## Status and scope

Working catalog of TASK-001 and ADR-100. B1 already implements `dixi init --agent none`, `dixi doctor`, `dixi check`, help and version as local development. Agent commands, upgrade and specialized capabilities remain proposed; their presence here does not indicate that they are installed. The open direction and incremental start are authorized.

B2a adds `dixi workflow list`, `show` and `prepare` for the eight definition/design recipes. They are deterministic access to the method and its context; not assisted execution of the `/dixi.*` commands. [B2a contract](../07-contracts/commands/workflow-preparation-contract.md) · [Guide](workflow-quickstart.md).

The `/dixi.*` names express shared operations of the core; the installable syntax is verified per adapter and may vary between tools. The `dixi ...` commands run in the terminal. The CLI performs deterministic operations; the chosen integration guides decisions and prepares documents using shared validators. The no-integration mode delivers the method, templates and guides for documentary use. Codex and Claude Code are candidates of equal priority, without announced support until they are verified.

The [joint review](v1-design-review.md) proposes including the 16 journey and design/traceability commands, and prioritizing the nine specialized entries afterwards. The [initial contract](../07-contracts/commands/command-contract.md) specifies inputs, writes, limits and results. This selection remains pending validation.

## Existing base and gaps

The review of the private origin found nine commands: `initsdd`, `initproject`, `build`, `risk-review`, `open`, `close`, `mode`, `promote` and `duediligence`. Their existence does not accredit that they work in the public product nor distribution rights.

| Existing capability | Proposed treatment |
|---|---|
| `initsdd` | Replace the dependency on the private repository with `dixi init` using packaged resources. |
| `initproject` | Adapt the interview to `discover`; make domains, architecture and contracts accessible separately. |
| `build` | Adapt TDD, risk classification and human gates; remove the mandatory dependency on the internal task system. |
| `risk-review` | Adapt to `review`, with an explicit Git base and without approving or merging. |
| `open`, `close` | Adapt to `status` and `handoff`, with local continuity and without implicit push. |
| `mode`, `promote` | Keep status lookup and design supervised promotion; do not confuse MODE promotion with deployment. |
| `duediligence` | Adapt as a specialized capability, with explicit evidence and gaps. |

A gap indicates that there is no verified autonomous public entry for that operation. Part of its logic may exist inside the origin's commands or guides; it is audited before creating another implementation.

## Candidate main journey for v1

`init → discover → specify → plan → tasks → build → verify → review`

`status` points to the next step and `handoff` allows work to be resumed. `plan` incorporates domains, architecture, contracts and security according to risk; those capabilities can also be invoked directly. Small changes follow EIS-IA's proportional process, without requiring the whole journey.

| Agent command | Observable result | Base or gap |
|---|---|---|
| `/dixi.discover` | Product vision, actors, scope, constraints and pending questions. | Adapt `initproject`. |
| `/dixi.specify` | Story and feature with rules, verifiable criteria and links to domain and module. | Specific entry pending. |
| `/dixi.clarify` | Answers and assumptions incorporated into a spec; blocking doubts identified. | Specific entry pending; also used during other steps. |
| `/dixi.plan` | Technical plan by blocks, affected contracts, ADRs, risks and verification path. | Extract and adapt planning from the existing cycle. |
| `/dixi.tasks` | Tasks with criteria, dependencies, risk level and links to specs. | Separate task generation from the interview and from `build`. |
| `/dixi.build` | Tests first, code change and execution evidence per task. | Adapt `build`. |
| `/dixi.verify` | Report of executed, failed or non-executed checks and criteria coverage. | Specific entry pending over the project's verifiers. |
| `/dixi.review` | Findings by risk and criterion → change → test comparison for human review. | Adapt `risk-review`. |
| `/dixi.status` | Status of artifacts, pending decisions and justified next step. | Adapt `open`. |
| `/dixi.handoff` | Local context to continue, evidence and pending items, without declaring closure without verification. | Adapt `close`. |

## Dixi's own capabilities that must be covered in v1

Proposal: expose these operations as direct commands and reuse them from `plan` or `verify`. The final partition is validated with the contracts to avoid two paths that produce contradictory documents.

| Proposed command | Observable result | When it is needed |
|---|---|---|
| `/dixi.domain` | Domain boundaries, ubiquitous language and modules linked to business goals. | Discovery or domain change. |
| `/dixi.architecture` | Design, alternatives, consequences and proposed ADRs. | Structural decision. |
| `/dixi.contract` | Contracts and schemas linked to their consumers; compatibility impact documented. | New or modified interfaces. |
| `/dixi.threat-model` | STRIDE threats, mitigations and planned tests per threat. | EIS-IA risk triggers; not optional when it applies. |
| `/dixi.analyze` | Report of gaps and contradictions between business, domain, module, feature, contract and test. | Before building and when specs change. |
| `/dixi.change` | Change proposal with impact on existing specs, contracts, tasks and tests. | Evolution of a feature; does not modify frozen tests. |

`analyze` interprets semantic consistency; `dixi check` checks mechanical rules. `verify` runs the project's ladder and gathers evidence. An agent report does not replace the result of those checks.

## Specialized capabilities to be delimited

They are included in the product map. Their inclusion as independent commands in v1 remains pending prioritization and testing; deferring an interface does not remove an applicable rule.

| Candidate | Result and limit |
|---|---|
| `/dixi.data` | Model, data classification, retention and migration plan; without running migrations in environments. |
| `/dixi.quality` | Test strategy, budgets and verification matrix, including i18n and accessibility according to scope. |
| `/dixi.ai` | Use cases, evaluation, data, costs and agent/MCP design according to the project's policies; Bedrock remains in force in the Dixi set, with public portability proposed in ADR-101. |
| `/dixi.release` | Readiness evidence and release proposal; without approving gates or deploying from the agent. |
| `/dixi.promote` | Review of requirements for MODE=prod and supervised ceremony; no silent promotion. |
| `/dixi.operate` | SLOs, observability, runbooks and incident preparation; without operating production from the laptop. |
| `/dixi.finops` | Estimates with assumptions, sources and budgets; without inventing real consumption or costs. |
| `/dixi.compliance` | Map of obligations and pending evidence; without declaring certifications. |
| `/dixi.duediligence` | Report backed by artifacts and gaps, for human evaluation. |

## Spec Kit parity (v1.7.0)

Added by [ADR-108](../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) so that every GitHub Spec Kit command has a DIXI counterpart ([contract](../07-contracts/commands/parity-commands-contract.md), [command map](coming-from-spec-kit.md)).

| Command | Observable result | Limit |
|---|---|---|
| `/dixi.constitution` | `00-governance/principles.md` versioned, with change log and impact list; every operation reads it. | Governance only; removing or redefining a principle needs an approved ADR. |
| `/dixi.checklist` | `05-features/<slug>/checklists/<domain>.md` with unchecked, traced `CHK-NNN` requirement-quality items. | Never ticks items; `/dixi.build` stops while items are open. |
| `/dixi.converge` | Convergence tasks appended to `05-features/<slug>/tasks.md`, typed and traced, or a converged report. | Never edits specs, contracts, code, existing tasks or tests. |

## Supporting CLI

| Command | Contract and status |
|---|---|
| `dixi init` | Available with `--agent none` and `--agent claude` (B3): creates documents and baseline without overwriting. |
| `dixi doctor` | B1 available: runtime, resources, filesystem and local metadata. Agent/profile diagnostics pending. |
| `dixi check` | B1 available: structure, references and declared graph according to the local contract. |
| `dixi upgrade --dry-run` | Deferred to v1.1 (ADR-102). |
| `dixi --help`, `dixi --version` | B1 available: installed capabilities and development version. |

The CLI does not invoke AI or AWS when installing or generating projects. Agent commands require the documented agent environment. Fully offline operation is not announced merely because templates are packaged locally.

## Mandatory contract per command

Before implementing, the following are specified: goal, arguments, inputs and prerequisites; files read and written; outputs and error states; human gates; behavior on repetition, interruption and local changes; next step; acceptance scenarios and expected evidence. Assumptions remain visible and are never presented as user decisions.

It is checked that installed commands reference only distributed resources. Verifiers must have automated tests; agent commands additionally require evaluation walkthroughs with controlled inputs and criteria, without requiring literal equality of the generated text. Missing information, conflicts between specs and refusal to skip gates are tested. Syntax and behavior are tested in the announced agent.

## Delivery order and acceptance

1. Review story + ADRs + catalog as a whole; fix included commands, eligible integrations, policies and support matrix.
2. Create traceability and contracts by blocks: installation; definition; design; tasks and build; verification and review; continuity and changes.
3. Per block, record red tests before implementing and check the installed resources. Resolve rights before incorporating material from the origin into the distribution.
4. Complete a public example from idea to verified code and prepared human review; repeat with a contract modification to check impact and gates.
5. Evaluate the specialized commands and record the inclusion or deferral decision, without announcing pending ones as available.
6. Validate packaging, es/en documentation and publication conditions. The number of commands alone does not accredit usefulness or quality.

## Related

- [Product](product-spec.md)
- [Design review](v1-design-review.md)
- [Command contract](../07-contracts/commands/command-contract.md)
- [Implemented B1 contract](../07-contracts/commands/local-core-contract.md)
- [Story](../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-100](../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101](../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Roadmap](../ROADMAP.md)
