# Secure coding standard

## Purpose

Give whoever writes or reviews code, person or agent, one page with the rules that must not fail.
These rules apply to every change, regardless of stack or profile.

Owner of this standard: {{pending: role responsible for security review}}

## Rules

1. **Authorize in the query.** Every access by identifier filters by owner and tenant, so a user
   cannot read another user's record by changing an ID (IDOR / broken object level authorization).
2. **Validate external input with a schema at the boundary.** Reject unknown fields, enforce
   types, lengths and ranges. Anything that crosses a trust boundary is external input.
3. **Parameterized queries only**, or a query builder that parameterizes. Never build queries,
   shell commands or file paths by concatenating input.
4. **Encode output for its context** (HTML body, attribute, URL, script). Do not inject raw
   external data into the page or evaluate it as code.
5. **Secrets outside the code and the repository.** Read them at runtime from a secret store;
   rotate them if they ever reach a log, a commit or a ticket.
6. **Verify dependencies before installing.** Check provenance, maintenance and known
   vulnerabilities; commit the lock file. {{pending: dependency scanning tool and policy}}
7. **Errors do not leak internals.** Users receive a stable code and a safe message; stack traces
   and queries stay in protected logs.
8. **Logs never contain secrets, tokens, passwords or unmasked personal data.**
9. **Least privilege** for services, tokens, database users and automation, including AI agents
   and the tools they can call.
10. **Treat model and user content as untrusted.** If the project uses language models, validate
    their output before acting on it and never let it widen permissions.
11. **Threat-model sensitive features**: authentication, personal data, money, file upload,
    external input or AI. Each identified threat gets at least one test.
12. **Automated checks in every pull request.** {{pending: static analysis and secret scanning
    tools wired into `make verify`}}

## Review checklist

- [ ] Every new endpoint or page checks authorization, not only authentication.
- [ ] All new inputs are validated; all new outputs are encoded.
- [ ] No secret, credential or personal data in code, fixtures, logs or screenshots.
- [ ] New dependencies were reviewed and pinned.
- [ ] Sensitive features list their threats and the tests that cover them.

## Reporting

Vulnerabilities found in the project are reported through {{pending: private disclosure channel,
e.g. security@example.com}}, never in a public issue.

## Related

- [Coding standards](coding-standards.md)
- [Postmortem template](templates/postmortem-template.md)
- [Test plan](../11-quality/test-plan.md)
- [Project instructions](../AGENTS.md)
