# Métricas de ingeniería

## Propósito

Elegir un conjunto pequeño de métricas que muestren si el proceso de entrega está sano, y usarlas para mejorar el proceso, nunca para clasificar personas.

Estado: borrador. {{pending: elegir las métricas que seguirá este proyecto}}

## Métricas candidatas

| Métrica | Qué muestra | Cómo se mide | Objetivo |
|---------|-------------|--------------|----------|
| Tiempo de entrega de cambios | Tiempo desde el commit hasta producción | {{pending: fuente}} | {{pending: objetivo}} |
| Frecuencia de despliegue | Cada cuánto llegan cambios a los usuarios | {{pending: fuente}} | {{pending: objetivo}} |
| Tasa de cambios fallidos | Proporción de cambios que causan un fallo | {{pending: fuente}} | {{pending: objetivo}} |
| Tiempo de recuperación | Tiempo para recuperarse de un fallo | {{pending: fuente}} | {{pending: objetivo}} |
| Tiempo de verificación | Duración de `make verify` y de CI | {{pending: fuente}} | {{pending: objetivo}} |
| Pruebas inestables | Pruebas en cuarentena por inestabilidad | {{pending: fuente}} | {{pending: objetivo}} |
| Defectos escapados | Defectos encontrados después del release | {{pending: fuente}} | {{pending: objetivo}} |

Elige solo las métricas que alguien revisará y sobre las que actuará.

## Reglas

- Las métricas describen el sistema, no a las personas.
- Una métrica convertida en meta pierde sentido; vigila la manipulación (commits diminutos solo para subir la frecuencia, pruebas borradas para acelerar CI).
- No bajes las puertas de calidad para mejorar una métrica.
- Los cambios generados por agentes se miden como cualquier otro cambio.

## Revisión

- {{pending: cada cuánto se revisan las métricas y quién lo hace}}
- Cada revisión termina con pocas acciones de mejora, cada una con responsable.

## Datos

{{pending: de dónde salen los datos de las métricas y cuánto tiempo se conservan}}

Recoge solo lo necesario; evita datos personales.

## Relacionados

- [Estrategia de calidad](quality-strategy.md)
- [Plan de regresión](regression-plan.md)
- [Escalera de verificación](verification-ladder.md)
- [Revisión basada en riesgo](risk-based-review.md)
