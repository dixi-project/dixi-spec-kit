# Reglas de alertas

## Propósito

Definir qué condiciones despiertan a una persona, cuáles solo abren un ticket y cuáles solo se muestran en un tablero. Una alerta existe para provocar una acción humana; si nadie necesita actuar, no es una alerta.

## Principios

- Alerta sobre síntomas que sienten las personas usuarias (errores, latencia, indisponibilidad), no sobre cada causa interna.
- Toda alerta que despierta a alguien enlaza a un runbook con los primeros pasos.
- Toda alerta tiene responsable, severidad y fecha de revisión.
- Una alerta que se dispara y se ignora dos veces se corrige, se reajusta o se elimina.
- Las alertas nunca incluyen secretos ni datos personales en su mensaje.

## Niveles de severidad

| Severidad | Significado | Respuesta | Canal |
|---|---|---|---|
| critical | Las personas usuarias no pueden completar el flujo principal | {{pending: tiempo de respuesta, p. ej. 15 minutos}} | {{pending: canal de guardia}} |
| warning | Degradación o riesgo de incumplir pronto | {{pending: en horario laboral}} | {{pending: canal del equipo}} |
| info | Contexto útil, sin acción requerida | Ninguna | Solo tablero |

## Inventario de alertas

| Alerta | Condición | Ventana | Severidad | Responsable | Runbook |
|---|---|---|---|---|---|
| Sitio o servicio no disponible | El chequeo de salud falla desde fuera | {{pending: p. ej. 3 chequeos seguidos}} | critical | {{pending: rol}} | {{pending: enlace}} |
| Tasa de errores alta | Errores de servidor por encima de {{pending: umbral}} | {{pending: ventana}} | critical | {{pending: rol}} | {{pending: enlace}} |
| Latencia degradada | p95 por encima de {{pending: presupuesto}} | {{pending: ventana}} | warning | {{pending: rol}} | {{pending: enlace}} |
| Certificado por vencer | Menos de {{pending: días}} para vencer | Diaria | warning | {{pending: rol}} | {{pending: enlace}} |
| Despliegue fallido | La versión no terminó o se revirtió | Por evento | warning | {{pending: rol}} | [Reversión](../14-delivery/rollback-strategy.md) |

Cuando existan objetivos de nivel de servicio, prefiere alertas por velocidad de consumo del presupuesto de error (una ventana rápida y una lenta) en lugar de umbrales fijos.

## Enrutamiento y escalamiento

- Primera respuesta: {{pending: rol o rotación}}
- Escalamiento si nadie reconoce la alerta: {{pending: tiempo y siguiente rol}}
- Política fuera de horario: {{pending: qué severidades despiertan fuera de horario}}
- Herramienta de notificación: {{pending: decidir y registrar en un ADR}}

## Ciclo de vida

1. Propón la alerta con su condición, severidad y runbook.
2. Pruébala en un entorno no productivo forzando la condición.
3. Revisa el inventario {{pending: frecuencia}} y elimina alertas ruidosas o sin uso.
4. Tras un incidente, comprueba si una alerta saltó a tiempo; ajústala si no.

## Relacionados

- [Respuesta a incidentes](../13-security/incident-response.md)
- [Plantilla de runbook](../10-engineering/templates/runbook-template.md)
- [Plantilla de postmortem](../10-engineering/templates/postmortem-template.md)
- [Estrategia de reversión](../14-delivery/rollback-strategy.md)
- [Plan de pruebas](../11-quality/test-plan.md)
