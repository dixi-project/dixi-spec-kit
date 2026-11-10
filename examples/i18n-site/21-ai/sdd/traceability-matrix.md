# Traceability matrix

## Purpose

Explain how artifacts are linked from business goal to test, where those links live, and how to find gaps. The source of truth is `.dixi/traceability.json`; this document describes how to read and maintain it.

## Chain

```text
GOAL → DOMAIN → MODULE → FEATURE → CONTRACT → TEST
```

Each item in `.dixi/traceability.json` has an `id`, a `kind`, a `path` and a list of `parents`. A child must reference an existing parent of the previous kind.

## Example view

| ID | Kind | Path | Parents |
| --- | --- | --- | --- |
| GOAL-001 | goal | `01-business/vision.md` | — |
| DOMAIN-001 | domain | `03-domains/example/domain-spec.md` | GOAL-001 |
| MODULE-001 | module | `04-modules/example/module-spec.md` | DOMAIN-001 |
| FEATURE-001 | feature | `05-features/example/feature-spec.md` | MODULE-001 |
| CONTRACT-001 | contract | `07-contracts/example.md` | FEATURE-001 |
| TEST-001 | test | `11-quality/test-plan.md` | CONTRACT-001 |

Replace the example rows as real artifacts are created. Never reuse an ID for a different artifact.

## Maintenance

1. Register a new spec in `.dixi/traceability.json` in the same change that creates it.
2. Run `dixi check` to detect missing files, unknown parents and broken links.
3. When an artifact is retired, mark it deprecated in the document before removing the entry.

## Gaps to look for

- Goals with no domain, or features with no contract.
- Contracts with no test entry.
- Code paths or tests that cannot be traced to any feature.
- Specs whose parent was deprecated.

## Project decisions

- ID scheme beyond the defaults: {{pending: ID prefixes and numbering rules}}
- Whether horizontal links (module to module dependencies) are tracked: {{pending: track dependencies or not}}

## Related

- [Methodology](methodology.md)
- [Validation rules](validation-rules.md)
- [Goal](../../01-business/vision.md)
- [Example feature](../../05-features/example/feature-spec.md)
- [Example contract](../../07-contracts/example.md)
- [Test plan](../../11-quality/test-plan.md)
