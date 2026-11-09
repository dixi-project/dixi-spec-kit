# Guía de TDD

## Propósito

Explicar cómo este proyecto escribe las pruebas antes que el código (rojo → verde → refactorizar) y mantiene congeladas las pruebas commiteadas, para que expresen la especificación y no lo que el código haga por casualidad.

Estado: borrador. {{pending: confirmar el flujo de TDD con el equipo}}

## Ciclo

1. **Leer la especificación.** Parte de la especificación de la funcionalidad y sus criterios de aceptación.
2. **Rojo.** Escribe la prueba más pequeña que exprese un criterio. Ejecútala y confirma que falla por el motivo esperado.
3. **Commitear la prueba en rojo.** El commit contiene solo la prueba, por ejemplo `[11-quality] test: <comportamiento> (red)`.
4. **Verde.** Escribe el código mínimo que la haga pasar. No toques la prueba.
5. **Refactorizar.** Mejora el código con todas las pruebas en verde.
6. **Verificar.** Ejecuta `make verify` y registra el resultado real.

## Pruebas congeladas

- Una prueba commiteada es un contrato con la especificación. No se edita para que el código pase.
- Si una prueba parece incorrecta, detente. Explica por qué, señala la especificación y pide a la persona responsable que decida.
- Cambiar una prueba congelada exige primero un cambio de especificación y una aprobación humana. {{pending: quién aprueba cambios a pruebas congeladas}}
- Los agentes siguen la misma regla que las personas; ver [instrucciones del proyecto](../AGENTS.md).

## Escribir buenas primeras pruebas

- Nombra la prueba por el comportamiento, no por la implementación.
- Un comportamiento observable por prueba.
- Cubre los límites: vacío, cero, uno, máximo, entrada inválida.
- Prefiere valores reales a mocks; simula solo las fronteras externas reales.
- Una prueba que no puede fallar no es una prueba. Confirma el estado rojo antes de escribir código.

## Trazabilidad

Enlaza cada prueba a su criterio en el [plan de pruebas](test-plan.md) y mantén los IDs en `.dixi/traceability.json` para que `dixi check` siga la cadena desde el objetivo hasta la prueba.

## Excepciones

{{pending: listar los casos en que las pruebas pueden ir después del código, por ejemplo prototipos desechables, y cómo se eliminan o cubren antes de integrar}}

## Relacionados

- [Estrategia de calidad](quality-strategy.md)
- [Pirámide de pruebas](test-pyramid.md)
- [Estrategia de aceptación](acceptance-strategy.md)
- [Escalera de verificación](verification-ladder.md)
- [Plan de pruebas](test-plan.md)
