# Esquema de acuerdo de encargo de tratamiento (DPA)

> **Ayuda de trabajo; no es asesoría legal.** Este esquema enumera los temas que suele cubrir un acuerdo de encargo de tratamiento para que el equipo reúna los hechos antes de que la asesoría legal redacte o revise el contrato. No es un contrato y ninguna plantilla certifica conformidad.

## Propósito

Preparar, para cada relación de tratamiento, el anexo de hechos que necesita un DPA: quién trata qué datos, para qué, dónde, con qué salvaguardas y con qué subencargados. La redacción jurídica corresponde a la asesoría legal.

Estado: borrador. {{pending: decidir si el proyecto usa su propio DPA, el del cliente o ambos, y quién aprueba las desviaciones}}

## Partes y roles

| Campo | Valor |
|-------|-------|
| Responsable del tratamiento | {{pending: entidad legal}} |
| Encargado del tratamiento | {{pending: entidad legal}} |
| Contacto para protección de datos | {{pending: rol y dirección, p. ej. privacy@example.com}} |
| Contrato principal al que se anexa | {{pending: referencia}} |

## Anexo: descripción del tratamiento

| Tema | Respuesta | Artefacto de origen |
|------|-----------|---------------------|
| Objeto y duración | {{pending: describir}} | {{pending: enlace}} |
| Naturaleza y finalidad | {{pending: describir}} | {{pending: enlace}} |
| Categorías de interesados | {{pending: p. ej. usuarios finales, empleados del cliente}} | [Clasificación de PII](../08-data/pii-classification.md) |
| Categorías de datos personales | {{pending: enumerar, marcar categorías especiales}} | [Clasificación de PII](../08-data/pii-classification.md) |
| Retención y devolución o borrado al final | {{pending: describir}} | [Política de retención](../08-data/retention-policy.md) |
| Ubicaciones de tratamiento y almacenamiento | {{pending: regiones}} | {{pending: enlace}} |
| Transferencias internacionales y mecanismo usado | {{pending: describir, confirmado por la asesoría}} | {{pending: enlace}} |

## Temas que suele tratar el acuerdo

- Tratamiento solo según instrucciones documentadas del responsable.
- Confidencialidad de las personas autorizadas a tratar los datos.
- Medidas de seguridad técnicas y organizativas: remitir a [Controles de protección de datos](../13-security/data-protection-controls.md).
- Contratación de subencargados, aviso de cambios y derecho de oposición: remitir a [Subencargados](gdpr/sub-processors.md).
- Asistencia con solicitudes de interesados y evaluaciones de impacto.
- Notificación de brechas al responsable sin dilación indebida: remitir a [Respuesta a incidentes](../13-security/incident-response.md).
- Borrado o devolución de los datos al terminar el servicio.
- Derechos de información y auditoría: {{pending: definir la evidencia que el proyecto puede ofrecer}}

## Registro de negociación

| Fecha | Contraparte | Cláusula | Solicitud | Decisión | Aprobado por |
|-------|-------------|----------|-----------|----------|--------------|
| {{pending: fecha}} | {{pending: parte}} | {{pending: cláusula}} | {{pending: solicitud}} | {{pending: decisión}} | {{pending: persona}} |

## Relacionados

- [Panorama de cumplimiento](compliance-overview.md)
- [Subencargados](gdpr/sub-processors.md)
- [Preparación para el RGPD](gdpr/gdpr-readiness.md)
- [Evaluación de riesgo de proveedores](../15-operations/vendor-management/vendor-risk-assessment.md)
