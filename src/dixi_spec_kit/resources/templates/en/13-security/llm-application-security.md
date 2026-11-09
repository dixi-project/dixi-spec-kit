# LLM application security

## Purpose

Set the security rules for features where the product itself calls a large language model: chat, summarization, classification, extraction, agents with tools. The core rule: model output is untrusted data, never an instruction the system executes without validation.

Status: draft. {{pending: decide whether the product uses language models and in which features}}

## When this applies

Any feature that sends user or business data to a model, or acts on what a model returns. Coding agents used by the team are covered in AI agent hardening.

## Main risks

| Risk | Example | Baseline control |
|------|---------|------------------|
| Prompt injection | User text or a fetched document overrides instructions | Separate instructions from data; never grant authority based on model output |
| Insecure output handling | Model output rendered as HTML or run as a query | Validate against a schema; encode before rendering |
| Sensitive data disclosure | Prompt includes secrets or another user's data | Minimize context; filter by the caller's permissions |
| Excessive agency | Model calls a tool that deletes or pays | Allowlisted tools, least privilege, human confirmation for irreversible actions |
| Unbounded consumption | Large or repeated requests exhaust budget | Token, rate and cost limits per user and globally |
| Supply chain | Untrusted model, plugin or dataset | Approve models and integrations explicitly |

## Design patterns

1. **Structured output**: request a defined schema and reject anything that does not validate.
2. **Read-only by default**: if the model needs data, give it narrow, read-only access filtered by the user's permissions.
3. **Tool gating**: each tool has an allowlist, argument validation and an owner; destructive tools require human confirmation.
4. **Context hygiene**: never include secrets, credentials or data the current user cannot see.

## Project decisions

- Model provider and hosting: {{pending: choose; record data-handling terms}}
- Data that must never be sent to the model: {{pending: list}}
- Limits on tokens, requests and cost: {{pending: define}}
- Logging of prompts and outputs without personal data: {{pending: define}}

## Checklist for a feature spec

- [ ] Inputs and outputs of the model are defined.
- [ ] Output is validated before use.
- [ ] Abuse cases (injection, data extraction) have tests in the test plan.
- [ ] Limits and fallbacks are specified.

## Related

- [AI agent hardening](ai-agent-hardening.md)
- [Threat model](threat-model.md)
- [Data protection controls](data-protection-controls.md)
- [Test plan](../11-quality/test-plan.md)
