# PCI DSS

> **Working aid, not legal advice.** This page helps decide how the Payment Card Industry Data Security Standard affects the project and how to keep that impact small. Validation is done by the means the card brands and acquirer require; no template certifies compliance.

## Purpose

Record whether the project stores, processes or transmits cardholder data, which parts of the system are in scope, and the validation path agreed with the payment partner. The usual goal is to reduce scope so card data never touches the project's systems.

Status: draft. {{pending: decide the payment integration approach and record it as an ADR}}

## Scope questions

| Question | Answer | Source |
|----------|--------|--------|
| Does any project system receive full card numbers, even transiently? | {{pending: answer}} | [Integration architecture](../../09-architecture/integration-architecture.md) |
| Is card entry handled by a hosted page, embedded field or redirect from the payment partner? | {{pending: answer}} | {{pending: link}} |
| Which systems could affect the security of the payment page (scripts, CDN, redirects)? | {{pending: list}} | {{pending: link}} |
| What validation does the acquirer or payment partner require? | {{pending: answer, from the partner}} | {{pending: link}} |

## Scope reduction options

| Option | Effect on scope | Trade-offs |
|--------|-----------------|------------|
| Redirect to a hosted payment page | Smallest footprint for the project | Less control over checkout experience |
| Embedded fields served by the payment partner | Small footprint; page integrity still matters | Script integrity must be managed |
| Card data passes through project servers | Large footprint; most requirements apply | High effort; avoid unless needed |

## If in scope: areas to prepare

Described in general terms; read the current standard from its official publisher.

- Network segmentation that isolates the cardholder data environment.
- Secure configuration and change control for in-scope systems.
- Protection of stored and transmitted card data; tokenisation where possible.
- Vulnerability management and regular testing: [Vulnerability management](../../13-security/vulnerability-management.md).
- Strong access control and unique accounts: [AuthN/AuthZ model](../../13-security/authn-authz-model.md).
- Logging and monitoring of access to card data.
- Integrity of payment page scripts.
- Policies, training and incident response: [Incident response](../../13-security/incident-response.md).

## Guardrails

- Never log card numbers or security codes; add a test that checks logs for card-like patterns. {{pending: decide where this test lives}}
- Use test card numbers from the payment partner only in non-production environments.

## Related

- [Compliance overview](../compliance-overview.md)
- [Vendor risk assessment](../../15-operations/vendor-management/vendor-risk-assessment.md)
- [Threat model](../../13-security/threat-model.md)
- [Risk register](../../13-security/risk-register.md)
