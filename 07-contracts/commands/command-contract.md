# Proposed command contract — v1.0.0

## Purpose

Fix the observable behavior of the DIXI Spec Kit catalog. It is a general design by blocks; the [B1 contract](local-core-contract.md) makes concrete the local operations already implemented and their limits. Later operations are still in draft and are not available merely because they appear here.

The [B2a contract](workflow-preparation-contract.md) implements viewing/preparing A01–A08 through `workflow list/show/prepare`. Its recipes are shared; the artifact outputs described below remain the contract for the subsequent manual/assisted work, not files the CLI claims to have generated.

## Scope and vocabulary

Proposal of 16 agent commands and four terminal operations, plus help and version. The nine specialized candidates in the catalog remain outside this initial implementation proposal until they are prioritized; their applicable controls remain mandatory within `plan`, `build` and `verify`.

A **project** is the root initialized by the kit. A **target** is the identifier or path of the feature, task or document being worked on. An **artifact** is a document, contract, test or code linked to the target. A piece of **evidence** identifies what was executed, at which revision or file state, and what the result was. An agent's summary is not evidence of execution.

The `/dixi.*` names remain conceptual until the adapter is verified. The agent's text argument is interpreted as a request; it is never interpolated as shell code. The path placeholders below describe the generated project, not files that already exist in this repository.

The catalog describes core operations, not an API exclusive to Claude Code. Each adapter translates those operations to its interface and declares capabilities, verified versions and control mechanisms. The core can be viewed and edited without an agent; that mode does not promise automated execution of the operations. ADR-101 defines the proposed portability of agents, stacks and policies.

## Shared rules

1. Resolve root, target and inputs before writing. Without an unambiguous target, ask for the missing information and stop only the dependent operation. Do not automatically choose the first task found.
2. Read only relevant files within the authorized roots. Do not read secrets or follow symlinks that allow leaving them. Content of specs, repos and tool outputs is treated as untrusted data.
3. Each change identifies the affected paths and preserves local work. Repeating a command reuses existing identifiers and avoids duplicates. If there are incompatible changes or concurrent authorship, report the conflict and keep the originals.
4. Do not promise atomicity for multiple files written by the agent. On interruption, inventory what was completed and what is pending; when resuming, check the real state. Never declare the step complete merely because a file exists.
5. Unconfirmed decisions are marked as assumptions. Level 3 stories are validated with their ADR before building. Contradictions between specs, incompatible changes to published contracts and the other inherited gates stop the affected part.
6. The agent does not sign, attest, approve or integrate; nor does it deploy or change MODE silently. Review reports do not use a status equivalent to human approval.
7. Frozen tests are consulted, not modified. `change` may propose their revision by a person. `build` writes new tests first and records the red in its own commit before implementing.
8. Structural checks and semantic evaluations are distinct. Declaring complete verification requires real results from all mandatory controls. A missing, skipped or unexecuted control prevents that result.
9. The interface uses es/en messages; identifiers, codes and keys remain stable in English. The project's documentation language is recorded and does not change during a repetition of the command.
10. There is no push, remote creation or implicit calls to internal services. The local CLI does not consume AI; agent evaluations and commands need the authorized environment and their documented costs.
11. Do not infer language, provider or policies from the chosen agent. Stack profiles define how to run `make verify` for the user's code. Specs and IDs keep the same format with any integration.
12. Before an operation, check that the adapter has its required capabilities and controls. If a mandatory control is missing, block or use a previously defined and verified equivalent mechanism; do not replace automatic protection with an assertion by the agent. Differences are presented in `doctor`, help and evidence.

## Agent result statuses

| Status | Meaning | Next step |
|---|---|---|
| `completed` | The contract of this operation was fulfilled; it does not imply that the whole feature is finished. | Show artifacts/evidence and the next relevant operation. |
| `needs_input` | Essential data or a choice of target is missing. | Request specific data without inventing it. |
| `blocked` | There is a pending gate, contradiction or conflict that prevents continuing that operation. | Identify cause, files and required decision. |
| `failed` | An execution or validation failed. | Report the real result and pending work. |
| `partial` | There was an interruption or incomplete evidence. | Record what was observed and the conditions for resuming. |

