# Contract — remaining content areas (block E)

## Purpose

Specify the templates for the areas not covered by [block D](profiles-contract.md): governance, business, platform, flows, contracts, observability, delivery, operations, product, UX, knowledge base, references, stack templates, FinOps, compliance, research, growth, customer success, fixtures and due diligence. Implements [TASK-009](../../tasks/backlog/TASK-009-remaining-content.md) under [ADR-104](../../09-architecture/adr/ADR-104-project-profiles-and-content.md).

CLI, metadata, template rules, inventory, checks and packaging are those of the [block D contract](profiles-contract.md). This contract adds files only.

## Templates

✓ = installed with that profile; R = only with `--regulated`; — = not installed.

### `00-governance/`

| File | S | A | P |
|---|---|---|---|
| `principles.md` (vision, architecture and engineering principles) | ✓ | ✓ | ✓ |
| `engineering-standards.md` | ✓ | ✓ | ✓ |
| `security-baseline.md` | ✓ | ✓ | ✓ |
| `ai-governance.md` | ✓ | ✓ | ✓ |
| `policies/branching-strategy.md` | ✓ | ✓ | ✓ |
| `policies/testing-policy.md` | ✓ | ✓ | ✓ |
| `policies/documentation-policy.md` | ✓ | ✓ | ✓ |
| `policies/naming-conventions.md` | ✓ | ✓ | ✓ |
| `policies/versioning-policy.md` | ✓ | ✓ | ✓ |
| `policies/i18n-policy.md` | ✓ | ✓ | ✓ |
| `policies/ai-usage-policy.md` | ✓ | ✓ | ✓ |
| `policies/dependency-policy.md` | ✓ | ✓ | ✓ |
| `policies/incident-policy.md` | — | ✓ | ✓ |
| `data-governance.md` | R | ✓ | ✓ |
| `release-management-standard.md` | — | ✓ | ✓ |
| `environment-strategy.md` | — | ✓ | ✓ |
| `observability-standard.md` | — | ✓ | ✓ |
| `integration-governance.md` | — | — | ✓ |

### `01-business/`

`vision.md` (GOAL-001) stays in every profile, as in `minimal`.

| File | S | A | P |
|---|---|---|---|
| `value-proposition.md` | ✓ | ✓ | ✓ |
| `actors/personas.md` | ✓ | ✓ | ✓ |
| `strategic-goals.md` | — | ✓ | ✓ |
| `actors/internal-roles.md` | — | ✓ | ✓ |
| `actors/external-partners.md` | — | ✓ | ✓ |
| `domains/ubiquitous-language.md` | — | ✓ | ✓ |
| `domains/business-capabilities.md` | — | ✓ | ✓ |
| `domains/domain-map.md` | — | ✓ | ✓ |
| `domains/bounded-context-map.md` | — | — | ✓ |
| `rules/business-rules.md` | — | ✓ | ✓ |
| `rules/operational-constraints.md` | — | ✓ | ✓ |
| `rules/pricing-rules.md` | — | ✓ | ✓ |
| `rules/compliance-rules.md` | R | R | ✓ |

### `02-platform/` (platform only)

| File | S | A | P |
|---|---|---|---|
| `platform-overview.md` | — | — | ✓ |
| `product-map.md` | — | — | ✓ |
| `ecosystem-landscape.md` | — | — | ✓ |
| `shared-services-map.md` | — | — | ✓ |
| `cross-product-integrations.md` | — | — | ✓ |
| `identity-and-access-strategy.md` | — | — | ✓ |
| `tenant-strategy.md` | — | — | ✓ |
| `products/README.md` (how to add one folder per product, with capabilities, context boundaries and dependencies) | — | — | ✓ |

### `06-flows/` and `07-contracts/`

| File | S | A | P |
|---|---|---|---|
| `06-flows/README.md` (how to describe a flow, linked to the flow template) | — | ✓ | ✓ |
| `07-contracts/api/README.md` | — | ✓ | ✓ |
| `07-contracts/schemas/README.md` | — | ✓ | ✓ |
| `07-contracts/external/README.md` | — | ✓ | ✓ |
| `07-contracts/events/README.md` | — | — | ✓ |
| `07-contracts/commands/README.md` | — | — | ✓ |
| `07-contracts/agent-interfaces/README.md` | — | — | ✓ |
| `07-contracts/mcp/README.md` | — | — | ✓ |

### `12-observability/`

| File | S | A | P |
|---|---|---|---|
| `alerting-rules.md` | ✓ | ✓ | ✓ |
| `observability-strategy.md` | — | ✓ | ✓ |
| `slis-slos-slas.md` | — | ✓ | ✓ |
| `metrics-catalog.md` | — | ✓ | ✓ |
| `logging-map.md` | — | ✓ | ✓ |
| `dashboard-map.md` | — | ✓ | ✓ |
| `tracing-strategy.md` | — | — | ✓ |
| `runbooks/README.md` (how to write one, with a neutral example) | — | ✓ | ✓ |

### `14-delivery/`

Named `delivery` rather than `devops` because it holds no infrastructure: no pipelines for a specific vendor and no account files.

