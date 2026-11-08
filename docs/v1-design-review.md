# Revisión de diseño de DIXI Spec Kit v1.0.0

## Propósito

Registrar el diseño, el alcance autorizado y las decisiones pendientes. El 2026-11-06 el usuario aceptó avanzar tras aclarar la independencia del agente y del stack. El primer bloque autorizado es CLI/paquete local, `init --agent none`, `doctor`, `check`, ayuda/versión y pruebas primero. La elección anterior del modelo del asistente era contexto; la autorización posterior de implementación es la que habilita B1. No supone confirmar licencia ni toda la matriz futura.

## Propuesta para revisar

Un ecosistema público de desarrollo SDD que acompaña desde la idea hasta una revisión preparada y permite evolucionar el trabajo. El usuario pidió que cada persona pueda elegir agente y lenguajes; esa dirección reemplaza la preferencia anterior por Claude Code. Propuesta de v1: cuatro operaciones CLI (`init`, `doctor`, `check`, `upgrade --dry-run`), ayuda/versión y 16 operaciones compartidas por las integraciones. Nombres y sintaxis de cada adaptador se verifican antes de anunciar disponibilidad.

## Dirección validada

DIXI Spec Kit v1 será un ecosistema SDD con núcleo independiente del agente y del stack, donde cada usuario elige sus herramientas. Las integraciones opcionales operan sobre las mismas especificaciones y conservan garantías comunes de trazabilidad, seguridad, pruebas y revisión humana.

La decisión estructural es separar núcleo, adaptadores, perfiles de stack y conjuntos de políticas. Elegir Python para implementar la CLI no obliga a desarrollar proyectos en Python. Proponer Codex y Claude Code para verificar portabilidad no los convierte en las únicas herramientas admisibles. La libertad de proveedor del conjunto público se concreta en ADR-101; no cambia automáticamente las políticas de desarrollo/publicación de este repositorio.

| Grupo | Comandos propuestos |
|---|---|
| Definir | `discover`, `specify`, `clarify` |
| Diseñar | `domain`, `architecture`, `contract`, `threat-model`, `plan` |
| Construir y comprobar | `tasks`, `build`, `analyze`, `verify`, `review` |
| Evolucionar y retomar | `change`, `status`, `handoff` |

Las capacidades especializadas `data`, `quality`, `ai`, `release`, `promote`, `operate`, `finops`, `compliance` y `duediligence` permanecen en el catálogo. Propongo evaluar sus entradas independientes después del primer recorrido completo; si se quieren todas como requisito de v1, hay que ampliar contratos, escenarios y bloques antes de construir. Los controles aplicables de esas áreas permanecen en el plan y la verificación, cualquiera que sea el número de comandos expuestos.

## Decisiones y evidencia pendiente

| Decisión | Propuesta | Estado y efecto |
|---|---|---|
| Resultado y alcance | Recorrido completo, 16 comandos y cambio posterior con trazabilidad. | Dirección e inicio incremental aceptados; B1 implementado. Los contratos posteriores siguen por concretar. |
| Runtime de la CLI | Python, sin dependencias de ejecución externas; recursos dentro del paquete. | Adoptado en B1; no impone el lenguaje del proyecto. Build local con Setuptools verificado. |
| Integraciones | Núcleo sin agente obligatorio; Codex y Claude Code como candidatos de igual prioridad. | S3 revisado por dirección del usuario; cada adaptador necesita evidencia y matriz de controles. |
| Stack del usuario | Elegible por proyecto, con perfiles opcionales de comprobación. | Evaluar dos lenguajes para detectar acoplamientos; elegir ejemplos antes de implementar ese bloque. |
| Actualización | Solo plan local sin escritura en v1; aplicar cambios queda fuera de esta propuesta. | Concretar S5 al validar; evita prometer una operación aún sin contrato de recuperación. |
| Licencia y derechos | MIT para material con derechos confirmados. | Confirmación humana pendiente por selección; no incorporar material heredado a la distribución ni publicar mientras falte. |
| Compatibilidad | Matriz explícita de Python, sistemas y versiones del agente. | B1 evaluado en macOS/Python 3.15.2, sin agente. Otras combinaciones siguen pendientes. |
| Políticas públicas | Conjunto portable con proveedores elegibles y conjunto Dixi con decisiones organizativas. | Dirección de separación aceptada; mecanismos y excepciones operativas siguen propuestos. B1 no consume IA ni despliega. |
| Infraestructura de este repositorio | Reglas heredadas CodeBuild/CodePipeline, sin credenciales AWS en GitHub Actions. | La apertura del producto no altera su plataforma de build/publicación; aislamiento pendiente antes de ese bloque. |
| Nombre | `dixi-spec-kit` y `dixi`. | Disponibilidad pendiente antes de fijar distribución; no se ha reservado ningún nombre. |