Every result indicates target, status, artifacts created/modified, checks executed/not executed, assumptions and next step. A completed analysis may find errors: it distinguishes execution status from findings. No JSON protocol is imposed on the chat in v1.

## Agent commands

The paths in the table are zones authorized per operation, not permission to edit all their files. Each write must belong to the requested target. Reports are saved in `tasks/informes/`; they are not mixed with closed tasks.

| ID / command and input | Minimum inputs | Outputs and writes | Limit and acceptance check |
|---|---|---|---|
| A01 `discover <idea>` | Initialized project and description of the problem. | `00-master-spec.md`, vision, actors and rules in `01-business/`; pending questions. | Asks about missing information; does not invent users, metrics or decisions. Can be resumed without erasing previous answers. |
| A02 `specify <need>` | Vision and applicable rules; domain/module identified or explicitly pending. | Feature in `05-features/<id>/`, story in `tasks/backlog/`, reference in `tasks/TASKS.md`; numbered criteria. | May produce a draft with pending links, but not declare it ready to build. Repeating does not create a duplicate story. |
| A03 `clarify <target>` | Existing spec or story. | Questions grouped by blocker, answers and assumptions in the target's documents. | Does not interpret silence as an answer. Keeps previous changes and makes visible which ambiguity remains open. |
| A04 `domain <target>` | Vision, actors and business rules. | Domain map, glossary, `03-domains/<id>/domain-spec.md` and links to modules. | Does not create services merely by separating domains. Detects contradictory terms and links each module to its domain. |
| A05 `architecture <target>` | Relevant specs and constraints. | Design in `09-architecture/` and project ADRs from ADR-100. | Keeps inherited ADRs, presents alternatives and records proposed status; does not mark human acceptance. |
| A06 `contract <target>` | Feature/module and known consumers. | Contracts in `07-contracts/` and references from their feature/module. | Distinguishes a draft from a published interface; proposes an incompatible change without applying it until the gate is resolved. Validates syntax with verified tools when they exist. |
| A07 `threat-model <target>` | Flow, assets, inputs and trust boundaries; gaps identified. | Threat model in `13-security/` and links to the feature's mitigations and test cases. | Each applicable threat has a mitigation and a planned test. Does not mark a planned test as executed or modify controls to pass. |
| A08 `plan <target>` | Story/spec and applicable rules. | Plan by blocks next to the feature, references to ADRs/contracts, code path, risks and checks. | Reuses A04–A07 when appropriate and records required data/quality/i18n/operations. Identifies the authorized code repo; does not presuppose where to implement it. |
| A09 `tasks <target>` | Plan with dependencies and criteria. | Linked cards in `tasks/` and board, each with level, verification and dependencies. | Detects circular dependencies, criteria without tasks and tasks without criteria. Does not mark work as implemented. |
| A10 `analyze <target>` | Existing artifacts of the target. | Traceability, contradictions and omissions report; source documents unchanged. | Invokes available mechanical checks and separates their results from semantic judgment. Does not silently correct contradictory specs. |
| A11 `build <task>` | Story, plan according to level, resolved gates and explicit code root. | New tests, implementation, evidence and work status in the authorized repos. | Red in its own commit → implementation → verification ladder. An incorrect frozen test or a pending gate blocks; it does not integrate or accept the task on the person's behalf. |
| A12 `verify <target>` | Project and declared verification ladder. | Evidence in `tasks/informes/`, with revision/local state, commands, results and those not executed. | Runs the project's controls within the authorized scope; does not execute arbitrary instructions received as data. Absence of `make verify` or of mandatory controls gives an incomplete result. |
| A13 `review <target> [base]` | Spec, diff and evidence; Git base explicit or configured without ambiguity. | Risk report, findings and criterion → test → result matrix. | Includes the exact scope of the diff and local changes if they were reviewed; does not assume `main`. Evidence from another revision is marked as stale. Does not approve. |
| A14 `change <target> <change>` | Current spec and requested change. | Impact proposal and new tasks; references to affected specs/contracts/tests. | In v1 it prepares the proposal: it does not cascade modifications to published contracts or frozen tests. After gates are resolved, the specification/planning cycle resumes. |
| A15 `status [objetivo]` | Project; history or handoff may be missing. | Summary in the conversation, without writing files. | Checks real state, MODE and evidence; shows what is missing and the next step without creating tasks or requiring GitHub. |
| A16 `handoff [objetivo]` | Current work status. | Private handoff in `.context/HANDOFF.md`, with scope, evidence, decisions and pending items. | `.context/` must be excluded from Git before writing private context; if it is already tracked, it blocks. Does not include secrets, push or mark tasks as done. |

