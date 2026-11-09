# Plan de pruebas de rendimiento

## Propósito

Planificar cómo comprueba el proyecto que cumple sus presupuestos de rendimiento con carga realista, antes de que los usuarios encuentren los límites. Este plan describe pruebas previstas; no es un registro de pruebas ejecutadas.

Estado: borrador. {{pending: confirmar el alcance y el entorno de las pruebas de rendimiento}}

## Objetivos

- Confirmar los [presupuestos de latencia de API](performance-budgets/api-latency-budgets.md) y los [presupuestos de web vitals](performance-budgets/web-vitals-budgets.md).
- Encontrar el límite de capacidad y cómo falla el sistema más allá de él.
- Detectar regresiones de rendimiento entre releases.

## Tipos de prueba

| Tipo | Pregunta que responde | Perfil de carga | Cuándo |
|------|-----------------------|-----------------|--------|
| Línea base | ¿Cómo vive el sistema un único usuario? | Un usuario | {{pending: cuándo}} |
| Carga | ¿Cumple los presupuestos con el tráfico esperado? | {{pending: tráfico esperado}} | {{pending: cuándo}} |
| Estrés | ¿Dónde se rompe y cómo? | Creciente hasta el fallo | {{pending: cuándo}} |
| Resistencia | ¿Se degrada con el tiempo? | Tráfico esperado durante horas | {{pending: cuándo}} |
| Picos | ¿Sobrevive a ráfagas repentinas? | Ráfagas cortas por encima de lo esperado | {{pending: cuándo}} |

## Escenarios

| Escenario | Endpoint o recorrido | Proporción del tráfico | Datos necesarios |
|-----------|----------------------|------------------------|------------------|
| {{pending: escenario}} | {{pending: endpoint}} | {{pending: proporción}} | {{pending: datos}} |

## Entorno

- {{pending: dónde corren las pruebas y cuán parecido es a producción}}
- Usa datos generados; nunca hagas pruebas de carga con datos personales reales.
- Nunca lances pruebas de carga contra sistemas que no son tuyos o sin permiso.

## Criterios de aprobación

Una ejecución pasa cuando todos los presupuestos se cumplen con la carga objetivo y la tasa de errores se mantiene dentro de {{pending: presupuesto de errores}}. Los resultados que incumplen un presupuesto se investigan; los presupuestos no se relajan para que una ejecución pase.

## Informe

Registra fecha, versión, entorno, perfil de carga, resultados por escenario y problemas abiertos.

## Relacionados

- [Presupuestos de latencia de API](performance-budgets/api-latency-budgets.md)
- [Presupuestos de web vitals](performance-budgets/web-vitals-budgets.md)
- [Requisitos no funcionales](non-functional-requirements.md)
- [Plan de regresión](regression-plan.md)
