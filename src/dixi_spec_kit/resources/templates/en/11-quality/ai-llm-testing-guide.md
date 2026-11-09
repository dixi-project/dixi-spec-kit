# AI and LLM testing guide

## Purpose

Explain how to test features that use language models or other AI components, whose outputs are probabilistic, so that quality is measured with evidence instead of impressions.

Status: draft. {{pending: list the AI features in scope and their owners}}

## What changes with AI components

- The same input can produce different outputs.
- "Correct" is often a range of acceptable answers, not one value.
- Model, prompt or data changes can shift behaviour without any code change.

The code around the model is still tested normally with TDD; this guide covers the model's behaviour.

## Layers

| Layer | What it checks | How |
|-------|----------------|-----|
| Deterministic code | Prompt building, parsing, validation, fallbacks | Unit tests with a fake model |
| Output contract | Responses match the expected structure | Schema validation on every response |
| Evaluation set | Quality on representative cases | Scored runs against a versioned dataset |
| Safety | Refusals, harmful content, data leaks, prompt injection | Adversarial cases in the evaluation set |
| Production | Drift and failures with real use | Monitoring and sampled human review |

## Evaluation sets

- Build a versioned set of inputs with expected outcomes or scoring rules. {{pending: size and source of the evaluation set}}
- Include edge cases, other languages and adversarial inputs.
- Never put real personal data or secrets in evaluation sets.
- Score with exact checks where possible; use rubric-based or model-assisted scoring only with periodic human calibration.

## Thresholds

| Metric | Threshold | Blocks release |
|--------|-----------|----------------|
| {{pending: metric, for example task success rate}} | {{pending: threshold}} | {{pending: yes/no}} |
| {{pending: metric, for example unsafe output rate}} | {{pending: threshold}} | {{pending: yes/no}} |

Re-run the evaluation set when the model, prompt, parameters or retrieval data change. Do not lower a threshold to pass a run.

## Untrusted content

Treat model output and retrieved documents as data, not instructions. Test that injected instructions in inputs do not change system behaviour.

## Related

- [Quality strategy](quality-strategy.md)
- [Security test plan](security-test-plan.md)
- [Regression plan](regression-plan.md)
- [Risk-based review](risk-based-review.md)
- [Test plan](test-plan.md)
