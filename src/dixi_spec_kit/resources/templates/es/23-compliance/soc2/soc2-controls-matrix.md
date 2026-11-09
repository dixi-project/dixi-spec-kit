# Matriz de controles SOC 2

> **Ayuda de trabajo; no es asesoría legal.** Esta matriz relaciona los controles propios del proyecto con temas generales de SOC 2. No reproduce el texto de los criterios, no es una auditoría y ninguna plantilla certifica conformidad.

## Propósito

Enumerar cada control que opera el proyecto, el tema SOC 2 al que contribuye, su responsable, cómo se prueba y dónde está su evidencia. Prevalece el mapeo del auditor; esta es la vista de trabajo del equipo.

Estado: borrador. {{pending: confirmar los criterios en alcance según el plan de preparación}}

## Cómo usarla

- Una fila por control que el proyecto realmente opera o planea operar; no copies una lista genérica.
- Referencia solo el identificador del criterio; lee los criterios oficiales del organismo emisor.
- Estados: planificado, diseñado, operando, brecha.

## Matriz

| ID de control | Tema | Control (con palabras del proyecto) | Responsable | Frecuencia | Método de prueba | Ubicación de la evidencia | Estado |
|---------------|------|-------------------------------------|-------------|------------|------------------|---------------------------|--------|
| CTL-01 | Entorno de control | Responsabilidades de seguridad asignadas y aceptadas | {{pending: responsable}} | Anual | Inspeccionar aceptaciones firmadas | {{pending: enlace}} | {{pending: estado}} |
| CTL-02 | Evaluación de riesgos | Riesgos revisados y puntuados según calendario | {{pending: responsable}} | {{pending: frecuencia}} | Inspeccionar el historial del [Registro de riesgos](../../13-security/risk-register.md) | {{pending: enlace}} | {{pending: estado}} |
| CTL-03 | Acceso lógico | Acceso concedido por rol y revisado periódicamente | {{pending: responsable}} | {{pending: frecuencia}} | Muestrear revisiones de acceso | [Modelo de AuthN/AuthZ](../../13-security/authn-authz-model.md) | {{pending: estado}} |
| CTL-04 | Acceso lógico | Acceso retirado a tiempo en las bajas | {{pending: responsable}} | Por evento | Cruzar bajas con logs de acceso | {{pending: enlace}} | {{pending: estado}} |
| CTL-05 | Gestión de cambios | Cambios revisados y probados antes de publicar | {{pending: responsable}} | Por cambio | Muestrear cambios integrados y ejecuciones del pipeline | [Visión general de CI/CD](../../14-delivery/ci-cd-overview.md) | {{pending: estado}} |
| CTL-06 | Operación de sistemas | Vulnerabilidades detectadas y corregidas en plazo | {{pending: responsable}} | {{pending: frecuencia}} | Inspeccionar resultados de escaneo y tickets | [Gestión de vulnerabilidades](../../13-security/vulnerability-management.md) | {{pending: estado}} |
| CTL-07 | Operación de sistemas | Incidentes gestionados y revisados | {{pending: responsable}} | Por incidente | Inspeccionar registros de incidentes | [Respuesta a incidentes](../../13-security/incident-response.md) | {{pending: estado}} |
| CTL-08 | Monitorización | Alertas para eventos relevantes de seguridad | {{pending: responsable}} | Continua | Inspeccionar configuración y muestras de alertas | [Reglas de alertas](../../12-observability/alerting-rules.md) | {{pending: estado}} |
| CTL-09 | Gestión de proveedores | Proveedores críticos evaluados antes de usarlos y revisados | {{pending: responsable}} | {{pending: frecuencia}} | Inspeccionar evaluaciones | [Evaluación de riesgo de proveedores](../../15-operations/vendor-management/vendor-risk-assessment.md) | {{pending: estado}} |
| CTL-10 | Disponibilidad | Copias realizadas y restauraciones probadas | {{pending: responsable}} | {{pending: frecuencia}} | Inspeccionar registros de pruebas de restauración | [Copias y recuperación](../../14-delivery/backup-and-recovery.md) | {{pending: estado}} |
| CTL-11 | Confidencialidad | Datos cifrados en tránsito y en reposo | {{pending: responsable}} | Continua | Inspeccionar configuración | [Controles de protección de datos](../../13-security/data-protection-controls.md) | {{pending: estado}} |
| {{pending: ID}} | {{pending: tema}} | {{pending: control}} | {{pending: responsable}} | {{pending: frecuencia}} | {{pending: método}} | {{pending: enlace}} | {{pending: estado}} |

## Brechas

Cada fila en estado «brecha» recibe un ticket y, si es relevante, una entrada de riesgo. {{pending: enlazar los tickets de brechas}}

## Relacionados

- [Preparación para SOC 2](soc2-readiness.md)
- [Descripción del sistema](system-description.md)
- [Solapamiento ISO 27001 y SOC 2](../iso-soc2-overlap-mapping.md)
- [Registro de riesgos](../../13-security/risk-register.md)
