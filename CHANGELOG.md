# Changelog

## Propósito

Registrar los cambios del producto público DIXI Spec Kit, con numeración independiente de cualquier versión interna. Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y [SemVer](https://semver.org/lang/es/).

## [1.0.0] — primera versión pública

### Añadido

- CLI `dixi` sin dependencias de ejecución: `init`, `doctor`, `check`, `workflow list/show/prepare`, `--help`, `--version`, `--lang es|en`, `--json`.
- `dixi init --agent none|claude`: base documental trazable que nunca sobrescribe, rechaza symlinks y rutas inseguras.
- Adaptador Claude Code: `CLAUDE.md` y diez comandos `/dixi.discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze`, `status` en español e inglés; sin hooks ni permisos.
- `dixi check`: estructura, enlaces Markdown locales y grafo objetivo → dominio → módulo → feature → contrato → prueba.
- Ocho procedimientos compartidos con preparación de contexto y manifiesto de fuentes con hashes.
- Ejemplo público `examples/notes` con evolución y análisis de impacto.
- Documentación es/en, matriz de soporte, CONTRIBUTING con DCO, SECURITY y CI pública sin credenciales.
- Licencia MIT.

### Limitaciones conocidas

- Sin `dixi upgrade`; Windows no soportado; un solo adaptador (Claude Code). Ver [matriz de soporte](docs/support-matrix.md).
- Renombrar o borrar archivos generados por `init` hace fallar `dixi check`, porque son parte del inventario del proyecto.

## Relacionados

- [Plan](ROADMAP.md)
- [Matriz de soporte](docs/support-matrix.md)
