# Puertas de calidad del trabajo asistido por IA

## Propósito

Enumerar, en orden, las puertas que debe superar un cambio antes de integrarse, y las puertas adicionales para features que llaman a un modelo de lenguaje. Una puerta existe solo si un mecanismo o una persona nombrada la hace cumplir y deja evidencia.

## Puertas en orden

| # | Puerta | Evidencia | La hace cumplir |
| --- | --- | --- | --- |
| 1 | Spec aprobada y trazada | Entrada en `.dixi/traceability.json` | `dixi check` y quien revisa |
| 2 | Pruebas escritas primero y en rojo | Orden de commits en el pull request | Quien revisa |
| 3 | Estructura válida | Salida de `dixi check` | Automático |
| 4 | Pasan las pruebas del proyecto | Salida del ejecutor de pruebas | {{pending: CI o comando local}} |
| 5 | Análisis estático y de seguridad | Informes de las herramientas | {{pending: herramientas elegidas}} |
| 6 | Revisión humana del diff | Aprobación sobre la revisión final | Persona |
| 7 | Integración | Reglas de rama protegida | {{pending: mecanismo}} |

## Puertas adicionales para features con modelo

### Pruebas del código que llama al modelo

- Las respuestas del modelo se simulan; las pruebas cubren salidas válidas, malformadas y rechazos.
- La validación de esquema rechaza salidas inesperadas.

### Evaluaciones contra el modelo real

- Un conjunto de evaluación versionado con un umbral de aceptación acordado antes de ejecutarlo.
- Se repite cuando cambian el modelo, la plantilla de prompt o los parámetros.
- Umbral y conjunto de evaluación: {{pending: definir el conjunto de evaluación y el umbral de aprobación}}

### Herramientas expuestas al modelo

- Cada herramienta tiene pruebas de comprobación de permisos y de entradas rechazadas.

## Lo que no es una puerta

- El veredicto de un agente: prepara la revisión humana, no la sustituye.
- La cobertura por sí sola: mide líneas ejecutadas, no errores detectados.
- Una evaluación sin umbral: un número sin criterio de aceptación es un dato, no un control.
- «Se veía bien»: sin mecanismo ni evidencia, no hay puerta.

## Relacionados

- [Rastro de auditoría de IA](ai-audit-trail.md)
- [IA responsable](responsible-ai.md)
- [Reglas de validación](../sdd/validation-rules.md)
- [Humano en el circuito](../agents/human-in-the-loop.md)
- [Plan de pruebas](../../11-quality/test-plan.md)
