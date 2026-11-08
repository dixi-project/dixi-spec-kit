# Catálogo propuesto de comandos de DIXI Spec Kit

## Propósito

Convertir las capacidades de EIS-IA en operaciones utilizables por terceros: definir, construir, verificar y mantener un producto con trazabilidad. La cobertura se deriva del método Dixi y de recorridos verificables, sin limitarse al catálogo de otra herramienta.

## Estado y alcance

Catálogo de trabajo de TASK-001 y ADR-100. B1 ya implementa `dixi init --agent none`, `dixi doctor`, `dixi check`, ayuda y versión como desarrollo local. Los comandos del agente, actualización y capacidades especializadas siguen propuestos; su presencia aquí no indica que estén instalados. La dirección abierta y el inicio incremental están autorizados.

B2a añade `dixi workflow list`, `show` y `prepare` para las ocho recetas de definición/diseño. Son acceso determinista al método y su contexto; no ejecución asistida de los comandos `/dixi.*`. [Contrato B2a](../07-contracts/commands/workflow-preparation-contract.md) · [Guía](workflow-quickstart.md).

Los nombres `/dixi.*` expresan operaciones compartidas del núcleo; la sintaxis instalable se verifica por adaptador y puede variar entre herramientas. Los comandos `dixi ...` se ejecutan en terminal. La CLI realiza operaciones deterministas; la integración elegida guía decisiones y prepara documentos usando validadores compartidos. El modo sin integración entrega el método, plantillas y guías para uso documental. Codex y Claude Code son candidatos de igual prioridad, sin soporte anunciado hasta verificarlos.

La [revisión conjunta](v1-design-review.md) propone incluir los 16 comandos del recorrido y de diseño/trazabilidad, y priorizar después las nueve entradas especializadas. El [contrato inicial](../07-contracts/commands/command-contract.md) concreta entradas, escrituras, límites y resultados. Esta selección sigue pendiente de validación.

## Base existente y brechas

En la revisión del origen privado se encontraron nueve comandos: `initsdd`, `initproject`, `build`, `risk-review`, `open`, `close`, `mode`, `promote` y `duediligence`. Su existencia no acredita funcionamiento en el producto público ni derechos de distribución.

| Capacidad existente | Tratamiento propuesto |
|---|---|
| `initsdd` | Sustituir la dependencia del repositorio privado por `dixi init` con recursos empaquetados. |
| `initproject` | Adaptar la entrevista a `discover`; hacer accesibles por separado dominios, arquitectura y contratos. |
| `build` | Adaptar TDD, clasificación de riesgo y gates humanos; eliminar dependencia obligatoria del sistema interno de tareas. |
| `risk-review` | Adaptar a `review`, con base Git explícita y sin aprobar ni integrar. |
| `open`, `close` | Adaptar a `status` y `handoff`, con continuidad local y sin push implícito. |
| `mode`, `promote` | Conservar consulta de estado y diseñar promoción supervisada; no confundir promoción de MODE con despliegue. |
| `duediligence` | Adaptar como capacidad especializada, con evidencias y faltantes explícitos. |

Una brecha indica que no hay una entrada pública autónoma verificada para esa operación. Parte de su lógica puede existir dentro de los comandos o guías del origen; se audita antes de crear otra implementación.

## Recorrido principal candidato para v1

`init → discover → specify → plan → tasks → build → verify → review`

`status` orienta el siguiente paso y `handoff` permite retomar el trabajo. `plan` incorpora dominios, arquitectura, contratos y seguridad según el riesgo; esas capacidades también pueden invocarse directamente. Los cambios pequeños siguen el proceso proporcional de EIS-IA, sin exigir todo el recorrido.

| Comando del agente | Resultado observable | Base o brecha |
|---|---|---|
| `/dixi.discover` | Visión, actores, alcance, restricciones y preguntas pendientes del producto. | Adaptar `initproject`. |
| `/dixi.specify` | Historia y feature con reglas, criterios verificables y enlaces a dominio y módulo. | Entrada específica pendiente. |
| `/dixi.clarify` | Respuestas y supuestos incorporados a una spec; dudas bloqueantes identificadas. | Entrada específica pendiente; también usada durante otros pasos. |
| `/dixi.plan` | Plan técnico por bloques, contratos afectados, ADRs, riesgos y ruta de verificación. | Extraer y adaptar planificación del ciclo existente. |
| `/dixi.tasks` | Tareas con criterios, dependencias, nivel de riesgo y enlaces a specs. | Separar generación de tareas de la entrevista y de `build`. |
| `/dixi.build` | Pruebas primero, cambio de código y evidencia de ejecución por tarea. | Adaptar `build`. |
| `/dixi.verify` | Informe de checks ejecutados, fallidos o no ejecutados y cobertura de criterios. | Entrada específica pendiente sobre verificadores del proyecto. |
| `/dixi.review` | Hallazgos por riesgo y contraste criterio → cambio → prueba para revisión humana. | Adaptar `risk-review`. |
| `/dixi.status` | Estado de artefactos, decisiones pendientes y siguiente paso justificado. | Adaptar `open`. |
| `/dixi.handoff` | Contexto local para continuar, evidencias y pendientes, sin declarar cierre sin verificar. | Adaptar `close`. |

## Capacidades propias de Dixi que deben quedar cubiertas en v1

Propuesta: exponer estas operaciones como comandos directos y reutilizarlas desde `plan` o `verify`. La partición final se valida con los contratos para evitar dos caminos que produzcan documentos contradictorios.

