# Quality gates for AI-assisted work

## Purpose

List, in order, the gates a change must pass before it is merged, and the extra gates for features that call a language model. A gate exists only if a mechanism or a named person enforces it and leaves evidence.

## Gates in order

| # | Gate | Evidence | Enforced by |
| --- | --- | --- | --- |
| 1 | Spec approved and traced | Entry in `.dixi/traceability.json` | `dixi check` plus reviewer |
| 2 | Tests written first and failing | Commit order in the pull request | Reviewer |
| 3 | Structure valid | `dixi check` output | Automated |
| 4 | Project tests pass | Test runner output | {{pending: CI or local command}} |
| 5 | Static analysis and security scan | Tool reports | {{pending: tools chosen}} |
| 6 | Human review of the diff | Approval on the final revision | Person |
| 7 | Merge | Protected branch rules | {{pending: mechanism}} |

## Extra gates for features with a model

### Tests of the calling code

- Model responses are stubbed; tests cover valid, malformed and refused outputs.
- Schema validation rejects unexpected output.

### Evaluations against the real model

- A versioned evaluation set with an acceptance threshold agreed before running it.
- Re-run when the model, prompt template or parameters change.
- Threshold and evaluation set: {{pending: define evaluation set and pass threshold}}

### Tools exposed to the model

- Each tool has tests for permission checks and for rejected inputs.

## What is not a gate

- An agent's verdict: it prepares the human review, it does not replace it.
- Coverage alone: it measures executed lines, not detected errors.
- An evaluation without a threshold: a number without acceptance criteria is data, not a control.
- "It looked fine": no mechanism, no evidence, no gate.

## Related

- [AI audit trail](ai-audit-trail.md)
- [Responsible AI](responsible-ai.md)
- [Validation rules](../sdd/validation-rules.md)
- [Human in the loop](../agents/human-in-the-loop.md)
- [Test plan](../../11-quality/test-plan.md)
