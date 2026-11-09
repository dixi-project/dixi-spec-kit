# Lista 09 — Proveedores y socios

> **Regla de evidencia.** Puntúa solo lo que prueba un artefacto. Un artefacto ausente se anota como «sin evidencia» y vale 0; nunca se rellena con un supuesto presentado como hecho.

## Propósito

Evaluar la dependencia del proyecto respecto a terceros: qué proveedores y socios son críticos, cómo se evaluaron, qué acuerdos los cubren y qué ocurre si uno falla o desaparece.

Estado: borrador. {{pending: decidir los criterios de criticidad de proveedores}}

## Insumos

- [Catálogo de proveedores](../../15-operations/vendor-management/vendor-catalog.md)
- [Evaluación de riesgo de proveedores](../../15-operations/vendor-management/vendor-risk-assessment.md)
- [Subencargados](../../23-compliance/gdpr/sub-processors.md) y [Plantilla de DPA](../../23-compliance/dpa-template.md)
- [Socios externos](../../01-business/actors/external-partners.md)
- [Contratos externos](../../07-contracts/external/README.md)
- [Política de licencias](../../13-security/licensing/licensing-policy.md)

## Elementos

| ID | Pregunta | Evidencia (artefacto) | Puntuación 0–5 | Hallazgo |
|----|----------|-----------------------|----------------|----------|
| VEN-01 | ¿Hay una lista completa de proveedores con responsable y criticidad? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| VEN-02 | ¿Los proveedores críticos se evaluaron en seguridad y continuidad antes de usarlos? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| VEN-03 | ¿Los acuerdos cubren protección de datos, niveles de servicio y salida? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| VEN-04 | ¿Hay un plan de salida o sustitución para cada proveedor crítico? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| VEN-05 | ¿Los proveedores que reciben datos personales figuran como subencargados? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| VEN-06 | ¿Se vigilan los incidentes y el estado de los proveedores? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| VEN-07 | ¿Las integraciones con socios están documentadas con contratos y manejo de errores? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| VEN-08 | ¿Los contratos son cedibles si la organización cambia de propietario? | {{pending: enlace, confirmado por la asesoría}} | {{pending: puntuación}} | {{pending: hallazgo}} |

## Mapa de concentración

| Capacidad | Categoría de proveedor | ¿Alternativas identificadas? | Esfuerzo de cambio |
|-----------|------------------------|------------------------------|--------------------|
| {{pending: capacidad}} | {{pending: categoría}} | {{pending: sí / no}} | {{pending: bajo / medio / alto, con motivo}} |

## Señales de alarma

- Un servicio crítico sin acuerdo o con condiciones que nadie ha leído.
- Datos personales enviados a un proveedor que no está en la lista de subencargados.

## Resultado

- Puntuación del área: {{pending: puntuación y método}}
- Hallazgos trasladados al [Informe de DD](../dd-report-template.md).

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Playbook de DD de proveedor](../playbooks/vendor-dd-playbook.md)
- [Lista 10 — Innovación](10-innovation.md)
- [Lista final](11-final-report.md)
