# TASK-008 — Project profiles and core templates (v1.4.0)

## Purpose

Deliver block D: `dixi init --profile site|app|platform [--regulated]` with generic templates for the six areas that agent operations already write in (data, architecture, engineering, quality, security, AI).

## Record

- Type: feature; priority P1; level 3 (new CLI options, new metadata, ~100 templates per language, packaging change). Created 2026-11-08. Product owner: Alfredo Castillejos.
- Scope requested on 2026-11-08 ("let's develop the whole proposal") after reviewing the gap with the private ecosystem. Story, contract and [ADR-104](../../09-architecture/adr/ADR-104-project-profiles-and-content.md) pending validation.

## Story

As a team starting a project with DIXI Spec Kit
I want to choose a profile that matches the size and risk of my project
so that I get the standards, guides and blanks my agent operations need, without the ceremony of a larger project.

## Acceptance criteria

1. `dixi init` without `--profile` produces exactly the v1.3 baseline, byte for byte, for every agent and language.
2. `--profile site|app|platform` installs the baseline plus the files of that profile in the [contract](../../07-contracts/commands/profiles-contract.md); `--regulated` adds the R files; `--regulated` with `minimal` and unknown profiles exit 2 without writing.
3. `.dixi/project.json` records `profile` and `regulated`; projects without them are `minimal`; `doctor` reports both.
4. The generated project passes `dixi check` for the seven profile combinations with `none`, `claude` and `codex`, in English and Spanish.
5. Templates exist in both languages with the same paths, follow the template rules (title, Purpose, `{{pending: …}}`, Related) and contain none of the internal markers of ADR-104.
6. A deleted profile template does not fail `dixi check`; `dixi upgrade --dry-run` lists it as missing, and with `--profile` lists the files another profile would add.
7. The inventory accepts up to 1 000 managed files.
8. README (en/es), support matrix and changelog explain profiles and what each one installs.

## Business rules

1. Templates are rewritten generically; nothing is copied from Dixi's internal material (ADR-104, decision 2).
2. No template names an AI provider, cloud account, company or customer as a requirement.

## Done when

1. Contract and tests were committed red before the implementation.
2. `make verify` passes and CI is green.
3. The owner ran the private customer-name check on the templates and recorded that it passed.

## Related

- [Contract](../../07-contracts/commands/profiles-contract.md)
- [ADR-104](../../09-architecture/adr/ADR-104-project-profiles-and-content.md)
- [TASK-009](TASK-009-remaining-content.md)
