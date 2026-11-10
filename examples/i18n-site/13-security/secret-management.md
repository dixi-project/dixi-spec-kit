# Secret management

## Purpose

Define how the project stores, distributes, uses and retires secrets (passwords, API keys, tokens, certificates, signing keys) so that none of them live in the repository, in logs or in an AI agent's context.

Status: draft. {{pending: name the owner of secret management}}

## Principles

- Secrets never enter version control, not even in history, examples or tests.
- Each environment has its own secrets; production secrets are never reused in development.
- Each secret has an owner, a purpose and a scope as narrow as possible.
- Applications read secrets at runtime from a managed store or the environment, never from source code.
- People and agents get access to the minimum set of secrets their task needs.

## Inventory

Keep a list of secret *names*, never values.

| Name | Purpose | Environments | Owner | Storage | Rotation |
|------|---------|--------------|-------|---------|----------|
| {{pending: e.g. DATABASE_PASSWORD}} | {{pending: purpose}} | {{pending: dev / staging / prod}} | {{pending: owner}} | {{pending: store}} | {{pending: frequency}} |

## Storage decision

- Where secrets live in each environment: {{pending: choose a secret store or mechanism per environment}}
- Who can read and who can write them: {{pending: define access roles}}
- How access is audited: {{pending: define audit trail}}

## Local development

- Use a local `.env` file that is ignored by version control; commit only a `.env.example` with placeholder values such as `CHANGE_ME`.
- Do not paste secrets into issues, pull requests, chat tools or AI prompts.
- AI agents must not read `.env*` files, key files or credential stores.

## Detection and prevention

- Scan commits for secrets before they are pushed: {{pending: choose a pre-commit or CI secret scanner}}
- Scan the full history at least once when adopting this policy.
- Mask secrets in logs and error messages.

## If a secret leaks

1. Treat it as compromised, even if the exposure was brief or the repository is private.
2. Revoke or rotate it first; cleaning history comes after.
3. Review access logs for misuse during the exposure window.
4. Record the event following the incident response process.

## Related

- [Threat model](threat-model.md)
- [Incident response](incident-response.md)
- [AI agent hardening](ai-agent-hardening.md)
- [Agent instructions](../AGENTS.md)
