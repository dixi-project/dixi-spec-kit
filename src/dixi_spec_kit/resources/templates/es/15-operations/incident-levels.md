# Niveles de incidente

## Propósito

Dar a todo el equipo la misma escala para clasificar un incidente, de modo que la respuesta, las personas involucradas y la comunicación correspondan al impacto real.

Estado: borrador. {{pending: nombrar al responsable de la escala de incidentes}}

## La escala

| Nivel | Significado | Señales de ejemplo | Primera respuesta | Aviso a clientes |
|-------|-------------|--------------------|-------------------|------------------|
| SEV1 | Servicio crítico caído o datos en riesgo para la mayoría de usuarios | Flujo principal no disponible, sospecha de pérdida o fuga de datos | {{pending: p. ej. 15 minutos, a cualquier hora}} | {{pending: p. ej. en 30 minutos}} |
| SEV2 | Degradación mayor o un flujo crítico roto para parte de los usuarios | Tasa de error muy por encima de lo normal, una región o segmento caído | {{pending: p. ej. 30 minutos}} | {{pending: p. ej. en 1 hora}} |
| SEV3 | Degradación menor con alternativa | Páginas lentas, una función secundaria falla | {{pending: p. ej. siguiente horario laboral}} | {{pending: solo si lo piden}} |
| SEV4 | Problema estético o interno, sin impacto en usuarios | Errata, alerta ruidosa, fallo de herramienta interna | Backlog | Ninguno |

Los tiempos anteriores son marcadores; fíjalos con las personas que estarán de guardia.

## Servicios y flujos críticos

Un fallo en alguno de estos nunca es menor que SEV2:

- {{pending: listar los flujos críticos, p. ej. inicio de sesión, pago, exportación de datos}}

## Cómo clasificar

1. Clasifica con la información disponible; no esperes a tener certeza.
2. Si dudas entre dos niveles, elige el más alto.
3. Cualquier sospecha de exposición de datos personales empieza en SEV1 hasta descartarla.
4. Registra el nivel, la hora y quién lo declaró en el canal del incidente.

## Subir y bajar de nivel

- Cualquier persona de la respuesta puede subir el nivel en cualquier momento.
- Solo quien lidera el incidente lo baja, y deja escrito el motivo.
- Un cambio de nivel activa la fila correspondiente de la [matriz de escalamiento](escalation-matrix.md).

## Mitigar primero, sin saltarse la cadena

Restaurar el servicio va antes que encontrar la causa raíz, pero la mitigación no se salta aprobaciones: sigue el playbook de [restaurar el servicio](playbooks/restore-service.md) y nunca dejes que un agente de IA opere producción por su cuenta.

## Después del incidente

SEV1 y SEV2 siempre llevan un postmortem sin culpables con la [plantilla de postmortem](../10-engineering/templates/postmortem-template.md). {{pending: decidir si SEV3 también requiere postmortem}}

## Relacionados

- [Matriz de escalamiento](escalation-matrix.md)
- [Restaurar el servicio](playbooks/restore-service.md)
- [Comunicación de caída a clientes](playbooks/comms-outage-customer.md)
- [Respuesta a incidentes](../13-security/incident-response.md)
- [Proyecto](../00-master-spec.md)
