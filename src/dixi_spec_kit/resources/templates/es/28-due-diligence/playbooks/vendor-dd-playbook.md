# Playbook de due diligence de proveedor

> **Regla de evidencia.** Evalúa a un proveedor por la evidencia que aporta, no por su marketing. La evidencia ausente se registra como hueco, nunca se sustituye por supuestos presentados como hechos; cada conclusión remite a un artefacto.

## Propósito

Decidir si el proyecto puede depender de un proveedor, con una profundidad proporcional al riesgo: qué datos recibiría, cuán crítico es y qué pasaría si fallara o desapareciera.

Estado: borrador. {{pending: decidir quién aprueba a los proveedores críticos}}

## Niveles

| Nivel | Criterio | Profundidad de la revisión |
|-------|----------|----------------------------|
| Crítico | Recibe datos sensibles o personales, o su caída detiene el producto | Revisión completa, acuerdo revisado por la asesoría, plan de salida |
| Importante | Sostiene un proceso central pero hay alternativa provisional | Cuestionario y revisión de evidencias |
| Bajo | Sin datos, fácil de sustituir | Registro básico en el catálogo de proveedores |

Nivel de este proveedor: {{pending: nivel y motivo}}

## Áreas de revisión

| Área | Qué pedir | Evidencia recibida | Valoración |
|------|-----------|--------------------|------------|
| Seguridad | Informes o certificados independientes con alcance y fecha, resumen de seguridad | {{pending: enlace}} | {{pending: hallazgo}} |
| Protección de datos | Ubicación de los datos, subencargados, DPA | {{pending: enlace}} | {{pending: hallazgo}} |
| Disponibilidad | Niveles de servicio, historial de estado, plan de continuidad | {{pending: enlace}} | {{pending: hallazgo}} |
| Gestión de incidentes | Compromiso de notificación y contacto | {{pending: enlace}} | {{pending: hallazgo}} |
| Continuidad financiera y de negocio | Señales de estabilidad relevantes para la dependencia | {{pending: enlace}} | {{pending: hallazgo}} |
| Salida | Exportación de datos, plazos de preaviso, opciones de sustitución | {{pending: enlace}} | {{pending: hallazgo}} |
| Licencias | Condiciones compatibles con el uso del proyecto | {{pending: enlace}} | {{pending: hallazgo}} |

## Pasos

1. Registrar la necesidad y los datos que recibiría el proveedor.
2. Asignar el nivel y pedir evidencia en consecuencia.
3. Completar la [Evaluación de riesgo de proveedores](../../15-operations/vendor-management/vendor-risk-assessment.md).
4. Si hay datos personales, añadirlo a [Subencargados](../../23-compliance/gdpr/sub-processors.md) y revisar los temas de la [Plantilla de DPA](../../23-compliance/dpa-template.md).
5. Decidir: aprobar, aprobar con condiciones o rechazar; anotar el motivo.
6. Añadir el proveedor al [Catálogo de proveedores](../../15-operations/vendor-management/vendor-catalog.md) con fecha de revisión.

## Decisión

- Resultado: {{pending: aprobar / aprobar con condiciones / rechazar}}
- Condiciones y responsable: {{pending: condiciones}}
- Próxima revisión: {{pending: fecha}}

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Lista 09 — Proveedores y socios](../checklist/09-vendors-partners.md)
- [Evaluación de riesgo de proveedores](../../15-operations/vendor-management/vendor-risk-assessment.md)
