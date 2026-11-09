# Lista 11 — Consolidación final

> **Regla de evidencia.** La consolidación no añade afirmaciones nuevas: solo reúne puntuaciones y hallazgos ya respaldados por artefactos en las listas 01–10. Los elementos sin puntuar quedan como «sin evidencia».

## Propósito

Comprobar que la revisión está completa y es coherente antes de emitir el [Informe de DD](../dd-report-template.md): todas las áreas puntuadas, cada hallazgo con fuente, señales de alarma explícitas, remediación con responsable y confidencialidad respetada.

Estado: borrador. {{pending: nombrar quién firma la consolidación}}

## Completitud

| Área | Lista | ¿Puntuada? | ¿Evidencia enlazada en cada elemento? | ¿Señales de alarma registradas? |
|------|-------|------------|---------------------------------------|---------------------------------|
| Infraestructura | [01](01-infrastructure.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |
| Arquitectura | [02](02-architecture.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |
| Código fuente | [03](03-source-code.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |
| Seguridad | [04](04-security.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |
| Gestión de datos | [05](05-data-management.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |
| Procesos | [06](06-processes.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |
| Equipo | [07](07-team.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |
| Finanzas | [08](08-financial.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |
| Proveedores y socios | [09](09-vendors-partners.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |
| Innovación | [10](10-innovation.md) | {{pending: sí / no}} | {{pending: sí / no}} | {{pending: sí / ninguna}} |

## Comprobaciones de coherencia

- [ ] Las puntuaciones siguen la escala y el método de agregación de la [Estrategia de DD](../dd-strategy.md).
- [ ] Cada hallazgo tiene gravedad, enlace a evidencia y recomendación.
- [ ] Las contradicciones entre áreas están resueltas o declaradas (p. ej. puntuación de seguridad frente a vulnerabilidades críticas abiertas).
- [ ] Las limitaciones (áreas no revisadas, accesos denegados) están listadas.
- [ ] No aparecen secretos, credenciales ni datos personales en el material.
- [ ] El material compartido fuera coincide con el acuerdo de confidencialidad.

## Traspaso de la remediación

- [ ] Cada hallazgo alto o crítico tiene responsable, fecha y ticket.
- [ ] Los hallazgos relevantes se añaden al [Registro de riesgos](../../13-security/risk-register.md).
- [ ] Se fija una fecha de revisión de seguimiento: {{pending: fecha}}

## Firma

| Rol | Nombre o rol | Fecha | Decisión |
|-----|--------------|-------|----------|
| Responsable de la DD | {{pending: rol}} | {{pending: fecha}} | {{pending: aprobada / cambios solicitados}} |
| Revisor técnico | {{pending: rol}} | {{pending: fecha}} | {{pending: aprobada / cambios solicitados}} |

## Relacionados

- [Plantilla de informe de DD](../dd-report-template.md)
- [Estrategia de DD](../dd-strategy.md)
- [Registro de riesgos](../../13-security/risk-register.md)
