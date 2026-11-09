# Vendor risk assessment

## Purpose

Assess the risk of depending on an external vendor before signing up and at regular intervals, so the decision to use it is explicit and its mitigations are known.

Status: draft. {{pending: name the owner of vendor assessments}}

## When to assess

- Before a new vendor processes personal or confidential data, or supports a critical service.
- At each renewal of a critical vendor.
- After a vendor incident, acquisition or major change of terms.

## Dimensions

Score each from 1 (low risk) to 5 (high risk) and write the evidence behind the score.

| # | Dimension | Questions |
|---|-----------|-----------|
| 1 | Operational criticality | What stops if it fails? Is there a workaround? |
| 2 | Data sensitivity | What data does it receive? Personal, financial, health? |
| 3 | Security posture | What independent evidence does it offer? How does it handle incidents? |
| 4 | Privacy | Data processing agreement, sub-processors, retention, deletion on exit? |
| 5 | Jurisdiction | Where is data stored and processed? Which laws apply? |
| 6 | Lock-in | Can data be exported in an open format? How long would a migration take? |
| 7 | Financial and continuity | Is the vendor likely to exist and support the product in two years? |
| 8 | Concentration | How many critical services already depend on this vendor? |
| 9 | Track record | Past incidents and support quality with this project |
| 10 | AI behaviour (if applicable) | Does it train on our data? Can outputs be logged and reviewed? |

## Result

| Total score | Tier | Required action |
|-------------|------|-----------------|
| {{pending: range}} | Low | Record and review at renewal |
| {{pending: range}} | Medium | Mitigations documented and owned |
| {{pending: range}} | High | Approval by {{pending: role}} and an exit plan before use |

## Assessment record

- Vendor and service: {{pending: name}}
- Assessor and date: {{pending: role, date}}
- Scores and evidence: {{pending: table above, filled}}
- Findings and mitigations: {{pending: list with owners}}
- Decision: {{pending: approve / approve with conditions / reject}}
- Next review: {{pending: date}}

Do not paste vendor confidential documents or credentials here; link to where they are stored.

## Related

- [Risk register](../../13-security/risk-register.md)
- [Data protection controls](../../13-security/data-protection-controls.md)
- [PII classification](../../08-data/pii-classification.md)
- [Incident response](../../13-security/incident-response.md)
