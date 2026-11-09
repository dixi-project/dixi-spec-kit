# Prompt template

## Purpose

Specify a prompt used by the product (not by developers) as a versioned, testable artifact: its
inputs, expected output contract, validation and evaluation cases. Copy the structure below for
each prompt.

## Template

````markdown
# Prompt: <name>

ID: {{pending: prompt ID}}
Version: 1.0.0
Owner: {{pending: person responsible}}
Used by: FEATURE-NNN
Model requirements: {{pending: capabilities needed, without tying the spec to a vendor}}

## Purpose

The task the model performs and why a model is the right tool for it.

## Inputs

| Variable | Source | Trusted? | Max length |
|---|---|---|---|
| `{{user_input}}` | user | no | |

## Prompt

```text
System instructions...
Context: {{context}}
Task: ...
Answer only in the format described below.
```

## Output contract

The structure the output must follow (e.g. a JSON schema), including allowed values.

## Validation

- Output is parsed and validated against the contract before use.
- Invalid output: retry once, then fall back to ...
- The output never grants permissions or triggers irreversible actions by itself.

## Evaluation cases

| Case | Input | Expected output or property |
|---|---|---|
| Normal | | |
| Edge | | |
| Injection attempt | | instruction ignored |

## Limits

- Cost and latency budget per call:
- Personal data sent to the model: {{pending: allowed data}}
````

## Related

- [Secure coding standard](../secure-coding-standard.md)
- [Feature template](feature-template.md)
- [Test plan](../../11-quality/test-plan.md)
