# TASK-009 — Remaining content areas (v1.5.0)

## Purpose

Deliver block E: templates for governance, business, platform, flows, contracts, observability, delivery, operations, product, UX, knowledge base, references, stack templates, FinOps, compliance, research, growth, customer success, fixtures and due diligence, assigned to profiles.

## Record

- Type: feature; priority P2; level 2 (content on the block D mechanism; compliance and due diligence content carries legal-sounding material). Created 2026-11-08. Product owner: Alfredo Castillejos.
- Depends on [TASK-008](TASK-008-profiles-and-core-templates.md). Contract validated on 2026-11-08 ("Approve the three" deviations: `14-delivery`, no `mode` operation, opt-in controls).

## Story

As a team using a DIXI profile
I want the rest of the method's areas available as templates
so that operations such as `operate`, `finops`, `compliance` and `duediligence` start from a structure instead of a blank page.

## Acceptance criteria

1. Each profile installs the files listed in the [contract](../../07-contracts/commands/remaining-content-contract.md), in English and Spanish, in addition to block D.
2. Compliance templates state that they are a working aid, not legal advice, and never claim conformity.
3. No shipped file contains the internal markers of ADR-104 or the material listed as "Not shipped".
4. All block D acceptance criteria 4–6 keep holding with the new files.
5. The kit repository gains `CODE_OF_CONDUCT.md` and `SUPPORT.md`, linked from README and CONTRIBUTING.

## Done when

1. Tests were committed red before the content.
2. `make verify` passes and CI is green.
3. The owner ran the private customer-name check and recorded that it passed.

## Progress — 2026-11-08

Contract tables reformatted (same content) so the generator and tests can read them; red tests committed first. 177 templates per language across the 20 areas, generated into `profiles.json`; `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1, reports to the maintainer's address `acastillejos@dixi-project.com` until a dedicated alias exists) and `SUPPORT.md`. `make verify` green with 143 tests. Pending: the owner's private customer-name check.

## Related

- [Contract](../../07-contracts/commands/remaining-content-contract.md)
- [ADR-104](../../09-architecture/adr/ADR-104-project-profiles-and-content.md)