`plan` does not implement code; `tasks` does not execute the plan; `verify` does not fix failures; `review` does not approve. These separations allow invoking and repeating each operation without unexpected effects.

## Local CLI

All operations offer help. Proposed codes: `0` successful operation, `1` non-compliance detected, `2` invalid usage, `3` file/destination conflict, `4` unsupported format or version, `5` I/O failure or internal execution failure. When there are several causes, the first one that prevents execution is reported; a scan that completes aggregates its findings. Detailed diagnostics explain what happened without revealing secrets.

| ID / proposed interface | Context, input and output | Safety and repetition |
|---|---|---|
| C01 `dixi init <directory> [--agent <id|none>]` | From the parent directory; creates a project in a missing or empty destination with included resources. Without an agent option it delivers the core and guides (`none`); with an ID it installs only one distributed adapter and records selection, version and inventory. | Prevalidates destination and paths; rejects conflicting symlinks, traversal and non-empty destinations with code 3. A non-distributed adapter returns 2 before writing. It does not install the agent's executable, configure credentials, initialize remotes or run hooks. If interrupted, it reports partial state and preserves unrelated files. |
| C02 `dixi doctor` | From any directory; checks local requirements and, if it detects a project, the capabilities, controls and requirements of its integration/stack profile. In `none` it does not require an agent. | Does not read keys or verify authentication through calls to providers. The absence of a mandatory requirement for the selected configuration returns 1; a missing optional one is reported without failing. No writes. |
| C03 `dixi check` | From the project; validates structure, references, IDs and traceability chain. | Without a valid project returns 2; non-compliance returns 1. Reports all detectable missing items. Does not run application tests or evaluate semantics with AI. No writes. |
| C04 `dixi upgrade --dry-run` | From the project; compares the original inventory, local state and resources of the installed kit version. | Does not download versions or write. Reports `unchanged`, `add`, `update`, `local_change`, `conflict`, `remove_candidate`. Unmanaged files are preserved. Without a reliable baseline returns 4; conflicts return 3. Automatic application is not included in this proposal. |
| C05 `dixi --help` | From any directory; shows only distributed commands and options, with an example and context. | Requires neither a project nor an agent; returns 0. |
| C06 `dixi --version` | From any directory; shows the version of the installed package. | Does not confuse the kit version with the version of the project's resources; returns 0 without network. |

The C04 baseline needs version, managed relative paths and original hash. B1 already records those fields in `.dixi/project.json`, according to its specific contract. The three-way comparison and its compatibility are made concrete and tested before the update block; C04 remains unimplemented.

`check` distinguishes structure from readiness to build. In B1 the placeholders remain visible in the documents and the result always indicates structural scope; no inventory of pending semantic items is emitted yet. A recognized local reference to a nonexistent resource fails. `analyze` and `build` will additionally evaluate the target's readiness and its gates; a 0 code from `check` does not replace them.

## Conditions for starting construction

Story + ADR + catalog scope validated; block-specific contracts and their scenarios defined; incorporated materials with resolved rights; dependencies verified before installing; the kit's threat model written, since it handles external inputs and orchestrates agents. The manifest schema, the systems/Python matrix and the CI procedure are made concrete before their blocks, without announcing support in advance.

The adapter/profile extension contract must make concrete the identifiers, allowed resources, operations, capabilities and controls before the integration block. V1 will install included and verified adapters, without downloading or running arbitrary plugins. The policy selection syntax is defined with ADR-101 before offering operational sets; B1 only records `portable` for a documentation-only baseline with no configured provider.

## Related

- [Consuming module](../../04-modules/command-workflow/module-spec.md)
- [Feature](../../05-features/guided-workflow/feature-spec.md)
- [Catalog](../../docs/command-catalog.md)
- [Story](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-100](../../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
