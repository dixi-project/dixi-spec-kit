# Frequently asked questions

## Purpose

Answer the questions newcomers and reviewers ask most often about how this project works, so that answers are consistent and nobody has to rediscover them. Add a question when it has been asked twice.

Status: draft. {{pending: add the questions specific to this project}}

## Getting started

**Where do I start reading?**
With the [project spec](../00-master-spec.md), the [business goal](../01-business/vision.md) and the [documentary workflow](../docs/guide.md).

**How do I know the documents are consistent?**
Run `dixi check`. It verifies structure and traceability links; it does not test the application.

**What does `make verify` run?**
At first only `dixi check`. The project must connect its real test suite to it. {{pending: what `make verify` runs in this project}}

## Specs and tests

**Can I write code before the spec?**
Only for a throwaway spike that never merges. Merged code traces to a feature spec.

**A committed test looks wrong. Can I fix it?**
Not directly. Stop, explain why, point to the spec and ask the responsible person. Changing a frozen test needs a spec change and approval.

**What does `{{pending: ...}}` mean?**
An open decision. Leave it visible until someone with authority decides.

## Agents

**What can an agent do on its own?**
Draft specs, tests and code on a branch and run read-only checks. See [AI governance](../00-governance/ai-governance.md).

**Can an agent merge or deploy?**
No. Agents never sign, approve, merge or deploy.

**Which commands exist for agents?**
`/dixi.*` operations in Claude Code or `$dixi-*` in Codex, when that integration is installed.

## Review and release

**Who approves a pull request?**
{{pending: who approves pull requests}}

**When is a feature "done"?**
When its criteria have passing tests, `make verify` is green and reported, and a person reviewed and merged it.

## Related

- [Glossary](glossary.md)
- [Onboarding guide](onboarding-guide.md)
- [Decision log](decision-log.md)
- [Project instructions](../AGENTS.md)
