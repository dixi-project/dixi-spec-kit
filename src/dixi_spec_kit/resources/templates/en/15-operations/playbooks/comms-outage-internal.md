# Internal outage communication

## Purpose

Keep the team, support and leadership informed during an outage through one place, so responders can focus and nobody acts on rumours.

Status: draft. {{pending: name the communications lead role}}

## When it applies

Every incident from SEV3 upward (see [incident levels](../incident-levels.md)).

## Channels

| Channel | Purpose | Who writes |
|---------|---------|-----------|
| {{pending: incident channel}} | Technical coordination, one per incident | Responders |
| {{pending: announcements channel}} | Short status for the whole company | Communications lead |
| {{pending: support channel or tool}} | What to tell users, macros | Communications lead |

## Steps

1. **Open** an incident channel named `inc-<date>-<short-name>` and pin the level, lead and start time.
2. **Announce** in the company channel within {{pending: minutes}}: what is affected, level, who leads, where to follow.
3. **Brief support** with a ready-to-use reply that matches the [customer outage communication](comms-outage-customer.md).
4. **Update** every {{pending: interval}}, or at once when the level changes.
5. **Close** with a final message: restored at, impact, next steps and postmortem date.

## Update template

> **[SEV level] Short title** — Status: investigating / mitigating / monitoring / resolved.
> Impact: {{pending: who is affected and how}}.
> Current action: {{pending: what is being done}}.
> Next update: {{pending: time}}. Lead: {{pending: role or name}}.

## Rules

- Only the incident lead or communications lead posts status updates; others ask in the incident channel.
- Keep side discussions out of the incident channel.
- Do not share credentials, personal data or raw customer records in any channel.
- If leadership needs a decision, ask for it explicitly with options.

## Close criteria

- Final message posted in every channel used.
- Support confirmed it has the closing reply.
- Incident channel archived after the postmortem.

## Related

- [Incident levels](../incident-levels.md)
- [Escalation matrix](../escalation-matrix.md)
- [Customer outage communication](comms-outage-customer.md)
- [Restore service](restore-service.md)
