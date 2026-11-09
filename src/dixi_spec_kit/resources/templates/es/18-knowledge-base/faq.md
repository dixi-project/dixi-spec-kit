# Preguntas frecuentes

## Propósito

Responder las preguntas que más hacen las personas nuevas y quienes revisan sobre cómo funciona el proyecto, para que las respuestas sean coherentes y nadie tenga que redescubrirlas. Añade una pregunta cuando se haya hecho dos veces.

Estado: borrador. {{pending: añadir las preguntas propias de este proyecto}}

## Primeros pasos

**¿Por dónde empiezo a leer?**
Por la [spec del proyecto](../00-master-spec.md), el [objetivo de negocio](../01-business/vision.md) y el [flujo documental](../docs/guide.md).

**¿Cómo sé que los documentos son coherentes?**
Ejecuta `dixi check`. Verifica la estructura y los enlaces de trazabilidad; no prueba la aplicación.

**¿Qué ejecuta `make verify`?**
Al principio solo `dixi check`. El proyecto debe conectarle su suite real de pruebas. {{pending: qué ejecuta `make verify` en este proyecto}}

## Specs y pruebas

**¿Puedo escribir código antes de la spec?**
Solo en un experimento desechable que nunca se integra. El código integrado se traza a una spec de funcionalidad.

**Una prueba commiteada parece incorrecta. ¿Puedo arreglarla?**
No directamente. Detente, explica por qué, señala la spec y consulta a la persona responsable. Cambiar una prueba congelada requiere un cambio de spec y aprobación.

**¿Qué significa `{{pending: ...}}`?**
Una decisión abierta. Déjala visible hasta que alguien con autoridad decida.

## Agentes

**¿Qué puede hacer un agente por su cuenta?**
Redactar specs, pruebas y código en una rama y ejecutar verificaciones de solo lectura. Ver [Gobernanza de IA](../00-governance/ai-governance.md).

**¿Puede un agente integrar o desplegar?**
No. Los agentes nunca firman, aprueban, integran ni despliegan.

**¿Qué comandos existen para agentes?**
Las operaciones `/dixi.*` en Claude Code o `$dixi-*` en Codex, cuando esa integración está instalada.

## Revisión y release

**¿Quién aprueba un pull request?**
{{pending: quién aprueba los pull requests}}

**¿Cuándo está «hecha» una funcionalidad?**
Cuando sus criterios tienen pruebas que pasan, `make verify` está en verde y reportado, y una persona la revisó e integró.

## Relacionados

- [Glosario](glossary.md)
- [Guía de incorporación](onboarding-guide.md)
- [Registro de decisiones](decision-log.md)
- [Instrucciones del proyecto](../AGENTS.md)
