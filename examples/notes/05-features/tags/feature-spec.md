# FEATURE-002 — Etiquetas normalizadas y filtro por etiqueta

## Propósito

Evolución del ejemplo: cambia el contrato de etiquetas de FEATURE-001. Antes de especificarla se ejecutó `/dixi.analyze` ([impacto](impact.md)).

## Historia

Como persona usuaria de terminal
quiero etiquetar notas sin preocuparme por mayúsculas o duplicados y filtrarlas por etiqueta
para agrupar ideas relacionadas.

## Criterios de aceptación

1. Las etiquetas se recortan, pasan a minúsculas y se deduplican conservando el primer orden.
2. Una etiqueta vacía, de más de 32 caracteres o con caracteres fuera de `a-z 0-9 - _` se rechaza sin modificar el almacén.
3. `list --tag X` devuelve solo las notas con la etiqueta normalizada de X.
4. Las notas guardadas con etiquetas en el formato anterior se normalizan al leer, sin reescribir el archivo.

## Relacionados

- [Módulo](../../04-modules/example/module-spec.md)
- [Contrato](../../07-contracts/example.md)
- [Impacto](impact.md)
- [Tareas](tasks.md)
