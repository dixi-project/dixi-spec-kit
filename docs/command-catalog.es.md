# Guía de comandos de DIXI Spec Kit

## Propósito

Mostrar el método como un mapa: por dónde empezar, qué comando usar en cada momento y qué viene después. Cada comando tiene su página en la [referencia de comandos](commands/index.es.md); esta guía te dice cuál abrir.

Los comandos de abajo se ejecutan dentro de tu agente. Aquí aparecen como los escribe Claude Code (`/dixi.specify`); en Codex la misma operación es `$dixi-specify` y en un agente compatible con Agent Skills es la skill `dixi-specify`. Los comandos que empiezan por `dixi ` sin barra, como `dixi check`, se ejecutan en la terminal.

## Recorrido

Una feature recorre este camino, de una idea a una versión que una persona decide publicar:

```text
discover → specify → clarify → plan → tasks → build → verify → review → release
```

1. **Definir.** `/dixi.discover` convierte la idea en visión, actores, alcance y preguntas abiertas. `/dixi.specify` escribe una feature con criterios comprobables desde fuera. `/dixi.clarify` te pregunta lo que sigue ambiguo y registra tus respuestas.
2. **Planear.** `/dixi.plan` escribe el plan técnico de la feature y `/dixi.tasks` lo divide en tareas pequeñas y ordenadas.
3. **Construir.** `/dixi.build` implementa una tarea a la vez: primero las pruebas en rojo, luego el código mínimo que las hace pasar y al final `make verify`.
4. **Comprobar.** `/dixi.verify` reúne la evidencia real de cada criterio y `/dixi.review` prepara la revisión para una persona. Ninguno de los dos aprueba nada.
5. **Publicar.** `/dixi.release` prepara la evidencia, el changelog y el plan de reversión. Tú decides, etiquetas y publicas.

En cualquier momento, `/dixi.status` te dice cómo está el proyecto y cuál es el siguiente paso. Un cambio pequeño no necesita todo el camino: empieza en el paso que corresponda a lo que ya tienes.

Las demás operaciones rodean ese camino. Úsalas cuando la feature las necesite, no por defecto.

### Diseño

Antes del plan o durante él, cuando una feature toca más de una parte del sistema: `/dixi.domain` delimita un dominio y su lenguaje, `/dixi.architecture` compara alternativas y escribe los registros de decisión, `/dixi.contract` especifica una interfaz y sus consumidores, y `/dixi.threat-model` enlaza cada amenaza con una mitigación y una prueba.

### Calidad

`/dixi.checklist` pone a prueba los requisitos de una feature antes de construirla. `/dixi.analyze` busca huecos y contradicciones entre specs y el impacto de un cambio, sin escribir. `/dixi.converge` compara el código con sus specs y añade como tareas lo que falta. `/dixi.risk-review` prepara un informe del riesgo de un pull request o una rama.

### Continuidad

`/dixi.status` y `/dixi.handoff` permiten que una sesión se detenga y otra continúe. `/dixi.change` convierte un cambio solicitado en un análisis con su impacto antes de editar nada. `/dixi.bugfix` lleva un bug del reporte a la corrección con la prueba en rojo commiteada primero. `/dixi.issues` publica las tareas abiertas de una feature como issues de GitHub después de que confirmes una vista previa.

### Preparación y adopción

`/dixi.constitution` escribe los principios del proyecto, que lee cualquier otra operación. `/dixi.interview` llena los huecos `{{pending: …}}` de las plantillas con una pregunta a la vez. `/dixi.onboard` lee una base de código existente y redacta borradores de sus dominios, módulos y features para que los valides.

### Especializadas

Estas solo escriben documentos: nunca ejecutan migraciones, despliegan, cambian `MODE` ni declaran una certificación. `/dixi.data` especifica el modelo de datos y sus migraciones, `/dixi.quality` la estrategia de pruebas, `/dixi.ai` una capacidad de IA y su evaluación, `/dixi.operate` la operación de un servicio, `/dixi.finops` los costos, `/dixi.compliance` las obligaciones de una regulación, `/dixi.duediligence` un informe para un inversionista, un cliente o una auditoría, y `/dixi.promote` comprueba si el proyecto está listo para cambiar `MODE` de `mvp` a `prod`.

## Qué comando usar y cuándo

