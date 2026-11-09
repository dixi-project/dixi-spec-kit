# Marco de priorización

## Propósito

Dar al equipo una forma única, compartida y explicable de decidir en qué trabajar después, para que la prioridad salga de la evidencia y de criterios acordados, no de quien pide más fuerte.

Estado: borrador. {{pending: elegir el método de puntuación y la persona que tiene la última palabra}}

## Entradas

Un elemento solo puede puntuarse cuando tiene:

- Un problema redactado desde el punto de vista del usuario.
- La evidencia que lo respalda (nota de investigación, métrica, tendencia de soporte, obligación regulatoria).
- Un tamaño aproximado acordado por quienes lo construirían.
- El público objetivo, incluidos los idiomas y mercados afectados.

## Método de puntuación

Elige un método y úsalo de forma consistente. Dos opciones comunes:

| Método | Fórmula | Útil para |
|--------|---------|-----------|
| Alcance, impacto, confianza, esfuerzo | (alcance × impacto × confianza) ÷ esfuerzo | Comparar muchos elementos con algunos datos |
| Matriz valor contra esfuerzo | Ubicar cada elemento en una cuadrícula 2×2 | Ordenar rápido con pocos datos |

{{pending: elegir el método y definir la escala de cada factor}}

### Definición de escalas

| Factor | Bajo | Medio | Alto |
|--------|------|-------|------|
| Alcance | {{pending: por ejemplo menos del 10 % de usuarios activos}} | {{pending}} | {{pending}} |
| Impacto | Mejora pequeña | Mejora notable | Cambia el resultado para el usuario |
| Confianza | Solo opinión | Algo de evidencia | Evidencia fuerte y repetida |
| Esfuerzo | {{pending: unidad, por ejemplo semanas-persona}} | {{pending}} | {{pending}} |

## Elementos que no hacen fila

Algunos trabajos no se puntúan contra funcionalidades:

- Las correcciones de seguridad e incidentes siguen el proceso de seguridad y operaciones.
- Las obligaciones legales o contractuales reciben una fecha límite, no una puntuación.
- Los defectos de accesibilidad que impiden completar una tarea se tratan como defectos, no como funcionalidades.

{{pending: listar otras categorías que se salten la puntuación}}

## Registro de decisiones

En cada sesión de priorización, registra:

| Fecha | Elementos revisados | Decisión | Motivo | Decidido por |
|-------|---------------------|----------|--------|--------------|
| {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |

## Antipatrones

- Puntuar después de haber tomado la decisión.
- Dar confianza alta sin evidencia.
- Ignorar el costo de mantener una funcionalidad después del lanzamiento.
- Priorizar solo el mercado del idioma principal y dejar las traducciones «para después» sin fecha.

## Relacionados

- [Hoja de ruta](roadmap.md)
- [Ciclo de vida de funcionalidades](feature-lifecycle.md)
- [Catálogo de eventos de analítica](analytics-events-catalog.md)
- [Trabajos por hacer](../24-research/jobs-to-be-done.md)
- [Objetivo de negocio](../01-business/vision.md)
