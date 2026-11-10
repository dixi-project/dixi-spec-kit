# TASK-003 — Claude Code adapter and main-flow commands

## Purpose

Deliver B3 of TASK-001 under the proposal of [ADR-102](../../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md): install the main-flow commands in Claude Code so that a person can walk through the method inside their agent.

## Record and story

- Type: feature; priority P1; level 3, structural (new adapter, controls and agent execution surface).
- Status: closed on 2026-11-09; released in v1.0.0.
- Dependency resolved: ADR-102 validated and MIT + DCO license decided on 2026-11-08 in the joint level 3 validation.
- As a person who uses Claude Code I want to install the DIXI Spec Kit commands in my project so that I can walk through discovery, specification, plan, tasks, build, verification and review preparation, keeping traceability and the human gates.

## Acceptance criteria

1. There is an adapter contract that declares the verified Claude Code version and syntax, capabilities, controls it automates, controls that remain in CI or review and those it does not support.
2. `dixi init` with the adapter installs only product files, without overwriting existing ones, without implicitly enabled hooks and without consuming AI or network. They are chosen explicitly.
3. Each of the ten commands (`discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze`, `status`) has a contract for inputs, writes, errors, gates, repetition and interruption, and references only distributed resources.
4. The commands do not modify frozen tests, do not sign, attest, approve or merge, and do not skip a gate when information is missing or there is a conflict between specs.
5. Deterministic tests cover installation, conflicts, symlinks and resources; evaluations with controlled inputs cover the commands without requiring identical text.
6. A public example walks through idea → verified code → prepared review and an evolution with impact analysis, with `make verify` green.
7. The published support matrix does not announce capabilities without evidence, nor untested systems.

## Business rules

1. Acceptance tests are recorded red in their own commit before implementing.
2. No command, adapter or control is announced unless it is verified.
3. AWS/Bedrock and the origin's rules are not relaxed without their own ADR; the public adapter follows ADR-101.

## The story is considered done when

1. ADR-102 was validated and TASK-001 updated.
2. The criteria have tests and evaluations, with the prior red recorded.
3. `make verify` passes, including wheel/sdist installed in clean environments.
4. The support matrix and the es/en documentation reflect the actual implementation.

## Progress — 2026-11-08

Implemented tests-first: contract, feature and threats (own commit), 15 red tests (own commit), adapter, es/en resources, `examples/notes` example with evolution and impact. Evidence in [B3](../../docs/b3-verification.md). Pending human review of the PR.

## Closed — 2026-11-09

Released in [v1.0.0](https://github.com/dixi-project/dixi-spec-kit/releases/tag/v1.0.0).

## Related

- [Main story](TASK-001-lanzamiento-v1.md)
- [ADR-102](../../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Command catalog](../../docs/command-catalog.md)
- [Command contract](../../07-contracts/commands/command-contract.md)
- [Comparison with GitHub Spec Kit](../../docs/spec-kit-comparison.md)
