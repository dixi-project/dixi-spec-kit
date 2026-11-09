# Marco de pruebas A/B

## Propósito

Definir cuándo ejecutar experimentos controlados, cómo diseñarlos para que el resultado sea confiable y cómo registrar las decisiones. Un experimento sirve para reducir incertidumbre, no para evitar tomar una decisión.

Estado: borrador. {{pending: decidir el tráfico mínimo, el nivel de significancia y quién aprueba los experimentos}}

## Cuándo experimentar

Experimenta cuando:

- El cambio es reversible y el resultado es realmente incierto.
- Hay tráfico suficiente en el segmento para detectar el efecto esperado en un tiempo razonable.
- La métrica se puede medir de forma fiable.

Decide sin experimento cuando:

- El cambio corrige un defecto, un problema de accesibilidad o un requisito legal.
- El tráfico es demasiado bajo para llegar a una conclusión.
- El cambio lo exige una spec independientemente del resultado.

## Diseño del experimento

| Campo | Contenido |
|-------|-----------|
| ID y responsable | {{pending}} |
| Hipótesis | Si cambiamos X para el segmento Y, la métrica Z se moverá N porque ... |
| Métrica principal | Una métrica que decide el resultado |
| Métricas de resguardo | Métricas que no deben empeorar (errores, rendimiento, quejas) |
| Segmento e idiomas | {{pending}} |
| Tamaño de muestra y duración | Calculados antes de empezar |
| Condiciones de parada | Cuándo detener antes por daño |

## Reglas para resultados confiables

- Fija el tamaño de muestra y la duración antes de empezar; no detengas cuando el resultado parezca bueno.
- Ejecuta ciclos semanales completos para evitar efectos del día de la semana.
- Comprueba que las variantes recibieron la proporción de tráfico esperada antes de leer resultados.
- Analiza idiomas y mercados por separado cuando se comportan distinto.
- Evita experimentos superpuestos en la misma página o métrica salvo que estén diseñados para ello.
- Las variantes en cada idioma son traducciones completas; una traducción faltante invalida la prueba.
- Las variantes renderizadas en servidor no deben mostrar a los crawlers contenido distinto del que verían las personas.

## Decisión

| Resultado | Acción |
|-----------|--------|
| La métrica principal mejora y los resguardos se mantienen | Publicar y registrar |
| Sin diferencia significativa | Elegir la opción más simple y registrar |
| Un resguardo empeora | No publicar; investigar |

## Registro del resultado

Registra cada experimento: hipótesis, fechas, segmentos, resultados con su incertidumbre, decisión y la persona que la tomó. Conserva también los experimentos fallidos.

## Relacionados

- [Embudo de conversión](conversion-funnel.md)
- [Estrategia de crecimiento](growth-strategy.md)
- [Catálogo de landing pages](landing-pages-catalog.md)
- [Registro de decisiones](../18-knowledge-base/decision-log.md)
- [Clasificación de PII](../08-data/pii-classification.md)
