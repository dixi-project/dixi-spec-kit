# Incident response

## Purpose

Give the team a short, rehearsed path for detecting, containing, resolving and learning from security incidents, so decisions under pressure follow a plan instead of improvisation.

Status: draft. {{pending: name the incident lead and a backup}}

## What counts as an incident

- Leaked or misused secret or credential.
- Unauthorized access to data, accounts or infrastructure.
- Exploited vulnerability or malicious dependency.
- Data loss, corruption or unexpected disclosure.
- An AI agent or automation acting outside its granted scope.
- {{pending: add project-specific cases}}

## Severity levels

| Level | Example | Response target |
|-------|---------|-----------------|
| Critical | Active data exposure, production compromise | {{pending: time to start response}} |
| High | Exploitable flaw, leaked production secret | {{pending: target}} |
| Medium | Limited exposure, no evidence of misuse | {{pending: target}} |
| Low | Weakness without immediate impact | {{pending: target}} |

## Contacts

| Role | Contact | Backup |
|------|---------|--------|
| Incident lead | {{pending: name, security@example.com}} | {{pending: backup}} |
| Technical owner | {{pending: contact}} | {{pending: backup}} |
| Communications / legal | {{pending: contact}} | {{pending: backup}} |

## Phases

1. **Detect and report**: anyone can raise an incident; record the time and what was observed.
2. **Triage**: assign severity and an incident lead; open a private record.
3. **Contain**: revoke credentials, disable affected access, isolate components. Preserve evidence before destroying anything.
4. **Eradicate**: remove the cause (patch, rotate, remove malicious code).
5. **Recover**: restore service, verify integrity, monitor closely.
6. **Notify**: decide whether users, partners or authorities must be informed. {{pending: list applicable notification obligations and deadlines}}
7. **Learn**: hold a blameless review; turn findings into specs, tests and threat-model updates.

## Incident record

For each incident keep: ID, dates and times, severity, timeline, affected assets, actions taken, people involved, root cause, follow-up items with owners.

## Rehearsal

Practice the plan with a tabletop exercise. {{pending: define rehearsal frequency}}

## Related

- [Threat model](threat-model.md)
- [Secret management](secret-management.md)
- [AI agent hardening](ai-agent-hardening.md)
- [Project](../00-master-spec.md)
