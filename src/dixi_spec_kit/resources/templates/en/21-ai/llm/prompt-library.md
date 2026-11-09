# Prompt library

## Purpose

Keep prompts used by the project (in development procedures and in product features) versioned, reviewed and testable, so that a response can be traced to the exact template that produced it.

## Where prompts live

- Development procedures: shared through `dixi workflow` and the agent commands (`/dixi.*` or `$dixi-*`); do not fork them silently.
- Product prompts: {{pending: directory for product prompt templates}}

## Template format

Each product template is a file with a header and a body:

```text
id: summarise-ticket
version: 1
purpose: Summarise a support ticket for an agent.
inputs: ticket_text (untrusted), language
output: JSON matching contract CONTRACT-xxx
owner: role responsible
```

Rules:

- One template per purpose; give it a stable ID.
- Mark which inputs are untrusted and keep them clearly delimited.
- Ask for structured output and validate it against the contract.
- Never embed secrets or personal data in templates.

## Versioning

- Any change to wording, examples or parameters increments the version.
- The version is logged with each call (see the AI audit trail).
- A new version re-runs the evaluation set before release.

## Catalogue

| ID | Version | Purpose | Contract | Evaluation set | Owner |
| --- | --- | --- | --- | --- | --- |
| {{pending: template ID}} | 1 | {{pending: define}} | {{pending: define}} | {{pending: define}} | {{pending: define}} |

## Review checklist

- [ ] Purpose and output format are explicit.
- [ ] Untrusted inputs are delimited and not treated as instructions.
- [ ] Refusal and error behaviour is defined.
- [ ] Language and tone match the product's locales.

## Related

- [Context strategy](context-strategy.md)
- [Model strategy](model-strategy.md)
- [AI audit trail](../governance/ai-audit-trail.md)
- [Quality gates](../governance/quality-gates.md)
