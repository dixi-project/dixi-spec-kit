# Registro de riesgos

## Propósito

Mantener un único lugar donde se registran, puntúan, asignan y revisan los riesgos de seguridad y privacidad, incluidos los que el proyecto decide aceptar. El registro une amenazas con decisiones; no sustituye al modelo de amenazas.

Estado: borrador. {{pending: nombrar al responsable del registro y la cadencia de revisión}}

## Puntuación

Puntúa probabilidad e impacto de 1 (bajo) a 3 (alto). Riesgo = probabilidad × impacto.

| Puntuación | Nivel | Acción esperada |
|------------|-------|-----------------|
| 6–9 | Alto | Tratar antes de publicar o aceptar al nivel de {{pending: decidir quién puede aceptar riesgos altos}} |
| 3–4 | Medio | Planificar el tratamiento con fecha |
| 1–2 | Bajo | Vigilar |

{{pending: confirmar o sustituir esta escala}}

## Opciones de tratamiento

- **Mitigar**: añadir un control; vincularlo a una amenaza y a una verificación.
- **Transferir**: trasladar parte del impacto (contrato, seguro).
- **Evitar**: eliminar la funcionalidad o los datos que generan el riesgo.
- **Aceptar**: registrar quién lo aceptó, por qué y hasta cuándo.

## Registro

| ID | Riesgo | Origen (amenaza, auditoría, incidente) | Probabilidad | Impacto | Puntuación | Tratamiento | Responsable | Fecha de revisión | Estado |
|----|--------|----------------------------------------|--------------|---------|------------|-------------|-------------|-------------------|--------|
| RK-01 | {{pending: descripción}} | {{pending: p. ej. TH-01}} | {{pending: 1-3}} | {{pending: 1-3}} | {{pending: puntuación}} | {{pending: opción}} | {{pending: responsable}} | {{pending: fecha}} | abierto |

## Revisión

- Revisa el registro con una cadencia fija y tras cada incidente relevante o cambio de arquitectura.
- Las aceptaciones caducadas vuelven a «abierto» hasta que se aprueben de nuevo.
- Los riesgos cerrados permanecen en el registro con la fecha y la razón.

## Relacionados

- [Modelo de amenazas](threat-model.md)
- [Controles de protección de datos](data-protection-controls.md)
- [Respuesta a incidentes](incident-response.md)
- [Proyecto](../00-master-spec.md)
