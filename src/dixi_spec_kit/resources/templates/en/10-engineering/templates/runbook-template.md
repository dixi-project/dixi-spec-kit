# Runbook template

## Purpose

Give the person on call a short, tested procedure to diagnose and resolve a known operational
situation without needing the author present. Copy the structure below for each alert or task.

## Template

```markdown
# Runbook: <situation or alert name>

Service: {{pending: affected component}}
Severity: {{pending: severity scale and level}}
Owner: {{pending: team or role that maintains this runbook}}
Last tested: YYYY-MM-DD

## When to use

The alert, symptom or request that triggers this runbook.

## Impact

What users or systems experience while this is happening.

## Prerequisites

- Access and permissions needed (never paste credentials here).
- Tools required.

## Diagnosis

1. Check ... (dashboard, log query or command, with what "normal" looks like).
2. Confirm ...

## Resolution

1. Step, with the expected result.
2. Step, with the expected result.

## Verification

How to confirm the service is healthy again.

## Rollback

How to undo the resolution steps if they make things worse.

## Escalation

Who to contact, through which channel, and after how long.

## History

| Date | Incident or change | Notes |
|---|---|---|
```

## Notes

- Every step is a concrete action with an expected result; avoid "investigate".
- Test runbooks periodically and after each incident that used them.

## Related

- [Postmortem template](postmortem-template.md)
- [Secure coding standard](../secure-coding-standard.md)
- [Project instructions](../../AGENTS.md)
