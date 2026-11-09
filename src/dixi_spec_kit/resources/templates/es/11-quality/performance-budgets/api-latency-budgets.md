# Presupuestos de latencia de API

## Propósito

Fijar presupuestos de latencia y de errores para las APIs del proyecto, de modo que los endpoints lentos o que fallan se detecten como regresiones y no los descubran los usuarios.

Estado: borrador. {{pending: decidir los presupuestos por grupo de endpoints}}

## Presupuestos

| Grupo de endpoints | Ejemplo | p50 | p95 | p99 | Tasa de errores |
|--------------------|---------|-----|-----|-----|-----------------|
| Lecturas | {{pending: endpoint}} | {{pending: ms}} | {{pending: ms}} | {{pending: ms}} | {{pending: %}} |
| Escrituras | {{pending: endpoint}} | {{pending: ms}} | {{pending: ms}} | {{pending: ms}} | {{pending: %}} |
| Búsqueda o listados | {{pending: endpoint}} | {{pending: ms}} | {{pending: ms}} | {{pending: ms}} | {{pending: %}} |
| Segundo plano o asíncrono | {{pending: tarea}} | {{pending: ms}} | {{pending: ms}} | {{pending: ms}} | {{pending: %}} |

Solo como ejemplo, no como recomendación: un equipo puede empezar midiendo la latencia actual, fijar presupuestos algo por encima y ajustarlos con el tiempo.

## Condiciones

Los presupuestos aplican bajo condiciones declaradas; regístralas para que los resultados sean comparables.

- Carga: {{pending: peticiones por segundo o usuarios concurrentes}}
- Tamaño de carga útil: {{pending: típico y máximo}}
- Medido desde: {{pending: cliente, gateway o servicio}}
- Excluido: {{pending: por ejemplo arranques en frío, si se justifica}}

## Trabajo asíncrono

Para trabajo en colas o guiado por eventos, presupuesta el tiempo desde que se publica el mensaje hasta que el trabajo termina, y la profundidad máxima de la cola. {{pending: presupuestos asíncronos}}

## Verificaciones

- Las pruebas del [plan de pruebas de rendimiento](../performance-test-plan.md) verifican estos presupuestos.
- {{pending: si la monitorización en producción alerta cuando se incumple un presupuesto}}

## Cuando se excede un presupuesto

Encuentra la causa y corrígela. Subir un presupuesto requiere una decisión registrada de la persona responsable, con un motivo; nunca se hace para que una ejecución pase.

## Relacionados

- [Plan de pruebas de rendimiento](../performance-test-plan.md)
- [Presupuestos de web vitals](web-vitals-budgets.md)
- [Requisitos no funcionales](../non-functional-requirements.md)
- [Contrato](../../07-contracts/example.md)
