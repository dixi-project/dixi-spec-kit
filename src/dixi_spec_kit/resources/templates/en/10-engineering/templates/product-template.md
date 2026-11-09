# Product template

## Purpose

Describe one product of the platform: its vision, users, core features, the modules it uses and
how success is measured. A platform may host several products that share modules. Copy the
structure below for each product.

## Template

```markdown
# Product: <product name>

ID: {{pending: product ID}}
Status: idea | discovery | building | live | retired
Owner: {{pending: product owner}}
Business goal: GOAL-NNN

## Vision

One paragraph: for whom, what problem, why now, and how it differs from alternatives.

## Users

| Persona | Need | Main journey |
|---|---|---|

## Core features

| Feature | Priority (must / should / could) | ID |
|---|---|---|

## Modules used

| Module | Shared with other products? | Notes |
|---|---|---|

## External dependencies

| System | Purpose | Integration spec |
|---|---|---|

## Non-functional requirements

- Availability: {{pending: target}}
- Performance: {{pending: target}}
- Languages and markets: {{pending: supported locales and regions}}
- Privacy and compliance: personal data handled, applicable obligations.

## Success metrics

| Metric | Baseline | Target | How it is measured |
|---|---|---|---|

## Roadmap

| Stage | Scope | Exit criteria |
|---|---|---|
```

## Related

- [Business goal](../../01-business/vision.md)
- [Module template](module-template.md)
- [External integration template](external-integration-template.md)
- [Feature template](feature-template.md)
