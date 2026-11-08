# FEATURE-001 — Capturar, listar y buscar notas

## Propósito

Primera funcionalidad del ejemplo, producida con `/dixi.specify`.

## Historia

Como persona usuaria de terminal
quiero añadir notas y buscarlas por texto
para recuperar ideas sin salir de la consola.

## Criterios de aceptación

1. `add` guarda una nota con texto recortado y devuelve su ID; los IDs crecen desde 1.
2. Texto vacío o de más de 1 000 caracteres se rechaza sin modificar el almacén.
3. `list` devuelve las notas en orden de creación; un almacén inexistente equivale a vacío.
4. `search` devuelve las notas cuyo texto contiene el término sin distinguir mayúsculas.
5. La CLI termina con código 0 al completar y 2 ante entrada inválida.

## Reglas de negocio

1. Las notas no se editan ni se borran en esta versión.

## Relacionados

- [Módulo](../../04-modules/example/module-spec.md)
- [Contrato](../../07-contracts/example.md)
- [Tareas](tasks.md)
