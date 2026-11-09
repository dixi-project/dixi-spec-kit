# Mapeo de controles ISO/IEC 27001

> **Ayuda de trabajo; no es asesoría legal.** Esta tabla de trabajo relaciona los controles del proyecto con los temas del conjunto de controles de referencia de ISO/IEC 27001. No reproduce el texto de la norma y ninguna plantilla certifica conformidad.

## Propósito

Preparar la declaración de aplicabilidad: para cada control de referencia el equipo anota si aplica, por qué, cómo lo implementa el proyecto y dónde está la evidencia. Usa los identificadores de tu copia con licencia de la norma.

Estado: borrador. {{pending: confirmar la edición de la norma que sigue el SGSI}}

## Reglas

- Las exclusiones necesitan un motivo ligado al alcance o al riesgo, nunca «aún no está hecho».
- La implementación se describe con palabras del proyecto y un enlace al artefacto.
- Un control del proyecto puede servir a varios controles de referencia; reutiliza su ID.

## Mapeo por tema

El conjunto de referencia agrupa los controles en cuatro temas. Añade una fila por cada control de referencia que evalúes.

| Tema | ID de control ref. | ¿Aplica? | Motivo | Control / artefacto del proyecto | Responsable | Estado |
|------|--------------------|----------|--------|----------------------------------|-------------|--------|
| Organizativo | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo}} | [Política del SGSI](isms-policy.md) | {{pending: responsable}} | {{pending: estado}} |
| Organizativo | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo}} | [Evaluación de riesgo de proveedores](../../15-operations/vendor-management/vendor-risk-assessment.md) | {{pending: responsable}} | {{pending: estado}} |
| Organizativo | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo}} | [Respuesta a incidentes](../../13-security/incident-response.md) | {{pending: responsable}} | {{pending: estado}} |
| Personas | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo}} | {{pending: registros de incorporación, concienciación y bajas}} | {{pending: responsable}} | {{pending: estado}} |
| Físico | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo, p. ej. heredado del proveedor de alojamiento}} | {{pending: evidencia del proveedor}} | {{pending: responsable}} | {{pending: estado}} |
| Tecnológico | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo}} | [Modelo de AuthN/AuthZ](../../13-security/authn-authz-model.md) | {{pending: responsable}} | {{pending: estado}} |
| Tecnológico | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo}} | [Gestión de secretos](../../13-security/secret-management.md) | {{pending: responsable}} | {{pending: estado}} |
| Tecnológico | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo}} | [Estándar de codificación segura](../../10-engineering/secure-coding-standard.md) | {{pending: responsable}} | {{pending: estado}} |
| Tecnológico | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo}} | [Copias y recuperación](../../14-delivery/backup-and-recovery.md) | {{pending: responsable}} | {{pending: estado}} |
| Tecnológico | {{pending: ID}} | {{pending: sí / no}} | {{pending: motivo}} | [Estándar de logging](../../10-engineering/logging-standard.md) | {{pending: responsable}} | {{pending: estado}} |

## Estados

planificado, implantado, operando con evidencia, excluido (con motivo).

## Revisión

Revisa el mapeo tras cada cambio de alcance, incidente significativo o nuevo tratamiento de riesgo, y antes de cada auditoría. {{pending: fijar la cadencia de revisión}}

## Relacionados

- [Preparación para ISO 27001](iso-27001-readiness.md)
- [Política del SGSI](isms-policy.md)
- [Solapamiento ISO 27001 y SOC 2](../iso-soc2-overlap-mapping.md)
- [Registro de riesgos](../../13-security/risk-register.md)
