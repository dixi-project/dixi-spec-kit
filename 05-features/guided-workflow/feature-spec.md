# Feature — Guided workflow and evolution of a feature

## Purpose

Define how a person uses the kit's commands from a need to a prepared review, and how they resume or change that work. Status: acceptance draft, with no implementation and no tests executed.

## Story and scope

As a person who develops with Dixi, I want commands that keep my decisions, specifications, tasks and checks connected, so I can build and evolve a feature while preserving its context and its controls.

This feature develops criteria 10 to 16 of TASK-001 and depends on a verified local installation. Package preparation/publication and the official repository's controls remain in TASK-001; the scenarios of this feature do not certify those other criteria.

## Acceptance criteria

- WF-01: discovery and specification produce linked artifacts and explicit questions when information is missing.
- WF-02: domain, architecture, contracts and threats feed the same plan both through direct entry and through the guided workflow; each applicable threat is linked to a mitigation and a planned test.
- WF-03: tasks cover the plan's criteria, have a level and verification, and contain no circular dependencies.
- WF-04: build respects the level 3 story gate and TDD; it does not alter frozen tests.
- WF-05: analyze, verify and review distinguish contradictions, unexecuted controls and stale evidence, without approving the change.
- WF-06: repeating, interrupting and resuming preserve identifiers and local changes; status does not write and handoff stays private.
- WF-07: change documents impact and compatibility blockers without automatically applying changes to published contracts or frozen tests.
- WF-08: the installed commands have complete resources and their help does not announce deferred capabilities; the workflow works in the announced adapter and matrix.
- WF-09: the person can choose a distributed integration or none; the core and its validations do not require an agent and the canonical artifacts have the same format.
- WF-10: the examples certify the workflow in two languages, evaluated with each announced adapter; differences in capabilities/controls are shown, and a missing mandatory control blocks the dependent operation if there is no verified equivalent mechanism.

## Proposed evaluation example

A local library of fictitious notes, with no accounts or personal data, allows creating and listing notes. The evolution adds a compatible filter and then requests an incompatible change to a published contract to check that the gate is respected. The es/en texts and the checks are declared in its plan. Equivalent examples are prepared in two languages and each announced adapter is evaluated against both; the stacks and locations are fixed before the build block. The matrix will certify those combinations, not universal support.

No customer information is used. The published version of the contract is represented by an identified evaluation fixture, without publishing a real service. The evidence includes inputs, artifacts, file state, executed controls and the human verdict on the rubric.

## Verification strategy

The [scenarios](scenarios.feature) are BDD specifications still without step definitions or a runner. [acceptance.yaml](acceptance.yaml) is a local design matrix; it does not claim conformance with an inherited schema not yet selected. Before implementing, executable red tests are added in their own commit, along with security cases per command.

Deterministic tests verify paths, structure, inventories, duplicates and script results. Agent evaluations verify decisions, artifacts and respect for gates with a rubric, without comparing literal text. Each of the 16 commands also needs its specific cases before its implementation block; these workflow scenarios do not replace that coverage.

## Related

- [Parent module](../../04-modules/command-workflow/module-spec.md)
- [Story TASK-001](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Contract](../../07-contracts/commands/command-contract.md)
- [BDD scenarios](scenarios.feature)
- [Acceptance matrix](acceptance.yaml)
