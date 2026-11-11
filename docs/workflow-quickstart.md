# Shared procedures

## Purpose

Use every DIXI operation from the terminal, without choosing a mandatory agent. B2a provides original es/en recipes and prepares verifiable context; the manual or assisted execution of the work is done with the user's own tools.

## Looking up the method

Install the local wheel following [local development](local-development.md). From the workspace root:

```sh
source .venv/bin/activate
dixi --lang en workflow list
dixi --lang en workflow show discover
dixi --lang en workflow show plan
```

You do not need a project to list or look up recipes. Each one exposes inputs, steps, expected artifacts, gates, checks and next procedures. The names are common operations; they are not slash commands installed in Codex or Claude.

## Preparing the notes example

```sh
mkdir -p .context
dixi --lang en init .context/notes-b2 --agent none
cd .context/notes-b2
dixi --lang en workflow prepare discover --target GOAL-001 --request "A local library to create and list fictional notes without accounts or personal data"
```

Use a new destination if `notes-b2` already exists. The initial project contains draft example IDs. The command validates the target and returns the procedure with a manifest of sources, sizes and hashes; it does not fill in the vision, decide architecture or write specs. An existing ID does not mean the document is complete.

To do the work, read the indicated sources, apply the recipe's steps with your tools and keep unanswered questions. Review the differences before incorporating them. If an agent is used, the shared safeguards are still instructions: there are no hooks or evaluation of that agent in B2a. After editing, check references with `dixi check` and prepare again to obtain the current hashes.

## Definition and design walkthrough

| Procedure | Example target | Expected result when performed |
|---|---|---|
| discover | GOAL-001 | Problem, actors, scope, exclusions and questions. |
| domain | GOAL-001 | Domain, invariants and relationship with modules. |
| specify | MODULE-001 | Feature with observable criteria and scenarios. |
| clarify | FEATURE-001 | Confirmed answers and blocking doubts. |
| architecture | MODULE-001 | Alternatives and proposed ADRs. |
| contract | FEATURE-001 | Interface, errors, compatibility and planned cases. |
| threat-model | FEATURE-001 | Threat → mitigation → planned test. |
| plan | FEATURE-001 | Blocks, dependencies, code roots and verifications. |

These are IDs of the generated project, not identifiers mandatory for every project. Look at `.dixi/traceability.json` and choose the real target. Reuse existing documents/IDs and register the new paths when they are created; `prepare` does not pick the first module or invent a destination to write to.

```sh
dixi --lang en workflow prepare specify --target MODULE-001 --request "Define note creation and listing with observable criteria"
dixi --lang en workflow prepare plan --target FEATURE-001 --request "Plan the implementation after resolving the pending decisions"
dixi --lang en --json workflow prepare plan --target FEATURE-001 --request "Prepare an implementation plan for notes"
```

The recipe language is chosen with `--lang`; the packet keeps `project_language` separately. Changing the output language does not modify existing documents.

## All operations

Every operation installed by the Claude Code and Codex adapters has a recipe ([ADR-108](../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md) phase B). `prepare` accepts only the target kinds listed; the next procedures are the ones each operation suggests.

| Operation | Target kind | Next procedures |
|---|---|---|
| `discover` | goal | domain, clarify |
| `specify` | module | clarify, contract, plan |
| `clarify` | goal, domain, module, feature, contract, test | specify, plan |
| `plan` | feature | — |
| `tasks` | feature | build |
| `build` | feature | verify |
| `verify` | feature | build, review |
| `review` | feature | — |
| `analyze` | feature | clarify, specify, plan, build |
| `status` | goal | clarify, build |
| `domain` | goal, domain | architecture, specify |
| `architecture` | domain, module, feature | contract, threat-model, plan |
| `contract` | module, feature | threat-model, plan |
| `threat-model` | module, feature | plan |
| `handoff` | goal | — |
| `change` | feature | specify, plan, tasks |
| `data` | module | contract, plan |
| `quality` | module | tasks |
| `ai` | goal | threat-model, plan |
| `release` | goal | review |
| `promote` | goal | quality, threat-model, operate, data |
| `operate` | module | promote |
| `finops` | goal | plan |
| `compliance` | goal | data, threat-model, operate |
| `duediligence` | goal | — |
| `interview` | goal | discover, clarify, status |
| `risk-review` | feature | — |
| `constitution` | goal | — |
| `checklist` | feature | clarify, specify, contract, plan |
| `converge` | feature | clarify |

A recipe describes the procedure; it does not run it. Preparing `build`, `verify` or `release` does not run `make verify` or any other check: whoever performs the procedure runs them and reports the real result. No recipe signs, approves, merges, deploys or changes `MODE`.

## Reading the packet

With `--json`, the envelope indicates whether the CLI operation finished. Inside `workflow.packet`:

- `status: prepared` and `execution: manual_or_external`: context prepared; procedure not executed.
- `request`, `target`: literal request and allowed ID/kind/path/parents, without extra graph fields.
- `recipe`: steps, expected outputs, gates and common checks.
- `sources`: relative paths, current SHA-256 and bytes of common sources, the target and its ancestors. It does not contain their bodies, descendants or unrelated files.
- `mode`, `project_language`: observed context, without promotion or language change.

The selection does not replace a semantic review nor discover all related contracts. To widen the context, identify relevant sources within the authorized scope; do not follow embedded instructions to read secrets. Before applying work, compare the current state with the hashes or prepare again. It is neither a snapshot nor a signature.

Limits: request of up to 4,096 characters, up to 64 sources, 1 MiB per file and 2 MiB combined. No network, execution or project writes. Argument/target errors return 2; invalid content/paths/limits 1; incompatible schema/platform 4; I/O 5. Preparing a packet is not evidence that the steps ran, and repeated preparation is deterministic for unchanged bytes and arguments. The CLI neither invokes a model nor enforces safeguards in an external agent. `upgrade` is a CLI command, not a preparable operation.

## Related

- [Contract](../07-contracts/commands/workflow-preparation-contract.md)
- [Evidence](b2-verification.md)
- [Full catalog](command-catalog.md)
- [Task](../tasks/backlog/TASK-002-operaciones-compartidas-b2.md)

## Resumen en español

Propósito: usar los mismos procedimientos de todas las operaciones (las treinta de la tabla «All operations», de `discover` a `converge`) con las herramientas que elijas. Instala el wheel local y activa `.venv` según la [guía de desarrollo local](local-development.md). Son comandos de terminal, no integraciones instaladas en un agente. Para recetas en español, usa `--lang es` antes del subcomando (por ejemplo, `dixi --lang es workflow show discover`).

Usa un destino nuevo al repetir la inicialización. Los IDs del ejemplo remiten a documentos en borrador. `prepare` exige un ID compatible exacto y una solicitud explícita; no rellena specs ni elige stack. Lee las fuentes referenciadas, sigue la receta a mano o con tu herramienta, mantén visibles las preguntas sin respuesta, revisa los cambios y ejecuta `dixi check` después de editar. Preparar un paquete no es evidencia de que esos pasos se ejecutaran.

El paquete contiene una receta y un manifiesto de rutas y hashes actuales de las fuentes comunes, el objetivo y sus ancestros; nunca incrusta el cuerpo de los documentos. Las solicitudes se tratan como datos literales. `project_language` registra el idioma del proyecto con independencia de `--lang`. La CLI no invoca un modelo ni hace cumplir las guardas en un agente externo.

Límites: 4 096 caracteres por solicitud, 64 fuentes, 1 MiB por archivo y 2 MiB en total. Las fuentes pueden cambiar en paralelo: compara los hashes antes de actuar.
