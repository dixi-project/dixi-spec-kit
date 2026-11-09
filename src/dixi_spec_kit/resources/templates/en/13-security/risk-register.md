# Risk register

## Purpose

Keep one place where security and privacy risks are recorded, scored, assigned and reviewed, including those the project decides to accept. The register links threats to decisions; it does not replace the threat model.

Status: draft. {{pending: name the owner of the register and the review cadence}}

## Scoring

Score likelihood and impact from 1 (low) to 3 (high). Risk = likelihood × impact.

| Score | Level | Expected action |
|-------|-------|-----------------|
| 6–9 | High | Treat before release or accept at {{pending: decide who can accept high risks}} level |
| 3–4 | Medium | Plan treatment with a date |
| 1–2 | Low | Monitor |

{{pending: confirm or replace this scale}}

## Treatment options

- **Mitigate**: add a control; link it to a threat and a verification.
- **Transfer**: move part of the impact elsewhere (contract, insurance).
- **Avoid**: remove the feature or data that creates the risk.
- **Accept**: record who accepted it, why and until when.

## Register

| ID | Risk | Source (threat, audit, incident) | Likelihood | Impact | Score | Treatment | Owner | Review date | Status |
|----|------|----------------------------------|------------|--------|-------|-----------|-------|-------------|--------|
| RK-01 | {{pending: description}} | {{pending: e.g. TH-01}} | {{pending: 1-3}} | {{pending: 1-3}} | {{pending: score}} | {{pending: option}} | {{pending: owner}} | {{pending: date}} | open |

## Review

- Review the register at a fixed cadence and after every significant incident or architecture change.
- Expired acceptances return to "open" until re-approved.
- Closed risks stay in the register with the date and reason.

## Related

- [Threat model](threat-model.md)
- [Data protection controls](data-protection-controls.md)
- [Incident response](incident-response.md)
- [Project](../00-master-spec.md)
