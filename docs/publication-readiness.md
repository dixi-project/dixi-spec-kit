# DIXI Spec Kit v1.0.0 publication gate

## Purpose

Define concrete evidence per phase: preparation before creating the repository, configuration before exposing it, and verification of the launch. The user authorized its creation when ready; there is no need to request that general authorization again. Status as of 2026-11-08: v1.0.0 published. Still open: manual evaluation of the commands in Claude Code and full validation of ADR-101 (policy sets, outside v1.0.0).

The product/license, technical evidence and documentation/maintenance sections are entry requirements for publication. The creation of the repository and of the release are checked afterwards, in their own phases; they are not requirements for starting their own creation.

## B1 local progress — 2026-11-06

Open direction and incremental start authorized. [B1 verified](b1-verification.md): 43 tests, local wheel/sdist, clean installs, no-agent mode and `make verify` of the documentary project. This evidence is partial with respect to the launch requirements below; it does not confirm the full scope, upgrade, adapters, rights/license or publication controls. The global checkboxes remain open when they include work from later blocks.

Update 2026-11-07: [B2a verified](b2-verification.md) extends the suite to 71 cases and adds lookup/preparation of eight common procedures. It does not yet accredit agent execution/evaluation nor close global requirements.

Update 2026-11-08: the [comparison with GitHub Spec Kit](spec-kit-comparison.md) and [ADR-102](../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md) propose reducing the minimum scope. Validated by the responsible person the same day, together with the MIT + DCO license and `upgrade` deferred to v1.1. The checkboxes that depended on the previous scope are adjusted to ADR-102.

## Product and license

- [x] TASK-001 story and structural decisions validated (2026-11-08, ADR-102).
- [ ] ADR-101 validated; separation of core, integrations, stacks and policies implemented without contradictions with the effective rules of each set.
- [x] Distribution rights confirmed and final public license applied (MIT; only material written for the product).
- [x] Third-party attributions and license scope of generated projects documented (no third-party material distributed; ADR-100 point 5).
- [x] Repository, package and executable names checked ([B3](b3-verification.md)).
- [x] First launch identified as v1.0.0; private releases not reused.

## Technical evidence

- [x] Acceptance tests in their own commit before implementation, without an agent signature.
- [x] `make verify` defined and green in the product and the generated example.
- [x] Wheel and sdist contain all resources and install in a clean environment.
- [x] Installation and `init` do not access the private repo, AWS or the internal task system.
- [x] Conflicts, non-empty destinations and symlinks do not lose local files (upgrade deferred to v1.1).
- [x] Announced operating systems and agents have real evidence of support: CI green on Ubuntu and macOS with Python 3.11 and 3.13; Claude Code with local evidence.
- [x] Documentary use without an agent tested; eligible integration without altering the canonical formats.
- [x] Public example evaluated with the announced adapter (Claude Code); capabilities/controls matrix and support limits published. The second language moves to v1.1 (ADR-102).
- [x] Catalog included and contracts validated; all installed commands reference resources that are present and distributable.
- [x] Example executed from discovery to verified code and prepared review, plus one evolution with impact analysis.
- [ ] Deterministic tests and agent evaluations cover errors, gates, repetition and continuity of the announced commands. Deterministic tests ready; manual evaluation in a new Claude Code session still missing.
- [x] Resource manifest reviewed (allowlist exporter), links valid and secret scan without findings.

## Documentation and maintenance

- [x] README and quickstart es/en, example and reproducible demo.
- [x] CONTRIBUTING, SECURITY, support, maintainers and trademark policy prepared.
- [x] External contribution checks isolated from internal infrastructure and credentials; runners decided in ADR-103 (accepted).
- [x] Real CODEOWNERS and rules configuration prepared before receiving contributions ([settings](repository-settings.md)).

## Publication entry and repository configuration

- [x] New history built only with distributable material, in a new repository; the preparation work is archived in a separate private repository.
- [x] Repository `dixi-project/dixi-spec-kit` created, public and protected with the `main-protegida` ruleset: PR required, checks and DCO required, no force push or deletion of `main`.
- [x] A person signs the commits and performs the merge according to the applicable policy. An agent does not sign, attest, approve or merge.

The distributable selection and the clean history are reviewed before creating the remote. The protective configuration must be verified before exposing or announcing the repository. If it is first created as private to configure protections, the switch to public happens after reviewing the final content.

## Launch

- [x] Release v1.0.0 created from `f317065` (signed by the person and green in CI), with wheel and sdist.
- [x] Publication on PyPI deferred to v1.1; installation from Git, `uv tool install` and the release wheel documented and tested.

## Related

- [Story](../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Roadmap](../ROADMAP.md)
- [Repository settings](repository-settings.md)
