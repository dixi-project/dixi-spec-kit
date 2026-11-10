# Customer outage communication

## Purpose

Tell users what is happening during an outage in a clear, honest and timely way, without speculating or promising what cannot be kept.

Status: draft. {{pending: name the communications lead role}}

## When it applies

Any incident that users can notice, usually SEV1 and SEV2 (see [incident levels](../incident-levels.md)).

## Channels

| Channel | Used for | Owner |
|---------|----------|-------|
| {{pending: status page}} | All visible incidents | Communications lead |
| {{pending: in-app banner}} | Ongoing outage | Communications lead |
| {{pending: e-mail, e.g. support@example.com}} | Affected accounts, final summary | Support |

## Steps

1. **First notice** within {{pending: minutes}} of declaring the incident, even if the cause is unknown.
2. **Updates** every {{pending: interval}} while the incident is open, even if nothing changed.
3. **Resolution notice** when the [restore service](restore-service.md) close criteria are met.
4. **Follow-up** with a short summary for SEV1 within {{pending: days}}.

Every message is reviewed by the incident lead before it goes out. An AI agent may draft, a person publishes.

## Message templates

First notice:

> We are investigating a problem affecting {{pending: feature}}. Some users may {{pending: symptom}}. Next update at {{pending: time and time zone}}.

Update:

> We have identified the cause and are applying a fix. {{pending: what works and what does not}}. Next update at {{pending: time}}.

Resolution:

> The problem affecting {{pending: feature}} was resolved at {{pending: time}}. {{pending: whether any action is needed from users}}. We are sorry for the disruption.

## Rules

- Say what users experience, not internal component names.
- Never blame a vendor or a person in public messages.
- Do not give an end time you are not confident about.
- Publish in every language the product supports. {{pending: list languages}}
- If personal data may be involved, stop and ask the incident lead before writing anything.

## Related

- [Incident levels](../incident-levels.md)
- [Escalation matrix](../escalation-matrix.md)
- [Restore service](restore-service.md)
- [Incident response](../../13-security/incident-response.md)
