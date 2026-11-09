# Biblioteca de prompts

## Propósito

Mantener los prompts del proyecto (en los procedimientos de desarrollo y en las features del producto) versionados, revisados y comprobables, para que una respuesta pueda rastrearse hasta la plantilla exacta que la produjo.

## Dónde viven los prompts

- Procedimientos de desarrollo: se comparten mediante `dixi workflow` y los comandos de agente (`/dixi.*` o `$dixi-*`); no los bifurques en silencio.
- Prompts del producto: {{pending: directorio de las plantillas de prompt del producto}}

## Formato de plantilla

Cada plantilla del producto es un archivo con una cabecera y un cuerpo:

```text
id: resumir-ticket
version: 1
purpose: Resumir un ticket de soporte para un agente.
inputs: ticket_text (no confiable), language
output: JSON conforme al contrato CONTRACT-xxx
owner: rol responsable
```

Reglas:

- Una plantilla por propósito, con un ID estable.
- Marca qué entradas no son confiables y delimítalas con claridad.
- Pide salida estructurada y valídala contra el contrato.
- Nunca incrustes secretos ni datos personales en las plantillas.

## Versionado

- Cualquier cambio de redacción, ejemplos o parámetros incrementa la versión.
- La versión se registra con cada llamada (ver el rastro de auditoría de IA).
- Una versión nueva vuelve a ejecutar el conjunto de evaluación antes de publicarse.

## Catálogo

| ID | Versión | Propósito | Contrato | Conjunto de evaluación | Responsable |
| --- | --- | --- | --- | --- | --- |
| {{pending: ID de plantilla}} | 1 | {{pending: definir}} | {{pending: definir}} | {{pending: definir}} | {{pending: definir}} |

## Lista de revisión

- [ ] El propósito y el formato de salida son explícitos.
- [ ] Las entradas no confiables están delimitadas y no se tratan como instrucciones.
- [ ] Está definido el comportamiento ante rechazos y errores.
- [ ] El idioma y el tono coinciden con los locales del producto.

## Relacionados

- [Estrategia de contexto](context-strategy.md)
- [Estrategia de modelos](model-strategy.md)
- [Rastro de auditoría de IA](../governance/ai-audit-trail.md)
- [Puertas de calidad](../governance/quality-gates.md)
