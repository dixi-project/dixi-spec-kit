# Contract — project profiles and core templates (block D)

## Purpose

Specify `dixi init --profile` and `--regulated`, the metadata they record and the templates installed for the six areas that agent operations already write in: data, architecture, engineering, quality, security and AI. Implements [TASK-008](../../tasks/backlog/TASK-008-profiles-and-core-templates.md) under [ADR-104](../../09-architecture/adr/ADR-104-project-profiles-and-content.md). The remaining areas follow in the [block E contract](remaining-content-contract.md).

## CLI

```text
dixi [--lang es|en] [--json] init <directory> [--agent none|claude|codex]
                                  [--profile minimal|site|app|platform] [--regulated]
```

- `--profile` defaults to `minimal`, which installs exactly the v1.3 baseline, byte for byte.
- `--regulated` adds the files marked **R** below. With `minimal` it exits 2 without writing.
- Unknown values exit 2 without writing. Destination rules are unchanged ([B1 contract](local-core-contract.md)).
- `dixi upgrade --dry-run [--profile <name>] [--regulated]` plans against the project's recorded profile, or against the one given, and lists the files that would be added as `new`. It still writes nothing.

## Profiles

| Profile | For | Content |
|---|---|---|
| `minimal` | Trying the method; any project that wants to add documents by hand | The v1.3 baseline (16 files) |
| `site` | Landing page or content site without its own backend | Baseline + the **S** column |
| `app` | A few deployable parts: web, admin, API, one database | Baseline + the **A** column |
| `platform` | Several services, events, apps or teams | Baseline + the **P** column |
| `--regulated` | Payments, health, sensitive data or enterprise customers | Adds the **R** files to `site`, `app` or `platform` |

## Metadata

`.dixi/project.json` gains `"profile"` (one of the four names) and `"regulated"` (boolean). `schema_version` stays 1. A project without these fields is `minimal` and not regulated. Any other value is invalid metadata (exit 1).

## Templates

Each table lists the files under its area. ✓ = installed with that profile; R = installed only with `--regulated`; — = not installed.

### `08-data/`

| File | S | A | P |
|---|---|---|---|
| `pii-classification.md` | ✓ | ✓ | ✓ |
| `retention-policy.md` | ✓ | ✓ | ✓ |
| `data-architecture.md` | — | ✓ | ✓ |
| `canonical-data-model.md` | — | ✓ | ✓ |
| `audit-fields-standard.md` | R | ✓ | ✓ |
| `models/erd-overview.md` | — | ✓ | ✓ |
| `migrations/migration-strategy.md` | — | ✓ | ✓ |
| `migrations/zero-downtime-migrations.md` | — | — | ✓ |
| `migrations/data-migration-playbook.md` | — | ✓ | ✓ |
| `master-data.md` | — | — | ✓ |
| `reporting-dimensions.md` | — | — | ✓ |

### `09-architecture/`

| File | S | A | P |
|---|---|---|---|
| `adr/README.md` (index and how to write an ADR) | ✓ | ✓ | ✓ |
| `system-context.md` | ✓ | ✓ | ✓ |
| `deployment-architecture.md` | ✓ | ✓ | ✓ |
| `security-architecture.md` | ✓ | ✓ | ✓ |
| `container-diagram.md` | — | ✓ | ✓ |
| `component-diagram.md` | — | ✓ | ✓ |
| `integration-architecture.md` | — | ✓ | ✓ |
| `resilience-architecture.md` | — | ✓ | ✓ |
| `performance-architecture.md` | — | ✓ | ✓ |
| `event-architecture.md` | — | — | ✓ |
| `multi-tenant-architecture.md` | — | — | ✓ |
| `offline-sync-architecture.md` | — | — | ✓ |

No ADR from Dixi's ecosystem is shipped; projects write their own from the template.

### `10-engineering/`

| File | S | A | P |
|---|---|---|---|
| `coding-standards.md` | ✓ | ✓ | ✓ |
| `secure-coding-standard.md` | ✓ | ✓ | ✓ |
| `error-handling-standard.md` | — | ✓ | ✓ |
| `logging-standard.md` | — | ✓ | ✓ |
| `api-design-standard.md` | — | ✓ | ✓ |
| `package-structure-standard.md` | — | ✓ | ✓ |
| `event-design-standard.md` | — | — | ✓ |
| `templates/adr-template.md` | ✓ | ✓ | ✓ |
| `templates/feature-template.md` | ✓ | ✓ | ✓ |
| `templates/page-template.md` | ✓ | ✓ | ✓ |
| `templates/runbook-template.md` | ✓ | ✓ | ✓ |
| `templates/postmortem-template.md` | ✓ | ✓ | ✓ |
| `templates/module-template.md` | — | ✓ | ✓ |
| `templates/domain-template.md` | — | ✓ | ✓ |
| `templates/flow-template.md` | — | ✓ | ✓ |
| `templates/api-template.yaml` (OpenAPI skeleton) | — | ✓ | ✓ |
| `templates/external-integration-template.md` | — | ✓ | ✓ |
| `templates/prompt-template.md` | — | ✓ | ✓ |
| `templates/event-template.json` | — | — | ✓ |
| `templates/product-template.md` | — | — | ✓ |
| `templates/agent-spec-template.md` | — | — | ✓ |
| `templates/mcp-server-template.md` | — | — | ✓ |

### `11-quality/`

`test-plan.md` stays in every profile, as in `minimal`.

