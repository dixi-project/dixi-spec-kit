# Lista 05 — Gestión de datos

> **Regla de evidencia.** Puntúa solo lo que prueba un artefacto. Un artefacto ausente se anota como «sin evidencia» y vale 0; nunca se rellena con un supuesto presentado como hecho.

## Propósito

Evaluar si el proyecto sabe qué datos tiene, dónde, para qué y durante cuánto tiempo; si los datos se modelan, migran y respaldan de forma segura; y si los datos personales se tratan según reglas documentadas.

Estado: borrador. {{pending: confirmar qué almacenes y flujos de datos entran en alcance}}

## Insumos

- [Arquitectura de datos](../../08-data/data-architecture.md) y [Modelo canónico de datos](../../08-data/canonical-data-model.md)
- [Clasificación de PII](../../08-data/pii-classification.md) y [Política de retención](../../08-data/retention-policy.md)
- [Estándar de campos de auditoría](../../08-data/audit-fields-standard.md)
- [Estrategia de migraciones](../../08-data/migrations/migration-strategy.md)
- [Copias y recuperación](../../14-delivery/backup-and-recovery.md)
- [Preparación para el RGPD](../../23-compliance/gdpr/gdpr-readiness.md), si hay datos personales en alcance

## Elementos

| ID | Pregunta | Evidencia (artefacto) | Puntuación 0–5 | Hallazgo |
|----|----------|-----------------------|----------------|----------|
| DAT-01 | ¿Hay un inventario de almacenes de datos, responsables y categorías de datos? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| DAT-02 | ¿Los datos personales y sensibles están clasificados a nivel de campo? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| DAT-03 | ¿Los plazos de retención están definidos y el borrado automatizado? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| DAT-04 | ¿El modelo de datos está documentado y es coherente entre servicios? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| DAT-05 | ¿Las migraciones de esquema están versionadas, revisadas y son reversibles? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| DAT-06 | ¿Los registros son auditables (quién cambió qué y cuándo)? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| DAT-07 | ¿Los datos de producción quedan fuera de los entornos de desarrollo y pruebas? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| DAT-08 | ¿Una solicitud de un interesado (exportación, supresión) se puede atender de principio a fin? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| DAT-09 | ¿Se vigila la calidad de los datos de las entidades críticas? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| DAT-10 | ¿Se conocen y registran las ubicaciones y transferencias de datos? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |

## Señales de alarma

- Nadie sabe enumerar dónde se guardan los datos personales.
- Copias de datos de producción en portátiles o unidades compartidas.
- Borrado prometido a los usuarios pero no implementado.

## Resultado

- Puntuación del área: {{pending: puntuación y método}}
- Hallazgos trasladados al [Informe de DD](../dd-report-template.md).

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Lista 04 — Seguridad](04-security.md)
- [Lista 06 — Procesos](06-processes.md)
- [Lista final](11-final-report.md)
