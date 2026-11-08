# TASK-002 — Shared definition and design procedures

## Purpose

Deliver B2a of TASK-001: local access to the eight B2 procedures and verifiable preparation of the context to use them manually or with the chosen tool.

## Record and story

- Type: feature; priority P1; level 2. Medium risk: reading external documents and preparing instructions, without execution or writing to the project.
- Status: implemented and verified locally; human review pending. Date: 2026-11-07.
- Authorization: the user asked to continue after delivering B1 and to present B2 as the next block. It implements the core separation accepted in ADR-100/101; it does not change provider, operational policies or license.
- As a user I want to consult procedures and prepare an explicit target so that I can apply the same method with my tools and keep traceability of the sources reviewed.

## Acceptance criteria

1. `workflow list/show` works without a project and exposes exactly discover, specify, clarify, domain, architecture, contract, threat-model and plan, in es/en.
2. Each procedure contains purpose, inputs, steps, outputs, gates, checks and next steps. The catalog is shared, with no syntax exclusive to one agent.
3. `prepare` requires an operation, a compatible target ID and a non-empty request. It does not pick the first item or interpret a path as an ID.
4. It returns a package with the contract, the request as data, the target, the project language, MODE and a manifest with the current paths/hashes of the target and its ancestors. It does not include document bodies or evaluate their semantics.
5. It verifies metadata/graph and rejects missing files, unsafe paths, symlinks, special files, limits and invalid MODE. It does not read links or unrelated branches of the graph to prepare the manifest.
6. Repeating without changes produces the same package; changes in the sources change their hashes. It does not write, invoke AI, install agents, run project tools or access the network.
7. The result distinguishes preparation from execution of the procedure. It does not mark specs, ADRs, gates or tests as accepted or complete.
8. The resources reach wheel/sdist and the flow works from both artifacts. `make verify` stays green without modifying frozen tests.

## Limits of this increment

B2a prepares instructions and context; it does not generate decisions through inference or install slash commands. Producing/evaluating artifacts with adapters remains pending in B2; the WF-01/WF-02 flow is not declared closed. `1.0.0.dev0` is kept during local development, with no promise of upgrade or release.

## Technical evidence

New tests frozen in `ca43f17` before implementing; unknown-fields regression in `d4d6f93` before fixing it. See [results, artifacts and limits](../../docs/b2-verification.md). No frozen tests were altered and no publication, signing or human approval was performed.

## Related

- [Main story](TASK-001-lanzamiento-v1.md)
- [Feature](../../05-features/workflow-preparation/feature-spec.md)
- [Contract](../../07-contracts/commands/workflow-preparation-contract.md)
- [Threats](../../13-security/workflow-preparation-threat-model.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
