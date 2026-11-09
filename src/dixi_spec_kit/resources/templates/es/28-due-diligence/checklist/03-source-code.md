# Lista 03 — Código fuente

> **Regla de evidencia.** Puntúa solo lo que prueba un artefacto. Un artefacto ausente se anota como «sin evidencia» y vale 0; nunca se rellena con un supuesto presentado como hecho.

## Propósito

Evaluar la calidad, titularidad, capacidad de prueba y limpieza legal del código fuente: quién puede cambiarlo, cómo se comprueban los cambios y si el código de terceros se usa con licencias aceptables.

Estado: borrador. {{pending: enumerar los repositorios en alcance}}

## Insumos

- [Repositorios](../../20-repos/README.md)
- [Estándares de codificación](../../10-engineering/coding-standards.md) y [Estándar de codificación segura](../../10-engineering/secure-coding-standard.md)
- [Estrategia de calidad](../../11-quality/quality-strategy.md) y [Pirámide de tests](../../11-quality/test-pyramid.md)
- [Visión general de CI/CD](../../14-delivery/ci-cd-overview.md)
- [Escaneo de dependencias](../../13-security/dependency-scanning.md)
- [Política de licencias](../../13-security/licensing/licensing-policy.md) y [Licencias aprobadas](../../13-security/licensing/approved-licenses.md)
- [Métricas de ingeniería](../../11-quality/engineering-metrics.md)

## Elementos

| ID | Pregunta | Evidencia (artefacto) | Puntuación 0–5 | Hallazgo |
|----|----------|-----------------------|----------------|----------|
| SRC-01 | ¿Todo el código está en control de versiones y los repositorios pertenecen a la organización? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SRC-02 | ¿Cada cambio pasa revisión y comprobaciones automáticas antes de integrarse? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SRC-03 | ¿Hay tests automáticos en varios niveles, ejecutados en cada cambio? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SRC-04 | ¿Se mide y reporta la cobertura de tests de los caminos críticos? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SRC-05 | ¿Los estándares de codificación se aplican con linters o formateadores? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SRC-06 | ¿Las dependencias están fijadas, escaneadas y se actualizan con calendario? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SRC-07 | ¿Las licencias de terceros están inventariadas y son compatibles con el modelo de negocio? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SRC-08 | ¿El historial está libre de secretos o se rotaron los filtrados? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SRC-09 | ¿Una persona nueva puede compilar y ejecutar el proyecto con la documentación? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| SRC-10 | ¿Los acuerdos de contribución o contratos laborales ceden la propiedad intelectual a la organización? | {{pending: enlace, confirmado por la asesoría}} | {{pending: puntuación}} | {{pending: hallazgo}} |

## Señales de alarma

- Código en cuentas personales o sin titularidad clara.
- Código copyleft en un producto distribuido sin decisión registrada.
- Secretos en el historial que nunca se rotaron.

## Resultado

- Puntuación del área: {{pending: puntuación y método}}
- Hallazgos trasladados al [Informe de DD](../dd-report-template.md).

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Lista 02 — Arquitectura](02-architecture.md)
- [Lista 04 — Seguridad](04-security.md)
- [Lista final](11-final-report.md)
