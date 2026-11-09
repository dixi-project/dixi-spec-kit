# Catálogo de landing pages

## Propósito

Mantener un único inventario de las landing pages del proyecto: para qué sirve cada una, en qué idiomas existe, qué conversión persigue y quién la mantiene. Una landing page que no está en este catálogo no tiene responsable y no debería publicarse.

Estado: borrador. {{pending: listar las primeras landing pages y sus responsables}}

## Reglas obligatorias

- Toda landing page existe bajo un prefijo de idioma, con la misma estructura en cada idioma.
- Cada versión tiene su propia URL canónica y alternativas `hreflang` recíprocas, incluido `x-default`.
- El contenido se renderiza en servidor o se pre-renderiza y viene de catálogos de traducción.
- Cada página tiene una llamada a la acción principal y un evento de conversión medido.
- Las páginas cumplen el estándar de accesibilidad y los presupuestos de rendimiento.

## Catálogo

| ID | Propósito | Audiencia | Idiomas | Patrón de URL | Evento de conversión | Responsable | Estado |
|----|-----------|-----------|---------|---------------|----------------------|-------------|--------|
| LP-001 | Inicio | Todos los visitantes | ES, EN | `/{lang}/` | {{pending}} | {{pending}} | {{pending}} |
| LP-002 | {{pending: producto o funcionalidad}} | {{pending}} | ES, EN | `/{lang}/{{pending}}` | {{pending}} | {{pending}} | {{pending}} |
| LP-003 | {{pending: campaña}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |

Valores de estado: borrador, publicada, en prueba, retirada. Las páginas retiradas redirigen a la página publicada más cercana del mismo idioma.

## Anatomía recomendada

1. Titular que expresa el resultado para el visitante.
2. Texto de apoyo breve y una llamada a la acción principal.
3. Evidencia: cómo funciona, ejemplos, límites honestos.
4. Respuestas a las objeciones más comunes.
5. Llamada a la acción repetida y enlaces a páginas relacionadas del mismo idioma.

## Medición

- Registra la tasa de conversión por idioma y por canal, no solo la global.
- Los parámetros de campaña se mantienen coherentes entre páginas.

## Mantenimiento

{{pending: definir cada cuánto se revisa el catálogo y quién aprueba páginas nuevas}}

En cada revisión comprueba: enlaces rotos, afirmaciones desactualizadas, texto sin traducir, alternativas faltantes y páginas sin tráfico ni propósito.

## Relacionados

- [Estrategia SEO](seo-strategy.md)
- [Embudo de conversión](conversion-funnel.md)
- [Estrategia de contenido](content-strategy.md)
- [Plantilla de página](../10-engineering/templates/page-template.md)
- [Estándar de accesibilidad](../17-ux/accessibility-standard.md)
- [Política de i18n](../00-governance/policies/i18n-policy.md)
