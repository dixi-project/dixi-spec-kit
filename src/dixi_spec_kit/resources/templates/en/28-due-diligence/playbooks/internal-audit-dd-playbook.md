# Internal audit due diligence playbook

> **Evidence rule.** An internal audit is only useful if it is honest. Score from artifacts, record gaps as gaps, and never present an assumption as a fact; every finding points to an artifact of the project.

## Purpose

Run the due diligence method on the project itself, on a schedule, to find weaknesses before an external party does and to measure progress between reviews.

Status: draft. {{pending: set the audit cadence and name the audit lead}}

## Principles

- The auditor should not score the areas they own; rotate reviewers or pair them.
- Use the same scale and checklists as external reviews so results are comparable.
- Findings are tracked like any other work, with owners and dates.

## Plan

| Field | Value |
|-------|-------|
| Cycle | {{pending: e.g. quarterly or before each major release}} |
| Areas this cycle | {{pending: all, or a rotating subset}} |
| Reviewers per area | {{pending: roles}} |
| Evidence period | {{pending: from – to}} |
| Time box | {{pending: duration}} |

## Steps

1. Pick the areas from the [checklists](../dd-strategy.md#checklist-areas) and assign reviewers.
2. Collect evidence; mark items with no artifact as "no evidence".
3. Score items and agree scores in a short calibration session.
4. Compare with the previous cycle; explain every score that went down.
5. Fill the [DD report template](../dd-report-template.md) and the [final checklist](../checklist/11-final-report.md).
6. Create tickets for gaps and add material ones to the [Risk register](../../13-security/risk-register.md).

## Trend

| Area | Previous score | Current score | Change explained by |
|------|----------------|---------------|---------------------|
| {{pending: area}} | {{pending: score}} | {{pending: score}} | {{pending: artifact or finding}} |

## Using the result

- Feed the top gaps into planning: {{pending: decide how much capacity is reserved for remediation}}
- Reuse current evidence when an external review arrives.
- Use `/dixi.duediligence` (Claude Code) or `$dixi-duediligence` (Codex) to prepare the cycle.

## Related

- [DD strategy](../dd-strategy.md)
- [Buyer DD playbook](buyer-dd-playbook.md)
- [Enterprise customer DD playbook](enterprise-customer-dd-playbook.md)
- [Final checklist](../checklist/11-final-report.md)
