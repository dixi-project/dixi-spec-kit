# Key rotation

## Purpose

Define how cryptographic keys, signing keys, certificates and long-lived credentials are rotated on schedule and in emergencies, without downtime and without leaving old material active.

Status: draft. {{pending: name the owner of key rotation}}

## Inventory

| Key or credential | Use | Owner | Rotation period | Method | Last rotated |
|-------------------|-----|-------|-----------------|--------|--------------|
| {{pending: e.g. data encryption key}} | {{pending: use}} | {{pending: owner}} | {{pending: period}} | {{pending: automatic / manual}} | {{pending: date}} |

Record names and metadata only, never key material.

## Principles

- Prefer short-lived, automatically issued credentials over long-lived ones.
- Prefer automatic rotation; manual rotation needs a written runbook and a calendar reminder.
- Rotation must be possible at any time, not only on schedule; practise it.
- Each key has a single purpose.

## Rotation procedure (zero downtime)

1. Create the new key or credential alongside the current one.
2. Deploy consumers that accept both old and new.
3. Switch producers to the new key.
4. Confirm no traffic still uses the old key (logs or metrics).
5. Revoke or disable the old key; keep decryption-only access if stored data still depends on it.
6. Record the rotation date and who performed it.

## Emergency rotation

Triggered by a suspected leak or compromise. Skip waiting periods, revoke first, accept short disruption if needed, then follow incident response. {{pending: define who can trigger emergency rotation}}

## Data encrypted with old keys

{{pending: decide whether stored data is re-encrypted after rotation or keeps old keys in decrypt-only mode}}

## Verification

- A rotation drill runs at least {{pending: frequency}} on a non-production environment.
- Alerts fire when a credential is older than its rotation period.

## Related

- [Secret management](secret-management.md)
- [Incident response](incident-response.md)
- [Break-glass access](break-glass-access.md)
- [Threat model](threat-model.md)
