# Política de incidentes

## Propósito

Definir qué cuenta como incidente en el proyecto, quién hace qué cuando ocurre, cómo se comunica y cómo aprende el equipo de él. La respuesta paso a paso vive en los runbooks y en el plan de respuesta a incidentes de seguridad.

Estado: borrador. {{pending: confirmar esta política con la persona responsable}}

## Principios

- Primero restaurar el servicio; investigar la causa raíz después.
- Sin culpables: describe sistemas y decisiones, no fallos de personas.
- Un único responsable del incidente a la vez.
- Todo incidente deja registro, por pequeño que sea.

## Niveles de severidad

| Nivel | Definición | Objetivo de respuesta | A quién avisar |
|-------|------------|-----------------------|----------------|
| SEV1 | Servicio caído o datos expuestos para muchos usuarios | {{pending: objetivo}} | {{pending: a quién}} |
| SEV2 | Funcionalidad importante degradada, con alternativa | {{pending: objetivo}} | {{pending: a quién}} |
| SEV3 | Impacto menor, pocos usuarios | {{pending: objetivo}} | {{pending: a quién}} |

## Roles

| Rol | Responsabilidad |
|-----|-----------------|
| Responsable del incidente | Coordina, decide y mantiene la cronología. |
| Responsable de operaciones | Investiga y aplica correcciones. |
| Responsable de comunicación | Informa a usuarios y partes interesadas. |
| Escriba | Registra acciones y decisiones con hora. |

Los agentes pueden ayudar a reunir datos y redactar comunicados; una persona toma cada decisión y hace cada cambio.

## Ciclo

1. **Detectar** mediante alertas o reportes.
2. **Declarar** con una severidad y un responsable.
3. **Mitigar** para detener el impacto.
4. **Resolver** y confirmarlo con el monitoreo.
5. **Revisar** con un postmortem.

## Acceso durante un incidente

- El acceso elevado se concede de forma temporal, se registra y se retira después. {{pending: procedimiento de acceso de emergencia}}

## Comunicación

- Canal del incidente: {{pending: canal}}
- Actualizaciones de estado cada {{pending: intervalo}} para SEV1 y SEV2.
- Notificaciones legales o regulatorias: {{pending: quién decide y en qué plazo}}

## Postmortem

- Obligatorio para SEV1 y SEV2, en un plazo de {{pending: días}}.
- Usa la [plantilla de postmortem](../../10-engineering/templates/postmortem-template.md).
- Las acciones tienen responsable y fecha.

## Relacionados

- [Respuesta a incidentes](../../13-security/incident-response.md)
- [Plantilla de runbook](../../10-engineering/templates/runbook-template.md)
- [Estándar de observabilidad](../observability-standard.md)
