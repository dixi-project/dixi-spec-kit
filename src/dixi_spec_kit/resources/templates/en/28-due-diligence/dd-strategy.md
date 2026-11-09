# Due diligence strategy

> **Evidence rule.** Due diligence describes what artifacts prove. Gaps are recorded as gaps, never filled with assumptions presented as facts, and every statement points to an artifact of the project.

## Purpose

Define how the project runs a technical due diligence (DD): who asks, what is in scope, how areas are scored, how evidence is gathered and how the outcome is turned into an action plan. The same method serves external and internal reviews.

Status: draft. {{pending: name the DD owner and who may share DD material outside the team}}

## DD types

| Type | Who asks | Typical question | Playbook |
|------|----------|------------------|----------|
| Buyer or investor | Acquirer, investor | Is the technology what it is said to be, and what does it cost to fix? | [Buyer DD](playbooks/buyer-dd-playbook.md) |
| Enterprise customer | Customer's security or procurement team | Can we trust this product with our data and operations? | [Enterprise customer DD](playbooks/enterprise-customer-dd-playbook.md) |
| Internal audit | The project itself | Where are we weak and what do we fix first? | [Internal audit DD](playbooks/internal-audit-dd-playbook.md) |
| Vendor | The project, assessing a supplier | Can we depend on this supplier? | [Vendor DD](playbooks/vendor-dd-playbook.md) |

## Maturity scale

Every checklist item is scored 0–5:

| Score | Meaning |
|-------|---------|
| 0 | Absent, or no evidence |
| 1 | Ad hoc, depends on individuals |
| 2 | Defined but not applied consistently |
| 3 | Defined, applied and documented |
| 4 | Measured and reviewed |
| 5 | Continuously improved, independently verified |

Area score: {{pending: decide between average of items and weakest critical item}}

## Process

1. **Scope**: confirm the DD type, the areas from the checklist and the deadline.
2. **Evidence sweep**: collect artifacts for each area; record where each one lives.
3. **Scoring**: score each item from its evidence; note who scored it and when.
4. **Gap analysis**: list gaps by severity; mark red flags explicitly.
5. **Outcome**: fill the [DD report template](dd-report-template.md) and the [Final checklist](checklist/11-final-report.md); turn gaps into tickets and risks.

## Checklist areas

[Infrastructure](checklist/01-infrastructure.md), [Architecture](checklist/02-architecture.md), [Source code](checklist/03-source-code.md), [Security](checklist/04-security.md), [Data management](checklist/05-data-management.md), [Processes](checklist/06-processes.md), [Team](checklist/07-team.md), [Financial](checklist/08-financial.md), [Vendors and partners](checklist/09-vendors-partners.md), [Innovation](checklist/10-innovation.md).

## Confidentiality

- Share DD material only under the agreement that governs the review: {{pending: e.g. NDA reference}}
- Use a controlled data room; never send secrets, credentials or personal data.
- Record what was shared, with whom and when.

## Anti-patterns

- Scoring from memory or interviews without an artifact.
- Hiding known gaps; they surface later at higher cost.
- Rewriting history: evidence keeps its original date.

Use `/dixi.duediligence` (Claude Code) or `$dixi-duediligence` (Codex) to prepare a review from this method.

## Related

- [DD report template](dd-report-template.md)
- [Final checklist](checklist/11-final-report.md)
- [Risk register](../13-security/risk-register.md)
- [Project](../00-master-spec.md)
