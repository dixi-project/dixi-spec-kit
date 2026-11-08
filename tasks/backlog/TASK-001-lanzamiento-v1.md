# TASK-001 — First public distribution of DIXI Spec Kit v1.0.0

## Purpose

Define a verifiable story before implementing a public distribution derived from selected EIS-IA materials.

## Metadata

- Type: feature. Priority: P1. Level: 3, structural.
- Status: in progress; B1 and B2a implemented; B3 (Claude Code adapter, [TASK-003](TASK-003-adaptador-claude-code.md)) in progress.
- Created: 2026-11-06. Product Owner: Alfredo Castillejos.
- Validation: on 2026-11-06 the user agreed to continue with the approach open to agents/languages and the first functional block with tests first. Incremental implementation of TASK-001 is authorized, starting with CLI/package, `init --agent none`, `doctor`, `check`, help/version. The prior authorization to publish when ready still stands. On 2026-11-08 the responsible person validated the set story + [ADR-102](../../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md) + assumptions: scope cut, MIT + DCO license and `upgrade --dry-run` deferred to v1.1. Criteria 5, 12, 13, 15 and 16 were adjusted to that cut.

## User story

As the person responsible for Dixi Project,
I want to offer DIXI Spec Kit as a public, installable and versioned tool with commands to define, build, verify and evolve products,
so that third parties can apply our SDD development ecosystem with the agent and stack they choose, create forks and adopt improvements, while Dixi keeps control of the official repository.

## Acceptance criteria

1. An external person installs the v1 artifact and consults help and version without Dixi credentials.
2. They can generate a new project and run its checks without access to the private repository or registration in the internal task system.
3. A non-empty destination or a conflict does not cause overwriting or deletion of the user's work.
4. They can learn about requirements and problems in their environment through diagnostics and documented exit codes.
5. ~~They can preview an upgrade without changing any file~~ — deferred to v1.1 (ADR-102). In v1.0.0 the documentation does not promise upgrades and `dixi --help` does not show it.
6. They find installation guidance in Spanish and English, a reproducible example and announced agent/system support backed by evidence.
7. The distribution contains only selected materials with confirmed rights, without private history or operational configuration.
8. The public repository allows forks; only authorized maintainers can incorporate changes through the review process and checks.
9. The first public release is identified as v1.0.0, independently of the private EIS-IA versions.
10. In the supported agent, a person walks through discovery → specification → plan → tasks → build → verification → review preparation on the public example, with linked artifacts and verifiable results.
11. The included commands have contracts for inputs, outputs, errors, gates and continuity; an interruption or repetition does not silently overwrite decisions or local changes.
12. They can prepare domain design, architecture, contracts and threats through `dixi workflow prepare`, and obtain with `/dixi.analyze` a traceability and impact report when changing a feature. The applicable gates are respected and frozen tests are not modified.
13. They can consult the status and the next step with `/dixi.status`; the help distinguishes installed commands from capabilities not yet included. `handoff` moves to v1.1.
14. They can use the documentation core and its validations without a mandatory agent, or choose a published integration; installing an integration does not modify their specs, contracts or tasks to adapt them to an exclusive format.
15. They can apply the method to different languages and frameworks; the CLI runtime does not fix the project's. In v1.0.0 one public example demonstrates the flow; the second language moves to v1.1 (ADR-102).
16. They can consult capabilities and controls of the published integration (support matrix); a missing capability is reported and is not presented as available automation or protection.

## Business rules

1. The private EIS-IA repository remains private and is not altered for this preparation.
2. An installation does not require internal accounts, does not create remotes and does not consume AI or AWS by surprise.
3. Traceability and human accountability are preserved; AI does not sign, attest, approve or merge.
4. No command, integration or license is announced that is not yet implemented or resolved.
5. The AWS/Bedrock rules are not relaxed without an exception ADR.
6. The public remote is created when the publication gate is met, according to the user's authorization.
7. The core does not require a specific agent, model, language or framework. The choice of providers/policies for external projects is governed by ADR-101 once validated, without changing the origin's rules or this repository's development rules.

## The story is considered done when

1. The story and the ADR were validated by the responsible person.
2. The criteria have acceptance and security tests; the red is recorded first in its own commit.
3. `make verify` passes and installation from wheel and sdist is tested in clean environments, in addition to the generated example.
4. The distributed inventory, the rights and the secret scan are resolved.
5. es/en documentation and the maintenance procedure reflect the final implementation.
6. The public repository configuration and the v1.0.0 release are verified, respecting the actions reserved to a person.
7. The distributed commands pass their script tests and agent evaluations; the example covers creation and evolution, and does not reference private or missing resources.

