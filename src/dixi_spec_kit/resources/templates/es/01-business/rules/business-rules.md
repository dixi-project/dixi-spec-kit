# Reglas de negocio

## Propósito

Reunir las reglas que gobiernan cómo opera el negocio, escritas para que una persona pueda
validarlas y una prueba pueda comprobarlas. Una regla de negocio es una restricción, un cálculo o
una decisión que se cumple sin importar la pantalla o el sistema que la aplique. Mantenerlas aquí,
con IDs, evita enterrarlas en el código donde nadie puede revisarlas.

## Cómo escribir una regla

- Una regla por fila, con un ID estable (`BR-NNN`).
- Usa el lenguaje ubicuo y una forma inequívoca: «Cuando X, entonces Y», «X nunca debe Y».
- Indica la fuente (política, contrato, normativa, decisión) y la persona responsable que puede cambiarla.
- Vincula cada regla con las funcionalidades y pruebas que la hacen cumplir.
- Prefiere valores concretos («en 30 días») a vagos («pronto»).

## Tipos de regla

| Tipo | Forma de ejemplo |
|---|---|
| Restricción | Un pedido no puede confirmarse sin al menos un artículo. |
| Derivación | El total es la suma de los artículos menos los descuentos. |
| Decisión | Si el importe supera un umbral, se requiere una segunda aprobación. |
| Temporal | Una reserva caduca tras un periodo definido sin pago. |

## Catálogo de reglas

| ID | Regla | Tipo | Dominio | Fuente | Responsable | Aplicada por |
|---|---|---|---|---|---|---|
| BR-001 | {{pending: enunciado de la regla}} | {{pending: tipo}} | {{pending: dominio}} | {{pending: fuente}} | {{pending: rol}} | {{pending: ID de FEATURE o de prueba}} |
| BR-002 | {{pending: enunciado de la regla}} | {{pending: tipo}} | {{pending: dominio}} | {{pending: fuente}} | {{pending: rol}} | {{pending: ID de FEATURE o de prueba}} |

## Ejemplos por regla

Escribe al menos un ejemplo positivo y uno negativo por regla; se convierten en pruebas de aceptación.

| Regla | Dado | Cuando | Entonces |
|---|---|---|---|
| {{pending: ID de BR}} | {{pending: contexto}} | {{pending: acción}} | {{pending: resultado esperado}} |

## Control de cambios

- Quién aprueba cambios de reglas: {{pending: rol}}
- Cómo se comunican los cambios a los equipos afectados: {{pending: canal}}

## Relacionados

- [Restricciones operativas](operational-constraints.md)
- [Reglas de precios](pricing-rules.md)
- [Lenguaje ubicuo](../domains/ubiquitous-language.md)
- [Ejemplo de funcionalidad](../../05-features/example/feature-spec.md)
