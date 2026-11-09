# Socios externos

## Propósito

Identificar las organizaciones y sistemas ajenos al equipo de los que depende el producto o a los
que sirve: proveedores, integradores, distribuidores, reguladores o fuentes de datos. Para cada uno,
registra qué se intercambia, quién gestiona la relación y qué ocurre si deja de estar disponible.
Usa etiquetas genéricas hasta que un socio esté confirmado contractualmente.

## Catálogo de socios

| ID | Tipo de socio | Qué aporta o recibe | Criticidad | Responsable de la relación |
|---|---|---|---|---|
| EXT-001 | {{pending: p. ej. procesador de pagos}} | {{pending: intercambio}} | {{pending: alta, media o baja}} | {{pending: rol}} |
| EXT-002 | {{pending: p. ej. proveedor de mensajería}} | {{pending: intercambio}} | {{pending: alta, media o baja}} | {{pending: rol}} |

Elegir un proveedor concreto es una decisión del proyecto: regístrala en un ADR, no aquí.

## Puntos de integración

| Socio | Dirección | Canal | Contrato |
|---|---|---|---|
| {{pending: ID del socio}} | {{pending: entrante, saliente o ambas}} | {{pending: API, archivo, webhook, manual}} | {{pending: enlace al contrato en 07-contracts/external}} |

## Riesgos de dependencia

Para cada socio crítico, responde:

- ¿Qué falla para los usuarios si el socio cae? {{pending: impacto}}
- ¿Hay alternativa o modo degradado? {{pending: alternativa}}
- ¿Qué datos compartimos y bajo qué acuerdo? {{pending: datos y acuerdo}}
- ¿Cómo dejaríamos al socio si fuera necesario? {{pending: plan de salida}}

## Obligaciones

- Niveles de servicio de los que dependemos: {{pending: disponibilidad, tiempo de respuesta, horario de soporte}}
- Niveles de servicio que ofrecemos a los socios: {{pending: compromisos, si los hay}}

## Relacionados

- [Roles internos](internal-roles.md)
- [Plantilla de integración externa](../../10-engineering/templates/external-integration-template.md)
- [Contratos externos](../../07-contracts/external/README.md)
- [Arquitectura de integración](../../09-architecture/integration-architecture.md)
