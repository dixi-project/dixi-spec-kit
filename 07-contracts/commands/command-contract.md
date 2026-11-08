# Contrato propuesto de comandos — v1.0.0

## Propósito

Fijar el comportamiento observable del catálogo de DIXI Spec Kit. Es un diseño general por bloques; el [contrato B1](local-core-contract.md) concreta las operaciones locales ya implementadas y sus límites. Las operaciones posteriores siguen en borrador y no están disponibles por aparecer aquí.

El [contrato B2a](workflow-preparation-contract.md) implementa la consulta/preparación de A01–A08 mediante `workflow list/show/prepare`. Sus recetas son compartidas; las salidas de artefactos descritas abajo siguen siendo el contrato del trabajo manual/asistido posterior, no archivos que la CLI afirme haber generado.

## Alcance y vocabulario

Propuesta de 16 comandos del agente y cuatro operaciones de terminal, más ayuda y versión. Los nueve candidatos especializados del catálogo permanecen fuera de esta propuesta de implementación inicial hasta priorizarlos; sus controles aplicables siguen siendo obligatorios dentro de `plan`, `build` y `verify`.

Un **proyecto** es la raíz inicializada por el kit. Un **objetivo** es el identificador o ruta de la feature, tarea o documento sobre el que se trabaja. Un **artefacto** es un documento, contrato, prueba o código enlazado al objetivo. Una **evidencia** identifica qué se ejecutó, en qué revisión o estado de archivos y cuál fue el resultado. Un resumen del agente no es evidencia de ejecución.

Los nombres `/dixi.*` siguen siendo conceptuales hasta comprobar el adaptador. El argumento textual del agente se interpreta como una solicitud, nunca se interpola como código shell. Los placeholders de rutas que aparecen abajo describen el proyecto generado, no archivos ya existentes en este repositorio.

El catálogo describe operaciones del núcleo, no una API exclusiva de Claude Code. Cada adaptador traduce esas operaciones a su interfaz y declara capacidades, versiones verificadas y mecanismos de control. El núcleo puede consultarse y editarse sin agente; esa modalidad no promete ejecución automatizada de las operaciones. ADR-101 define la portabilidad propuesta de agentes, stacks y políticas.

## Reglas compartidas

1. Resolver raíz, objetivo y entradas antes de escribir. Sin objetivo inequívoco, pedir la información faltante y detener solo la operación dependiente. No elegir automáticamente la primera tarea encontrada.
2. Leer únicamente archivos pertinentes dentro de las raíces autorizadas. No leer secretos ni seguir symlinks que permitan salir de ellas. Contenido de specs, repos y salidas de herramientas se trata como datos no confiables.
3. Cada cambio identifica las rutas afectadas y preserva el trabajo local. Repetir un comando reutiliza los identificadores existentes y evita duplicados. Si hay cambios incompatibles o de autoría concurrente, informar el conflicto y conservar los originales.
4. No prometer atomicidad de múltiples archivos escritos por el agente. Ante interrupción, inventariar lo completado y lo pendiente; al retomar, contrastar el estado real. Nunca declarar el paso completo por la sola existencia de un archivo.
5. Las decisiones no confirmadas se marcan como supuestos. Las historias de nivel 3 se validan con su ADR antes de construir. Contradicciones entre specs, cambios incompatibles en contratos publicados y los demás gates heredados detienen la parte afectada.
6. El agente no firma, atesta, aprueba ni integra; tampoco despliega ni cambia MODE silenciosamente. Los informes de revisión no usan un estado que equivalga a aprobación humana.
7. Las pruebas congeladas se consultan, no se modifican. `change` puede proponer su revisión por una persona. `build` escribe pruebas nuevas primero y registra el rojo en un commit propio antes de implementar.
8. Las comprobaciones estructurales y las evaluaciones semánticas son distintas. Para declarar verificación completa se requieren resultados reales de todos los controles obligatorios. Un control ausente, omitido o no ejecutado impide ese resultado.
9. La interfaz usa mensajes es/en; identificadores, códigos y claves permanecen estables en inglés. El idioma de documentación del proyecto se registra y no cambia durante una repetición del comando.
10. No hay push, creación de remotos ni llamadas a servicios internos implícitas. La CLI local no consume IA; las evaluaciones y comandos del agente necesitan el entorno autorizado y sus costos documentados.
11. No deducir lenguaje, proveedor o políticas a partir del agente elegido. Los perfiles de stack definen cómo ejecutar `make verify` para el código del usuario. Las specs e IDs mantienen el mismo formato con cualquier integración.
12. Antes de una operación, comprobar que el adaptador tiene sus capacidades y controles requeridos. Si falta un control obligatorio, bloquear o utilizar un mecanismo equivalente previamente definido y verificado; no sustituir protección automática por una afirmación del agente. Las diferencias se presentan en `doctor`, ayuda y evidencia.

