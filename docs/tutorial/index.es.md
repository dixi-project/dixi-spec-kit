# Empieza aquí: tu primera feature

## Propósito

Llevar una feature pequeña desde una carpeta vacía hasta un build verificado, un paso por página, para que aprendas el orden de los pasos de DIXI haciéndolos. Cada paso dice qué haces, qué deberías ver y qué viene después, y enlaza la referencia de cada comando que usa.

## Qué vas a construir

Una herramienta de línea de comandos que guarda notas cortas con etiquetas, el mismo ejemplo de la [guía de comandos](../command-catalog.es.md). El repositorio tiene una versión terminada en [`examples/notes`](../../examples/notes): ábrela cuando quieras comparar tu resultado.

## Antes de empezar

- Python 3.11 o superior, en macOS o Linux. En Windows, usa WSL 2 con el proyecto bajo `~` ([matriz de soporte](../support-matrix.md)).
- Uno de los agentes que DIXI soporta, o ninguno: los comandos se muestran para Claude Code, y cada paso dice cómo ejecutarlos con los demás adaptadores.
- Git, para hacer commit de tu trabajo. El agente nunca firma, empuja ni integra por ti.

| Adaptador | Agente | Cómo se ejecuta una operación |
|---|---|---|
| `--agent claude` | Claude Code | `/dixi.specify añadir una nota con etiquetas` |
| `--agent codex` | Codex CLI | `$dixi-specify añadir una nota con etiquetas` |
| `--agent skills` | OpenCode, y otros agentes que leen Agent Skills (no verificados) | `@dixi-specify añadir una nota con etiquetas` |
| `--agent none` | Cualquier agente o editor | `dixi workflow prepare` imprime el procedimiento y tú se lo das a tu agente |

## Pasos

1. [Instalar el kit](01-install.es.md): instalar `dixi` y comprobar su versión.
2. [Crear el proyecto](02-init.es.md): la base documental y los comandos del agente.
3. [Especificar la feature](03-specify.es.md): una historia y criterios de aceptación numerados con un ID.
4. [Planificarla](04-plan.es.md): el contrato, el plan de pruebas y las decisiones que hay que validar.
5. [Dividirla en tareas](05-tasks.es.md): tareas pequeñas enlazadas a los criterios que cubren.
6. [Construir una tarea](06-build.es.md): primero pruebas que fallan, luego el código y luego `make verify`.
7. [Verificar la feature](07-verify.es.md): cada criterio con la prueba que lo cubre.

Con un agente lleva más o menos una hora. Puedes parar después de cualquier paso y retomarlo más tarde: `/dixi.status` dice dónde lo dejaste.

## Relacionado

- [Índice de la documentación](../documentation.es.md)
- [Guía de comandos](../command-catalog.es.md)
- [Referencia de comandos](../commands/index.es.md)
- [Referencia de la CLI](../cli/index.es.md)