| Comando propuesto | Resultado observable | Cuándo se necesita |
|---|---|---|
| `/dixi.domain` | Límites de dominio, lenguaje ubicuo y módulos vinculados a objetivos de negocio. | Discovery o cambio de dominio. |
| `/dixi.architecture` | Diseño, alternativas, consecuencias y ADRs propuestos. | Decisión estructural. |
| `/dixi.contract` | Contratos y schemas enlazados a sus consumidores; impacto de compatibilidad documentado. | Interfaces nuevas o modificadas. |
| `/dixi.threat-model` | Amenazas STRIDE, mitigaciones y pruebas previstas por amenaza. | Disparadores de riesgo de EIS-IA; no es opcional cuando aplica. |
| `/dixi.analyze` | Informe de faltantes y contradicciones entre negocio, dominio, módulo, feature, contrato y prueba. | Antes de construir y al cambiar specs. |
| `/dixi.change` | Propuesta de cambio con impacto en specs, contratos, tareas y pruebas existentes. | Evolución de una funcionalidad; no modifica pruebas congeladas. |

`analyze` interpreta coherencia semántica; `dixi check` comprueba reglas mecánicas. `verify` ejecuta la escalera del proyecto y reúne evidencia. Un informe del agente no sustituye el resultado de esas comprobaciones.

## Capacidades especializadas a delimitar

Se incluyen en el mapa del producto. Su inclusión como comandos independientes en v1 queda pendiente de priorización y pruebas; diferir una interfaz no elimina una norma aplicable.

| Candidato | Resultado y límite |
|---|---|
| `/dixi.data` | Modelo, clasificación de datos, retención y plan de migración; sin ejecutar migraciones en entornos. |
| `/dixi.quality` | Estrategia de pruebas, presupuestos y matriz de verificación, incluyendo i18n y accesibilidad según alcance. |
| `/dixi.ai` | Casos de uso, evaluación, datos, costos y diseño de agentes/MCP según políticas del proyecto; Bedrock sigue vigente en el conjunto Dixi, con portabilidad pública propuesta en ADR-101. |
| `/dixi.release` | Evidencia de preparación y propuesta de release; sin aprobar gates ni desplegar desde el agente. |
| `/dixi.promote` | Revisión de requisitos para MODE=prod y ceremonia supervisada; sin promoción silenciosa. |
| `/dixi.operate` | SLOs, observabilidad, runbooks y preparación de incidentes; sin operar producción desde la laptop. |
| `/dixi.finops` | Estimaciones con supuestos, fuentes y presupuestos; sin inventar consumo o costos reales. |
| `/dixi.compliance` | Mapa de obligaciones y evidencias pendientes; sin declarar certificaciones. |
| `/dixi.duediligence` | Informe sustentado por artefactos y faltantes, para evaluación humana. |

## CLI de soporte

| Comando | Contrato y estado |
|---|---|
| `dixi init` | Disponible con `--agent none` y `--agent claude` (B3): crea documentos y baseline sin sobrescribir. |
| `dixi doctor` | B1 disponible: runtime, recursos, filesystem y metadata local. Diagnóstico de agentes/perfiles pendiente. |
| `dixi check` | B1 disponible: estructura, referencias y grafo declarado según el contrato local. |
| `dixi upgrade --dry-run` | Aplazado a v1.1 (ADR-102). |
| `dixi --help`, `dixi --version` | B1 disponible: capacidades instaladas y versión de desarrollo. |

La CLI no invoca IA ni AWS al instalar o generar proyectos. Los comandos del agente requieren el entorno del agente documentado. No se anuncia operación completa offline por el hecho de empaquetar plantillas locales.

## Contrato obligatorio por comando

Antes de implementar se especifican: objetivo, argumentos, entradas y requisitos previos; archivos leídos y escritos; salidas y estados de error; gates humanos; comportamiento ante repetición, interrupción y cambios locales; siguiente paso; escenarios de aceptación y evidencia esperada. Los supuestos quedan visibles y nunca se presentan como decisiones del usuario.

Se comprueba que los comandos instalados referencien solo recursos distribuidos. Los verificadores deben tener pruebas automatizadas; los comandos del agente requieren además recorridos de evaluación con entradas y criterios controlados, sin exigir igualdad literal del texto generado. Se prueba la falta de información, el conflicto entre specs y la negativa a saltar gates. La sintaxis y el funcionamiento se prueban en el agente anunciado.

## Orden de entrega y aceptación

1. Revisar historia + ADRs + catálogo como un conjunto; fijar comandos incluidos, integraciones elegibles, políticas y matriz de soporte.
2. Crear trazabilidad y contratos por bloques: instalación; definición; diseño; tareas y construcción; verificación y revisión; continuidad y cambios.
3. Por bloque, registrar pruebas en rojo antes de implementar y comprobar los recursos instalados. Resolver derechos antes de incorporar material del origen a la distribución.
4. Completar un ejemplo público desde idea hasta código verificado y revisión humana preparada; repetir con una modificación de contrato para comprobar impacto y gates.
5. Evaluar los comandos especializados y registrar la decisión de inclusión o aplazamiento, sin anunciar los pendientes como disponibles.
6. Validar empaquetado, documentación es/en y condiciones de publicación. La cantidad de comandos por sí sola no acredita utilidad ni calidad.

## Relacionados

- [Producto](product-spec.md)
- [Revisión de diseño](v1-design-review.md)
- [Contrato de comandos](../07-contracts/commands/command-contract.md)
- [Contrato implementado B1](../07-contracts/commands/local-core-contract.md)
- [Historia](../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-100](../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101](../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Plan](../ROADMAP.md)
