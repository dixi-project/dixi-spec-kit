# Playbook de due diligence de cliente empresarial

> **Regla de evidencia.** Responde los cuestionarios solo con lo que prueban los artefactos. Nunca marques «sí» en un control planificado que no está operando; los huecos se declaran como huecos y cada respuesta remite a un artefacto del proyecto.

## Propósito

Responder de forma coherente y veraz cuando el equipo de seguridad, privacidad o compras de un cliente empresarial evalúa el producto, normalmente mediante un cuestionario, una solicitud de documentos o una llamada.

Estado: borrador. {{pending: nombrar quién gestiona las revisiones de seguridad de clientes y quién aprueba las respuestas}}

## Recepción

| Campo | Valor |
|-------|-------|
| Cliente (solo referencia interna) | {{pending: referencia}} |
| Formato | {{pending: cuestionario / solicitud de documentos / llamada}} |
| Plazo | {{pending: fecha}} |
| Condiciones de confidencialidad | {{pending: referencia del acuerdo}} |
| Responsable comercial y técnico | {{pending: roles}} |

## Biblioteca de respuestas

Mantén respuestas aprobadas y reutilizables para que cada revisión parta de la anterior. Cada respuesta tiene un artefacto de origen y una fecha de revisión.

| Tema | Respuesta aprobada | Artefacto de origen | Última revisión |
|------|--------------------|---------------------|-----------------|
| Cifrado | {{pending: respuesta}} | [Controles de protección de datos](../../13-security/data-protection-controls.md) | {{pending: fecha}} |
| Control de acceso | {{pending: respuesta}} | [Modelo de AuthN/AuthZ](../../13-security/authn-authz-model.md) | {{pending: fecha}} |
| Respuesta a incidentes | {{pending: respuesta}} | [Respuesta a incidentes](../../13-security/incident-response.md) | {{pending: fecha}} |
| Subencargados | {{pending: respuesta}} | [Subencargados](../../23-compliance/gdpr/sub-processors.md) | {{pending: fecha}} |
| Continuidad de negocio | {{pending: respuesta}} | [Estrategia de DR](../../14-delivery/disaster-recovery/dr-strategy.md) | {{pending: fecha}} |
| Gestión de vulnerabilidades | {{pending: respuesta}} | [Gestión de vulnerabilidades](../../13-security/vulnerability-management.md) | {{pending: fecha}} |
| Certificaciones e informes | Solo lo que existe, con fecha y alcance | [Panorama de cumplimiento](../../23-compliance/compliance-overview.md) | {{pending: fecha}} |

## Pasos

1. Registrar la solicitud y confirmar el plazo.
2. Completar desde la biblioteca de respuestas; marcar las preguntas nuevas.
3. Enviar las preguntas nuevas al responsable del área; responder desde artefactos.
4. Revisar la exactitud; señalar con honestidad lo «parcial» o «planificado», con fecha.
5. Enviar por el canal acordado; guardar copia de lo enviado.
6. Añadir las nuevas respuestas aprobadas a la biblioteca y las brechas al backlog.

## Documentos solicitados con frecuencia

- Resumen de seguridad, diagrama de flujo de datos, lista de subencargados, DPA, resumen de respuesta a incidentes, resumen de prueba de penetración (si existe y puede compartirse). {{pending: decidir cuáles puede aportar el proyecto}}

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Lista 04 — Seguridad](../checklist/04-security.md)
- [Plantilla de DPA](../../23-compliance/dpa-template.md)
- [Panorama de cumplimiento](../../23-compliance/compliance-overview.md)
