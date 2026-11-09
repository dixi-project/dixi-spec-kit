# Tokens de diseño

## Propósito

Nombrar como tokens las decisiones básicas de diseño (color, tipografía, espaciado, radios, elevación, movimiento), para que los archivos de diseño y el código usen los mismos valores, los temas cambien en un solo lugar y reglas de accesibilidad como el contraste se revisen una sola vez.

Estado: borrador. {{pending: decidir la fuente de verdad de los tokens, por ejemplo un archivo JSON en el repositorio, y cómo se convierte en código}}

## Capas de tokens

| Capa | Nombre de ejemplo | Apunta a | Quién la usa |
|------|-------------------|----------|--------------|
| Base | `color.blue.600` | Un valor directo | Solo otros tokens |
| Semántica | `color.text.primary` | Un token base | Componentes |
| Componente | `button.primary.background` | Un token semántico | Un componente |

Los componentes nunca usan tokens base ni valores directos.

## Nombres

- Formato: `categoria.rol.variante.estado`, en minúsculas, separado por puntos; los nombres se escriben en inglés para que sean iguales en todo el código.
- Los nombres describen el propósito, no la apariencia (`color.feedback.error`, no `color.red`).
- {{pending: confirmar el formato de nombres y los formatos de salida necesarios, por ejemplo propiedades personalizadas de CSS}}

## Conjunto inicial

### Color

| Token | Tema claro | Tema oscuro | Contraste revisado contra |
|-------|------------|-------------|---------------------------|
| `color.text.primary` | {{pending}} | {{pending}} | `color.surface.default` |
| `color.surface.default` | {{pending}} | {{pending}} | — |
| `color.action.primary` | {{pending}} | {{pending}} | `color.surface.default` |
| `color.feedback.error` | {{pending}} | {{pending}} | `color.surface.default` |
| `color.focus.ring` | {{pending}} | {{pending}} | Colores adyacentes |

### Tipografía

| Token | Valor | Notas |
|-------|-------|-------|
| `font.family.base` | {{pending}} | Debe cubrir todos los sistemas de escritura soportados y caracteres acentuados |
| `font.size.body` | {{pending: en rem}} | Unidades relativas para que funcione el zoom del usuario |
| `font.line-height.body` | {{pending}} | — |

### Espaciado, radios, movimiento

| Token | Valor |
|-------|-------|
| `space.1` … `space.8` | {{pending: escala, por ejemplo múltiplos de 4 px en rem}} |
| `radius.default` | {{pending}} |
| `motion.duration.short` | {{pending}} |

## Reglas

- Los pares de color de texto e interacción cumplen el contraste exigido por el estándar de accesibilidad en cada tema.
- Usa propiedades lógicas (inicio/fin) para que los diseños puedan soportar idiomas de derecha a izquierda si se agregan después.
- Los tokens de movimiento tienen una alternativa de movimiento reducido.
- Cambiar el valor de un token es un cambio revisado, con una comprobación visual de los componentes afectados.

## Relacionados

- [Catálogo de estados de interfaz](ui-state-catalog.md)
- [Estándar de accesibilidad](accessibility-standard.md)
- [Principios de diseño](design-principles.md)
- [Presupuestos de Web Vitals](../11-quality/performance-budgets/web-vitals-budgets.md)
