# Proyecto — Notas locales

## Propósito

Ejemplo público de DIXI Spec Kit: una biblioteca y CLI pequeña para guardar notas de texto con etiquetas en un archivo local. Muestra el recorrido idea → specs → pruebas → código verificado → revisión, y una evolución con análisis de impacto. La persona responsable es ficticia; sus decisiones se marcan como «Decisión (persona del ejemplo)».

## Problema y alcance

- Problema: apuntar ideas rápidas desde terminal y encontrarlas después sin depender de un servicio en red.
- Alcance: añadir, listar y buscar notas; etiquetas normalizadas y filtro por etiqueta (evolución, FEATURE-002).
- Fuera de alcance: sincronización, cifrado, varios usuarios, interfaz web.
- Stack: Python 3.11+ con biblioteca estándar y `unittest`. Decisión (persona del ejemplo, 2026-11-08).
- Restricciones: sin red, sin dependencias de terceros, datos en un único JSON elegido por quien usa la CLI.

## Relacionados

- [Objetivo](01-business/vision.md)
- [Guía](docs/guide.md)
- [Recorrido del ejemplo](docs/walkthrough.md)
