# ADR-103 — CI pública de verificación en GitHub Actions, sin credenciales

## Propósito

Decidir dónde se ejecutan los checks de los PR del repositorio público, incluidos los que llegan desde forks, sin exponer infraestructura ni credenciales de Dixi.

## Estado

Propuesto el 2026-11-08. Requiere validación de la persona responsable antes de exigir el check en la protección de `main`.

## Contexto

La norma heredada de EIS-IA ejecuta los checks en runners CodeBuild de la cuenta de Dixi y despliega por CodePipeline (ADR-006 del origen). Un repositorio público recibe PRs de forks: ejecutarlos en runners de la organización expondría infraestructura interna a código de terceros. DIXI Spec Kit no despliega nada: su release es un tag y unos artefactos que publica una persona.

## Decisión propuesta

1. Los checks públicos corren en runners alojados por GitHub (`ubuntu-latest` y `macos-latest`), con `permissions: contents: read`, sin secretos, sin OIDC y sin acceso a AWS.
2. El evento es `pull_request` (nunca `pull_request_target`) y `push` a `main`. Las acciones se fijan por SHA.
3. El job `verify` instala solo Setuptools fijado por hash y ejecuta `make verify` en Python 3.11 y 3.13.
4. El job `dco` exige `Signed-off-by` en cada commit del PR (ADR-010 del origen).
5. No hay despliegue automático. La release v1.0.0 la crea una persona desde un commit en verde.

## Consecuencias

Excepción acotada a este repositorio público: no cambia las normas del origen ni de los proyectos Dixi privados. Los minutos de CI corren por cuenta de GitHub para repositorios públicos. Si en el futuro se publica en PyPI desde CI, requerirá otro ADR (por ejemplo, publicación confiable con aprobación manual).

## Relacionados

- [ADR-100](ADR-100-distribucion-publica-v1.md)
- [Configuración del repositorio](../../docs/repository-settings.md)
- [Workflow](../../.github/workflows/verify.yml)
