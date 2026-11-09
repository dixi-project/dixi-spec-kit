# Plantilla de postmortem

## Propósito

Aprender de un incidente sin culpables: reconstruir qué pasó, por qué fue posible y qué acciones lo
evitarán o acortarán la próxima vez. Copia la estructura de abajo después de cada incidente que
supere el umbral del proyecto.

Umbral para escribir un postmortem: {{pending: severidad o impacto que lo exige}}

## Plantilla

```markdown
# Postmortem: <título corto del incidente>

Fecha del incidente: AAAA-MM-DD
Severidad: {{pending: nivel de severidad}}
Estado: borrador | revisado | acciones cerradas
Autores: ...

## Resumen

Dos o tres frases: qué falló, a quién afectó y durante cuánto tiempo.

## Impacto

- Usuarios o clientes afectados:
- Duración (de la detección a la resolución):
- Datos afectados (pérdida, exposición, corrupción):

## Cronología (UTC)

| Hora | Evento |
|---|---|
| hh:mm | Primer síntoma |
| hh:mm | Detectado por ... |
| hh:mm | Mitigado |
| hh:mm | Resuelto |

## Causa raíz y factores contribuyentes

Describe las condiciones que hicieron posible el fallo. Enfócate en sistemas y
procesos, no en personas.

## Detección

Cómo se detectó y cómo pudo detectarse antes.

## Qué salió bien / qué salió mal

- ...

## Acciones

| Acción | Tipo (prevenir / detectar / mitigar) | Responsable | Fecha límite | Ticket |
|---|---|---|---|---|

## Aprendizajes

Lo que el equipo sabe ahora y no sabía antes.
```

## Reglas

- Sin culpables: nombra roles y sistemas, no personas responsables del fallo.
- Nunca incluyas secretos ni datos personales; si se expusieron, dilo y explica cómo se contuvo.
- Cada acción tiene responsable y fecha; el postmortem se cierra cuando se cierran las acciones.

## Relacionados

- [Plantilla de runbook](runbook-template.md)
- [Plantilla de ADR](adr-template.md)
- [Estándar de código seguro](../secure-coding-standard.md)