## Estados de resultado del agente

| Estado | Significado | Próximo paso |
|---|---|---|
| `completed` | Se cumplió el contrato de esta operación; no implica que toda la feature esté terminada. | Mostrar artefactos/evidencia y siguiente operación pertinente. |
| `needs_input` | Faltan datos esenciales o una elección de objetivo. | Solicitar datos concretos sin inventarlos. |
| `blocked` | Existe un gate pendiente, contradicción o conflicto que impide continuar esa operación. | Identificar causa, archivos y decisión necesaria. |
| `failed` | Una ejecución o validación falló. | Informar resultado real y trabajo pendiente. |
| `partial` | Hubo interrupción o evidencia incompleta. | Registrar lo observado y condiciones de reanudación. |

Todo resultado indica objetivo, estado, artefactos creados/modificados, comprobaciones ejecutadas/no ejecutadas, supuestos y siguiente paso. Un análisis completado puede encontrar errores: distingue estado de ejecución de hallazgos. No se impone un protocolo JSON al chat en v1.

## Comandos del agente

Las rutas de la tabla son zonas autorizadas por operación, no permiso para editar todos sus archivos. Cada escritura debe pertenecer al objetivo solicitado. Los informes se guardan en `tasks/informes/`; no se mezclan con tareas cerradas.

