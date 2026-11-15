# 3. Especificar la feature

## Propósito

Convertir la idea en una especificación: una historia, criterios de aceptación numerados que se pueden comprobar desde fuera y un ID que enlaza la feature con su módulo.

## Qué haces

Abre tu agente en la carpeta `notes` y ejecuta [`/dixi.specify`](../commands/specify.es.md) con la feature en tus propias palabras:

```text
/dixi.specify añadir una nota con etiquetas
```

Con Codex, escribe `$dixi-specify añadir una nota con etiquetas`; con un agente de Agent Skills, `@dixi-specify añadir una nota con etiquetas`. Con `--agent none`, [`dixi workflow`](../cli/workflow.es.md) imprime el mismo procedimiento para cualquier agente:

```bash
dixi workflow prepare specify --target MODULE-001 --request "Add a note with tags"
```

El agente pregunta a qué módulo pertenece la feature cuando no está claro, y pregunta por lo que la petición deja abierto. Responde con lenguaje llano. Si quedan dudas después de escribir la spec, [`/dixi.clarify`](../commands/clarify.es.md) las pregunta una a una y registra las respuestas.

## Qué deberías ver

- Un archivo nuevo `05-features/<slug>/feature-spec.md` con la historia (Como / Quiero / Para), criterios de aceptación numerados como «una nota sin texto se rechaza» y los supuestos marcados como tales.
- La feature registrada en `.dixi/traceability.json` con un ID nuevo, normalmente `FEATURE-002` (el ejemplo del kit es `FEATURE-001`), y `MODULE-001` como padre.

Lee los criterios ahora: cada uno se convertirá después en al menos una prueba. Cámbialos mientras es barato. Compáralos con [`examples/notes`](../../examples/notes), que tiene sus criterios en `05-features/`.

## Siguiente

[4. Planificarla](04-plan.es.md).

## Relacionado

- [Tutorial](index.es.md)
- [Referencia de comandos](../commands/index.es.md)
