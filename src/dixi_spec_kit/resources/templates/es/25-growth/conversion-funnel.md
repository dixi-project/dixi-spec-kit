# Embudo de conversión

## Propósito

Definir los pasos que recorre un visitante hasta convertirse en usuario activo o cliente, cómo se mide cada paso y cómo se investigan los abandonos. Las definiciones deben ser lo bastante precisas para que dos personas que calculen la misma métrica obtengan el mismo número.

Estado: borrador. {{pending: definir los pasos del embudo y el evento clave de conversión}}

## Pasos del embudo

| Paso | Definición (evento) | Conversión desde el paso anterior | Línea base | Objetivo |
|------|---------------------|-----------------------------------|------------|----------|
| Visita | {{pending: vista de una página pública}} | n/a | {{pending}} | {{pending}} |
| Interés | {{pending: por ejemplo ve una página de precios o de funcionalidad}} | {{pending}} | {{pending}} | {{pending}} |
| Registro | {{pending: cuenta creada}} | {{pending}} | {{pending}} | {{pending}} |
| Activación | {{pending: primera acción clave completada}} | {{pending}} | {{pending}} | {{pending}} |
| Conversión | {{pending: acción de pago o compromiso, si aplica}} | {{pending}} | {{pending}} | {{pending}} |

Las líneas base se llenan solo con datos reales medidos; déjalas pendientes hasta entonces.

## Segmentos

Mira siempre el embudo desglosado por:

- Idioma y mercado.
- Canal de adquisición.
- Tipo de dispositivo.
- Visitantes nuevos frente a recurrentes.

## Instrumentación

- Cada paso corresponde a un evento con nombre y esquema documentado.
- Cada evento incluye idioma, canal (cuando se conoce) y marca de tiempo; excluye datos personales innecesarios.
- Los nombres y propiedades de eventos se versionan; un cambio se revisa como un cambio de contrato.
- La medición respeta el consentimiento: nada de medición opcional antes de que la persona acepte.

{{pending: decidir el enfoque de analítica y dónde vive el esquema de eventos}}

## Análisis de abandono

1. Encuentra el paso con mayor pérdida relativa en un segmento.
2. Reúne evidencia: observación de sesiones, preguntas de soporte, hallazgos de investigación.
3. Escribe una hipótesis y el cambio esperado en la conversión del paso.
4. Corrige directamente los defectos evidentes; prueba los cambios inciertos cuando el tráfico lo permita.
5. Registra el resultado, incluidos los cambios que no ayudaron.

## Cadencia de revisión

| Revisión | Frecuencia | Participantes |
|----------|------------|---------------|
| Métricas del embudo | {{pending}} | {{pending}} |
| Análisis profundo por segmento | {{pending}} | {{pending}} |

## Relacionados

- [Estrategia de crecimiento](growth-strategy.md)
- [Catálogo de landing pages](landing-pages-catalog.md)
- [Clasificación de PII](../08-data/pii-classification.md)
- [Estrategia de descubrimiento](../24-research/discovery-strategy.md)
- [Estrategia de aceptación](../11-quality/acceptance-strategy.md)
