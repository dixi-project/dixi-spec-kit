# Checklist 07 — Team

> **Evidence rule.** Score only what an artifact proves. A missing artifact is recorded as "no evidence" and scored 0; it is never filled with an assumption presented as fact. Do not include personal data about individuals in DD material; describe roles, not people.

## Purpose

Assess whether the team can keep operating and evolving the product: roles are clear, knowledge is shared, key-person risk is known and onboarding works.

Status: draft. {{pending: decide what team information may be shared and under which agreement}}

## Inputs

- [Internal roles](../../01-business/actors/internal-roles.md)
- [RACI matrix](../../15-operations/team/raci-matrix.md)
- [On-call rotation](../../15-operations/team/on-call-rotation.md)
- [Onboarding guide](../../18-knowledge-base/onboarding-guide.md)
- [Escalation matrix](../../15-operations/escalation-matrix.md)

## Items

| ID | Question | Evidence (artifact) | Score 0–5 | Finding |
|----|----------|---------------------|-----------|---------|
| TEAM-01 | Are roles and responsibilities documented for product, engineering, security and operations? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| TEAM-02 | Does each critical system have at least two people able to operate it? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| TEAM-03 | Is knowledge written down rather than held by individuals? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| TEAM-04 | Can a new member contribute safely within a defined onboarding period? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| TEAM-05 | Is on-call shared fairly and documented? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| TEAM-06 | Are contractors and agencies covered by the same access and IP rules as staff? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| TEAM-07 | Is security awareness training given and recorded? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| TEAM-08 | Is offboarding a checklist with access removal confirmed? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |

## Key-person map

| Area | Primary role | Backup role | Documented? |
|------|--------------|-------------|-------------|
| {{pending: area}} | {{pending: role}} | {{pending: role or "none"}} | {{pending: yes / no, link}} |

## Red flags

- One person is the only one who can deploy, restore or access production.
- Core code written by contractors with no IP assignment.

## Output

- Area score: {{pending: score and method}}
- Findings carried to the [DD report](../dd-report-template.md).

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 06 — Processes](06-processes.md)
- [Checklist 08 — Financial](08-financial.md)
- [Final checklist](11-final-report.md)
