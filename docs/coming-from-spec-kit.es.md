# Si vienes de Spec Kit

## Propósito

Que una persona que conoce GitHub Spec Kit sea productiva en DIXI Spec Kit: los mismos pasos con los nombres de DIXI, dónde vive cada documento y qué cambia en el trabajo diario. Los datos sobre Spec Kit corresponden a la v1.4.0, leída el 2026-11-11 ([comparación](spec-kit-comparison.md)).

## Instalar y empezar

```sh
uv tool install dixi-spec-kit                       # o: pipx install dixi-spec-kit
dixi --lang es init mi-proyecto --agent claude      # o --agent codex, o --agent none
cd mi-proyecto
dixi doctor && dixi check
```

Añade `--profile site|app|platform` para tener plantillas más completas y `--controls` para que los hooks del agente hagan cumplir las reglas.

## Mapa de comandos

| Spec Kit | DIXI | Qué cambia |
|---|---|---|
| `/speckit.constitution` | `/dixi.constitution` | Escribe `00-governance/principles.md` con versión y registro de cambios; quitar o redefinir un principio requiere un ADR. |
| `/speckit.specify` | `/dixi.discover` y después `/dixi.specify` | `discover` enmarca el objetivo; `specify` escribe la feature bajo un módulo y un dominio. |
| `/speckit.clarify` | `/dixi.clarify` | Las respuestas quedan en la spec; las anteriores se conservan. |
| `/speckit.plan` | `/dixi.plan` | Incorpora `/dixi.domain`, `/dixi.architecture`, `/dixi.contract` y `/dixi.threat-model` cuando el riesgo lo requiere. |
| `/speckit.checklist` | `/dixi.checklist` | `05-features/<slug>/checklists/<domain>.md`; `/dixi.build` se detiene mientras haya puntos abiertos. |
| `/speckit.tasks` | `/dixi.tasks` | `05-features/<slug>/tasks.md` con `T-NNN`, niveles de riesgo y enlaces a los criterios. |
| `/speckit.analyze` | `/dixi.analyze` | Además, `dixi check` para las reglas mecánicas. |
| `/speckit.implement` | `/dixi.build` | Una tarea a la vez: primero las pruebas en rojo, commiteadas, y después el código; `make verify` debe quedar en verde. |
| `/speckit.github.taskstoissues` | `/dixi.issues` | Crea los issues con `gh` después de que confirmes una vista previa; los registra en `05-features/<slug>/issues.md`. |
| `/speckit.converge` | `/dixi.converge` | Añade tareas `## Convergence` de tipo `missing`, `partial`, `contradicts` o `unrequested`. |
| — | `/dixi.verify`, `/dixi.review` | Informan las comprobaciones ejecutadas, fallidas y no ejecutadas; preparan una revisión humana. DIXI nunca aprueba ni integra. |
| — | `/dixi.status`, `/dixi.handoff` | El siguiente paso y un traspaso para retomar entre sesiones. |

## Dónde vive cada cosa

| Spec Kit | DIXI |
|---|---|
| `.specify/memory/constitution.md` | `00-governance/principles.md` |
| `specs/NNN-name/spec.md` | `05-features/<slug>/feature-spec.md`, bajo `04-modules/<module>/` y `03-domains/<domain>/` |
| `specs/NNN-name/plan.md`, `research.md` | El plan junto a la feature; las decisiones como ADR en `09-architecture/adr/` |
| `specs/NNN-name/data-model.md` | `08-data/` (con `/dixi.data`) |
| `specs/NNN-name/contracts/` | `07-contracts/` |
| `specs/NNN-name/tasks.md` | `05-features/<slug>/tasks.md` |
| `specs/NNN-name/checklists/` | `05-features/<slug>/checklists/` |
| — | `.dixi/traceability.json`: la cadena objetivo → dominio → módulo → feature → contrato → prueba que verifica `dixi check` |

## Mover un proyecto existente de Spec Kit

1. En una rama nueva del repositorio, ejecuta `dixi init . --existing`: añade DIXI junto a los archivos existentes, nunca sobrescribe ninguno y lista los que conservó (por ejemplo tu propio `README.md`).
2. Copia los principios de la constitución a `00-governance/principles.md` con `/dixi.constitution`, conservando su significado y dándoles ID.
3. Por cada `specs/NNN-name/`, ejecuta `/dixi.specify` con la spec existente como entrada y coloca la feature bajo su módulo; mueve los contratos y los modelos de datos a `07-contracts/` y `08-data/`.
4. Ejecuta `dixi check` y `/dixi.analyze`, y después `/dixi.converge` por feature para ver qué cubre ya el código.

Nada se convierte de forma automática: una persona revisa cada paso. `/dixi.onboard` redacta borradores de módulos y features a partir de una base de código existente para que los valides, como punto de partida de esos pasos.

## Relacionado

- [Comparación (en inglés)](spec-kit-comparison.md)
- [Inicio rápido de recetas (en inglés)](workflow-quickstart.md)
- [Matriz de soporte (en inglés, con resumen en español)](support-matrix.md)
