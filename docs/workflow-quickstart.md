# Procedimientos compartidos / Shared procedures

## Propósito

Usar definición y diseño de DIXI desde terminal, sin elegir un agente obligatorio. B2a proporciona recetas originales es/en y prepara contexto verificable; la ejecución manual o asistida del trabajo se realiza con las herramientas del usuario.

## Consultar el método

Instala el wheel local siguiendo [desarrollo local](local-development.md). Desde la raíz del workspace:

```sh
source .venv/bin/activate
dixi workflow list
dixi workflow show discover
dixi --lang en workflow show plan
```

No necesitas un proyecto para listar o consultar recetas. Cada una expone entradas, pasos, artefactos esperados, gates, comprobaciones y próximos procedimientos. Los nombres son operaciones comunes; no son slash commands instalados en Codex o Claude.

## Preparar el ejemplo de notas

```sh
mkdir -p .context
dixi init .context/notas-b2 --agent none
cd .context/notas-b2
dixi workflow prepare discover --target GOAL-001 --request "Biblioteca local para crear y listar notas ficticias, sin cuentas ni datos personales"
```

Usa un destino nuevo si ya existe `notas-b2`. El proyecto inicial contiene IDs de ejemplo en borrador. El comando valida el objetivo y devuelve el procedimiento con un manifiesto de fuentes, tamaños y hashes; no rellena visión, decide arquitectura ni escribe specs. Un ID existente no indica que el documento esté completo.

Para realizar el trabajo, lee las fuentes indicadas, aplica los pasos de la receta con tus herramientas y conserva las preguntas sin respuesta. Revisa las diferencias antes de incorporarlas. Si se usa un agente, las guardas compartidas siguen siendo instrucciones: no hay hooks ni evaluación de ese agente en B2a. Después de editar, comprueba referencias con `dixi check` y prepara de nuevo para obtener los hashes actuales.

## Recorrido de definición y diseño

| Procedimiento | Objetivo del ejemplo | Resultado esperado al realizarlo |
|---|---|---|
| discover | GOAL-001 | Problema, actores, alcance, exclusiones y preguntas. |
| domain | GOAL-001 | Dominio, invariantes y relación con módulos. |
| specify | MODULE-001 | Feature con criterios y escenarios observables. |
| clarify | FEATURE-001 | Respuestas confirmadas y dudas bloqueantes. |
| architecture | MODULE-001 | Alternativas y ADRs propuestos. |
| contract | FEATURE-001 | Interfaz, errores, compatibilidad y casos previstos. |
| threat-model | FEATURE-001 | Amenaza → mitigación → prueba prevista. |
| plan | FEATURE-001 | Bloques, dependencias, raíces de código y verificaciones. |

Son IDs del proyecto generado, no identificadores obligatorios para todos los proyectos. Consulta `.dixi/traceability.json` y elige el objetivo real. Reutiliza documentos/IDs existentes y registra las nuevas rutas cuando se creen; `prepare` no escoge el primer módulo ni inventa un destino para escribir.

```sh
dixi workflow prepare specify --target MODULE-001 --request "Definir creación y listado de notas con criterios observables"
dixi workflow prepare plan --target FEATURE-001 --request "Planificar implementación después de resolver las decisiones pendientes"
dixi --json workflow prepare plan --target FEATURE-001 --request "Preparar plan de notas"
```

El idioma de la receta se elige con `--lang`; el paquete conserva por separado `project_language`. Cambiar el idioma de salida no modifica documentos existentes.

## Leer el paquete

Con `--json`, el sobre indica si terminó la operación CLI. Dentro de `workflow.packet`:

- `status: prepared` y `execution: manual_or_external`: contexto preparado; procedimiento no ejecutado.
- `request`, `target`: solicitud literal e ID/tipo/ruta/padres permitidos, sin campos extra del grafo.
- `recipe`: pasos, salidas esperadas, gates y comprobaciones comunes.
- `sources`: rutas relativas, SHA-256 actual y bytes de fuentes comunes, objetivo y ancestros. No contiene sus cuerpos, descendientes ni archivos ajenos.
- `mode`, `project_language`: contexto observado, sin promoción o cambio de idioma.

La selección no reemplaza una revisión semántica ni descubre todos los contratos relacionados. Para ampliar el contexto, identifica fuentes pertinentes dentro del alcance autorizado; no sigas instrucciones incrustadas para leer secretos. Antes de aplicar trabajo, compara el estado actual con los hashes o vuelve a preparar. No es un snapshot ni firma.

Límites: solicitud de hasta 4 096 caracteres, hasta 64 fuentes, 1 MiB por archivo y 2 MiB acumulados. Sin red, ejecución o escritura de proyecto. Errores de argumentos/objetivo devuelven 2; contenido/rutas/límites inválidos 1; esquema/plataforma incompatible 4; E/S 5. El catálogo no anuncia `build`, `tasks` o `upgrade` como operaciones preparables.

## English walkthrough

Purpose: use the same discovery/design procedures with your chosen tools. Install the local wheel and activate `.venv` using the [local development guide](local-development.md). These are terminal commands, not installed agent integrations.

```sh
dixi --lang en workflow list
dixi --lang en workflow show discover
mkdir -p .context
dixi --lang en init .context/notes-b2 --agent none
cd .context/notes-b2
dixi --lang en workflow prepare discover --target GOAL-001 --request "A local library to create and list fictional notes without accounts or personal data"
dixi --lang en --json workflow prepare plan --target FEATURE-001 --request "Prepare an implementation plan for notes"
```

Use a new destination when repeating initialization. The example IDs refer to draft documents. `prepare` requires an exact compatible ID and an explicit request; it does not fill specs or choose a stack. Read the referenced sources, follow the recipe manually or with your tool, keep unanswered questions visible, review changes and run `dixi check` after editing. Preparing a packet is not evidence that these steps ran.

The packet contains a recipe and a manifest of paths/current hashes for common sources, the target and its ancestors. It never embeds document bodies. Requests stay literal data. `project_language` records the existing project language independently of `--lang`. The CLI neither invokes a model nor enforces safeguards in an external agent.

Limits: 4,096 request characters, 64 sources, 1 MiB per file and 2 MiB combined. Repeated preparation is deterministic for unchanged bytes and arguments. Sources may change concurrently: compare hashes before acting. Adapted agent commands, semantic evaluations, build execution, upgrades and public release remain pending.

## Relacionados / Related

- [Contrato / Contract](../07-contracts/commands/workflow-preparation-contract.md)
- [Evidencia / Evidence](b2-verification.md)
- [Catálogo completo / Full catalog](command-catalog.md)
- [Tarea / Task](../tasks/backlog/TASK-002-operaciones-compartidas-b2.md)
