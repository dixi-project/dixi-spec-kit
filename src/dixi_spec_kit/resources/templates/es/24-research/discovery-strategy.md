# Estrategia de descubrimiento

## Propósito

Explicar cómo el proyecto aprende sobre sus usuarios y sus problemas antes de comprometerse a construir, para que las especificaciones se basen en evidencia y no en supuestos, y para que cada mercado e idioma soportado se considere desde el inicio.

Estado: borrador. {{pending: nombrar a la persona responsable del descubrimiento y el tiempo reservado para él}}

## Preguntas por responder

El descubrimiento se guía por preguntas, no por métodos. Empieza por los supuestos más riesgosos.

| Supuesto | Riesgo si es falso | Pregunta | Cómo aprenderemos |
|----------|--------------------|----------|-------------------|
| {{pending: por ejemplo a los usuarios les cuesta comparar ofertas}} | {{pending: alto, medio, bajo}} | {{pending}} | {{pending: entrevistas, analítica, prueba de prototipo}} |
| {{pending}} | {{pending}} | {{pending}} | {{pending}} |

Tipos de supuesto que cubrir:

- **Valor**: ¿la gente lo querrá?
- **Usabilidad**: ¿la gente podrá usarlo?
- **Factibilidad**: ¿podemos construirlo y operarlo?
- **Viabilidad**: ¿funciona para el negocio, en lo legal y en lo financiero?

## Métodos

Elige el método más ligero que responda la pregunta.

| Método | Útil para | Esfuerzo |
|--------|-----------|----------|
| Investigación documental | Contexto, evidencia existente | Bajo |
| Entrevistas | Motivaciones, comportamiento actual, problemas | Medio |
| Encuestas | Tamaño de un problema conocido | Medio |
| Revisión de analítica | Lo que los usuarios hacen en realidad | Bajo a medio |
| Prototipo o prueba de usabilidad | Si una solución funciona | Medio |

## Participantes

- Recluta del público objetivo real, incluido cada idioma y mercado atendido.
- Incluye personas que usan tecnologías de apoyo.
- {{pending: decidir cómo se recluta a los participantes y si reciben compensación}}
- Obtén consentimiento informado y guarda solo los datos personales necesarios.

## Cadencia

{{pending: elegir un ritmo, por ejemplo algunas conversaciones con usuarios cada semana o una fase de descubrimiento por elemento de la hoja de ruta}}

## De los hallazgos a las especificaciones

1. Registra cada estudio y sus hallazgos en las notas de investigación, con fecha y evidencia.
2. Convierte los hallazgos en problemas redactados y actualiza las personas.
3. Usa `/dixi.discover` (o el flujo equivalente) para preparar el contexto de descubrimiento de un objetivo.
4. Enlaza la evidencia desde el objetivo de negocio y las especificaciones que respalda.

## Ética

- Nunca grabes ni compartas datos de participantes sin consentimiento.
- Anonimiza las citas antes de compartirlas fuera del equipo de investigación.
- No presentes una sola conversación como un hallazgo validado.

## Relacionados

- [Plantilla de persona](persona-template.md)
- [Objetivo de negocio](../01-business/vision.md)
- [Propuesta de valor](../01-business/value-proposition.md)
- [Personas](../01-business/actors/personas.md)
- [Guía](../docs/guide.md)
