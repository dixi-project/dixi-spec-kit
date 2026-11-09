# Política de pruebas

## Propósito

Fijar las reglas de pruebas no negociables del proyecto. Cómo aplicarlas en el día a día se explica en la guía de TDD; esta política dice qué debe cumplirse siempre.

Estado: borrador. {{pending: confirmar esta política con la persona responsable}}

## Alcance

Todo el código de producción, los scripts que cambian datos o infraestructura y los contratos. Los experimentos desechables quedan fuera solo si nunca se integran.

## Reglas

| ID | Regla |
|----|-------|
| T-1 | **Pruebas primero.** Se commitea una prueba que falla antes del código que la hace pasar. |
| T-2 | **Pruebas congeladas.** Nadie, persona o agente, edita una prueba commiteada para que el código pase. Cambiar una prueba requiere un cambio de spec y aprobación humana. |
| T-3 | **Sin verde no hay hecho.** Nada se reporta como hecho mientras `make verify` falle. Reporta el resultado real. |
| T-4 | **Criterios cubiertos.** Cada criterio de aceptación tiene al menos una prueba, enlazada en el plan de pruebas. |
| T-5 | **Cada error trae su prueba.** Cada corrección incluye una prueba que primero reprodujo el error. |
| T-6 | **Sin omisiones silenciosas.** Una prueba omitida referencia un issue abierto y un responsable. |
| T-7 | **Umbrales por riesgo.** El código de mayor riesgo tiene cobertura y revisión más estrictas. |
| T-8 | **Deterministas y rápidas.** Las pruebas no dependen de la hora, el orden, la red ni estado compartido. |

## Umbrales por riesgo

| Riesgo | Ejemplo | Mínimo |
|--------|---------|--------|
| Alto | Pagos, permisos, datos personales | {{pending: umbral, p. ej. cobertura o puntuación de mutación}} |
| Medio | Lógica de negocio central | {{pending: umbral}} |
| Bajo | Presentación, código de unión | {{pending: umbral}} |

Los umbrales solo suben. Un cambio no puede rebajar un umbral existente.

## Definición de hecho (calidad)

- [ ] Existen y pasan pruebas para cada criterio.
- [ ] `dixi check` y `make verify` pasan y se reporta la salida.
- [ ] No hay pruebas omitidas nuevas sin issue.
- [ ] Una persona revisó las pruebas, no solo el código.

## Cómo se hace cumplir

{{pending: listar las verificaciones que hacen cumplir cada regla y cuáles siguen siendo solo de revisión}}

## Relacionados

- [Guía de TDD](../../11-quality/tdd-guide.md)
- [Pirámide de pruebas](../../11-quality/test-pyramid.md)
- [Plan de pruebas](../../11-quality/test-plan.md)
- [Estrategia de ramas](branching-strategy.md)
