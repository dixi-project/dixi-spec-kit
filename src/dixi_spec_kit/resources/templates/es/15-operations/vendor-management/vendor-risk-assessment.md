# Evaluación de riesgo de proveedores

## Propósito

Evaluar el riesgo de depender de un proveedor externo antes de contratarlo y de forma periódica, para que la decisión de usarlo sea explícita y sus mitigaciones sean conocidas.

Estado: borrador. {{pending: nombrar al responsable de las evaluaciones de proveedores}}

## Cuándo evaluar

- Antes de que un proveedor nuevo trate datos personales o confidenciales, o soporte un servicio crítico.
- En cada renovación de un proveedor crítico.
- Tras un incidente del proveedor, una adquisición o un cambio importante de términos.

## Dimensiones

Puntúa cada una de 1 (riesgo bajo) a 5 (riesgo alto) y escribe la evidencia detrás de la puntuación.

| # | Dimensión | Preguntas |
|---|-----------|-----------|
| 1 | Criticidad operativa | ¿Qué se detiene si falla? ¿Hay alternativa? |
| 2 | Sensibilidad de los datos | ¿Qué datos recibe? ¿Personales, financieros, de salud? |
| 3 | Postura de seguridad | ¿Qué evidencia independiente ofrece? ¿Cómo gestiona los incidentes? |
| 4 | Privacidad | ¿Acuerdo de tratamiento de datos, subencargados, retención, borrado al salir? |
| 5 | Jurisdicción | ¿Dónde se guardan y procesan los datos? ¿Qué leyes aplican? |
| 6 | Dependencia (lock-in) | ¿Se pueden exportar los datos en formato abierto? ¿Cuánto tardaría una migración? |
| 7 | Solidez financiera y continuidad | ¿Es probable que el proveedor exista y mantenga el producto en dos años? |
| 8 | Concentración | ¿Cuántos servicios críticos dependen ya de este proveedor? |
| 9 | Historial | Incidentes pasados y calidad del soporte con este proyecto |
| 10 | Comportamiento de IA (si aplica) | ¿Entrena con nuestros datos? ¿Se pueden registrar y revisar las salidas? |

## Resultado

| Puntuación total | Nivel | Acción requerida |
|------------------|-------|------------------|
| {{pending: rango}} | Bajo | Registrar y revisar en la renovación |
| {{pending: rango}} | Medio | Mitigaciones documentadas y con responsable |
| {{pending: rango}} | Alto | Aprobación de {{pending: rol}} y un plan de salida antes de usarlo |

## Registro de la evaluación

- Proveedor y servicio: {{pending: nombre}}
- Evaluador y fecha: {{pending: rol, fecha}}
- Puntuaciones y evidencia: {{pending: tabla anterior, completada}}
- Hallazgos y mitigaciones: {{pending: lista con responsables}}
- Decisión: {{pending: aprobar / aprobar con condiciones / rechazar}}
- Próxima revisión: {{pending: fecha}}

No pegues aquí documentos confidenciales del proveedor ni credenciales; enlaza a donde se guardan.

## Relacionados

- [Registro de riesgos](../../13-security/risk-register.md)
- [Controles de protección de datos](../../13-security/data-protection-controls.md)
- [Clasificación de PII](../../08-data/pii-classification.md)
- [Respuesta a incidentes](../../13-security/incident-response.md)
