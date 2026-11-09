# Estructura del centro de ayuda

## Propósito

Definir cómo se organiza el centro de ayuda, cómo se escriben y localizan los artículos y cómo se mantiene exacto. Un buen centro de ayuda permite que las personas resuelvan problemas por su cuenta, en su idioma, y es encontrable desde buscadores y desde dentro del producto.

Estado: borrador. {{pending: decidir si el centro de ayuda forma parte del sitio principal o es independiente, y quién es responsable}}

## Estructura de URLs

- Los artículos viven bajo un prefijo de idioma: `/es/help/...`, `/en/help/...`.
- Cada artículo tiene una URL canónica de su idioma y alternativas `hreflang` recíprocas, incluido `x-default`.
- Los artículos se renderizan en servidor o se pre-renderizan para que los buscadores indexen el texto traducido.
- Los slugs son legibles y estables; un artículo renombrado redirige a la nueva URL del mismo idioma.

## Taxonomía

| Nivel | Ejemplo |
|-------|---------|
| Categoría | Primeros pasos, Cuenta, Facturación, Funcionalidades, Solución de problemas |
| Sección | {{pending: grupo dentro de una categoría}} |
| Artículo | Una tarea o una pregunta |

{{pending: definir las primeras categorías a partir de las preguntas más comunes}}

## Estructura de un artículo

1. Título que coincide con cómo la gente formula la pregunta.
2. Resumen de una frase de lo que resuelve el artículo.
3. Requisitos previos, si los hay.
4. Pasos numerados, una acción por paso.
5. Solución de problemas para los fallos comunes.
6. Artículos relacionados del mismo idioma.
7. Cómo contactar con soporte si el problema persiste.

## Reglas de redacción

- Lenguaje claro, frases cortas, términos coherentes con el glosario.
- Capturas y medios tienen texto alternativo y se actualizan cuando cambia la interfaz.
- Sin datos personales, secretos ni detalles reales de clientes en los ejemplos.

## Localización

- Cada artículo existe en todos los idiomas soportados, o se marca claramente como no disponible en ese idioma.
- Las traducciones las revisa una persona con dominio del idioma; los términos siguen el glosario por idioma.
- Cuando cambia el artículo de origen, sus traducciones se marcan como desactualizadas hasta revisarlas.

## Enlaces desde el producto

- Las pantallas enlazan al artículo que las explica, en el idioma del usuario.
- Los mensajes de error pueden enlazar a un artículo de solución de problemas.

## Mantenimiento

| Tarea | Frecuencia | Responsable |
|-------|------------|-------------|
| Revisar la exactitud de los artículos más vistos | {{pending}} | {{pending}} |
| Revisar búsquedas sin resultados | {{pending}} | {{pending}} |
| Actualizar tras cada versión | En cada versión | {{pending}} |

## Relacionados

- [Niveles de soporte](support-tiers.md)
- [Estrategia de éxito del cliente](success-strategy.md)
- [Guías de contenido](../17-ux/content-guidelines.md)
- [Glosario](../18-knowledge-base/glossary.md)
- [Preguntas frecuentes](../18-knowledge-base/faq.md)
- [Política de i18n](../00-governance/policies/i18n-policy.md)
