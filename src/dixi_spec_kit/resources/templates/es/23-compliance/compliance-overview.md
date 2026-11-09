# Panorama de cumplimiento

> **Ayuda de trabajo; no es asesoría legal.** Esta plantilla ayuda a organizar trabajo y evidencias. Ninguna plantilla certifica conformidad con una ley o norma; solo la autoridad competente o un evaluador acreditado puede llegar a esa conclusión. Toda decisión legal debe revisarla asesoría cualificada.

## Propósito

Mantener un único mapa de las regulaciones y marcos que pueden aplicar al proyecto: por qué podría aplicar cada uno, si aplica, quién es responsable y dónde están sus evidencias. Este archivo es la entrada al área `23-compliance/`.

Estado: borrador. {{pending: nombrar al responsable de cumplimiento y la cadencia de revisión}}

## Matriz de aplicabilidad

Registra también el «no» con su motivo: una no aplicabilidad documentada también es evidencia.

| Regulación o marco | Disparador habitual | ¿Aplica? | Responsable | Carpeta de evidencias | Próxima revisión |
|--------------------|---------------------|----------|-------------|-----------------------|------------------|
| Ley de protección de datos (p. ej. RGPD) | Datos personales de personas en esa jurisdicción | {{pending: sí / no / por evaluar}} | {{pending: responsable}} | `23-compliance/gdpr/` | {{pending: fecha}} |
| SOC 2 | Clientes empresariales piden un informe independiente de aseguramiento | {{pending: sí / no / por evaluar}} | {{pending: responsable}} | `23-compliance/soc2/` (perfiles app y platform) | {{pending: fecha}} |
| ISO/IEC 27001 | Un mercado o cliente exige un SGSI certificado | {{pending: sí / no / por evaluar}} | {{pending: responsable}} | `23-compliance/iso-27001/` (perfiles app y platform) | {{pending: fecha}} |
| HIPAA | Información de salud tratada para una entidad cubierta | {{pending: sí / no / por evaluar}} | {{pending: responsable}} | `23-compliance/hipaa/` (perfiles app y platform) | {{pending: fecha}} |
| PCI DSS | Se almacenan, procesan o transmiten datos de tarjetas | {{pending: sí / no / por evaluar}} | {{pending: responsable}} | `23-compliance/pci-dss/` (perfiles app y platform) | {{pending: fecha}} |
| Otras normas locales o sectoriales | {{pending: enumerarlas}} | {{pending: sí / no / por evaluar}} | {{pending: responsable}} | {{pending: carpeta}} | {{pending: fecha}} |

## Niveles de preparación

Describe el estado con estos niveles, nunca con «conforme» o «certificado»:

| Nivel | Significado |
|-------|-------------|
| 0 | Sin evaluar |
| 1 | Aplicabilidad decidida y responsable nombrado |
| 2 | Brechas identificadas y registradas como riesgos |
| 3 | Controles diseñados y documentados |
| 4 | Controles operando con evidencia |
| 5 | Revisado por un tercero independiente (anotar quién y cuándo) |

## Piezas compartidas

- Inventario y clasificación de datos: [Clasificación de PII](../08-data/pii-classification.md).
- Retención y borrado: [Política de retención](../08-data/retention-policy.md).
- Controles técnicos y organizativos: [Controles de protección de datos](../13-security/data-protection-controls.md).
- Brechas y riesgos aceptados: [Registro de riesgos](../13-security/risk-register.md).
- Incidentes y notificación de brechas: [Respuesta a incidentes](../13-security/incident-response.md) y [Playbook de brecha de datos](../15-operations/playbooks/data-breach.md).
- Encargados y contratos: [Subencargados](gdpr/sub-processors.md) y [Plantilla de DPA](dpa-template.md).
- Reglas de producto derivadas de obligaciones: [Reglas de cumplimiento](../01-business/rules/compliance-rules.md).

## Reglas de trabajo

- Cada afirmación de esta área remite a un artefacto: especificación, test, log, ticket o documento firmado.
- Lo desconocido queda como `{{pending: …}}`; no se rellena con supuestos.
- Usa `/dixi.compliance` (Claude Code) o `$dixi-compliance` (Codex) para revisar brechas. `dixi check` solo valida estructura, no cumplimiento.

## Relacionados

- [Vigilancia regulatoria](regulatory-watch.md)
- [Preparación para el RGPD](gdpr/gdpr-readiness.md)
- [Plantilla de DPA](dpa-template.md)
- [Registro de riesgos](../13-security/risk-register.md)
- [Proyecto](../00-master-spec.md)
