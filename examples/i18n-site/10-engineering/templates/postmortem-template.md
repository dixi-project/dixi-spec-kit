# Postmortem template

## Purpose

Learn from an incident without blame: reconstruct what happened, why it was possible and which
actions will prevent or shorten it next time. Copy the structure below after each incident that
meets the project's threshold.

Threshold for writing a postmortem: {{pending: severity or impact that requires one}}

## Template

```markdown
# Postmortem: <short incident title>

Date of incident: YYYY-MM-DD
Severity: {{pending: severity level}}
Status: draft | reviewed | actions closed
Authors: ...

## Summary

Two or three sentences: what failed, who was affected, for how long.

## Impact

- Users or clients affected:
- Duration (detection to resolution):
- Data affected (loss, exposure, corruption):

## Timeline (UTC)

| Time | Event |
|---|---|
| hh:mm | First symptom |
| hh:mm | Detected by ... |
| hh:mm | Mitigated |
| hh:mm | Resolved |

## Root cause and contributing factors

Describe the conditions that made the failure possible. Focus on systems and
processes, not on individuals.

## Detection

How it was detected and how it could have been detected earlier.

## What went well / what went poorly

- ...

## Actions

| Action | Type (prevent / detect / mitigate) | Owner | Due date | Ticket |
|---|---|---|---|---|

## Lessons

What the team now knows that it did not know before.
```

## Rules

- Blameless: name roles and systems, not people at fault.
- Never include secrets or personal data; if any were exposed, say so and how it was contained.
- Each action has an owner and a date; the postmortem closes when actions close.

## Related

- [Runbook template](runbook-template.md)
- [ADR template](adr-template.md)
- [Secure coding standard](../secure-coding-standard.md)
