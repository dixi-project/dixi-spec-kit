# Accessibility standard

## Purpose

Set the accessibility level the project commits to and the checks that show each feature meets it, so that people with disabilities can perceive, operate and understand the product in every supported language.

Status: draft. {{pending: confirm the target conformance level, for example WCAG 2.2 level AA}}

This document is a working standard, not a statement of conformance. Conformance can only be claimed after real audits.

## Target

| Item | Decision |
|------|----------|
| Guideline and level | {{pending: guideline version and level}} |
| Scope | {{pending: all public pages and authenticated screens, or a subset}} |
| Supported assistive technologies | {{pending: screen readers, voice control, magnification to test with}} |
| Supported browsers and devices | {{pending: list}} |

## Requirements every screen meets

### Perceivable

- Text alternatives for meaningful images; decorative images are hidden from assistive technology.
- Colour contrast of at least 4.5:1 for normal text and 3:1 for large text and interface components.
- Information is never conveyed by colour alone.
- Content reflows at 320 CSS pixels wide and at 200% zoom without loss.
- Captions for video and transcripts for audio.

### Operable

- Every action works with a keyboard alone, with a visible focus indicator and a logical focus order.
- No keyboard traps; skip link to the main content.
- Target size large enough to tap comfortably.
- Motion and auto-playing content can be paused; respect the reduced-motion preference.
- Time limits can be extended or turned off.

### Understandable

- The `lang` attribute is set for the page and for any passage in another language.
- Form fields have visible labels; errors explain what went wrong and how to fix it.
- Navigation and naming are consistent across pages and languages.

### Robust

- Semantic HTML first; ARIA only when no native element fits, and used correctly.
- Status messages are announced to assistive technology without moving focus.

## Verification

| Check | When | Evidence |
|-------|------|----------|
| Automated scan | Every change, in the pipeline | {{pending: report location}} |
| Keyboard walkthrough | Every new screen | Notes in the feature spec |
| Screen reader pass | Before release of a feature | Notes per supported language |
| Audit by a qualified person | {{pending: frequency}} | Audit report |

Automated tools catch only part of the issues; manual checks are required.

## Defects

- An accessibility defect that blocks a task is treated with the same severity as a functional defect that blocks a task.
- {{pending: decide where accessibility feedback from users is received and how fast it is answered}}

## Related

- [Design principles](design-principles.md)
- [Content guidelines](content-guidelines.md)
- [Navigation map](navigation-map.md)
- [Acceptance strategy](../11-quality/acceptance-strategy.md)
- [Non-functional requirements](../11-quality/non-functional-requirements.md)
- [Internationalization policy](../00-governance/policies/i18n-policy.md)
