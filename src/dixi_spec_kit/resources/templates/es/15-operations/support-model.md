# Modelo de soporte

## Propósito

Describir cómo obtienen ayuda los usuarios, quién responde, cómo pasan las solicitudes entre niveles de soporte y qué tiempos de respuesta asume el proyecto.

Estado: borrador. {{pending: nombrar al responsable del modelo de soporte}}

## Canales

| Canal | Audiencia | Horario | Responsable |
|-------|-----------|---------|-------------|
| {{pending: p. ej. centro de ayuda}} | Todos los usuarios | Siempre disponible | {{pending: rol}} |
| {{pending: p. ej. support@example.com}} | Todos los usuarios | {{pending: horario y zona horaria}} | {{pending: rol}} |
| {{pending: p. ej. chat dedicado}} | {{pending: ¿solo planes de pago?}} | {{pending: horario}} | {{pending: rol}} |

## Niveles

| Nivel | Atiende | Escala cuando |
|-------|---------|---------------|
| Nivel 0 | Autoservicio: artículos de ayuda, página de estado, guías en el producto | La respuesta no está documentada |
| Nivel 1 | Dudas de cuenta, cómo hacer algo, problemas conocidos | Se sospecha un bug o un problema de datos |
| Nivel 2 | Reproducción, logs, configuración, alternativas | Hace falta un cambio de código o infraestructura |
| Nivel 3 | Corrección de ingeniería | — |

Una posible caída se salta los niveles y va directo a los [niveles de incidente](incident-levels.md).

## Objetivos de respuesta

| Prioridad | Definición | Primera respuesta | Objetivo de resolución |
|-----------|------------|-------------------|------------------------|
| P1 | El usuario no puede trabajar | {{pending: objetivo}} | {{pending: objetivo}} |
| P2 | Función importante rota, hay alternativa | {{pending: objetivo}} | {{pending: objetivo}} |
| P3 | Pregunta o problema menor | {{pending: objetivo}} | {{pending: objetivo}} |

No publiques estos objetivos como compromiso contractual hasta haberlos medido durante un tiempo.

## Uso de IA en soporte

{{pending: decidir si un asistente de IA redacta o envía respuestas, y qué temas siempre requieren una persona}}

- Las respuestas redactadas con IA sobre facturación, borrado de datos o seguridad siempre las revisa una persona.
- El asistente solo lee lo que el ticket necesita; nunca recibe acceso amplio a datos de usuarios.

## Ciclo de mejora

- Las preguntas repetidas se convierten en artículos de ayuda.
- Los bugs repetidos van a [problemas conocidos](known-issues.md) y al backlog.
- Un resumen mensual de volumen y temas de tickets llega al dueño del producto.

## Relacionados

- [Catálogo de servicios](service-catalog.md)
- [Problemas conocidos](known-issues.md)
- [Niveles de incidente](incident-levels.md)
- [Matriz de escalamiento](escalation-matrix.md)