| File | S | A | P |
|---|---|---|---|
| `ci-cd-overview.md` | ✓ | ✓ | ✓ |
| `environments.md` | ✓ | ✓ | ✓ |
| `deployment-strategy.md` | ✓ | ✓ | ✓ |
| `rollback-strategy.md` | ✓ | ✓ | ✓ |
| `continuous-verification.md` | — | ✓ | ✓ |
| `backup-and-recovery.md` | — | ✓ | ✓ |
| `infra-modules.md` | — | ✓ | ✓ |
| `pipelines/build-pipeline.md` | — | ✓ | ✓ |
| `pipelines/release-pipeline.md` | — | ✓ | ✓ |
| `pipelines/migration-pipeline.md` | — | ✓ | ✓ |
| `cron-jobs.md` | — | — | ✓ |
| `workers-and-queues.md` | — | — | ✓ |
| `disaster-recovery/dr-strategy.md` | R | ✓ | ✓ |
| `disaster-recovery/rto-rpo-matrix.md` | R | ✓ | ✓ |
| `disaster-recovery/dr-runbook.md` | — | R | ✓ |
| `disaster-recovery/bcp-plan.md` | — | R | ✓ |

### `15-operations/`

| File | S | A | P |
|---|---|---|---|
| `incident-levels.md` | ✓ | ✓ | ✓ |
| `escalation-matrix.md` | ✓ | ✓ | ✓ |
| `playbooks/restore-service.md` | ✓ | ✓ | ✓ |
| `playbooks/comms-outage-customer.md` | ✓ | ✓ | ✓ |
| `support-model.md` | — | ✓ | ✓ |
| `service-catalog.md` | — | ✓ | ✓ |
| `known-issues.md` | — | ✓ | ✓ |
| `maintenance-window-policy.md` | — | ✓ | ✓ |
| `playbooks/comms-outage-internal.md` | — | ✓ | ✓ |
| `playbooks/cost-spike.md` (generic, replaces provider-specific playbooks) | — | ✓ | ✓ |
| `playbooks/reprocess-events.md` | — | — | ✓ |
| `playbooks/tenant-onboarding.md` | — | — | ✓ |
| `playbooks/manual-refund.md` | — | ✓ | ✓ |
| `playbooks/data-breach.md` | R | ✓ | ✓ |
| `playbooks/comms-breach-customer.md` | R | ✓ | ✓ |
| `team/raci-matrix.md` | — | ✓ | ✓ |
| `team/on-call-rotation.md` | — | ✓ | ✓ |
| `vendor-management/vendor-catalog.md` | — | ✓ | ✓ |
| `vendor-management/vendor-risk-assessment.md` | R | ✓ | ✓ |
| `vendor-management/sla-matrix.md` | — | — | ✓ |

### `16-product/`, `17-ux/`, `24-research/`, `25-growth/`, `26-customer-success/`

| File | S | A | P |
|---|---|---|---|
| `16-product/roadmap.md` | — | ✓ | ✓ |
| `16-product/prioritization-framework.md` | — | ✓ | ✓ |
| `16-product/feature-lifecycle.md` | — | ✓ | ✓ |
| `16-product/release-notes.md` | — | ✓ | ✓ |
| `16-product/analytics-events-catalog.md` | — | ✓ | ✓ |
| `16-product/experimentation-framework.md` | — | — | ✓ |
| `17-ux/design-principles.md` | ✓ | ✓ | ✓ |
| `17-ux/accessibility-standard.md` | ✓ | ✓ | ✓ |
| `17-ux/content-guidelines.md` | ✓ | ✓ | ✓ |
| `17-ux/information-architecture.md` | ✓ | ✓ | ✓ |
| `17-ux/navigation-map.md` | ✓ | ✓ | ✓ |
| `17-ux/design-tokens.md` | — | ✓ | ✓ |
| `17-ux/ui-state-catalog.md` | — | ✓ | ✓ |
| `24-research/discovery-strategy.md` | ✓ | ✓ | ✓ |
| `24-research/persona-template.md` | ✓ | ✓ | ✓ |
| `24-research/jobs-to-be-done.md` | — | ✓ | ✓ |
| `24-research/user-research-plan.md` | — | ✓ | ✓ |
| `24-research/competitive-analysis.md` | — | ✓ | ✓ |
| `24-research/interview-templates/discovery-interview.md` | — | ✓ | ✓ |
| `24-research/interview-templates/usability-test.md` | — | ✓ | ✓ |
| `24-research/research-log/README.md` | — | ✓ | ✓ |
| `25-growth/growth-strategy.md` | ✓ | ✓ | ✓ |
| `25-growth/seo-strategy.md` | ✓ | ✓ | ✓ |
| `25-growth/conversion-funnel.md` | ✓ | ✓ | ✓ |
| `25-growth/landing-pages-catalog.md` | ✓ | ✓ | ✓ |
| `25-growth/content-strategy.md` | ✓ | ✓ | ✓ |
| `25-growth/ab-testing-framework.md` | — | ✓ | ✓ |
| `26-customer-success/success-strategy.md` | — | ✓ | ✓ |
| `26-customer-success/support-tiers.md` | — | ✓ | ✓ |
| `26-customer-success/help-center-structure.md` | — | ✓ | ✓ |
| `26-customer-success/churn-playbook.md` | — | — | ✓ |

