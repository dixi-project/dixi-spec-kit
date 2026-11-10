# Design principles

## Purpose

State the few principles that guide every design and product decision, so that people and agents can settle trade-offs the same way without a meeting. Principles are useful only if they help choose between two reasonable options.

Status: draft. {{pending: agree the final list of principles with the people responsible for product and design}}

## How to write a principle

- Short, memorable and specific to this product.
- Expresses a trade-off: what we favour and what we accept giving up.
- Comes with an example of a decision it settled.
- Avoids slogans that nobody would disagree with, such as "be user-friendly".

## Starting set

Adapt, replace or remove these; keep between three and seven.

| Principle | We favour | Over | Example decision |
|-----------|-----------|------|------------------|
| Clarity first | Plain words and obvious actions | Clever or decorative interfaces | {{pending: example}} |
| Accessible by default | Interfaces everyone can use with keyboard, screen reader or zoom | Visual effects that exclude people | {{pending: example}} |
| Every language is first class | Layouts that work in any supported language and text length | Designs tuned only for the primary language | {{pending: example}} |
| Fast is a feature | Lightweight pages and immediate feedback | Heavy assets and animations | {{pending: example}} |
| Respect the user's attention | Fewer, meaningful notifications | Growth tricks and dark patterns | {{pending: example}} |
| {{pending: product-specific principle}} | {{pending}} | {{pending}} | {{pending}} |

## Using the principles

- Cite the principle when recording a design decision in a spec or review.
- When two principles conflict, record which one won and why; repeated conflicts mean a principle needs rewording.
- Agents preparing UI proposals list the principles they applied.

## Reviewing the principles

{{pending: decide how often the principles are reviewed and what evidence can change them}}

- Check them against research findings and support trends.
- Retire principles that no longer settle real decisions.

## Related

- [Accessibility standard](accessibility-standard.md)
- [Content guidelines](content-guidelines.md)
- [Information architecture](information-architecture.md)
- [Web vitals budgets](../11-quality/performance-budgets/web-vitals-budgets.md)
- [Persona template](../24-research/persona-template.md)
- [Business goal](../01-business/vision.md)