## Trazabilidad preparada

`GOAL-001 → spec-driven-delivery → command-workflow → guided-workflow → command-contract → escenarios WF-01…WF-08`

Hay 20 escenarios BDD y una matriz de aceptación en borrador para el flujo guiado; todavía no tienen runner. B1 añade su propia feature, contrato, threat model, inventario de distribución y pruebas ejecutables. Su [informe](b1-verification.md) distingue esa evidencia de la validación todavía pendiente del recorrido completo.

## Entrega por bloques

Cada bloque puede requerir varios PRs; se respeta el límite de 1 500 líneas de código y las pruebas se registran primero en su propio commit.

| Bloque | Entregable | Evidencia para avanzar |
|---|---|---|
| B0 — Diseño | Historia/ADRs validados, separación del núcleo y políticas, contrato del bloque, threat model y selección distribuible. | Decisiones registradas y escenarios revisables; sin afirmar aceptación del agente. |
| B1 — Instalación | CLI mínima, núcleo, elección explícita de integración o ninguna, ayuda, diagnóstico y comprobaciones estructurales. | Instalación limpia, recursos sin dependencia exclusiva de agente y rechazo seguro de destinos/conflictos. |
| B2 — Definición y diseño | `discover`, `specify`, `clarify`, `domain`, `architecture`, `contract`, `threat-model`, `plan`. | Artefactos del ejemplo enlazados, entradas faltantes visibles y uso común desde plan o comandos directos. |
| B3 — Construcción y revisión | `tasks`, `build`, `analyze`, `verify`, `review`. | TDD y controles reales; gates y evidencia incompleta/desactualizada detectados. |
| B4 — Continuidad y evolución | `change`, `status`, `handoff`, plan de actualización y evaluación de comandos especializados. | Repetición, interrupción, cambios locales, contrato incompatible y dry-run sin escritura. |
| B5 — Distribución | Docs es/en, ejemplos en dos lenguajes, evaluaciones cruzadas de adaptadores, CI, paquete, licencia y protección del repositorio. | Matriz y controles por combinación verificados; condiciones de publicación cumplidas en su fase correspondiente. |

## Resultado de esta revisión

Continuación del 2026-11-07: el usuario pidió seguir tras entregar B1. TASK-002 concreta B2a dentro del núcleo aceptado: consulta y preparación determinista de ocho procedimientos comunes, con pruebas propias. No modifica la decisión de agentes elegibles ni acredita todavía generación/evaluación de artefactos por adaptador.

Registrada la autorización para avanzar con el enfoque abierto y B1; no volver a pedirla. B2 concreta definición/diseño sobre contratos comunes, seguido de adaptadores opcionales y evaluaciones. Licencia/derechos, políticas operativas, alcance final de comandos especializados y matriz de soporte permanecen abiertos. La autorización general de publicar cuando se cumplan las condiciones ya existe; B1 no satisface por sí solo la puerta de publicación.

## Relacionados

- [Historia](../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-100](../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101](../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Contrato de comandos](../07-contracts/commands/command-contract.md)
- [Feature y escenarios](../05-features/guided-workflow/feature-spec.md)
- [Catálogo completo](command-catalog.md)
- [Publicación](publication-readiness.md)
