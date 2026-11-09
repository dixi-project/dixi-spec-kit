# Property-based testing guide

## Purpose

Explain how to use property-based tests, which check rules that must hold for many generated inputs, to find edge cases that hand-picked examples miss.

Status: draft. {{pending: decide where property-based tests are expected}}

## When to use them

- Pure functions with clear rules: parsing, serialisation, calculations, money, dates.
- Code with large input spaces where examples cover only a fraction.
- Invariants that must never break (a balance never goes negative, a sort keeps all items).

They complement, not replace, example-based tests.

## Finding properties

| Pattern | Example property |
|---------|------------------|
| Round trip | Decoding an encoded value returns the original |
| Invariant | Sorting keeps the same number of items |
| Idempotence | Applying a normalisation twice equals applying it once |
| Oracle | The optimised version matches a simple reference version |
| Commutativity | Order of independent operations does not change the result |
| Bounds | A computed discount never exceeds the subtotal |

## Guidelines

- Write the property from the spec before the code, as with any test (red first).
- Constrain generators to valid domain values; test invalid input separately.
- When a failure is found, keep the shrunk counterexample as a regular example test.
- Fix the random seed or record it so failures are reproducible.
- Keep run counts reasonable for local runs. {{pending: example count locally and in CI}}

## Tooling

{{pending: choose a property-based testing library for the stack}}

## Pitfalls

- Properties that restate the implementation prove nothing.
- Over-filtered generators that rarely produce useful input.
- Ignoring a failure as "random"; every failure is a real counterexample.

## Related

- [TDD guide](tdd-guide.md)
- [Test pyramid](test-pyramid.md)
- [Mutation testing guide](mutation-testing-guide.md)
- [Verification ladder](verification-ladder.md)
