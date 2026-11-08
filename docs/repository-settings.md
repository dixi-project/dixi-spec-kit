# Configuración del repositorio público

## Propósito

Dejar escrita la configuración de `dixi-project/dixi-spec-kit` que garantiza: `main` público y descargable por cualquiera, forks y PRs abiertos, e integración reservada a los mantenedores con revisión y checks. Aplicada y comprobada el 2026-11-08.

## Ajustes

| Ajuste | Valor |
|---|---|
| Visibilidad | Pública, solo después de revisar el historial final (abajo). |
| Rama por defecto | `main`. |
| Forks | Permitidos. |
| Escritura | Solo mantenedores de Dixi; colaboradores externos sin permiso de escritura. |
| Merge | Squash o merge commit; borrar ramas al integrar. |
| Private vulnerability reporting | Activado (Settings → Security). |
| Actions | Aprobación requerida para workflows de PRs de colaboradores nuevos. |

## Protección de `main` (ruleset)

Aplicado el 2026-11-08 como ruleset `main-protegida` (rama por defecto, sin `bypass_actors`):

| Regla | Valor |
|---|---|
| Borrado de `main` | Prohibido |
| Force push | Prohibido |
| Pull request | Obligatorio; hilos resueltos; revisiones obsoletas se descartan al hacer push |
| Aprobaciones | 0 mientras haya un solo mantenedor (GitHub no permite aprobar el propio PR). Los PRs externos los revisa el mantenedor antes de integrar. Subir a 1 con CODEOWNERS cuando haya un segundo mantenedor |
| Checks obligatorios | `make verify` (ubuntu/macos × Python 3.11/3.13) y `DCO sign-off`, con la rama al día |

Consultar: `gh api repos/dixi-project/dixi-spec-kit/rulesets`. Los rulesets requieren repositorio público o GitHub Pro.

## Historial limpio antes de hacerlo público

La preparación (con material heredado no distribuible y un PR que no puede borrarse) se archivó en un repositorio privado aparte. Este repositorio se creó nuevo, con `main` construido por una lista explícita de inclusión, y antes de hacerlo público se comprobó con `git ls-remote` que solo contenía `main`.

## Relacionados

- [ADR-100](../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-103](../09-architecture/adr/ADR-103-ci-publica-en-github-actions.md)
- [Puerta de publicación](publication-readiness.md)
- [Contribuir](../CONTRIBUTING.md)
