# Referencia de comandos

## Propósito

Una página por operación de DIXI: qué hace, cuándo usarla, qué lee y escribe, dónde se detiene y cómo invocarla desde Claude Code, Codex o un agente compatible con Agent Skills.

Generada por `scripts/build-command-reference.py` a partir del texto empaquetado del comando; no la edites a mano.

## Comandos

- [`/dixi.discover`](discover.es.md) — Descubrir visión, actores, alcance y preguntas abiertas del producto
- [`/dixi.specify`](specify.es.md) — Especificar dominio, módulo y feature con criterios verificables
- [`/dixi.clarify`](clarify.es.md) — Resolver dudas de una spec con preguntas y registrar decisiones y supuestos
- [`/dixi.domain`](domain.es.md) — Diseñar dominios, contextos delimitados y lenguaje ubicuo
- [`/dixi.architecture`](architecture.es.md) — Proponer diseño y decisiones de arquitectura como ADR
- [`/dixi.contract`](contract.es.md) — Definir o cambiar un contrato y su impacto en consumidores
- [`/dixi.threat-model`](threat-model.es.md) — Modelar amenazas STRIDE con mitigaciones y pruebas previstas
- [`/dixi.plan`](plan.es.md) — Planificar contratos, decisiones, riesgos y pruebas de una feature
- [`/dixi.constitution`](constitution.es.md) — Crear o modificar los principios del proyecto (su constitución), versionados
- [`/dixi.checklist`](checklist.es.md) — Escribir checklists de calidad de requisitos de una feature (pruebas unitarias de la spec)
- [`/dixi.converge`](converge.es.md) — Comparar el código con las specs de la feature y añadir tareas de convergencia trazadas
- [`/dixi.tasks`](tasks.es.md) — Dividir un plan en tareas con criterio, dependencias y nivel de riesgo
- [`/dixi.build`](build.es.md) — Construir una tarea con pruebas primero: rojo, verde y verificación
- [`/dixi.verify`](verify.es.md) — Ejecutar la verificación del proyecto y relacionar criterios con pruebas
- [`/dixi.review`](review.es.md) — Preparar la revisión humana de un cambio por riesgo
- [`/dixi.analyze`](analyze.es.md) — Analizar coherencia de la cadena de specs e impacto de un cambio
- [`/dixi.status`](status.es.md) — Mostrar el estado del proyecto y el siguiente paso justificado
- [`/dixi.handoff`](handoff.es.md) — Dejar un traspaso local para retomar el trabajo
- [`/dixi.change`](change.es.md) — Proponer un cambio a una funcionalidad con su impacto
- [`/dixi.data`](data.es.md) — Especificar modelo de datos, clasificación de datos personales, retención y migraciones
- [`/dixi.quality`](quality.es.md) — Definir estrategia de pruebas, presupuestos de calidad y matriz de verificación
- [`/dixi.ai`](ai.es.md) — Diseñar casos de uso de IA, evaluación, datos y agentes según la política de proveedores del proyecto
- [`/dixi.release`](release.es.md) — Preparar evidencia de release, propuesta de changelog y plan de rollback
- [`/dixi.promote`](promote.es.md) — Revisar los requisitos para pasar MODE a prod y listar la evidencia que falta
- [`/dixi.operate`](operate.es.md) — Definir SLOs, observabilidad, runbooks y preparación ante incidentes
- [`/dixi.finops`](finops.es.md) — Estimar costos de nube e IA con supuestos explícitos y presupuestos
- [`/dixi.compliance`](compliance.es.md) — Mapear obligaciones de cumplimiento y la evidencia que falta
- [`/dixi.duediligence`](duediligence.es.md) — Elaborar un informe de due diligence sustentado en artefactos del proyecto, con brechas
- [`/dixi.interview`](interview.es.md) — Rellenar los huecos pendientes del proyecto con una entrevista guiada, una pregunta a la vez
- [`/dixi.risk-review`](risk-review.es.md) — Preparar para una persona un informe de revisión por riesgo de un pull request, rama o diff
- [`/dixi.onboard`](onboard.es.md) — Incorporar un código existente a DIXI: borradores de módulos, features y trazabilidad a partir del código
- [`/dixi.bugfix`](bugfix.es.md) — Corregir un bug con trazabilidad: reproducción, prueba en rojo primero, arreglo mínimo, spec actualizada
- [`/dixi.issues`](issues.es.md) — Convertir las tareas de una feature en issues de GitHub con gh, tras una vista previa que confirma la persona

## Relacionado

- [README](../../README.es.md)
