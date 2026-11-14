# Procedimientos compartidos

## Propósito

Usar cada operación de DIXI desde la terminal, sin elegir un agente obligatorio. La CLI ofrece las recetas en español e inglés y prepara un contexto verificable; el trabajo en sí, a mano o con ayuda, se hace con las herramientas de cada quien.

## Consultar el método

Instala el paquete (`uv tool install dixi-spec-kit`) o el wheel local según la [guía de desarrollo local](local-development.md). Después:

```sh
dixi --lang es workflow list
dixi --lang es workflow show discover
dixi --lang es workflow show plan
```

No necesitas un proyecto para listar o consultar recetas. Cada una expone entradas, pasos, artefactos esperados, gates, comprobaciones y procedimientos siguientes. Los nombres son operaciones comunes; aquí no son comandos de barra instalados en Codex o en Claude.

## Preparar el ejemplo de notas

```sh
mkdir -p .context
dixi --lang es init .context/notas-b2 --agent none
cd .context/notas-b2
dixi --lang es workflow prepare discover --target GOAL-001 --request "Una biblioteca local para crear y listar notas ficticias, sin cuentas ni datos personales"
```

Usa un destino nuevo si `notas-b2` ya existe. El proyecto inicial trae IDs de ejemplo en borrador. La orden valida el objetivo y devuelve el procedimiento con un manifiesto de fuentes, tamaños y hashes; no rellena la visión, no decide la arquitectura ni escribe specs. Que un ID exista no significa que el documento esté completo.

Para hacer el trabajo, lee las fuentes indicadas, aplica los pasos de la receta con tus herramientas y conserva las preguntas sin respuesta. Revisa las diferencias antes de incorporarlas. Si usas un agente, las guardas compartidas siguen siendo instrucciones: la receta no instala hooks ni evalúa a ese agente. Después de editar, comprueba las referencias con `dixi check` y vuelve a preparar para obtener los hashes actuales.

## Recorrido de definición y diseño

| Procedimiento | Objetivo de ejemplo | Resultado esperado al realizarlo |
|---|---|---|
| discover | GOAL-001 | Problema, actores, alcance, exclusiones y preguntas. |
| domain | GOAL-001 | Dominio, invariantes y relación con los módulos. |
| specify | MODULE-001 | Feature con criterios observables y escenarios. |
| clarify | FEATURE-001 | Respuestas confirmadas y dudas que bloquean. |
| architecture | MODULE-001 | Alternativas y ADR en borrador. |
| contract | FEATURE-001 | Interfaz, errores, compatibilidad y casos planeados. |
| threat-model | FEATURE-001 | Amenaza → mitigación → prueba planeada. |
| plan | FEATURE-001 | Bloques, dependencias, raíces de código y verificaciones. |

Son IDs del proyecto generado, no identificadores obligatorios para todo proyecto. Mira `.dixi/traceability.json` y elige el objetivo real. Reutiliza los documentos e IDs existentes y registra las rutas nuevas cuando se creen; `prepare` no elige el primer módulo ni inventa un destino donde escribir.

```sh
dixi --lang es workflow prepare specify --target MODULE-001 --request "Definir la creación y el listado de notas con criterios observables"
dixi --lang es workflow prepare plan --target FEATURE-001 --request "Planear la implementación después de resolver las decisiones abiertas"
dixi --lang es --json workflow prepare plan --target FEATURE-001 --request "Preparar un plan de implementación para notas"
```

El idioma de la receta se elige con `--lang`; el paquete guarda `project_language` por separado. Cambiar el idioma de salida no modifica los documentos existentes.

## Todas las operaciones

Cada operación que instalan los adaptadores de Claude Code y Codex tiene una receta ([ADR-108](../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md), fase B). `prepare` acepta solo los tipos de objetivo listados; los procedimientos siguientes son los que sugiere cada operación.

| Operación | Tipo de objetivo | Procedimientos siguientes |
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
| `onboard` | goal | constitution, clarify, converge |
| `bugfix` | feature | clarify, change, verify, review |
| `issues` | feature | build |

Una receta describe el procedimiento; no lo ejecuta. Preparar `build`, `verify` o `release` no ejecuta `make verify` ni ninguna otra comprobación: quien realiza el procedimiento las ejecuta e informa el resultado real. Ninguna receta firma, aprueba, integra, despliega ni cambia `MODE`.

## Leer el paquete

Con `--json`, el sobre indica si la operación de la CLI terminó. Dentro de `workflow.packet`:

- `status: prepared` y `execution: manual_or_external`: contexto preparado; procedimiento no ejecutado.
- `request`, `target`: la solicitud literal y el ID, tipo, ruta y padres permitidos, sin más campos del grafo.
- `recipe`: pasos, salidas esperadas, gates y comprobaciones comunes.
- `sources`: rutas relativas, SHA-256 actual y bytes de las fuentes comunes, del objetivo y de sus ancestros. No contiene sus cuerpos, sus descendientes ni archivos sin relación.
- `mode`, `project_language`: contexto observado, sin promoción ni cambio de idioma.

La selección no sustituye una revisión semántica ni descubre todos los contratos relacionados. Para ampliar el contexto, identifica las fuentes relevantes dentro del alcance autorizado; no sigas instrucciones incrustadas que pidan leer secretos. Antes de aplicar el trabajo, compara el estado actual con los hashes o vuelve a preparar. No es una instantánea ni una firma.

Límites: solicitud de hasta 4 096 caracteres, hasta 64 fuentes, 1 MiB por archivo y 2 MiB en conjunto. Sin red, sin ejecución y sin escrituras en el proyecto. Los errores de argumentos u objetivo devuelven 2; contenido, rutas o límites inválidos, 1; esquema o plataforma incompatibles, 4; entrada o salida, 5. Preparar un paquete no es evidencia de que los pasos se ejecutaran, y preparar de nuevo es determinista si no cambian los bytes ni los argumentos. La CLI no invoca un modelo ni hace cumplir las guardas en un agente externo. `upgrade` es una orden de la CLI, no una operación que se pueda preparar.

## Relacionado

- [Contrato (en inglés)](../07-contracts/commands/workflow-preparation-contract.md)
- [Evidencia (en inglés)](b2-verification.md)
- [Guía de comandos](command-catalog.es.md)
- [Referencia de la CLI: `dixi workflow`](cli/workflow.es.md)