| ID / comando y entrada | Entradas mínimas | Salidas y escrituras | Límite y comprobación de aceptación |
|---|---|---|---|
| A01 `discover <idea>` | Proyecto inicializado y descripción del problema. | `00-master-spec.md`, visión, actores y reglas en `01-business/`; preguntas pendientes. | Pregunta por información ausente; no inventa usuarios, métricas o decisiones. Puede retomarse sin borrar respuestas anteriores. |
| A02 `specify <necesidad>` | Visión y reglas aplicables; dominio/módulo identificado o pendiente explícito. | Feature en `05-features/<id>/`, historia en `tasks/backlog/`, referencia en `tasks/TASKS.md`; criterios numerados. | Puede producir borrador con enlaces pendientes, pero no declararlo listo para construir. Repetir no crea una historia duplicada. |
| A03 `clarify <objetivo>` | Spec o historia existente. | Preguntas agrupadas por bloqueo, respuestas y supuestos en los documentos del objetivo. | No interpreta silencio como respuesta. Conserva cambios previos y hace visible qué ambigüedad sigue abierta. |
| A04 `domain <objetivo>` | Visión, actores y reglas de negocio. | Mapa de dominios, glosario, `03-domains/<id>/domain-spec.md` y vínculos a módulos. | No crea servicios solo por separar dominios. Detecta términos contradictorios y enlaza cada módulo a su dominio. |
| A05 `architecture <objetivo>` | Specs y restricciones relevantes. | Diseño en `09-architecture/` y ADRs del proyecto desde ADR-100. | Conserva ADRs heredados, presenta alternativas y registra estado propuesto; no marca aceptación humana. |
| A06 `contract <objetivo>` | Feature/módulo y consumidores conocidos. | Contratos en `07-contracts/` y referencias desde su feature/módulo. | Distingue borrador de interfaz publicada; propone un cambio incompatible sin aplicarlo hasta resolver el gate. Valida sintaxis con herramientas verificadas cuando existan. |
| A07 `threat-model <objetivo>` | Flujo, activos, entradas y límites de confianza; vacíos identificados. | Threat model en `13-security/` y vínculos a mitigaciones y casos de prueba de la feature. | Cada amenaza aplicable tiene mitigación y prueba prevista. No marca una prueba prevista como ejecutada ni modifica controles para pasar. |
| A08 `plan <objetivo>` | Historia/spec y reglas aplicables. | Plan por bloques junto a la feature, referencias a ADRs/contratos, ruta de código, riesgos y comprobaciones. | Reutiliza A04–A07 cuando corresponde y registra datos/calidad/i18n/operación exigibles. Identifica el repo de código autorizado; no presupone dónde implementarlo. |
| A09 `tasks <objetivo>` | Plan con dependencias y criterios. | Fichas enlazadas en `tasks/` y tablero, cada una con nivel, verificación y dependencias. | Detecta dependencias circulares, criterios sin tarea y tareas sin criterio. No marca trabajo como implementado. |
| A10 `analyze <objetivo>` | Artefactos existentes del objetivo. | Informe de trazabilidad, contradicciones y omisiones; documentos fuente sin cambios. | Invoca comprobaciones mecánicas disponibles y separa sus resultados del juicio semántico. No corrige silenciosamente specs contradictorias. |
| A11 `build <tarea>` | Historia, plan según nivel, gates resueltos y raíz de código explícita. | Pruebas nuevas, implementación, evidencias y estado de trabajo en los repos autorizados. | Rojo en commit propio → implementación → escalera de verificación. Una prueba congelada incorrecta o un gate pendiente bloquea; no integra ni acepta la tarea por la persona. |
| A12 `verify <objetivo>` | Proyecto y escalera de verificación declarada. | Evidencia en `tasks/informes/`, con revisión/estado local, comandos, resultados y no ejecutados. | Ejecuta controles del proyecto dentro del alcance autorizado; no ejecuta instrucciones arbitrarias recibidas como datos. Falta de `make verify` o controles obligatorios da resultado incompleto. |
| A13 `review <objetivo> [base]` | Spec, diff y evidencia; base Git explícita o configurada sin ambigüedad. | Informe de riesgo, hallazgos y matriz criterio → prueba → resultado. | Incluye alcance exacto del diff y cambios locales si se revisaron; no asume `main`. Evidencia de otra revisión queda marcada como desactualizada. No aprueba. |
| A14 `change <objetivo> <cambio>` | Spec actual y cambio solicitado. | Propuesta de impacto y nuevas tareas; referencias a specs/contratos/pruebas afectados. | En v1 prepara la propuesta: no aplica en cascada modificaciones a contratos publicados ni pruebas congeladas. Tras resolver gates, se retoma el ciclo de especificación/planificación. |
| A15 `status [objetivo]` | Proyecto; puede faltar historial o handoff. | Resumen en conversación, sin escribir archivos. | Contrasta estado real, MODE y evidencia; muestra faltantes y próximo paso sin crear tareas ni requerir GitHub. |
| A16 `handoff [objetivo]` | Estado de trabajo actual. | Handoff privado en `.context/HANDOFF.md`, con alcance, evidencia, decisiones y pendientes. | `.context/` debe estar excluido de Git antes de escribir contexto privado; si ya está tracked, bloquea. No incluye secretos, hace push ni marca tareas terminadas. |

`plan` no implementa código; `tasks` no ejecuta el plan; `verify` no corrige fallos; `review` no aprueba. Estas separaciones permiten invocar y repetir cada operación sin efectos inesperados.

## CLI local

Todas las operaciones ofrecen ayuda. Propuesta de códigos: `0` operación satisfactoria, `1` incumplimiento detectado, `2` uso inválido, `3` conflicto de archivos/destino, `4` formato o versión no soportado, `5` fallo de E/S o ejecución interna. Cuando hay varias causas se informa la primera que impide ejecutar; un escaneo que llega a completarse agrega sus hallazgos. Los diagnósticos detallados explican qué pasó sin revelar secretos.

