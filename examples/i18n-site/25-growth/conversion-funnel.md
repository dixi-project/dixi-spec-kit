# Conversion funnel

## Purpose

Define the steps a visitor goes through to become an active user or customer, how each step is measured, and how drop-offs are investigated. Definitions here must be precise enough that two people computing the same metric get the same number.

Status: draft. {{pending: define the funnel steps and the key conversion event}}

## Funnel steps

| Step | Definition (event) | Conversion from previous step | Baseline | Target |
|------|--------------------|-------------------------------|----------|--------|
| Visit | {{pending: page view on a public page}} | n/a | {{pending}} | {{pending}} |
| Interest | {{pending: for example views a pricing or feature page}} | {{pending}} | {{pending}} | {{pending}} |
| Sign-up | {{pending: account created}} | {{pending}} | {{pending}} | {{pending}} |
| Activation | {{pending: first key action completed}} | {{pending}} | {{pending}} | {{pending}} |
| Conversion | {{pending: paid or committed action, if applicable}} | {{pending}} | {{pending}} | {{pending}} |

Baselines are filled with real measured data only; leave them pending until then.

## Segments

Always look at the funnel broken down by:

- Language and market.
- Acquisition channel.
- Device type.
- New versus returning visitors.

## Instrumentation

- Each step maps to one named event with a documented schema.
- Every event includes language, channel (when known) and a timestamp; it excludes unnecessary personal data.
- Event names and properties are versioned; a change is reviewed like a contract change.
- Tracking respects consent: no optional tracking before the person agrees.

{{pending: decide the analytics approach and where the event schema lives}}

## Drop-off analysis

1. Find the step with the largest relative loss for a segment.
2. Gather evidence: session observations, support questions, research findings.
3. Write a hypothesis and the expected change in the step's conversion.
4. Fix obvious defects directly; test uncertain changes when traffic allows.
5. Record the result, including changes that did not help.

## Review cadence

| Review | Frequency | Participants |
|--------|-----------|--------------|
| Funnel metrics | {{pending}} | {{pending}} |
| Segment deep dive | {{pending}} | {{pending}} |

## Related

- [Growth strategy](growth-strategy.md)
- [Landing pages catalog](landing-pages-catalog.md)
- [PII classification](../08-data/pii-classification.md)
- [Discovery strategy](../24-research/discovery-strategy.md)
- [Acceptance strategy](../11-quality/acceptance-strategy.md)
