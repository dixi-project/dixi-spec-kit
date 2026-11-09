# Estrategia de aceptación

## Propósito

Definir cómo se redactan, prueban y aceptan los criterios de aceptación, para que «terminado» signifique el comportamiento observable que pidió el negocio, confirmado por una persona.

Estado: borrador. {{pending: decidir quién acepta las funcionalidades y cómo se registra la aceptación}}

## Redactar criterios

Cada especificación de funcionalidad lista criterios que son:

- **Observables:** describen lo que ve un usuario o sistema, no cómo se construye.
- **Comprobables:** una prueba puede pasar o fallar contra ellos.
- **Independientes:** un comportamiento por criterio.
- **Identificados:** cada criterio tiene un ID estable al que se refieren las pruebas.

Una forma habitual es *Dado* un contexto, *Cuando* ocurre una acción, *Entonces* se observa un resultado. Las frases simples sirven si siguen siendo observables.

## De criterios a pruebas

| Paso | Resultado | Responsable |
|------|-----------|-------------|
| Redactar criterios | Criterios en la [especificación de funcionalidad](../05-features/example/feature-spec.md) | {{pending: responsable}} |
| Revisar criterios | Ambigüedades resueltas, IDs asignados | {{pending: responsable}} |
| Escribir pruebas que fallan | Pruebas enlazadas desde el [plan de pruebas](test-plan.md) | Desarrollador o agente |
| Hacerlas pasar | Código, con `make verify` en verde | Desarrollador o agente |
| Aceptar | Decisión humana registrada | {{pending: responsable}} |

## Evidencia de aceptación

Registra para cada funcionalidad:

- IDs de los criterios y las pruebas que los cubren.
- Resultado real de `make verify` y de cualquier verificación manual.
- Quién aceptó, cuándo y los pendientes abiertos.

{{pending: dónde vive la evidencia de aceptación, por ejemplo la descripción del pull request}}

## Verificaciones manuales

Algunos criterios no se automatizan a bajo costo (diseño visual, tono del texto). Márcalos como manuales, describe los pasos y registra quién los ejecutó. Una verificación manual no se informa como automática.

## Rechazo

Si un criterio no se cumple, la funcionalidad vuelve a desarrollo. Los criterios no se reescriben a posteriori para ajustarse a lo entregado sin una decisión registrada.

## Relacionados

- [Estrategia de calidad](quality-strategy.md)
- [Guía de TDD](tdd-guide.md)
- [Pirámide de pruebas](test-pyramid.md)
- [Plan de pruebas](test-plan.md)
- [Objetivo](../01-business/vision.md)