## Assumptions to review

- S1: adopted in B1: Python CLI with the standard library at runtime and packaged resources. This does not restrict the projects' languages. Setuptools is used only for build; provenance and version in the B1 contract.
- S2: `dixi` as the executable and `dixi-spec-kit` as the package/repository. The `dixi-project/dixi-spec-kit` repository already exists (private); availability on PyPI is resolved when publishing the package, an operation separate from v1.0.0.
- S3: agent-independent core at the user's direction. ADR-102 validated: Claude Code is the only adapter in v1.0.0, together with documentation-only use without integration; Codex moves to v1.1. Do not announce compatibility just for having AGENTS.md; each adapter needs its own tests and controls matrix.
- S4: resolved: MIT + DCO (2026-11-08). Only materials written for this product are distributed.
- S5: resolved: upgrade deferred to v1.1.
- S6: the proposed catalog covers the main flow and Dixi's design and traceability capabilities; specialized interfaces are explicitly prioritized before announcing v1. The user asked to consider missing commands; the selection and the concrete contracts remain pending validation.
- S7: the `/dixi.*` names are conceptual until the adapter syntax is verified. Deterministic tests and agent evaluations provide different evidence and both are necessary.
- S8: concrete review proposal: 16 agent commands and four CLI operations; nine specialized entries to prioritize. The contract proposes limiting upgrade to dry-run in v1 and using a public example of fictitious notes to evaluate the flow and its evolution. These decisions remain pending joint validation.
- S9: ADR-101 records the accepted direction and proposes mechanisms for portable public policies and Dixi organizational policies. Operational exceptions remain pending for their blocks. The opening does not attest universal technical support nor authorize other platforms to develop/publish this repository; B1 does not consume AI or deploy.

## B1 progress

Implemented help/version, creation without an agent, diagnostics, structural check and local distribution `1.0.0.dev0`. Acceptance tests frozen before implementing; security regressions added in separate commits. Resources written for this product, without copying proprietary templates. See the [verification report](../../docs/b1-verification.md) and the [local guide](../../docs/local-development.md).

This provides partial evidence for criteria 1–4, 6, 11 and 14. It does not complete the story: missing are upgrade, commands/adapters, examples in two languages, operational controls, expanded matrix, rights/license, publication scan and release.

## B2a progress — 2026-11-07

[TASK-002](TASK-002-operaciones-compartidas-b2.md) implements `workflow list/show/prepare` for the eight definition/design recipes. See the [evidence](../../docs/b2-verification.md). It provides shared preparation and verifiable context; artifact production and evaluation in integrations remain pending. It does not complete the agent execution criteria or the launch.

## Validated cut — 2026-11-08

[ADR-102](../../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md) was accepted: one adapter, ten commands, one example and upgrade deferred, after the [comparison with GitHub Spec Kit](../../docs/spec-kit-comparison.md). The derived block is [TASK-003](TASK-003-adaptador-claude-code.md).

## v1.0.0 progress — 2026-11-08

Claude Code adapter, example, public documentation, CI (ADR-103 proposed), allowlist exporter, MIT license and version 1.0.0 verified ([evidence](../../docs/b3-verification.md)). The actions reserved to a person in the [publication gate](../../docs/publication-readiness.md) remain.

## Traceability

- [Product](../../docs/product-spec.md)
- [Proposed command catalog](../../docs/command-catalog.md)
- [Joint design review](../../docs/v1-design-review.md)
- [Business goal](../../01-business/vision/product-vision.md)
- [Domain](../../03-domains/spec-driven-delivery/domain-spec.md)
- [Module](../../04-modules/command-workflow/module-spec.md)
- [Feature and scenarios](../../05-features/guided-workflow/feature-spec.md)
- [Command contract](../../07-contracts/commands/command-contract.md)
- [B1 feature](../../05-features/local-core/feature-spec.md)
- [B1 contract](../../07-contracts/commands/local-core-contract.md)
- [ADR-100](../../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Board](../TASKS.md)
- [Publication](../../docs/publication-readiness.md)

The documentation chain business → domain → module → feature → contract → BDD scenarios covers the design of criteria 10 to 16; its guided-flow scenarios do not yet have a runner. B1 does have specific executable tests for installation, structure and local security. Each subsequent block must complete its particular cases and record red tests before implementing.