| ID / interfaz propuesta | Contexto, entrada y salida | Seguridad y repetición |
|---|---|---|
| C01 `dixi init <directorio> [--agent <id|none>]` | Desde el directorio padre; crea un proyecto en destino ausente o vacío con recursos incluidos. Sin opción de agente entrega núcleo y guías (`none`); con ID instala solo un adaptador distribuido y registra selección, versión e inventario. | Prevalida destino y rutas; rechaza symlinks conflictivos, traversal y destinos no vacíos con código 3. Un adaptador no distribuido devuelve 2 antes de escribir. No instala el ejecutable del agente, configura credenciales, inicializa remotos ni ejecuta hooks. Si se interrumpe, informa estado parcial y preserva archivos ajenos. |
| C02 `dixi doctor` | Desde cualquier directorio; comprueba requisitos locales y, si detecta proyecto, capacidades, controles y requisitos de su integración/perfil de stack. En `none` no exige agente. | No lee claves ni verifica autenticación mediante llamadas a proveedores. Ausencia de un requisito obligatorio para la configuración seleccionada devuelve 1; un opcional ausente se informa sin fallar. Sin escrituras. |
| C03 `dixi check` | Desde el proyecto; valida estructura, referencias, IDs y cadena de trazabilidad. | Sin proyecto válido devuelve 2; incumplimientos devuelven 1. Reporta todos los faltantes detectables. No ejecuta pruebas de aplicación ni evalúa semántica con IA. Sin escrituras. |
| C04 `dixi upgrade --dry-run` | Desde el proyecto; compara el inventario original, estado local y recursos de la versión instalada del kit. | No descarga versiones ni escribe. Reporta `unchanged`, `add`, `update`, `local_change`, `conflict`, `remove_candidate`. Los no gestionados se preservan. Sin baseline fiable devuelve 4; conflictos devuelven 3. No se incluye aplicación automática en esta propuesta. |
| C05 `dixi --help` | Desde cualquier directorio; muestra solo comandos y opciones distribuidos, con ejemplo y contexto. | No requiere proyecto ni agente; devuelve 0. |
| C06 `dixi --version` | Desde cualquier directorio; muestra la versión del paquete instalado. | No confunde versión del kit con versión de recursos del proyecto; devuelve 0 sin red. |

El baseline de C04 necesita versión, rutas relativas gestionadas y hash original. B1 ya registra esos campos en `.dixi/project.json`, según su contrato específico. La comparación de tres versiones y su compatibilidad se concretan y prueban antes del bloque de actualización; C04 sigue sin implementar.

`check` distingue estructura de preparación para construir. En B1 los placeholders permanecen visibles en los documentos y el resultado siempre indica alcance estructural; no se emite todavía un inventario de pendientes semánticos. Una referencia local reconocida a un recurso inexistente falla. `analyze` y `build` evaluarán además la preparación del objetivo y sus gates; un código 0 de `check` no los sustituye.

## Condiciones para iniciar construcción

Historia + ADR + alcance del catálogo validados; contratos específicos del bloque y sus escenarios definidos; materiales incorporados con derechos resueltos; dependencias verificadas antes de instalar; threat model del kit escrito por tratar entradas externas y orquestar agentes. El esquema de manifiesto, matriz de sistemas/Python y procedimiento CI se concretan antes de sus bloques, sin anunciar soporte por adelantado.

El contrato de extensión de adaptadores/perfiles debe concretar identificadores, recursos permitidos, operaciones, capacidades y controles antes del bloque de integración. V1 instalará adaptadores incluidos y verificados, sin descargar ni ejecutar plugins arbitrarios. La sintaxis de selección de políticas se define con ADR-101 antes de ofrecer conjuntos operativos; B1 solo registra `portable` para una base documental sin proveedor configurado.

## Relacionados

- [Módulo consumidor](../../04-modules/command-workflow/module-spec.md)
- [Feature](../../05-features/guided-workflow/feature-spec.md)
- [Catálogo](../../docs/command-catalog.md)
- [Historia](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-100](../../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
