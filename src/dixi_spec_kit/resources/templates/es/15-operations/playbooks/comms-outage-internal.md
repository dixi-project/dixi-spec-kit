# Comunicación interna de caídas

## Propósito

Mantener informados al equipo, a soporte y a la dirección durante una caída desde un único lugar, para que quienes responden se concentren y nadie actúe por rumores.

Estado: borrador. {{pending: nombrar el rol de líder de comunicación}}

## Cuándo aplica

Todo incidente de SEV3 hacia arriba (ver [niveles de incidente](../incident-levels.md)).

## Canales

| Canal | Propósito | Quién escribe |
|-------|-----------|---------------|
| {{pending: canal del incidente}} | Coordinación técnica, uno por incidente | Quienes responden |
| {{pending: canal de anuncios}} | Estado breve para toda la organización | Líder de comunicación |
| {{pending: canal o herramienta de soporte}} | Qué decir a los usuarios, respuestas predefinidas | Líder de comunicación |

## Pasos

1. **Abrir** un canal de incidente llamado `inc-<fecha>-<nombre-corto>` y fijar el nivel, el líder y la hora de inicio.
2. **Anunciar** en el canal general en menos de {{pending: minutos}}: qué está afectado, nivel, quién lidera, dónde seguirlo.
3. **Informar a soporte** con una respuesta lista para usar, coherente con la [comunicación de caída a clientes](comms-outage-customer.md).
4. **Actualizar** cada {{pending: intervalo}}, o de inmediato cuando cambie el nivel.
5. **Cerrar** con un mensaje final: hora de restauración, impacto, próximos pasos y fecha del postmortem.

## Plantilla de actualización

> **[Nivel SEV] Título breve** — Estado: investigando / mitigando / vigilando / resuelto.
> Impacto: {{pending: a quién afecta y cómo}}.
> Acción actual: {{pending: qué se está haciendo}}.
> Próxima actualización: {{pending: hora}}. Líder: {{pending: rol o nombre}}.

## Reglas

- Solo el líder del incidente o el de comunicación publican actualizaciones de estado; los demás preguntan en el canal del incidente.
- Mantén las conversaciones paralelas fuera del canal del incidente.
- No compartas credenciales, datos personales ni registros de clientes en ningún canal.
- Si la dirección debe decidir algo, pídelo explícitamente y con opciones.

## Criterios de cierre

- Mensaje final publicado en todos los canales usados.
- Soporte confirma que tiene la respuesta de cierre.
- Canal del incidente archivado tras el postmortem.

## Relacionados

- [Niveles de incidente](../incident-levels.md)
- [Matriz de escalamiento](../escalation-matrix.md)
- [Comunicación de caída a clientes](comms-outage-customer.md)
- [Restaurar el servicio](restore-service.md)
