# Feature — Installable local core B1

## Purpose

Deliver the first local workflow of TASK-001: install, view help, generate without an agent, diagnose and check structure. The user authorized moving forward with this block after validating the open approach.

## Story and criteria

As an external user I want to create an SDD baseline with local resources so I can apply the method with my own tools without requiring internal accounts or specific agents.

- LC-01: help and version work outside a project; they only announce implemented operations.
- LC-02: init creates resources, baseline and es/en traceability in a new/empty destination and does not execute external code.
- LC-03: occupied destinations, unsafe paths and missing adapters are rejected before writing; repeating preserves files.
- LC-04: doctor does not require an agent in `none`; check distinguishes valid structure, incorrect links/IDs/parents and a missing project, without modifying files.
- LC-05: malformed metadata, external paths, symlinks, special files and excessive sizes produce controlled errors without reading outside the project.
- LC-06: wheel/sdist include only the chosen material, install in clean environments and produce the same verifiable result.

## Verification

`tests/test_local_core.py` covers the contract observable through the CLI; `tests/test_distribution.py` validates artifacts and installation. `tests/test_safety_edges.py` and `tests/test_link_destinations.py` cover regressions in reading, paths, limits and interruptions. The BDD matrix links those cases without requiring an additional Gherkin runner. `make verify` integrates tests and the distribution check; its result is in the [B1 report](../../docs/b1-verification.md), separate from the full launch.

## Related

- [Parent module](../../04-modules/command-workflow/module-spec.md)
- [B1 contract](../../07-contracts/commands/local-core-contract.md)
- [Scenarios](scenarios.feature)
- [Acceptance](acceptance.yaml)
- [Threats](../../13-security/local-core-threat-model.md)
- [Story](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
