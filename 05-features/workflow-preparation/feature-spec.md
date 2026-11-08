# Feature — Prepare definition and design without coupling an agent

## Purpose

Deliver B2a on the command-workflow module: view eight shared procedures and prepare explicit, verifiable context. A person or a later adapter uses the same contract to produce artifacts.

## Acceptance

- WP-01: complete es/en catalog and recipes, available without a project.
- WP-02: explicit target of the allowed type and a valid request; no automatic selection.
- WP-03: minimal manifest of sources and ancestors, current hashes, limits and confined reading.
- WP-04: prepared, repeatable result with no external effects, clearly distinct from semantic execution.
- WP-05: availability of the workflow in clean wheel and sdist; B1 regression green.

The story and its detailed criteria live in TASK-002. This does not certify assisted spec generation, semantic compliance, verified adapters or the full B2 workflow.

## Verification

New deterministic tests in `tests/test_workflows.py` and `tests/test_workflow_distribution.py`, frozen before implementation. `tests/test_workflow_edges.py` adds regressions for output and shared context. The BDD scenarios link the behavior; no Gherkin runner is required. The later rubric must evaluate the artifacts produced by each integration, including missing decisions and gates. [B2a evidence](../../docs/b2-verification.md).

## Related

- [Parent module](../../04-modules/command-workflow/module-spec.md)
- [Contract](../../07-contracts/commands/workflow-preparation-contract.md)
- [Task](../../tasks/backlog/TASK-002-operaciones-compartidas-b2.md)
- [Scenarios](scenarios.feature)
- [Acceptance](acceptance.yaml)
