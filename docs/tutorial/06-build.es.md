# 6. Construir una tarea

## Propósito

Construir una tarea con las pruebas primero: las pruebas se escriben y se muestran fallando antes de cualquier código, y una vez en un commit quedan congeladas.

## Qué haces

Ejecuta [`/dixi.build`](../commands/build.es.md) con la primera tarea:

```text
/dixi.build T-001
```

Con Codex, `$dixi-build T-001`; con un agente de Agent Skills, `@dixi-build T-001`.

El agente trabaja en este orden:

1. Escribe las pruebas de los criterios de la tarea y las ejecuta, para mostrar que fallan por el motivo esperado. Sin prueba que falle no hay código.
2. Propone hacer un commit solo con esas pruebas. Revísalas y haz el commit: desde ese momento quedan congeladas y nadie las edita para que el código pase.
3. Escribe el código mínimo para que pasen.
4. Ejecuta `make verify` y muestra el resultado real.

Después revisa el cambio y haz tú el commit:

```bash
make verify
git add .
git commit -m "T-001 save a note with tags"
```

El agente no firma, no empuja ni integra por ti. Repite este paso para `T-002` y el resto de las tareas, de una en una.

## Qué deberías ver

- Las pruebas en la carpeta de pruebas de tu proyecto, primero en rojo y después en verde.
- `make verify` en verde. En un proyecto nuevo ejecuta [`dixi check`](../cli/check.es.md); añade el comando de tus pruebas al `Makefile` para que también las ejecute.
- La tarea marcada como hecha en `tasks.md` y las pruebas registradas en `.dixi/traceability.json`.

Si una prueba congelada parece incorrecta, el agente se detiene y lo explica en lugar de cambiarla. Si creaste el proyecto con [`dixi init`](../cli/init.es.md) y `--controls`, los hooks de Claude Code y Codex hacen cumplir esta regla ([controles automáticos](../controls.es.md)).

## Siguiente

[7. Verificar la feature](07-verify.es.md).

## Relacionado

- [Tutorial](index.es.md)
- [Referencia de comandos](../commands/index.es.md)
- [Subagentes](../subagents.es.md)
