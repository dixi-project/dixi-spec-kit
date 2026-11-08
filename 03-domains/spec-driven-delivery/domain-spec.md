# Domain — Specification-driven development

## Purpose

Define the rules of the public workflow of DIXI Spec Kit. Status: proposal for GOAL-001; it does not describe an existing implementation.

## Boundaries and concepts

The domain coordinates project, goal, artifact, decision, task, evidence and gate. A command transforms or inspects those elements with an explicit scope. The agent interface and the CLI share their rules, although only the agent interprets needs expressed in natural language.

Out of scope: production execution, human approval, compliance certification and Dixi's internal services. A project may have separate code repos; the plan identifies the authorized roots before building.

## Business rules

- BR-001: every task links its business goal, domain, module and feature; contracts and tests complete the chain depending on the stage. Pending links prevent declaring readiness to build.
- BR-002: installing and generating do not require private credentials, registration in the internal task system or AI/AWS consumption. Using the agent does require the documented authorized environment.
- BR-003: repeating or resuming preserves decisions, identifiers and local changes. A conflict is not resolved by silently overwriting.
- BR-004: a piece of evidence corresponds to a specific revision or state and distinguishes execution, failure and absence of execution. A later change requires re-evaluating the affected evidence.
- BR-005: validation of a structural story, acceptance of ADRs, signatures, attestations, approvals and integration belong to the person according to the standard; the kit records their status, it does not impersonate them.
- BR-006: an incompatible change to a published contract and the revision of a frozen test require resolving the corresponding gate before applying the change.
- BR-007: inherited standards remain in force and exceptions need their own ADR. A deferred specialized command does not remove its mandatory controls.
- BR-008: help, documentation and publication announce only verified capabilities and materials with resolved rights.
- BR-009: agent, stack and policies are explicit choices, separate from the core. The absence of an integration does not prevent documentation-only use; it does not imply workflow automation. A change of tool preserves the canonical artifacts and their identifiers.
- BR-010: each adapter declares its effective controls; a missing capability is not presented as implemented. Provider separation for external projects applies only after ADR-101 is validated.

## Related

- [Goal GOAL-001](../../01-business/vision/product-vision.md)
- [Module](../../04-modules/command-workflow/module-spec.md)
- [Story](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
