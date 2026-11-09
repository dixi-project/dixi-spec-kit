# Checklist 02 — Architecture

> **Evidence rule.** Score only what an artifact proves. A missing artifact is recorded as "no evidence" and scored 0; it is never filled with an assumption presented as fact.

## Purpose

Assess whether the architecture is documented, matches the running system, supports the stated non-functional requirements and can evolve without a rewrite.

Status: draft. {{pending: confirm which systems and integrations are in scope}}

## Inputs

- [System context](../../09-architecture/system-context.md), [Container diagram](../../09-architecture/container-diagram.md), [Component diagram](../../09-architecture/component-diagram.md)
- [ADR index](../../09-architecture/adr/README.md)
- [Integration architecture](../../09-architecture/integration-architecture.md)
- [Resilience architecture](../../09-architecture/resilience-architecture.md) and [Performance architecture](../../09-architecture/performance-architecture.md)
- [Security architecture](../../09-architecture/security-architecture.md)
- [Non-functional requirements](../../11-quality/non-functional-requirements.md)

## Items

| ID | Question | Evidence (artifact) | Score 0–5 | Finding |
|----|----------|---------------------|-----------|---------|
| ARC-01 | Do diagrams exist and match what is deployed today? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| ARC-02 | Are significant decisions recorded as ADRs with context and consequences? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| ARC-03 | Are module boundaries clear, with dependencies flowing one way? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| ARC-04 | Are external integrations documented with contracts and failure handling? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| ARC-05 | Are non-functional requirements stated and tested? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| ARC-06 | Are failure modes known (timeouts, retries, degradation)? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| ARC-07 | Can the system scale the expected load without redesign? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| ARC-08 | Is known technical debt listed with impact and plan? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| ARC-09 | Is there lock-in to a provider, and is it a recorded decision? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |

## Red flags

- No diagram, or diagrams that contradict the running system.
- Critical decisions only in someone's memory.
- A shared database used by unrelated services with no ownership.

## Output

- Area score: {{pending: score and method}}
- Findings carried to the [DD report](../dd-report-template.md).

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 01 — Infrastructure](01-infrastructure.md)
- [Checklist 03 — Source code](03-source-code.md)
- [Final checklist](11-final-report.md)
