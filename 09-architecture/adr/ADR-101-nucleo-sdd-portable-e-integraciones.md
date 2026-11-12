# ADR-101 — Portable SDD core and eligible integrations

## Purpose

Design DIXI Spec Kit as a public SDD development ecosystem whose method does not depend on a specific agent, model, language or infrastructure provider.

## Status

Direction accepted for incremental implementation on 2026-11-06: a core independent of agent/stack, optional integrations, and starting with a documentary no-agent mode. The B1 authorization is recorded in ADR-100 and TASK-001. The operational mechanisms of the policy sets and their provider exceptions remain proposed for their blocks; B1 does not run AI or configure infrastructure. The inherited rules of this repository have not been changed.

## Context

The previous proposal favored Claude Code because there are reusable commands in the origin. That base must not become a requirement of the public product. Python as the CLI runtime does not determine the language of the generated software either.

Offering different agent interfaces does not by itself resolve provider dependencies: the inherited rules mandate Bedrock, CodePipeline, CodeBuild and AWS secrets services. Public portability requires stating explicitly which items are guarantees of the method and which are organizational implementations of those guarantees.

## Proposed decision

1. **Shared SDD core.** Stories, domains, modules, features, contracts, tasks, decisions and evidence use open formats and stable references. Catalog operations have a common definition, independent of how they are invoked in an agent.
2. **Eligible integrations.** The person selects a published adapter or the no-integration mode. No agent is installed, authenticated or selected implicitly. Codex and Claude Code are initial candidates of equal priority to demonstrate portability; their support is announced only after each one is evaluated.
3. **Documentary use without a mandatory agent.** The no-integration mode delivers structure, templates, operation guides and local validations. It allows the method to be applied with manual editing or one's own tools. It does not promise the automation, hooks or `build` execution of a verified adapter.
4. **Product language separate from the kit runtime.** Python implements the B1 local core. Projects can choose their language and framework, even combine several. A stack profile will connect its checks to `make verify`; it does not turn a specific language into a requirement of the method, nor does it promise to generate any complete application.
5. **Explicit policies.** Propose a portable public set and a Dixi organizational set. Both preserve traceability, risk-based validation of decisions, TDD, test protection, human review, secret protection and verification evidence. The effective options and requirements are shown at initialization.
6. **Provider chosen by the project.** In the public set, agent/model, authentication, AI provider, hosting and CI/CD tools are documented as project decisions. The kit does not create accounts or obtain credentials. The AI provider is not inferred from the agent's name.
7. **Equivalent guarantees, declared mechanisms.** Each adapter identifies which controls it automates, which remain in CI or review and which it does not support. It does not claim a hook exists merely because instructions were written in Markdown. If a mandatory control is missing, the dependent operation is blocked or an equivalent mechanism, previously documented and verifiable, is required.
8. **Switching adapters while preserving the project.** Specs, IDs, contracts, tasks and evidence belong to the core. A future adapter-switch operation must preserve those artifacts and flag lost capabilities; no new public migration command is added yet, and `init` is not assumed to be able to overwrite an existing project.

## Proposed exception and limits

The proposed exception is limited to the public distribution and to external projects that choose the portable set. It does not change the policies of the private origin nor authorize other platforms to build/publish this repository itself. The inherited rules of this repository remain in effect. B1's `policy: portable` label identifies a documentary base with no configured provider; it does not certify operational controls nor yet implement policy set selection.

| Rule or coupling | Proposed public set | Dixi set and development of this repository |
|---|---|---|
| ADR-012 / rule 15: AI via Bedrock with IAM. | Provider and authentication chosen/documented by the project, with credential protection and data limits. | Keeps Bedrock and IAM unless there is another exception of its own. |
| ADR-006 and ADR-014 / rules 10–12: CodePipeline, CodeBuild and AWS runners. | Eligible tools with reviewed PR, checks, separate build and deployment, traceable artifact and a human production gate. No production deploy from the agent. | Keeps the inherited chain and credential separation. |
| Rule 14: Secrets Manager/SSM. | Equivalent secret store chosen by the project; secrets outside the repo and outside the agent's reach. | Keeps the AWS services defined by the rule. |
| Stack assumptions in the origin's commands/templates. | Neutral templates and optional stack profiles; validation connected to the project's tools. | Dixi preferences remain in its set, without carrying them over as a universal requirement. |

Removing human sign-offs, attestation, review, risk limits, i18n, MODE, frozen tests or the `make verify` ladder is not proposed. Choosing a different provider is not the same as disabling controls. MODE promotion and the other gates remain supervised.

Policy sets are not the inherited S/A/P profiles: they are a different dimension. Their format, option names and selection mechanism are specified before implementation. No portable combination is published with contradictory clauses that still require AWS exclusively.

## Compatibility and evidence

| Level | What can be claimed | Evidence required |
|---|---|---|
| Portable method | The operations and artifacts can be understood without a specific agent or stack. | Review of the core, guides and a documentary walkthrough without integration. |
| Verified adapter | The commands work in a stated tool/versions. | Walkthrough, interruptions, gates, artifact preservation and a per-adapter control matrix. |
| Verified stack profile | The example and its checks work on a stated stack/systems. | Real execution of `make verify` and of the example on the declared matrix. |
| Community or manual integration | A documented adaptation path exists. | Identification of provenance, limitations and status, without equating it to official support. |

Proposed neutrality validation: the same use case with Codex and Claude Code, and equivalent examples in two different languages, to be chosen before implementing those blocks. Each adapter is tested against both examples to detect couplings. This accredits those combinations, not universal compatibility. Adapters may translate the same operation into different syntaxes.

## Consequences

The product needs a compatibility and controls matrix, in addition to the operations catalog. Maintaining two adapters and example profiles increases testing and documentation. In return, the core keeps a single source of truth and users can choose tools without redoing their specs.

The availability of an integration does not imply the absence of costs or additional permissions. Installing and validating structure still consume no AI; using an agent requires its chosen environment and provider in accordance with the project's policies.

## Related

- [ADR-100](ADR-100-distribucion-publica-v1.md)
- [Product](../../docs/product-spec.md)
- [Joint review](../../docs/history/v1-design-review.md)
- [Contract](../../07-contracts/commands/command-contract.md)
- [Story](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