### `18-knowledge-base/`, `19-references/`, `20-repos/`, `27-fixtures/`

| File | S | A | P |
|---|---|---|---|
| `18-knowledge-base/glossary.md` | ✓ | ✓ | ✓ |
| `18-knowledge-base/faq.md` | ✓ | ✓ | ✓ |
| `18-knowledge-base/onboarding-guide.md` | ✓ | ✓ | ✓ |
| `18-knowledge-base/decision-log.md` | ✓ | ✓ | ✓ |
| `18-knowledge-base/troubleshooting-index.md` | — | ✓ | ✓ |
| `18-knowledge-base/acronyms.md` | — | ✓ | ✓ |
| `18-knowledge-base/maturity-model.md` | — | — | ✓ |
| `19-references/reading-list.md` | ✓ | ✓ | ✓ |
| `20-repos/README.md` (one repository per deployable part; how to link code to specs) | — | ✓ | ✓ |
| `20-repos/backend-service.md` | — | ✓ | ✓ |
| `20-repos/frontend-app.md` | — | ✓ | ✓ |
| `20-repos/worker.md` | — | — | ✓ |
| `20-repos/mobile-app.md` | — | — | ✓ |
| `20-repos/mcp-server.md` | — | — | ✓ |
| `27-fixtures/fixtures-strategy.md` | — | ✓ | ✓ |
| `27-fixtures/sample-data-catalog.md` | — | ✓ | ✓ |
| `27-fixtures/demo-scenarios.md` | — | ✓ | ✓ |

Stack templates describe folder layout and conventions; they create no source folders, because the project's code lives in its own repositories.

### `22-finops/`

| File | S | A | P |
|---|---|---|---|
| `cost-strategy.md` | — | ✓ | ✓ |
| `budget-alerts.md` | — | ✓ | ✓ |
| `ai-cost-management.md` | — | ✓ | ✓ |
| `cloud-cost-optimization.md` | — | — | ✓ |
| `cost-allocation-model.md` | — | — | ✓ |
| `templates/cost-report-template.md` | — | ✓ | ✓ |

### `23-compliance/` (regulated only)

| File | S | A | P |
|---|---|---|---|
| `compliance-overview.md` | R | R | R |
| `regulatory-watch.md` | R | R | R |
| `dpa-template.md` | R | R | R |
| `gdpr/gdpr-readiness.md` | R | R | R |
| `gdpr/sub-processors.md` | R | R | R |
| `soc2/soc2-readiness.md` | — | R | R |
| `soc2/soc2-controls-matrix.md` | — | R | R |
| `soc2/system-description.md` | — | R | R |
| `soc2/type-i-vs-type-ii.md` | — | R | R |
| `iso-27001/iso-27001-readiness.md` | — | R | R |
| `iso-27001/controls-mapping.md` | — | R | R |
| `iso-27001/isms-policy.md` | — | R | R |
| `iso-soc2-overlap-mapping.md` | — | R | R |
| `hipaa/README.md` | — | R | R |
| `pci-dss/README.md` | — | R | R |

Every compliance template states at the top that it is a working aid, not legal advice, and that no template certifies conformity.

### `28-due-diligence/` (regulated only)

| File | S | A | P |
|---|---|---|---|
| `dd-strategy.md` | — | R | R |
| `dd-report-template.md` | — | R | R |
| `checklist/01-infrastructure.md` | — | R | R |
| `checklist/02-architecture.md` | — | R | R |
| `checklist/03-source-code.md` | — | R | R |
| `checklist/04-security.md` | — | R | R |
| `checklist/05-data-management.md` | — | R | R |
| `checklist/06-processes.md` | — | R | R |
| `checklist/07-team.md` | — | R | R |
| `checklist/08-financial.md` | — | R | R |
| `checklist/09-vendors-partners.md` | — | R | R |
| `checklist/10-innovation.md` | — | R | R |
| `checklist/11-final-report.md` | — | R | R |
| `playbooks/buyer-dd-playbook.md` | — | R | R |
| `playbooks/enterprise-customer-dd-playbook.md` | — | R | R |
| `playbooks/internal-audit-dd-playbook.md` | — | R | R |
| `playbooks/vendor-dd-playbook.md` | — | R | R |

## Not shipped

Dixi's own ADRs, account and customer files, team structure and organization chart, project catalogs, integrations with internal tools, CodeBuild/CodePipeline material, provider-specific cost playbooks, backlog, migrations, session handoffs and the proprietary license. Product comparisons with named competitors are not shipped either.

## Kit repository

Block E also adds `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1) and `SUPPORT.md` to the kit repository itself. They are not generated into projects.

## Related

- [Block D contract](profiles-contract.md)
- [ADR-104](../../09-architecture/adr/ADR-104-project-profiles-and-content.md)
- [TASK-009](../../tasks/backlog/TASK-009-remaining-content.md)
