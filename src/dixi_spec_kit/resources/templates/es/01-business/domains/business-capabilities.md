# Capacidades de negocio

## Propósito

Describir lo que el negocio debe ser capaz de hacer, con independencia de cómo se implemente hoy.
Las capacidades son estables en el tiempo (los procesos y sistemas cambian, la necesidad permanece),
por lo que son una buena base para trazar fronteras de dominios y módulos y para priorizar la
inversión.

## Cómo identificar capacidades

1. Parte de los objetivos estratégicos y la propuesta de valor: ¿qué debe hacer la organización para cumplir?
2. Nombra cada capacidad con un sintagma nominal («Alta de clientes», «Gestión de facturas»).
3. Agrúpalas en niveles: el nivel 1 es amplio y el nivel 2 lo desglosa en habilidades concretas.
4. No nombres equipos, herramientas ni pantallas; son implementaciones.
5. Indica cómo diferencia cada capacidad al producto: núcleo, soporte o genérica.

## Mapa de capacidades

| ID | Nivel 1 | Nivel 2 | Tipo | Objetivo al que sirve | Dominio |
|---|---|---|---|---|---|
| CAP-001 | {{pending: capacidad}} | {{pending: subcapacidad}} | {{pending: núcleo, soporte o genérica}} | {{pending: ID de GOAL}} | {{pending: dominio}} |
| CAP-002 | {{pending: capacidad}} | {{pending: subcapacidad}} | {{pending: tipo}} | {{pending: ID de GOAL}} | {{pending: dominio}} |

Las capacidades núcleo merecen diseño propio y las pruebas más sólidas. Las genéricas son candidatas
a reutilización o a un servicio externo (esa elección se registra en un ADR).

## Madurez y brechas

| Capacidad | Estado actual | Estado objetivo | Brecha |
|---|---|---|---|
| {{pending: ID de CAP}} | {{pending: manual, parcial o automatizada}} | {{pending: objetivo}} | {{pending: qué falta}} |

## Priorización

- Capacidades dentro del alcance del periodo actual: {{pending: IDs de CAP}}
- Capacidades aplazadas y motivo: {{pending: IDs de CAP y motivo}}

## Relacionados

- [Objetivos estratégicos](../strategic-goals.md)
- [Mapa de dominios](domain-map.md)
- [Lenguaje ubicuo](ubiquitous-language.md)
- [Objetivo de negocio](../vision.md)
