# MODULE-001 — Paquete `notes`

## Propósito

Implementar el dominio de notas como paquete Python `notes` con API (`NoteStore`) y CLI (`python3 -m notes`).

## Responsabilidades

- Validar texto y etiquetas antes de guardar.
- Persistir de forma atómica (escritura temporal y reemplazo).
- Mensajes de la CLI en catálogos `notes/locales/es.json` y `en.json`.

## Relacionados

- [Dominio](../../03-domains/example/domain-spec.md)
- [Funcionalidad: capturar y buscar](../../05-features/example/feature-spec.md)
- [Funcionalidad: etiquetas](../../05-features/tags/feature-spec.md)
