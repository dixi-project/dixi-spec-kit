# IA responsable

## Propósito

Fijar los principios que rigen cómo usa la IA este proyecto, tanto para construir software como dentro del producto. Son compromisos que se siguen y se comprueban, no certificaciones.

## Principios

### Transparencia

- Declarar cuándo la IA generó o cambió de forma sustancial un artefacto (código, spec, prueba, revisión).
- Etiquetar como tales las revisiones y resúmenes de agentes.
- Avisar a los usuarios del producto cuando interactúan con contenido generado por IA. {{pending: cómo declara el producto el uso de IA}}

### Responsabilidad

- Toda salida de IA tiene una persona responsable.
- Quien aprueba un cambio es dueño de su contenido.
- Las decisiones estructurales siempre son humanas, aunque las proponga un agente.

### Equidad

- Vigilar sesgos en ejemplos, datos de prueba, textos y flujos generados.
- Usar ejemplos sintéticos y variados; no suponer demografías ni capacidades.

### Privacidad

- Nunca poner credenciales ni secretos en los prompts.
- Evitar datos personales en los prompts; preferir datos sintéticos o anonimizados.
- Comprobar que el código generado no filtra datos sensibles en logs o errores.

### Seguridad

- Revisar el código generado en busca de vulnerabilidades como cualquier otro código.
- No depender solo de la IA para lógica crítica de seguridad.
- Impedir acciones destructivas sin confirmación humana.

### Honestidad sobre la evidencia

- Reportar comprobaciones y pruebas tal como se observaron; nunca afirmar una evaluación que no se ejecutó.

## Datos enviados a servicios de IA

| Clase de dato | ¿Permitido en prompts? |
| --- | --- |
| Público | {{pending: sí / no}} |
| Interno | {{pending: sí / no / con condiciones}} |
| Personal o confidencial | {{pending: sí / no / con condiciones}} |

## Preguntas de impacto para features con IA

1. ¿Qué decide o produce la IA, y sobre quién?
2. ¿Qué daño puede causar un error, un sesgo o una manipulación?
3. ¿Qué controles lo mitigan y cómo se prueba cada uno?
4. ¿Cómo interviene una persona o impugna un resultado?

## Relacionados

- [Rastro de auditoría de IA](ai-audit-trail.md)
- [Guardarraíles](../agents/guardrails.md)
- [Humano en el circuito](../agents/human-in-the-loop.md)
- [Instrucciones del proyecto](../../AGENTS.md)
