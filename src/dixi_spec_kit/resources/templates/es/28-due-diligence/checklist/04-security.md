# Lista 04 — Seguridad

> **Regla de evidencia.** Puntúa solo lo que prueba un artefacto. Un artefacto ausente se anota como «sin evidencia» y vale 0; nunca se rellena con un supuesto presentado como hecho.

## Propósito

Evaluar cómo identifica el proyecto las amenazas, controla el acceso, protege secretos y datos, encuentra y corrige vulnerabilidades y responde a incidentes.

Estado: borrador. {{pending: confirmar si los resultados de pruebas de penetración pueden compartirse en esta revisión}}

## Insumos

- [Modelo de amenazas](../../13-security/threat-model.md) y [Registro de riesgos](../../13-security/risk-register.md)
- [Modelo de AuthN/AuthZ](../../13-security/authn-authz-model.md) y [Acceso de emergencia](../../13-security/break-glass-access.md)
- [Gestión de secretos](../../13-security/secret-management.md)
- [Controles de protección de datos](../../13-security/data-protection-controls.md)
- [Gestión de vulnerabilidades](../../13-security/vulnerability-management.md) y [Plan de pruebas de seguridad](../../11-quality/security-test-plan.md)
- [Respuesta a incidentes](../../13-security/incident-response.md)
- [Seguridad de aplicaciones con LLM](../../13-security/llm-application-security.md), si hay funciones de IA

## Elementos

| ID | Pregunta | Evidencia (artefacto) | Puntuación 0–5 | Hallazgo |
|----|----------|-----------------------|----------------|----------|
| SEC-01 | ¿Hay un modelo de amenazas actual para los flujos principales? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SEC-02 | ¿La autenticación es fuerte, con multifactor para personal y administradores? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SEC-03 | ¿La autorización se aplica en servidor y se prueba, incluido el aislamiento entre clientes si existe? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SEC-04 | ¿Los datos se cifran en tránsito y en reposo, con llaves gestionadas? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SEC-05 | ¿Los secretos están fuera del código y se rotan? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SEC-06 | ¿Las vulnerabilidades se detectan con escaneos y pruebas y se corrigen en plazos definidos? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SEC-07 | ¿Se valida la entrada y se codifica la salida en los límites de confianza? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SEC-08 | ¿Los eventos de seguridad se registran, conservan y generan alertas? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SEC-09 | ¿Hay un proceso de respuesta a incidentes probado, con registros de incidentes pasados? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SEC-10 | ¿Los accesos privilegiados y de emergencia están controlados y revisados? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |

## Señales de alarma

- Vulnerabilidades críticas conocidas abiertas sin plan.
- Cuentas de administración compartidas o acceso a producción sin multifactor.
- Una brecha pasada que no se investigó ni se comunicó como correspondía.

## Resultado

- Puntuación del área: {{pending: puntuación y método}}
- Hallazgos trasladados al [Informe de DD](../dd-report-template.md).

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Lista 03 — Código fuente](03-source-code.md)
- [Lista 05 — Gestión de datos](05-data-management.md)
- [Lista final](11-final-report.md)
