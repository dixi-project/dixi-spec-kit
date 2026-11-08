# ADR-104 — Project profiles and generic content templates

## Purpose

Decide how DIXI Spec Kit grows from a minimal documentary baseline (16 files) to the full method content of Dixi's private ecosystem (29 areas), without loading small projects with ceremony and without publishing internal material.

## Status

Accepted on 2026-11-08 by the responsible person, who, on behalf of Dixi Project as owner of the ecosystem, authorized publishing generic rewrites under MIT and kept `minimal` as the default profile. Implementation in [TASK-008](../../tasks/backlog/TASK-008-profiles-and-core-templates.md) and [TASK-009](../../tasks/backlog/TASK-009-remaining-content.md).

## Context

- The kit already ships the method: 25 operations with traceability and human gates for Claude Code and Codex. Several of them write in areas for which `dixi init` installs no template (`08-data`, `09-architecture`, `13-security`, `21-ai`, `22-finops`, `23-compliance`, `28-due-diligence`).
- Dixi's private ecosystem holds ~795 files across 29 areas under a proprietary license that forbids public redistribution. Part of it is generic (standards, guides, templates); part is internal (Dixi's own ADRs, AWS accounts and customers, team, CI on CodeBuild, the "AI only through Bedrock" rule, backlog and history).
- The ecosystem already solves "a landing page should not carry a platform's ceremony" with profiles (site, application, platform, plus a regulated modifier).
- `dixi init` keeps its templates in one JSON file per language, capped at 500 entries, and the project inventory is capped at 500 managed files.

## Decision

1. **Profiles.** `dixi init` gains `--profile minimal|site|app|platform` and `--regulated`. `minimal` is the default and produces exactly the current baseline, so nothing changes for anyone who does not opt in. `--regulated` adds compliance, due diligence and stricter security content to `site`, `app` or `platform`; it is rejected with `minimal`.
2. **Content is rewritten, not copied.** Dixi Project, as owner of the ecosystem, authorizes publishing *generic rewrites* of its method content under the kit's MIT license, in English and Spanish. Internal material is never published: Dixi's ADRs, accounts, customers, team and service catalogs, CodeBuild/CodePipeline pipelines, provider rules, backlog, migrations, `.context` and the proprietary license.
3. **Provider and stack neutrality.** Templates name no AI provider, cloud account, company or customer as a requirement. Examples use placeholders (`{{pending: …}}`) and neutral names.
4. **Templates live as files.** Templates move from the per-language JSON to a file tree inside the package (`resources/templates/<language>/<path>`), with one manifest (`resources/profiles.json`) that assigns each path to profiles. The existing JSON baseline remains the `minimal` set.
5. **Profile templates are optional after creation.** The person may delete templates that do not apply. `dixi check` keeps requiring the core files and the v1.0 agent files; a deleted profile template is reported as `missing` by `dixi upgrade --dry-run`, not as an error.
6. **Limits.** The managed-file limit rises from 500 to 1 000 to fit `platform --regulated` with an adapter and future growth.
7. **Leak guard.** A public test rejects internal markers in every template (ecosystem identity, provider-only rules, CI vendor names, 12-digit account numbers, e-mail addresses outside `example.com`). Customer names are checked by a private list the owner keeps outside the repository, because publishing that list would itself leak them.

## Alternatives considered

- **Publish the ecosystem as is.** Rejected: it requires relicensing internal material and cannot be undone once forked.
- **A private preset for Dixi only.** Not rejected, but deferred: the public kit first needs the generic content; a private preset can later add Dixi's own rules on top.
- **Install everything in every project.** Rejected: hundreds of files for a landing page bury the few documents that matter.

## Consequences

- Profile choice becomes part of `.dixi/project.json` (`profile`, `regulated`); projects without those fields are `minimal`.
- Older 1.x kits ignore the new fields; the files they do not know are left alone.
- Changing the profile of an existing project is not automated in this ADR: `dixi upgrade --dry-run --profile <name>` will show what would be added, and applying upgrades stays on the roadmap.
- Translation doubles the content to maintain. Parity tests keep both languages aligned.

## Related

- [ADR-101](ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [ADR-102](ADR-102-recorte-de-alcance-v1.md)
- [Profiles contract](../../07-contracts/commands/profiles-contract.md)
- [Remaining content contract](../../07-contracts/commands/remaining-content-contract.md)