| File | S | A | P |
|---|---|---|---|
| `quality-strategy.md` | ✓ | ✓ | ✓ |
| `verification-ladder.md` | ✓ | ✓ | ✓ |
| `test-pyramid.md` | ✓ | ✓ | ✓ |
| `tdd-guide.md` | ✓ | ✓ | ✓ |
| `acceptance-strategy.md` | ✓ | ✓ | ✓ |
| `non-functional-requirements.md` | ✓ | ✓ | ✓ |
| `risk-based-review.md` | ✓ | ✓ | ✓ |
| `performance-budgets/web-vitals-budgets.md` | ✓ | ✓ | ✓ |
| `bdd-guide.md` | — | ✓ | ✓ |
| `regression-plan.md` | — | ✓ | ✓ |
| `security-test-plan.md` | R | ✓ | ✓ |
| `engineering-metrics.md` | — | ✓ | ✓ |
| `performance-test-plan.md` | — | ✓ | ✓ |
| `performance-budgets/api-latency-budgets.md` | — | ✓ | ✓ |
| `contract-testing-guide.md` | — | — | ✓ |
| `property-based-testing-guide.md` | — | — | ✓ |
| `mutation-testing-guide.md` | — | — | ✓ |
| `ai-llm-testing-guide.md` | — | ✓ | ✓ |

### `13-security/`

| File | S | A | P |
|---|---|---|---|
| `threat-model.md` | ✓ | ✓ | ✓ |
| `secret-management.md` | ✓ | ✓ | ✓ |
| `dependency-scanning.md` | ✓ | ✓ | ✓ |
| `incident-response.md` | ✓ | ✓ | ✓ |
| `ai-agent-hardening.md` | ✓ | ✓ | ✓ |
| `authn-authz-model.md` | — | ✓ | ✓ |
| `data-protection-controls.md` | R | ✓ | ✓ |
| `vulnerability-management.md` | — | ✓ | ✓ |
| `risk-register.md` | R | ✓ | ✓ |
| `llm-application-security.md` | — | ✓ | ✓ |
| `licensing/licensing-policy.md` | ✓ | ✓ | ✓ |
| `licensing/approved-licenses.md` | ✓ | ✓ | ✓ |
| `key-rotation.md` | — | — | ✓ |
| `licensing/sbom-strategy.md` | — | — | ✓ |
| `break-glass-access.md` | R | R | ✓ |

### `21-ai/`

| File | S | A | P |
|---|---|---|---|
| `sdd/methodology.md` | ✓ | ✓ | ✓ |
| `sdd/spec-lifecycle.md` | ✓ | ✓ | ✓ |
| `sdd/traceability-matrix.md` | ✓ | ✓ | ✓ |
| `sdd/validation-rules.md` | ✓ | ✓ | ✓ |
| `sdd/adoption-guide.md` | ✓ | ✓ | ✓ |
| `agents/guardrails.md` | ✓ | ✓ | ✓ |
| `agents/human-in-the-loop.md` | ✓ | ✓ | ✓ |
| `governance/ai-audit-trail.md` | ✓ | ✓ | ✓ |
| `governance/responsible-ai.md` | ✓ | ✓ | ✓ |
| `governance/quality-gates.md` | — | ✓ | ✓ |
| `agents/agent-architecture.md` | — | ✓ | ✓ |
| `agents/capability-matrix.md` | — | ✓ | ✓ |
| `llm/model-strategy.md` (provider-neutral) | — | ✓ | ✓ |
| `llm/context-strategy.md` | — | ✓ | ✓ |
| `llm/prompt-library.md` | — | ✓ | ✓ |
| `mcp/mcp-architecture.md` | — | — | ✓ |
| `mcp/tool-catalog.md` | — | — | ✓ |
| `memory/memory-architecture.md` | — | — | ✓ |

Files added over the baseline by block D: `site` 37, `app` 76, `platform` 96; `--regulated` adds 5 to `site` and 1 to `app`. With block E the totals become `site` 77 (94 regulated), `app` 190 (226) and `platform` 241 (273), plus the 16 baseline files and the agent files.

## Template rules

1. One file per path in English and Spanish, with the same paths in both languages.
2. Markdown templates start with `# <title>`, include a `## Purpose` section, mark project decisions as `{{pending: <what to decide>}}` and end with `## Related`.
3. Local links point only to files installed in **every** profile that installs the linking file; `dixi check` must pass for each of the seven combinations (`minimal`, `site`, `app`, `platform`, each of the last three with `--regulated`), with every agent.
4. No template contains the internal markers listed in [ADR-104](../../09-architecture/adr/ADR-104-project-profiles-and-content.md) (decision 7). Examples use `example.com` addresses and neutral names.
5. Templates are guidance and blanks, not decisions: nothing in them claims a certification, a provider choice or an executed test.

## Inventory and checks

- Every installed template is recorded in `managed_files` with its hash.
- `dixi check` requires the baseline and the v1.0 agent files; a deleted profile template is not an error. Link checks apply to the templates that exist.
- The inventory limit is 1 000 managed files.
- `dixi doctor` reports the profile and whether the project is regulated.

## Packaging

Templates live in `src/dixi_spec_kit/resources/templates/<language>/<path>`, assigned to profiles by `src/dixi_spec_kit/resources/profiles.json`. Both are declared in `pyproject.toml`, `MANIFEST.in` and `scripts/build-local.py`, and `scripts/verify-source.py` checks language parity and that every manifest path exists.

## Errors

Same exit codes as v1.0. `--regulated` with `minimal`, or an unknown profile, exits 2 without writing.

## Related

- [ADR-104](../../09-architecture/adr/ADR-104-project-profiles-and-content.md)
- [TASK-008](../../tasks/backlog/TASK-008-profiles-and-core-templates.md)
- [Specialized commands contract](specialized-commands-contract.md)
- [Block E contract](remaining-content-contract.md)
