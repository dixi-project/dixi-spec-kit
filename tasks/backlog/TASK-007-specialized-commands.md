# TASK-007 — Specialized commands (v1.3.0)

## Purpose

Deliver block C of the roadmap: nine agent operations for data, quality, AI, release, promotion, operations, FinOps, compliance and due diligence, available in both adapters.

## Record

- Type: feature; priority P2; level 3 (new commands with high-risk domains). Created 2026-11-08. Product owner: Alfredo Castillejos.
- Scope validated on 2026-11-08 ("releases A→B→C"). Story and contract validated the same day ("Validate and build"); the product owner authorized extending the frozen operation lists in the adapter and block A tests.

## Story

As a team running a product with DIXI Spec Kit
I want guided operations for data, quality, AI, release, promotion, operations, costs, compliance and due diligence
so that these concerns are specified and evidenced with the same traceability as features, without the agent taking actions reserved to people.

## Acceptance criteria

1. Claude Code installs `/dixi.<operation>` and Codex installs `$dixi-<operation>` for `data`, `quality`, `ai`, `release`, `promote`, `operate`, `finops`, `compliance` and `duediligence`, in English and Spanish, with the common limits.
2. Each operation writes only documents in its area (see the contract) and never executes the action it documents: no migrations, deployments, `MODE` changes, real cost queries or certification claims.
3. Projects created with earlier versions keep passing `check`; the nine operations are optional in their inventory and appear as new in `dixi upgrade --dry-run`.
4. README, support matrix and changelog list the operations and their limits.

## Done when

1. Contract and tests were committed red before the implementation.
2. `make verify` passes and CI is green.

## Progress — 2026-11-08

Contract, authorized test update and red tests first; nine operations in English and Spanish for both adapters; `examples/notes` updated through its upgrade plan. `make verify` green with 119 tests. Pull request pending review.

## Related

- [Contract](../../07-contracts/commands/specialized-commands-contract.md)
- [Roadmap](../../ROADMAP.md)
