# Objetivos estratégicos

## Propósito

Convertir el objetivo de negocio en un conjunto pequeño de objetivos medibles para un periodo
definido. Los objetivos estratégicos son la cima de la cadena de trazabilidad: cada uno debería
tener un ID que dominios y funcionalidades citen como padre en `.dixi/traceability.json`, para que
todo trabajo pueda responder «¿a qué objetivo sirve esto?».

## Cómo definir objetivos

- Escribe resultados, no entregables: «reducir el tiempo de alta» en vez de «crear un asistente de alta».
- Da a cada objetivo una línea base, una meta y una fecha. Sin línea base la meta es una suposición.
- Limita el conjunto a entre tres y cinco objetivos por periodo.
- Asigna una persona responsable que pueda decidir compromisos sobre el objetivo.
- Revisa los objetivos al final de cada periodo y registra lo aprendido.

## Periodo

- Horizonte: {{pending: trimestre, semestre o año}}
- Aprobado por: {{pending: persona o rol que valida los objetivos}}

## Objetivos

| ID | Objetivo (resultado) | Métrica | Línea base | Meta | Fecha | Responsable |
|---|---|---|---|---|---|---|
| GOAL-001 | {{pending: resultado}} | {{pending: métrica}} | {{pending: valor actual}} | {{pending: meta}} | {{pending: fecha}} | {{pending: responsable}} |
| GOAL-002 | {{pending: resultado}} | {{pending: métrica}} | {{pending: valor actual}} | {{pending: meta}} | {{pending: fecha}} | {{pending: responsable}} |

`GOAL-001` corresponde al objetivo base de `vision.md`. Añade los nuevos IDs a
`.dixi/traceability.json` con `kind: goal` y sin padres, y ejecuta `dixi check`.

## Métricas de salvaguarda

Métricas que no deben empeorar mientras se persiguen los objetivos (por ejemplo, tasa de errores,
accesibilidad o carga de soporte):

| Métrica | Límite aceptable | Por qué importa |
|---|---|---|
| {{pending: salvaguarda}} | {{pending: límite}} | {{pending: motivo}} |

## Lo que no se persigue en este periodo

- {{pending: lo que el equipo explícitamente no abordará ahora}}

## Registro de revisiones

| Fecha | Objetivo | Resultado | Decisión |
|---|---|---|---|
| {{pending: fecha}} | {{pending: ID del objetivo}} | {{pending: resultado medido}} | {{pending: mantener, ajustar o descartar}} |

## Relacionados

- [Objetivo de negocio](vision.md)
- [Propuesta de valor](value-proposition.md)
- [Capacidades de negocio](domains/business-capabilities.md)
- [Proyecto](../00-master-spec.md)
