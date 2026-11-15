# 4. Planificarla

## Propósito

Decidir cómo se construirá la feature antes de escribir código: el contrato, el plan de pruebas y las decisiones estructurales que una persona debe validar.

## Qué haces

Ejecuta [`/dixi.plan`](../commands/plan.es.md) con el ID de tu feature:

```text
/dixi.plan FEATURE-002
```

Con Codex, `$dixi-plan FEATURE-002`; con un agente de Agent Skills, `@dixi-plan FEATURE-002`. Usa el ID que informó el paso anterior si no es `FEATURE-002`.

Si el proyecto aún no registra un stack tecnológico, el agente te pide que elijas uno en lugar de suponerlo. Para este ejemplo basta un paquete pequeño de Python con la biblioteca estándar.

## Qué deberías ver

- Un contrato en `07-contracts/` y un plan de pruebas en `11-quality/`, ambos registrados en `.dixi/traceability.json` bajo tu feature.
- Un ADR en `09-architecture/adr/` por cada decisión estructural, por ejemplo dónde se guardan las notas, con estado «Proposed».

Un ADR propuesto bloquea el trabajo hasta que lo validas: léelo y cambia su estado a «Accepted» si estás de acuerdo, o pide al agente que cambie el enfoque. Es el momento más barato para cambiar de idea.

## Siguiente

[5. Dividirla en tareas](05-tasks.es.md).

## Relacionado

- [Tutorial](index.es.md)
- [Referencia de comandos](../commands/index.es.md)
