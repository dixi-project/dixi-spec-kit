# Design tokens

## Purpose

Name the basic design decisions (colour, typography, spacing, radius, elevation, motion) as tokens, so that design files and code use the same values, themes can change in one place and accessibility rules such as contrast are checked once.

Status: draft. {{pending: decide the source of truth for tokens, for example a JSON file in the repository, and how it is turned into code}}

## Token layers

| Layer | Example name | Refers to | Who uses it |
|-------|--------------|-----------|-------------|
| Base | `color.blue.600` | A raw value | Only other tokens |
| Semantic | `color.text.primary` | A base token | Components |
| Component | `button.primary.background` | A semantic token | One component |

Components never use base tokens or raw values directly.

## Naming

- Format: `category.role.variant.state`, lowercase, dot-separated.
- Names describe purpose, not appearance (`color.feedback.error`, not `color.red`).
- {{pending: confirm the naming format and the output formats needed, for example CSS custom properties}}

## Starting set

### Colour

| Token | Light theme | Dark theme | Contrast checked against |
|-------|-------------|------------|--------------------------|
| `color.text.primary` | {{pending}} | {{pending}} | `color.surface.default` |
| `color.surface.default` | {{pending}} | {{pending}} | — |
| `color.action.primary` | {{pending}} | {{pending}} | `color.surface.default` |
| `color.feedback.error` | {{pending}} | {{pending}} | `color.surface.default` |
| `color.focus.ring` | {{pending}} | {{pending}} | Adjacent colours |

### Typography

| Token | Value | Notes |
|-------|-------|-------|
| `font.family.base` | {{pending}} | Must cover every supported script and accented characters |
| `font.size.body` | {{pending: in rem}} | Relative units so user zoom works |
| `font.line-height.body` | {{pending}} | — |

### Spacing, radius, motion

| Token | Value |
|-------|-------|
| `space.1` … `space.8` | {{pending: scale, for example multiples of 4 px in rem}} |
| `radius.default` | {{pending}} |
| `motion.duration.short` | {{pending}} |

## Rules

- Text and interactive colour pairs meet the contrast required by the accessibility standard in every theme.
- Use logical properties (start/end) so layouts can support right-to-left languages if added later.
- Motion tokens have a reduced-motion alternative.
- Changing a token value is a reviewed change with a visual check of affected components.

## Related

- [UI state catalog](ui-state-catalog.md)
- [Accessibility standard](accessibility-standard.md)
- [Design principles](design-principles.md)
- [Web vitals budgets](../11-quality/performance-budgets/web-vitals-budgets.md)
