# Registro de decisiones

## Propósito

Registrar las decisiones del proyecto que no justifican un ADR pero no deben perderse (recortes de alcance, convenciones, riesgos aceptados, excepciones) e indicar dónde vive cada tipo de decisión.

Estado: borrador. {{pending: nombrar a quién mantiene este registro al día}}

## Dónde vive cada decisión

| Tipo de decisión | Dónde se registra |
|------------------|-------------------|
| Arquitectura, difícil de revertir | ADR en [09-architecture/adr](../09-architecture/adr/README.md) |
| Alcance y prioridades | [Proyecto](../00-master-spec.md) |
| Comportamiento de una funcionalidad | La spec de la funcionalidad |
| Interfaz | El contrato |
| Pequeña, reversible, transversal | Este registro |
| Excepciones a una política | Este registro, con fecha de caducidad |

## Reglas

- Una fila por decisión; nunca reescribas una fila pasada. Sustitúyela con una nueva.
- Cada decisión tiene fecha, responsable y alternativas consideradas.
- Los agentes pueden proponer entradas; una persona las confirma.
- Si una decisión resulta difícil de revertir, conviértela en un ADR.

## Registro

| ID | Fecha | Decisión | Alternativas | Responsable | Estado | Sustituye a |
|----|-------|----------|--------------|-------------|--------|-------------|
| DEC-001 | {{pending: fecha}} | {{pending: decisión}} | {{pending: alternativas}} | {{pending: responsable}} | propuesta | — |

Valores de estado: `propuesta`, `aceptada`, `sustituida`, `caducada`.

## Revisión

{{pending: cada cuánto se revisa el registro y quién comprueba las excepciones caducadas}}

## Relacionados

- [Plantilla de ADR](../10-engineering/templates/adr-template.md)
- [Preguntas frecuentes](faq.md)
- [Principios](../00-governance/principles.md)
