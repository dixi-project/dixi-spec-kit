# Lenguaje ubicuo

## Propósito

Mantener un único vocabulario compartido entre negocio, especificaciones, código y pruebas. Cuando
un término significa lo mismo en todas partes, las especificaciones se revisan mejor y los agentes
hacen menos suposiciones erróneas. Si dos dominios usan la misma palabra con significados distintos,
registra ambos y nombra el dominio propietario de cada uno.

## Reglas

- Un término, un significado por dominio. Los sinónimos se listan, no se usan indistintamente.
- Identificadores de código, campos de API y nombres de eventos reutilizan estos términos (solo se
  traducen en la interfaz).
- Los términos nuevos entran en esta página antes de aparecer en un contrato.
- Las palabras ambiguas («usuario», «cuenta», «pedido») siempre llevan un calificativo o dominio.
- Mantén el término canónico en inglés si el código está en inglés, y añade la traducción.

## Glosario

| Término | Definición | Dominio propietario | Sinónimos a evitar | Traducción (en) | Ejemplo |
|---|---|---|---|---|---|
| {{pending: término}} | {{pending: definición en una frase}} | {{pending: dominio}} | {{pending: sinónimos}} | {{pending: traducción}} | {{pending: ejemplo de uso}} |
| {{pending: término}} | {{pending: definición}} | {{pending: dominio}} | {{pending: sinónimos}} | {{pending: traducción}} | {{pending: ejemplo de uso}} |

## Términos con distinto significado según el dominio

| Término | Significado en el dominio A | Significado en el dominio B | Cómo desambiguar |
|---|---|---|---|
| {{pending: término}} | {{pending: significado}} | {{pending: significado}} | {{pending: calificativo o renombrado}} |

## Estados y ciclos de vida

Las entidades con estados deben listarlos aquí con los mismos nombres que en el código:

| Entidad | Estados | Transiciones permitidas |
|---|---|---|
| {{pending: entidad}} | {{pending: p. ej. borrador, activo, cerrado}} | {{pending: p. ej. de borrador a activo}} |

## Mantenimiento

- Responsable del glosario: {{pending: rol}}
- `/dixi.domain` puede proponer términos al redactar un dominio; una persona los confirma aquí.

## Relacionados

- [Mapa de dominios](domain-map.md)
- [Capacidades de negocio](business-capabilities.md)
- [Ejemplo de dominio](../../03-domains/example/domain-spec.md)
- [Plantilla de dominio](../../10-engineering/templates/domain-template.md)
