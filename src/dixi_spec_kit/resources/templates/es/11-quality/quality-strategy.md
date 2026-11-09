# Estrategia de calidad

## Propósito

Describir cómo decide este proyecto que un cambio es suficientemente bueno para integrarse. La estrategia une especificaciones, pruebas escritas primero, verificaciones automáticas y revisión humana en un único camino que sigue todo cambio.

Estado: borrador. {{pending: confirmar la estrategia con la persona responsable de calidad}}

## Principios

- **Especificación antes que código.** Todo cambio de comportamiento parte de una especificación de funcionalidad con criterios de aceptación observables.
- **Pruebas primero (rojo → verde).** Se commitea una prueba que falla antes del código que la hace pasar.
- **Pruebas congeladas.** Una prueba commiteada no se edita para que el código pase. Si parece incorrecta, se detiene el trabajo, se explica y se pide una decisión humana.
- **Las máquinas verifican lo que pueden.** Formato, tipos, pruebas unitarias y de integración corren solas; las personas revisan intención, riesgo y encaje con el negocio.
- **Evidencia, no afirmaciones.** «Verificado» significa que una comprobación se ejecutó y se registró su salida real.

## Alcance

| Área | Incluido | Responsable |
|------|----------|-------------|
| Comportamiento funcional | {{pending: listar las funcionalidades cubiertas}} | {{pending: responsable}} |
| Requisitos no funcionales | Ver [requisitos no funcionales](non-functional-requirements.md) | {{pending: responsable}} |
| Rendimiento | Ver [presupuestos de web vitals](performance-budgets/web-vitals-budgets.md) | {{pending: responsable}} |
| Fuera de alcance | {{pending: qué no cubre esta estrategia y por qué}} | — |

## Puertas de calidad

1. Existen especificación y criterios de aceptación trazables (`dixi check`).
2. Las pruebas se escribieron primero y están enlazadas desde el [plan de pruebas](test-plan.md).
3. `make verify` pasa en local, siguiendo la [escalera de verificación](verification-ladder.md).
4. La profundidad de revisión corresponde al riesgo, según la [revisión basada en riesgo](risk-based-review.md).
5. Una persona aprueba e integra. Los agentes nunca aprueban ni integran.

{{pending: decidir qué puertas bloquean la integración y cuáles solo avisan}}

## Cuando una puerta falla

Se corrige el código o la especificación, nunca el umbral. Bajar un objetivo de cobertura, un presupuesto o un nivel de rigor para que un cambio pase exige una decisión explícita y registrada de la persona responsable, y nunca la toma un agente.

## Frecuencia de revisión

{{pending: cada cuánto se revisa esta estrategia y quién la aprueba}}

## Relacionados

- [Escalera de verificación](verification-ladder.md)
- [Pirámide de pruebas](test-pyramid.md)
- [Guía de TDD](tdd-guide.md)
- [Estrategia de aceptación](acceptance-strategy.md)
- [Plan de pruebas](test-plan.md)
- [Proyecto](../00-master-spec.md)
