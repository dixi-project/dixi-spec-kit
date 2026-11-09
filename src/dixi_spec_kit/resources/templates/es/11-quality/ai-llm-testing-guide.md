# Guía de pruebas de IA y LLM

## Propósito

Explicar cómo probar funcionalidades que usan modelos de lenguaje u otros componentes de IA, cuyas salidas son probabilísticas, para que la calidad se mida con evidencia y no con impresiones.

Estado: borrador. {{pending: listar las funcionalidades de IA en alcance y sus responsables}}

## Qué cambia con componentes de IA

- La misma entrada puede producir salidas distintas.
- «Correcto» suele ser un rango de respuestas aceptables, no un único valor.
- Cambios de modelo, prompt o datos pueden alterar el comportamiento sin tocar el código.

El código alrededor del modelo se sigue probando con TDD; esta guía cubre el comportamiento del modelo.

## Capas

| Capa | Qué comprueba | Cómo |
|------|---------------|------|
| Código determinista | Construcción del prompt, parseo, validación, alternativas | Pruebas unitarias con un modelo simulado |
| Contrato de salida | Las respuestas tienen la estructura esperada | Validación de esquema en cada respuesta |
| Conjunto de evaluación | Calidad en casos representativos | Ejecuciones puntuadas contra un conjunto versionado |
| Seguridad | Rechazos, contenido dañino, fugas de datos, inyección de prompts | Casos adversarios en el conjunto de evaluación |
| Producción | Deriva y fallos con uso real | Monitorización y revisión humana por muestreo |

## Conjuntos de evaluación

- Construye un conjunto versionado de entradas con resultados esperados o reglas de puntuación. {{pending: tamaño y origen del conjunto de evaluación}}
- Incluye casos límite, otros idiomas y entradas adversarias.
- Nunca pongas datos personales reales ni secretos en los conjuntos de evaluación.
- Puntúa con comprobaciones exactas cuando sea posible; usa rúbricas o puntuación asistida por modelo solo con calibración humana periódica.

## Umbrales

| Métrica | Umbral | Bloquea el release |
|---------|--------|--------------------|
| {{pending: métrica, por ejemplo tasa de éxito de la tarea}} | {{pending: umbral}} | {{pending: sí/no}} |
| {{pending: métrica, por ejemplo tasa de salidas inseguras}} | {{pending: umbral}} | {{pending: sí/no}} |

Vuelve a ejecutar el conjunto de evaluación cuando cambien el modelo, el prompt, los parámetros o los datos de recuperación. No bajes un umbral para que una ejecución pase.

## Contenido no confiable

Trata la salida del modelo y los documentos recuperados como datos, no como instrucciones. Prueba que las instrucciones inyectadas en las entradas no cambien el comportamiento del sistema.

## Relacionados

- [Estrategia de calidad](quality-strategy.md)
- [Plan de pruebas de seguridad](security-test-plan.md)
- [Plan de regresión](regression-plan.md)
- [Revisión basada en riesgo](risk-based-review.md)
- [Plan de pruebas](test-plan.md)