| Comando | Úsalo cuando | Deja |
|---|---|---|
| [`/dixi.discover`](commands/discover.es.md) | Tienes una idea o una necesidad y nada escrito todavía. | Visión, actores, alcance y preguntas abiertas en `01-business/`. |
| [`/dixi.specify`](commands/specify.es.md) | Sabes qué debe hacer una feature y quieres dejarlo escrito. | `05-features/<slug>/feature-spec.md` con una historia y criterios numerados. |
| [`/dixi.clarify`](commands/clarify.es.md) | Una spec tiene dudas, huecos o dos lecturas posibles. | Tus respuestas registradas en la spec, separadas de los supuestos. |
| [`/dixi.plan`](commands/plan.es.md) | La feature está clara y hay que decidir cómo construirla. | El plan técnico: contratos afectados, decisiones por tomar, riesgos y cómo verificar. |
| [`/dixi.tasks`](commands/tasks.es.md) | El plan está acordado y hay que dividir el trabajo. | `05-features/<slug>/tasks.md` con tareas pequeñas y ordenadas, enlazadas a sus specs. |
| [`/dixi.build`](commands/build.es.md) | Una tarea está lista para implementarse. | Pruebas en rojo, luego el código que las hace pasar y `make verify` en verde. |
| [`/dixi.verify`](commands/verify.es.md) | Las tareas están hechas y quieres la prueba de cada criterio. | Un informe de evidencia por criterio; no cambia ningún archivo. |
| [`/dixi.review`](commands/review.es.md) | El cambio está listo para que lo revise una persona. | Una revisión preparada por riesgo contra una rama base; no aprueba nada. |
| [`/dixi.release`](commands/release.es.md) | Estás por publicar una versión. | `docs/releases/<version>.md` con evidencia, changelog y plan de reversión, para que decidas. |
| [`/dixi.domain`](commands/domain.es.md) | Un objetivo necesita fijar su lenguaje de negocio y sus límites antes de dividirlo. | `03-domains/<slug>/domain-spec.md` y sus módulos, enlazados a objetivos de negocio. |
| [`/dixi.architecture`](commands/architecture.es.md) | Una decisión tiene alternativas con consecuencias distintas. | Registros de decisión en `09-architecture/adr/`, como borradores para que los aceptes. |
| [`/dixi.contract`](commands/contract.es.md) | Dos partes, o tú y un consumidor, deben acordar una interfaz. | `07-contracts/<slug>.md` con entradas, salidas, errores y consumidores. |
| [`/dixi.threat-model`](commands/threat-model.es.md) | La feature maneja datos, permisos o una superficie expuesta. | `13-security/<slug>-threat-model.md` con una mitigación y una prueba por amenaza. |
| [`/dixi.checklist`](commands/checklist.es.md) | Quieres poner a prueba los requisitos antes de construir sobre ellos. | Un checklist en `05-features/<slug>/checklists/` que marca una persona. |
| [`/dixi.analyze`](commands/analyze.es.md) | Sospechas huecos o contradicciones, o necesitas el impacto de un cambio. | Un informe de hallazgos; no escribe nada. |
| [`/dixi.converge`](commands/converge.es.md) | El código y las specs pueden haberse separado. | Una tarea trazada por cada hueco, añadida al `tasks.md` de la feature. |
| [`/dixi.risk-review`](commands/risk-review.es.md) | Un pull request o una rama necesita un informe de riesgo antes de la revisión humana. | Un informe de riesgo por área; no aprueba nada. |
| [`/dixi.status`](commands/status.es.md) | Abres el proyecto y no sabes qué sigue. | Un resumen y un siguiente paso justificado; no cambia ningún archivo. |
| [`/dixi.handoff`](commands/handoff.es.md) | Te detienes y alguien, o una sesión posterior, debe continuar. | `.context/handoff.md` con el estado actual. |
| [`/dixi.change`](commands/change.es.md) | Alguien pide cambiar algo que ya está especificado. | `05-features/<slug>/changes/CHANGE-NNN.md` con el impacto, antes de editar nada. |
| [`/dixi.bugfix`](commands/bugfix.es.md) | Algo que funcionaba se rompió, o nunca coincidió con su spec. | Una prueba en rojo commiteada primero, la corrección y `05-features/<slug>/bugs/BUG-NNN.md`. |
| [`/dixi.issues`](commands/issues.es.md) | El equipo sigue el trabajo en GitHub y las tareas viven en el repositorio. | Issues de GitHub para las tareas abiertas, creados con `gh` tras confirmar una vista previa. |
| [`/dixi.constitution`](commands/constitution.es.md) | El proyecto necesita sus principios por escrito, o cambia uno de ellos. | `00-governance/principles.md`, versionado. |
| [`/dixi.interview`](commands/interview.es.md) | Las plantillas todavía tienen huecos `{{pending: …}}`. | Los huecos llenos con tus respuestas, una pregunta a la vez. |
| [`/dixi.onboard`](commands/onboard.es.md) | Añades DIXI a una base de código que ya existe. | Borradores de dominios, módulos y features con evidencia `file:line`, para que los valides. |
| [`/dixi.data`](commands/data.es.md) | Una feature guarda o mueve datos, sobre todo datos personales. | `08-data/<slug>.md` con modelo, clasificación, retención y plan de migración. |
| [`/dixi.quality`](commands/quality.es.md) | Necesitas decidir cómo se verifica un alcance. | `11-quality/strategy.md` y una matriz de criterio a prueba. |
| [`/dixi.ai`](commands/ai.es.md) | Una feature usa un modelo o un agente. | `21-ai/<slug>.md` con caso de uso, evaluación, datos y costos. |
| [`/dixi.operate`](commands/operate.es.md) | Un servicio está por atender a usuarios reales. | `15-operations/<service>.md` con objetivos, observabilidad y runbooks. |
| [`/dixi.finops`](commands/finops.es.md) | Necesitas una estimación de costos con sus supuestos. | `22-finops/<slug>.md` con fuentes y presupuestos. |
| [`/dixi.compliance`](commands/compliance.es.md) | Un marco o una regulación aplica al proyecto. | `23-compliance/<framework>.md` que relaciona obligaciones con evidencia. |
| [`/dixi.duediligence`](commands/duediligence.es.md) | Un inversionista, un cliente o un auditor pide un informe. | `28-due-diligence/<type>.md` armado con artefactos existentes, con sus huecos. |
| [`/dixi.promote`](commands/promote.es.md) | Consideras pasar el proyecto de `mvp` a `prod`. | `docs/promotion/<date>-prod.md` con la evidencia que falta, para que decidas. |

