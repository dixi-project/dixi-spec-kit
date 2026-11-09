# Break-glass access

## Purpose

Define the emergency access path used when normal access controls block a person from resolving a critical incident. Break-glass access exists to be rare, loud and fully audited.

Status: draft. {{pending: name the owner of break-glass access}}

## When it may be used

- A critical incident is active and normal access is unavailable or insufficient.
- {{pending: list other allowed situations}}

It must not be used for convenience, routine maintenance or to bypass review.

## Who may use it

| Person or role | Scope of access | Second approver |
|----------------|-----------------|-----------------|
| {{pending: role}} | {{pending: systems}} | {{pending: role}} |

Keep the list short; review it at least {{pending: frequency}}.

## Mechanism

- Where emergency credentials are kept and how they are protected: {{pending: define, e.g. sealed store requiring two people}}
- Second factor required: {{pending: yes / method}}
- Access is time-limited: {{pending: maximum duration}}
- Credentials are never shared with AI agents or automations.

## Detection

Every use triggers an immediate alert to {{pending: recipients}}. An unexpected alert is treated as a security incident.

## After use

1. Record who, when, why, what was accessed and what was changed.
2. Rotate the emergency credentials.
3. Review the event in the incident post-mortem.
4. Fix the gap that made break-glass necessary, if possible.

## Rehearsal

Test the procedure on a non-production environment at a fixed cadence so it works when needed. {{pending: define cadence}}

## Related

- [Incident response](incident-response.md)
- [Secret management](secret-management.md)
- [Data protection controls](data-protection-controls.md)
- [Risk register](risk-register.md)
