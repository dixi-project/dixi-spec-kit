# 7. Verificar la feature

## Propósito

Comprobar que cada criterio de aceptación de la feature está cubierto por una prueba que pasa, y encontrar los que no lo están.

## Qué haces

Cuando todas las tareas estén construidas, ejecuta [`/dixi.verify`](../commands/verify.es.md) con el ID de tu feature:

```text
/dixi.verify FEATURE-002
```

Con Codex, `$dixi-verify FEATURE-002`; con un agente de Agent Skills, `@dixi-verify FEATURE-002`.

Puedes ejecutar tú las mismas comprobaciones en la terminal en cualquier momento:

```bash
make verify
dixi check
```

## Qué deberías ver

- La salida de `make verify`, tal como se ejecutó. El agente nunca da por verde algo que no ejecutó.
- Cada criterio de aceptación con las pruebas que lo cubren, y una lista de los criterios sin prueba o con pruebas omitidas o fallidas.
- Para cada hueco, una propuesta de volver a ejecutar [`/dixi.build`](../commands/build.es.md). La verificación no corrige código.
- [`dixi check`](../cli/check.es.md) terminando con código de salida 0: la cadena desde el objetivo hasta las pruebas está completa.

Cuando todo está en verde, [`/dixi.review`](../commands/review.es.md) agrupa el cambio por riesgo para la persona que revisa el pull request. Tú abres el pull request y una persona lo aprueba.

## Qué viene después

Has llevado una feature por todo el camino. A partir de aquí:

- Cambia un comportamiento que ya existe con [`/dixi.change`](../commands/change.es.md): muestra qué toca el cambio antes de editar ninguna spec ni código.
- Prepara una versión con [`/dixi.release`](../commands/release.es.md): evidencia, una entrada de changelog y un plan de vuelta atrás. Etiquetar y publicar te corresponde a ti.
- Encuentra la operación adecuada para cualquier otro momento en la [guía de comandos](../command-catalog.es.md).

## Relacionado

- [Tutorial](index.es.md)
- [Referencia de comandos](../commands/index.es.md)
- [Índice de la documentación](../documentation.es.md)