## Ejemplo completo

Un ejemplo pequeño, de una carpeta vacía a una primera versión: una herramienta de línea de comandos que guarda notas cortas con etiquetas. El repositorio tiene una versión terminada en [`examples/notes`](../examples/notes).

**1. Crea el proyecto.** En la terminal:

```sh
uv tool install dixi-spec-kit
dixi --lang es init notas --agent claude
cd notas
dixi doctor
dixi check
```

`dixi init` crea la base documental e instala los comandos para el agente; con `--lang es`, documentos y mensajes salen en español. `dixi doctor` revisa el entorno y `dixi check` revisa estructura, enlaces y trazabilidad.

**2. Define.** Abre el agente en `notas` y describe la idea:

```text
/dixi.discover una herramienta de línea de comandos para guardar notas cortas con etiquetas
/dixi.specify agregar una nota con etiquetas
/dixi.clarify FEATURE-001
```

El descubrimiento pregunta por usuarios, alcance y límites y escribe lo que respondes. La especificación da a la feature un ID, aquí `FEATURE-001`, y criterios numerados como «una nota sin texto se rechaza». La aclaración pregunta lo que la spec deja abierto, por ejemplo si las etiquetas distinguen mayúsculas; respondes y lo registra.

**3. Planea.**

```text
/dixi.plan FEATURE-001
/dixi.tasks FEATURE-001
```

Lee el plan antes de seguir: es el momento de cambiar el enfoque a bajo costo. Las tareas reciben IDs como `T-001`, cada una enlazada a los criterios que cubre.

**4. Construye, una tarea a la vez.**

```text
/dixi.build T-001
```

El agente escribe primero las pruebas y las muestra en rojo; después escribe el código. Termina con `make verify`. Tú revisas y haces el commit; el agente no firma, no empuja y no integra. Repite con `T-002` y las demás.

**5. Comprueba.**

```text
/dixi.verify FEATURE-001
/dixi.review main
```

La verificación relaciona cada criterio con la prueba que lo cubre y dice cuáles no tienen evidencia. La revisión agrupa el cambio por riesgo para quien lo revisa. Abre el pull request y deja que una persona lo apruebe.

**6. Publica.**

```text
/dixi.release 0.1.0
```

Obtienes la evidencia, una entrada de changelog y un plan de reversión en `docs/releases/0.1.0.md`. Etiquetar y publicar te corresponde a ti.

Cuando una petición posterior cambie el comportamiento, empieza con `/dixi.change`: muestra lo que toca el cambio antes de editar specs o código.

## Relacionado

- [Referencia de comandos](commands/index.es.md)
- [Inicio rápido de recetas (en inglés)](workflow-quickstart.md)
- [Matriz de soporte (en inglés, con resumen en español)](support-matrix.md)
- [Si vienes de GitHub Spec Kit](coming-from-spec-kit.es.md)
- [Catálogo de trabajo con el que se diseñó la v1 (historial, en inglés)](history/command-catalog.md)
- [README](../README.es.md)
