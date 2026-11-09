# Rotación de guardia

## Propósito

Definir quién responde a las alertas dentro y fuera del horario laboral, cómo funcionan los turnos y cómo la rotación se mantiene justa y sostenible.

Estado: borrador. {{pending: nombrar al responsable de la rotación}}

## Cobertura

| Aspecto | Decisión |
|---------|----------|
| Horario cubierto | {{pending: p. ej. solo horario laboral, o 24/7}} |
| Duración del turno | {{pending: p. ej. una semana}} |
| Hora de traspaso | {{pending: día y hora, zona horaria}} |
| Principal y secundario | {{pending: sí / solo principal}} |
| Herramienta de avisos | {{pending: categoría de herramienta, no proveedor}} |
| Objetivo de reconocimiento | {{pending: minutos}} |

Con menos de {{pending: número}} personas, una cobertura 24/7 no es sostenible; prefiere horario laboral más mejor esfuerzo y dilo en el modelo de soporte.

## Quién hace guardia

- Ingenieros que completaron su incorporación, acompañaron al menos un turno y tienen acceso a los runbooks.
- {{pending: decidir si líderes y gerentes hacen turnos}}

## Durante el turno

- Mantén el teléfono localizable y poder empezar a trabajar dentro del objetivo de reconocimiento.
- Reconoce cada aviso, clasifícalo con los [niveles de incidente](../incident-levels.md) y escala con la [matriz de escalamiento](../escalation-matrix.md).
- Escribe un registro breve de cada aviso: hora, causa, acción, seguimiento.

## Traspaso

1. Revisa el registro del turno junto con la siguiente persona.
2. Traspasa los incidentes abiertos y lo que pueda volver a avisar.
3. Confirma que la configuración de avisos de la siguiente persona funciona.

## Equidad y salud

- Compensación o tiempo libre tras los turnos: {{pending: definir según la normativa local}}
- Nadie hace dos turnos seguidos salvo que se ofrezca.
- Un turno con aviso nocturno da derecho a empezar más tarde al día siguiente.
- Las alertas ruidosas que avisan sin requerir acción se corrigen o eliminan en {{pending: días}}.

## Métricas

- Avisos por turno, avisos fuera de horario, tiempo hasta reconocer.
- Revísalas cada {{pending: frecuencia}} con el equipo.

## Relacionados

- [Matriz RACI](raci-matrix.md)
- [Matriz de escalamiento](../escalation-matrix.md)
- [Niveles de incidente](../incident-levels.md)
- [Restaurar el servicio](../playbooks/restore-service.md)
