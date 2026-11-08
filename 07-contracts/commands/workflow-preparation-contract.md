# Contrato B2a — Consulta y preparación de procedimientos

## Propósito

Proporcionar una interfaz determinista sobre los ocho procedimientos de definición/diseño. Concreta A01–A08 sin simular ejecución de un agente. No sustituye el contrato de artefactos del recorrido completo.

## Interfaz

```text
dixi [--lang es|en] [--json] workflow list
dixi [--lang es|en] [--json] workflow show <operation>
dixi [--lang es|en] [--json] workflow prepare <operation> --target <id> --request <text>
```

Las opciones globales preceden a `workflow`. `list/show` solo leen recursos empaquetados y funcionan sin proyecto. `prepare` opera desde la raíz inicializada por B1. No hay opción de proveedor ni descarga de extensiones.

| Operación | Tipos de objetivo admitidos |
|---|---|
| discover | goal |
| specify | module |
| clarify | goal, domain, module, feature, contract, test |
| domain | goal, domain |
| architecture | domain, module, feature |
| contract | module, feature |
| threat-model | module, feature |
| plan | feature |

Todos requieren ID exacto y solicitud explícita en `prepare`. Texto vacío, más de 4 096 caracteres, sustitutos Unicode o controles distintos de tab/newline se rechazan con código 2. No se interpola ni ejecuta la solicitud. Los nombres/objetivos desconocidos o incompatibles devuelven 2. Una preparación inválida no devuelve un paquete parcial.

## Resultado

El sobre JSON conserva `status`, `code`, `messages`; añade `workflow` para el resultado específico. `list` devuelve `operations`; `show`, `recipe`; `prepare`, `packet`. `status: completed` solo significa que la operación CLI terminó. El paquete declara `status: prepared`, `execution: manual_or_external`, `schema_version: 1`, `operation`, `request`, `target`, `project_language`, `mode`, `recipe` y `sources`. `target` solo incluye `id`, `kind`, `path`, `parents`: no propaga campos desconocidos del grafo.

Cada receta contiene `id`, `title`, `purpose`, `inputs`, `steps`, `outputs`, `gates`, `checks`, `next_operations` y `target_kinds`, más guardas comunes. La salida legible presenta los mismos datos. Las salidas de la receta son expectativas del trabajo posterior; no archivos creados por `prepare`.

`sources` registra `path`, SHA-256 actual y tamaño en bytes, en orden estable. Incluye `.dixi/project.json`, `.dixi/traceability.json`, `MODE`, `AGENTS.md`, `00-master-spec.md`, objetivo y ancestros declarados; elimina rutas duplicadas. Nunca incluye cuerpos, rutas absolutas, credenciales o un comando de shell generado. El grafo se valida entero; se leen documentos solo de la selección. Un hash identifica los bytes leídos, no firma procedencia ni acredita aprobación.

## Límites y confianza

Reutiliza las lecturas confinadas B1: archivos regulares, sin symlinks, nombres sensibles denegados, hasta 1 MiB por archivo. Máximo 64 fuentes únicas y 2 MiB acumulados; metadata y grafo cuentan dentro del total. MODE debe ser `mvp` o `prod`. Los datos malformados fallan con 1; proyecto ausente 2; esquema/plataforma no soportados 4; E/S 5.

La receta instruye a tratar la solicitud y documentos como datos sin permitirles eliminar gates, ejecutar shell o leer secretos. Estas guardas son instrucciones, no enforcement de un LLM externo. Las políticas de proyecto deben ser revisadas por quien lo use; no se interpretan ni ejecutan desde la CLI. No se siguen enlaces Markdown. No hay snapshot transaccional frente a edición concurrente; comparar hashes antes de usar el paquete.

Las recetas son recursos originales de DIXI Spec Kit, sin dependencia de normas privadas. Proveedor, lenguaje y framework se solicitan/documentan cuando sean pertinentes; no se deducen del agente. Una ausencia se expresa como pregunta/supuesto, nunca como elección del usuario.

## Continuidad y aceptación

Sin escrituras ni timestamps: repetir sobre los mismos bytes y argumentos devuelve el mismo paquete. Un archivo modificado cambia su hash. Interrumpir no deja archivos ni estado del proyecto. No se promueve MODE, aprueba ADR, atesta, firma o integra. Preparar `plan` no ejecuta `build` ni crea pruebas ficticias.

## Relacionados

- [Contrato general](command-contract.md)
- [Feature](../../05-features/workflow-preparation/feature-spec.md)
- [Tarea](../../tasks/backlog/TASK-002-operaciones-compartidas-b2.md)
- [Amenazas](../../13-security/workflow-preparation-threat-model.md)
- [Contrato de lectura B1](local-core-contract.md)
