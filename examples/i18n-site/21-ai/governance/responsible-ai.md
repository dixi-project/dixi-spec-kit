# Responsible AI

## Purpose

Set the principles that govern how this project uses AI, both to build software and inside the product. These are commitments to follow and check, not certifications.

## Principles

### Transparency

- Disclose when AI generated or substantially changed an artifact (code, spec, test, review).
- Label agent reviews and summaries as such.
- Tell product users when they interact with AI-generated content. {{pending: how the product discloses AI use}}

### Accountability

- Every AI output has a responsible person.
- The person who approves a change owns its content.
- Structural decisions are always human, even when an agent proposes them.

### Fairness

- Watch for bias in generated examples, test data, copy and user flows.
- Use varied, synthetic examples; do not assume demographics or abilities.

### Privacy

- Never put credentials or secrets in prompts.
- Avoid personal data in prompts; prefer synthetic or anonymised data.
- Check that generated code does not leak sensitive data in logs or errors.

### Safety and security

- Review generated code for vulnerabilities like any other code.
- Do not rely on AI alone for security-critical logic.
- Prevent destructive actions without human confirmation.

### Honesty about evidence

- Report checks and tests exactly as observed; never claim an evaluation that did not run.

## Data sent to AI services

| Data class | Allowed in prompts? |
| --- | --- |
| Public | {{pending: yes / no}} |
| Internal | {{pending: yes / no / with conditions}} |
| Personal or confidential | {{pending: yes / no / with conditions}} |

## Impact questions for product features with AI

1. What does the AI decide or produce, and about whom?
2. What harm can an error, bias or manipulation cause?
3. Which controls mitigate it, and how is each one tested?
4. How does a person intervene or contest a result?

## Related

- [AI audit trail](ai-audit-trail.md)
- [Guardrails](../agents/guardrails.md)
- [Human in the loop](../agents/human-in-the-loop.md)
- [Project instructions](../../AGENTS.md)
