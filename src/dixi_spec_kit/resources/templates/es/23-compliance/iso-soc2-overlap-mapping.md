# Solapamiento entre ISO/IEC 27001 y SOC 2

> **Ayuda de trabajo; no es asesoría legal.** Esta tabla ayuda a reutilizar un control y una evidencia para ambos marcos. Los solapamientos son aproximados, prevalece el mapeo del evaluador y ninguna plantilla certifica conformidad.

## Propósito

Evitar dos programas en paralelo. Cada control del proyecto se implanta una vez, se relaciona con los controles de referencia de ISO/IEC 27001 y con los temas SOC 2 a los que contribuye, y se evidencia una sola vez.

Estado: borrador. {{pending: decidir qué marco es el programa principal y cuál reutiliza su evidencia}}

## Diferencias clave en términos generales

| Aspecto | ISO/IEC 27001 | SOC 2 |
|---------|---------------|-------|
| Resultado | Certificado de un sistema de gestión | Informe del auditor sobre los controles |
| Enfoque | El SGSI: proceso de riesgos, política, revisión, mejora | Controles relevantes para los criterios en alcance |
| Elección de alcance | Alcance del SGSI definido por la organización | Sistema y criterios elegidos para el informe |
| Ciclo recurrente | Auditorías de seguimiento y recertificación | Nuevo informe por periodo |

## Mapa de controles compartidos

| Control del proyecto | ID ref. ISO/IEC 27001 | Tema SOC 2 | Evidencia compartida | Responsable | Brechas propias de un marco |
|----------------------|-----------------------|------------|----------------------|-------------|-----------------------------|
| Evaluación y tratamiento de riesgos | {{pending: ID}} | Evaluación de riesgos | [Registro de riesgos](../13-security/risk-register.md) | {{pending: responsable}} | {{pending: brecha}} |
| Control de acceso y revisiones | {{pending: ID}} | Acceso lógico | [Modelo de AuthN/AuthZ](../13-security/authn-authz-model.md) | {{pending: responsable}} | {{pending: brecha}} |
| Gestión de cambios | {{pending: ID}} | Gestión de cambios | [Visión general de CI/CD](../14-delivery/ci-cd-overview.md) | {{pending: responsable}} | {{pending: brecha}} |
| Gestión de vulnerabilidades | {{pending: ID}} | Operación de sistemas | [Gestión de vulnerabilidades](../13-security/vulnerability-management.md) | {{pending: responsable}} | {{pending: brecha}} |
| Gestión de incidentes | {{pending: ID}} | Operación de sistemas | [Respuesta a incidentes](../13-security/incident-response.md) | {{pending: responsable}} | {{pending: brecha}} |
| Gestión de proveedores | {{pending: ID}} | Gestión de proveedores | [Evaluación de riesgo de proveedores](../15-operations/vendor-management/vendor-risk-assessment.md) | {{pending: responsable}} | {{pending: brecha}} |
| Copias y continuidad | {{pending: ID}} | Disponibilidad | [Estrategia de DR](../14-delivery/disaster-recovery/dr-strategy.md) | {{pending: responsable}} | {{pending: brecha}} |
| Protección de datos | {{pending: ID}} | Confidencialidad, privacidad | [Controles de protección de datos](../13-security/data-protection-controls.md) | {{pending: responsable}} | {{pending: brecha}} |
| Revisión por la dirección y auditoría interna | {{pending: ID}} | Actividades de seguimiento | {{pending: enlace}} | {{pending: responsable}} | Sobre todo propio de ISO |

## Reglas de trabajo

- Mantener un único repositorio de evidencias con etiquetas para ambos marcos.
- Si un auditor pide otro formato, derivarlo de la misma fuente; no crear una segunda verdad.
- Registrar las brechas propias de un marco en el archivo de preparación de ese marco.

## Relacionados

- [Matriz de controles SOC 2](soc2/soc2-controls-matrix.md)
- [Mapeo de controles ISO 27001](iso-27001/controls-mapping.md)
- [Preparación para SOC 2](soc2/soc2-readiness.md)
- [Preparación para ISO 27001](iso-27001/iso-27001-readiness.md)
- [Panorama de cumplimiento](compliance-overview.md)
