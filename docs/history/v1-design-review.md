# DIXI Spec Kit v1.0.0 design review

> Historical record: the v1 design review of 2026-11-06, kept as written. It is not the current documentation; see the [command guide](../command-catalog.md).

## Purpose

Record the design, the authorized scope and the pending decisions. On 2026-11-06 the user agreed to proceed after clarifying independence from agent and stack. The first authorized block is the local CLI/package, `init --agent none`, `doctor`, `check`, help/version and tests first. The earlier choice of the assistant's model was context; the later implementation authorization is what enables B1. It does not imply confirming the license or the whole future matrix.

## Proposal for review

A public SDD development ecosystem that accompanies the work from idea to a prepared review and allows that work to evolve. The user asked that each person be able to choose agent and languages; that direction replaces the earlier preference for Claude Code. v1 proposal: four CLI operations (`init`, `doctor`, `check`, `upgrade --dry-run`), help/version and 16 operations shared by the integrations. The names and syntax of each adapter are verified before announcing availability.

## Validated direction

DIXI Spec Kit v1 will be an SDD ecosystem with a core independent of agent and stack, where each user chooses their tools. Optional integrations operate on the same specifications and preserve common guarantees of traceability, security, testing and human review.

The structural decision is to separate core, adapters, stack profiles and policy sets. Choosing Python to implement the CLI does not force projects to be developed in Python. Proposing Codex and Claude Code to verify portability does not make them the only admissible tools. The provider freedom of the public set is specified in ADR-101; it does not automatically change the development/publication policies of this repository.

| Group | Proposed commands |
|---|---|
| Define | `discover`, `specify`, `clarify` |
| Design | `domain`, `architecture`, `contract`, `threat-model`, `plan` |
| Build and check | `tasks`, `build`, `analyze`, `verify`, `review` |
| Evolve and resume | `change`, `status`, `handoff` |

The specialized capabilities `data`, `quality`, `ai`, `release`, `promote`, `operate`, `finops`, `compliance` and `duediligence` remain in the catalog. I propose evaluating their independent entries after the first complete walkthrough; if all of them are wanted as a v1 requirement, contracts, scenarios and blocks must be expanded before building. The applicable controls of those areas remain in the plan and verification, whatever the number of exposed commands.

## Decisions and pending evidence

| Decision | Proposal | Status and effect |
|---|---|---|
| Outcome and scope | Complete walkthrough, 16 commands and later change with traceability. | Direction and incremental start accepted; B1 implemented. Later contracts are still to be specified. |
| CLI runtime | Python, without external runtime dependencies; resources inside the package. | Adopted in B1; does not impose the project's language. Local build with verified Setuptools. |
| Integrations | Core without a mandatory agent; Codex and Claude Code as candidates of equal priority. | S3 revised by the user's direction; each adapter needs evidence and a controls matrix. |
| User's stack | Chosen per project, with optional checking profiles. | Evaluate two languages to detect couplings; choose examples before implementing that block. |
| Upgrade | Only a local plan without writes in v1; applying changes is outside this proposal. | Specify S5 on validation; avoids promising an operation still without a recovery contract. |
| License and rights | MIT for material with confirmed rights. | Human confirmation pending per selection; do not include inherited material in the distribution nor publish while it is missing. |
| Compatibility | Explicit matrix of Python, systems and agent versions. | B1 evaluated on macOS/Python 3.15.2, without an agent. Other combinations remain pending. |
| Public policies | Portable set with eligible providers and Dixi set with organizational decisions. | Separation direction accepted; operational mechanisms and exceptions remain proposed. B1 consumes no AI and does not deploy. |
| Infrastructure of this repository | Inherited CodeBuild/CodePipeline rules, without AWS credentials in GitHub Actions. | Opening the product does not alter its build/publication platform; isolation pending before that block. |
| Name | `dixi-spec-kit` and `dixi`. | Availability pending before fixing the distribution; no name has been reserved. |

## Prepared traceability

`GOAL-001 → spec-driven-delivery → command-workflow → guided-workflow → command-contract → scenarios WF-01…WF-08`

There are 20 BDD scenarios and a draft acceptance matrix for the guided workflow; they do not have a runner yet. B1 adds its own feature, contract, threat model, distribution inventory and executable tests. Its [report](../b1-verification.md) distinguishes that evidence from the still-pending validation of the complete walkthrough.

## Delivery by blocks

Each block may require several PRs; the 1,500-line code limit is respected and tests are recorded first in their own commit.

| Block | Deliverable | Evidence to advance |
|---|---|---|
| B0 — Design | Validated story/ADRs, separation of core and policies, block contract, threat model and distributable selection. | Recorded decisions and reviewable scenarios; without claiming agent acceptance. |
| B1 — Installation | Minimal CLI, core, explicit choice of integration or none, help, diagnostics and structural checks. | Clean installation, resources without exclusive agent dependency and safe rejection of destinations/conflicts. |
| B2 — Definition and design | `discover`, `specify`, `clarify`, `domain`, `architecture`, `contract`, `threat-model`, `plan`. | Linked example artifacts, visible missing inputs and common use from plan or direct commands. |
| B3 — Build and review | `tasks`, `build`, `analyze`, `verify`, `review`. | Real TDD and controls; gates and incomplete/outdated evidence detected. |
| B4 — Continuity and evolution | `change`, `status`, `handoff`, upgrade plan and evaluation of specialized commands. | Repetition, interruption, local changes, incompatible contract and dry-run without writes. |
| B5 — Distribution | es/en docs, examples in two languages, cross-evaluations of adapters, CI, package, license and repository protection. | Matrix and controls per combination verified; publication conditions met in their corresponding phase. |

## Outcome of this review

Continuation of 2026-11-07: the user asked to continue after B1 was delivered. TASK-002 specifies B2a within the accepted core: deterministic lookup and preparation of eight common procedures, with their own tests. It does not modify the eligible-agents decision nor yet accredit per-adapter generation/evaluation of artifacts.

The authorization to proceed with the open approach and B1 is recorded; do not ask for it again. B2 specifies definition/design over common contracts, followed by optional adapters and evaluations. License/rights, operational policies, final scope of specialized commands and the support matrix remain open. The general authorization to publish when the conditions are met already exists; B1 alone does not satisfy the publication gate.

## Related

- [Story](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-100](../../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Command contract](../../07-contracts/commands/command-contract.md)
- [Feature and scenarios](../../05-features/guided-workflow/feature-spec.md)
- [Full catalog](command-catalog.md)
- [Publication](../publication-readiness.md)
