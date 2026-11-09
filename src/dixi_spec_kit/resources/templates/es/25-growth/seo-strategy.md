# Estrategia SEO

## Propósito

Definir cómo las páginas públicas se vuelven encontrables en buscadores en cada idioma soportado. El SEO internacional es parte de la arquitectura: URLs con prefijo de idioma, `hreflang`, URLs canónicas por idioma y contenido renderizado en servidor son requisitos, no mejoras posteriores.

Estado: borrador. {{pending: confirmar los idiomas indexables y los mercados prioritarios}}

## SEO técnico

- Toda página pública vive bajo un prefijo de idioma: `/es/...`, `/en/...`.
- La raíz `/` redirige al idioma del navegador, con uno por defecto; esa redirección no se cachea para todos.
- Cada página declara una URL canónica de su propio idioma, nunca apuntando a otro idioma.
- Cada página lista `<link rel="alternate" hreflang="xx">` para cada versión de idioma y `x-default`; las alternativas son recíprocas.
- El contenido se renderiza en servidor o se pre-renderiza; los crawlers no deben necesitar ejecutar scripts para ver el texto.
- Un sitemap por idioma (o uno con alternativas) lista solo URLs canónicas e indexables.
- Las reglas de robots bloquean áreas privadas, nunca recursos públicos necesarios para renderizar las páginas.
- Las páginas cumplen los presupuestos de rendimiento y son usables en móvil.

## SEO en página

| Elemento | Regla |
|----------|-------|
| Título | Único por página e idioma, describe el contenido |
| Meta descripción | Única, escrita para personas, traducida por idioma |
| Encabezados | Un solo `h1`, jerarquía lógica |
| Slug de URL | Legible, traducido por idioma cuando sea útil |
| Imágenes | Texto alternativo descriptivo por idioma |
| Datos estructurados | {{pending: decidir qué tipos de esquema aplican}} |
| Enlaces internos | Cada página enlaza a páginas relacionadas del mismo idioma |

## SEO de contenido

- La investigación de palabras clave e intención se hace por idioma y mercado, no traduciendo desde otro idioma.
- Cada tema tiene una página principal para evitar que varias páginas compitan entre sí.
- Las páginas desactualizadas se actualizan, se fusionan con redirecciones o se retiran a propósito.

## Métricas

| Métrica | Por idioma | Objetivo |
|---------|------------|----------|
| Páginas indexadas frente a publicadas | Sí | {{pending}} |
| Visitas orgánicas | Sí | {{pending}} |
| Conversiones orgánicas | Sí | {{pending}} |
| Páginas con errores técnicos | Sí | {{pending}} |

## Auditoría periódica

{{pending: definir la frecuencia de auditoría y su responsable}}

Revisa enlaces rotos, `hreflang` faltante o incorrecto, errores de canónicas, títulos duplicados, texto sin traducir y regresiones de rendimiento.

## Relacionados

- [Estrategia de crecimiento](growth-strategy.md)
- [Catálogo de landing pages](landing-pages-catalog.md)
- [Estrategia de contenido](content-strategy.md)
- [Política de i18n](../00-governance/policies/i18n-policy.md)
- [Presupuestos de web vitals](../11-quality/performance-budgets/web-vitals-budgets.md)
- [Arquitectura de información](../17-ux/information-architecture.md)
