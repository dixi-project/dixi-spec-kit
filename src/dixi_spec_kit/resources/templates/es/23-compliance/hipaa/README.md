# HIPAA

> **Ayuda de trabajo; no es asesoría legal.** Esta página ayuda a decidir si puede aplicar la ley estadounidense HIPAA (Health Insurance Portability and Accountability Act) y qué preparar en ese caso. No interpreta la ley y ninguna plantilla certifica conformidad; la aplicabilidad debe confirmarla una asesoría cualificada.

## Propósito

Registrar si el proyecto trata información de salud protegida (PHI) y con qué rol y, en ese caso, seguir las salvaguardas, acuerdos y evidencias que debe implantar el equipo. Mientras no se decida la aplicabilidad, esta carpeta solo contiene esta página.

Estado: borrador. {{pending: decidir si HIPAA aplica y anotar el motivo en el panorama de cumplimiento}}

## Preguntas de aplicabilidad

| Pregunta | Respuesta | Fuente |
|----------|-----------|--------|
| ¿El producto crea, recibe, almacena o transmite información de salud de personas identificables? | {{pending: respuesta}} | [Clasificación de PII](../../08-data/pii-classification.md) |
| ¿El proyecto es una entidad cubierta o actúa por cuenta de una (socio comercial)? | {{pending: respuesta, confirmada por la asesoría}} | {{pending: enlace}} |
| ¿Los clientes piden un acuerdo de socio comercial (BAA)? | {{pending: respuesta}} | {{pending: enlace}} |
| ¿Los subencargados reciben esa información? | {{pending: respuesta}} | [Subencargados](../gdpr/sub-processors.md) |

Si todas las respuestas son «no», registra la decisión y detente aquí.

## Si aplica: áreas a preparar

Descritas en términos generales; consulta las normas oficiales para los requisitos exactos.

| Área | Qué prepara el proyecto | Evidencia | Brecha / ticket |
|------|-------------------------|-----------|-----------------|
| Análisis de riesgos | Una evaluación documentada de riesgos sobre la información de salud | [Registro de riesgos](../../13-security/risk-register.md) | {{pending: brecha}} |
| Salvaguardas administrativas | Responsable de seguridad, formación, gestión de accesos, plan de contingencia | {{pending: enlace}} | {{pending: brecha}} |
| Salvaguardas físicas | Controles de instalaciones y dispositivos, en parte heredados del alojamiento | {{pending: enlace}} | {{pending: brecha}} |
| Salvaguardas técnicas | Control de acceso, logs de auditoría, integridad, seguridad en la transmisión | [Controles de protección de datos](../../13-security/data-protection-controls.md) | {{pending: brecha}} |
| Acuerdos | Acuerdos de socio comercial con clientes y encargados posteriores | {{pending: enlace}} | {{pending: brecha}} |
| Notificación de brechas | Proceso de evaluación y notificación, con plazos confirmados por la asesoría | [Playbook de brecha de datos](../../15-operations/playbooks/data-breach.md) | {{pending: brecha}} |
| Mínimo necesario | Acceso y divulgación limitados a lo que necesita cada finalidad | {{pending: enlace}} | {{pending: brecha}} |

## Salvaguardas de producto a considerar

- Mantener la información de salud fuera de logs, analítica e informes de errores.
- Restringir qué entornos pueden contener información de salud real.
- Confirmar que las funciones de IA nunca envían información de salud a proveedores sin acuerdo. {{pending: decidir por funcionalidad}}

## Relacionados

- [Panorama de cumplimiento](../compliance-overview.md)
- [Vigilancia regulatoria](../regulatory-watch.md)
- [Controles de protección de datos](../../13-security/data-protection-controls.md)
- [Registro de riesgos](../../13-security/risk-register.md)
