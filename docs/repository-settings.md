# Configuración del repositorio público

## Propósito

Dejar escrita la configuración de `dixi-project/dixi-spec-kit` que garantiza: `main` público y descargable por cualquiera, forks y PRs abiertos, e integración reservada a los mantenedores con revisión y checks. Una persona con rol de administración la aplica y la comprueba **antes** de hacer público el repositorio.

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

```sh
gh api -X POST repos/dixi-project/dixi-spec-kit/rulesets --input - <<'JSON'
{
  "name": "main-protegida",
  "target": "branch",
  "enforcement": "active",
  "conditions": {"ref_name": {"include": ["~DEFAULT_BRANCH"], "exclude": []}},
  "rules": [
    {"type": "deletion"},
    {"type": "non_fast_forward"},
    {"type": "pull_request", "parameters": {
      "required_approving_review_count": 1,
      "require_code_owner_review": true,
      "dismiss_stale_reviews_on_push": true,
      "require_last_push_approval": true,
      "required_review_thread_resolution": true}},
    {"type": "required_status_checks", "parameters": {
      "strict_required_status_checks_policy": true,
      "required_status_checks": [
        {"context": "make verify (ubuntu-latest, Python 3.11)"},
        {"context": "make verify (ubuntu-latest, Python 3.13)"},
        {"context": "make verify (macos-latest, Python 3.11)"},
        {"context": "make verify (macos-latest, Python 3.13)"},
        {"context": "DCO sign-off"}]}}
  ]
}
JSON
```

Sin `bypass_actors`: nadie, tampoco administradores, puede saltarse la regla. Con un solo mantenedor, `require_last_push_approval` impide que se apruebe su propio último push; mientras no haya un segundo mantenedor, la persona responsable decide si relajarlo y lo deja registrado.

## Historial limpio antes de hacerlo público

Las ramas de preparación (`preparation/v1`, `alfdixi/v1-spec-kit-dixi-project`) contienen material heredado no distribuible. `main` se construye con `scripts/export-release.py`, que copia solo la lista permitida, en un historial nuevo. Antes de cambiar la visibilidad, esas ramas se borran del remoto (o se conservan en un repositorio privado aparte) y se comprueba con `git ls-remote` que solo queda `main` y el tag `v1.0.0`.

## Relacionados

- [ADR-100](../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-103](../09-architecture/adr/ADR-103-ci-publica-en-github-actions.md)
- [Puerta de publicación](publication-readiness.md)
- [Contribuir](../CONTRIBUTING.md)
