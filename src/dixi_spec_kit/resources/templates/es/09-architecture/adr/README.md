# Registros de decisiones de arquitectura

## Propósito

Índice de los registros de decisiones de arquitectura (ADR) de este proyecto. Un ADR recoge una decisión estructural, el contexto que la motivó, las opciones consideradas y las consecuencias aceptadas. Los ADR explican *por qué* la arquitectura es como es, para que futuras personas y agentes no reabran temas cerrados ni los rompan sin darse cuenta.

## Cuándo escribir un ADR

Escribe uno cuando una decisión sea difícil de revertir o afecte a más de un módulo, por ejemplo:

- Elegir un modelo de persistencia, un estilo de mensajería o una topología de despliegue.
- Definir una frontera de confianza, un esquema de autenticación o un modelo de tenencia.
- Adoptar o abandonar un framework, protocolo o integración externa.
- Aceptar a propósito una limitación conocida o una deuda técnica.

Las decisiones pequeñas y locales van en la especificación del módulo o de la funcionalidad.

## Cómo escribir uno

1. Copia la [plantilla de ADR](../../10-engineering/templates/adr-template.md) a `ADR-NNN-titulo-corto.md` en esta carpeta, con el siguiente número libre.
2. Describe el contexto y las fuerzas en juego, no solo la opción elegida.
3. Enumera al menos dos opciones con sus ventajas y desventajas.
4. Expón la decisión y sus consecuencias, incluido lo que se vuelve más difícil.
5. Enlaza las especificaciones, contratos y pruebas que la decisión afecta.
6. Añade una fila al índice de abajo.

## Ciclo de estados

| Estado | Significado |
|---|---|
| Proposed | Redactado, en discusión. Aún no es vinculante. |
| Accepted | Validado por una persona responsable. Vinculante para todas las personas y agentes. |
| Superseded | Reemplazado por un ADR más reciente. Conserva el archivo y enlaza el sustituto. |

Una decisión estructural permanece en **Proposed** hasta que una persona la valida. Los agentes pueden redactar ADR y proponer cambios, pero no deben marcar un ADR como Accepted por su cuenta. Nunca borres ni reescribas un ADR aceptado: reemplázalo con uno nuevo.

## Índice

| ID | Título | Estado | Fecha |
|---|---|---|---|
| {{pending: ADR-001}} | {{pending: primera decisión estructural del proyecto}} | Proposed | {{pending: fecha}} |

## Responsables

- Quién valida los ADR: {{pending: nombre o rol de la persona responsable de arquitectura}}
- Cadencia de revisión: {{pending: cuándo se revisan los ADR en Proposed}}

## Relacionados

- [Especificación maestra](../../00-master-spec.md)
- [Instrucciones para agentes](../../AGENTS.md)
- [Plantilla de ADR](../../10-engineering/templates/adr-template.md)
- [Contexto del sistema](../system-context.md)
- [Guía](../../docs/guide.md)
