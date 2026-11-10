# Threat model

## Purpose

Identify what the project must protect, who could attack it and how, and link every mitigation to a verification that can be traced to the test plan. This is a living document: update it when a feature changes a trust boundary, adds a data flow or handles new sensitive data.

Status: draft. {{pending: name the person who owns and reviews this threat model}}

## Scope

- System or features covered: {{pending: list the features and components in scope}}
- Out of scope and why: {{pending: list exclusions}}
- Last review date: {{pending: date}}

## Assets

| ID | Asset | Why it matters | Sensitivity |
|----|-------|----------------|-------------|
| AS-01 | {{pending: e.g. user accounts}} | {{pending: impact if compromised}} | {{pending: low / medium / high}} |

## Actors and trust boundaries

| Actor | Trust level | Entry points |
|-------|-------------|--------------|
| Anonymous visitor | Untrusted | {{pending: public pages, forms, APIs}} |
| Authenticated user | Partially trusted | {{pending: entry points}} |
| Operator or administrator | Trusted, audited | {{pending: entry points}} |
| AI coding agent | Untrusted by default | Repository, terminal, tools granted |

Draw or describe the data flow: which component talks to which, over what channel, and where data crosses a trust boundary. {{pending: add the data-flow description or diagram}}

## Method: STRIDE per data flow

For each flow that crosses a boundary, ask the six questions:

- **Spoofing**: can someone pretend to be another user or service?
- **Tampering**: can data be modified in transit or at rest?
- **Repudiation**: can an action be denied for lack of records?
- **Information disclosure**: can data reach someone who should not see it?
- **Denial of service**: can the flow be exhausted or blocked?
- **Elevation of privilege**: can someone gain rights they should not have?

## Threats, mitigations and verification

| ID | Flow / asset | STRIDE | Threat | Mitigation | Verification (test or check) | Status |
|----|--------------|--------|--------|------------|------------------------------|--------|
| TH-01 | {{pending: flow}} | S | {{pending: threat}} | {{pending: control}} | {{pending: test ID in the test plan}} | open |

Every mitigation needs a verification. A mitigation without a planned test or check is a known gap, not a control. Writing a test ID here does not mean it has been executed.

## Accepted risks

Threats that will not be mitigated now must be accepted explicitly, with an owner and a review date. {{pending: list accepted risks or state "none"}}

## How to work on it

- Prepare context with `dixi workflow prepare threat-model`, or use `/dixi.threat-model` (Claude Code) or `$dixi-threat-model` (Codex) if the integration is installed.
- Run `dixi check` after editing to keep structure and references consistent.
- A human reviews and approves the result; an agent can draft, not approve.

## Related

- [Project](../00-master-spec.md)
- [Test plan](../11-quality/test-plan.md)
- [Secret management](secret-management.md)
- [Incident response](incident-response.md)
- [AI agent hardening](ai-agent-hardening.md)
