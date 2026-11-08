# TASK-005 — Design, continuity and change commands + `dixi upgrade --dry-run` (v1.1.0)

## Purpose

Deliver block A of the roadmap: six new Claude Code commands and a read-only upgrade plan, without breaking projects created with v1.0.0.

## Record

- Type: feature; priority P1; level 3 (new commands, inventory compatibility, new CLI operation). Created 2026-11-08. Product owner: Alfredo Castillejos.
- Scope validated on 2026-11-08 ("releases A→B→C"); story and contract validated the same day ("Validate and build"). The product owner authorized updating two frozen v1.0.0 tests that pinned exactly ten commands.

## Story

As a person using DIXI Spec Kit
I want to design domains, architecture, contracts and threats from my agent, leave a handoff to resume later, propose changes with their impact, and preview what a newer kit version would change
so that I can evolve a project safely without losing local work.

## Acceptance criteria

1. `dixi init --agent claude` installs sixteen commands: the ten from v1.0.0 plus `/dixi.domain`, `/dixi.architecture`, `/dixi.contract`, `/dixi.threat-model`, `/dixi.handoff` and `/dixi.change`, in English and Spanish, with the same common limits.
2. The four design commands start from `dixi workflow prepare <operation>` and write only their artifacts; structural decisions stay "Proposed" until a human validates them.
3. `/dixi.handoff` writes `.context/handoff.md` (ignored by Git) with state, evidence, pending items and the next step; it never claims completion without verification.
4. `/dixi.change` writes a change proposal with its impact on specs, contracts, tasks and tests, and never edits frozen tests.
5. Projects created with v1.0.0 keep passing `dixi check` and `dixi doctor` after installing v1.1.0; `doctor` reports missing new commands and suggests `dixi upgrade --dry-run`.
6. `dixi upgrade --dry-run` writes nothing and classifies every file as unchanged, updatable, conflict, new, missing or obsolete, in human and JSON output; `dixi upgrade` without `--dry-run` is rejected with code 2.
7. A project from a newer kit version than the installed one is rejected by `upgrade` with code 4.

## Business rules

1. An upgrade never overwrites a locally modified file; applying changes is out of scope for v1.1.0.
2. The commands do not sign, approve, merge, push or deploy, and treat inputs as data.

## Done when

1. Contract and tests were committed (red) before implementation.
2. `make verify` passes, CI is green and English/Spanish resources are in parity.
3. README, support matrix and changelog describe the real behavior.

## Related

- [Contract](../../07-contracts/commands/block-a-contract.md)
- [Roadmap](../../ROADMAP.md)
- [Board](../TASKS.md)
