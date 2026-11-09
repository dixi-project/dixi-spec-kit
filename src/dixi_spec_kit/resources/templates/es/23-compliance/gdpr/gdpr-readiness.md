# Preparación para el RGPD

> **Ayuda de trabajo; no es asesoría legal.** Esta lista organiza el trabajo y las evidencias que suelen esperarse bajo el Reglamento General de Protección de Datos de la UE. No interpreta el reglamento y ninguna plantilla certifica conformidad; confirma las conclusiones con asesoría cualificada.

## Propósito

Mostrar, área por área, qué tiene el proyecto en materia de protección de datos personales, qué falta y dónde está la evidencia. Las brechas se convierten en riesgos o tareas, no en supuestos.

Estado: borrador. {{pending: decidir si el reglamento aplica y anotar el motivo en el panorama de cumplimiento}}

## Roles

- ¿El proyecto es responsable, encargado o ambos, y en qué tratamientos? {{pending: decidir por actividad de tratamiento}}
- ¿Se necesita delegado de protección de datos o representante local? {{pending: decidir con la asesoría}}

## Lista de preparación

La preparación usa los niveles del [Panorama de cumplimiento](../compliance-overview.md).

| Área | Qué se espera (en términos generales) | Nivel | Evidencia | Brecha / ticket |
|------|---------------------------------------|-------|-----------|-----------------|
| Registro de actividades | Inventario de tratamientos, finalidades, datos y destinatarios | {{pending: 0-5}} | [Clasificación de PII](../../08-data/pii-classification.md) | {{pending: brecha}} |
| Base jurídica | Una base documentada para cada finalidad | {{pending: 0-5}} | {{pending: enlace}} | {{pending: brecha}} |
| Transparencia | Aviso de privacidad que coincide con el tratamiento real | {{pending: 0-5}} | {{pending: enlace}} | {{pending: brecha}} |
| Consentimiento | Donde se use: libre, registrado, revocable | {{pending: 0-5}} | {{pending: enlace}} | {{pending: brecha}} |
| Derechos de los interesados | Proceso de acceso, rectificación, supresión, portabilidad, oposición | {{pending: 0-5}} | {{pending: enlace}} | {{pending: brecha}} |
| Minimización y retención | Solo los datos necesarios, durante el tiempo necesario | {{pending: 0-5}} | [Política de retención](../../08-data/retention-policy.md) | {{pending: brecha}} |
| Privacidad desde el diseño | Privacidad revisada en las especificaciones antes de construir | {{pending: 0-5}} | {{pending: enlace}} | {{pending: brecha}} |
| Evaluaciones de impacto | Realizadas para tratamientos de alto riesgo | {{pending: 0-5}} | {{pending: enlace}} | {{pending: brecha}} |
| Seguridad del tratamiento | Medidas adecuadas al riesgo | {{pending: 0-5}} | [Controles de protección de datos](../../13-security/data-protection-controls.md) | {{pending: brecha}} |
| Encargados | Contratos y lista actualizada | {{pending: 0-5}} | [Subencargados](sub-processors.md) | {{pending: brecha}} |
| Transferencias internacionales | Mecanismo identificado para cada transferencia | {{pending: 0-5}} | {{pending: enlace}} | {{pending: brecha}} |
| Gestión de brechas | Detección, evaluación y notificación en el plazo legal | {{pending: 0-5}} | [Playbook de brecha de datos](../../15-operations/playbooks/data-breach.md) | {{pending: brecha}} |

## Preguntas de producto a responder en las especificaciones

- ¿Qué funcionalidades recogen datos personales y es necesario cada campo?
- ¿Puede un usuario exportar y borrar sus datos sin trabajo manual?
- ¿Los logs, la analítica y las copias de seguridad entran en retención y supresión?
- ¿Las funciones de IA envían datos personales a terceros? {{pending: responder por funcionalidad}}

## Relacionados

- [Panorama de cumplimiento](../compliance-overview.md)
- [Subencargados](sub-processors.md)
- [Plantilla de DPA](../dpa-template.md)
- [Registro de riesgos](../../13-security/risk-register.md)
