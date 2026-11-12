# DIXI Spec Kit v1 product specification

## Purpose

Turn selected EIS-IA materials into a public solution that an external person can install, understand and use without Dixi's internal accounts or repositories.

DIXI Spec Kit is an SDD development ecosystem with a core independent of the project's agent, model, language and framework. Each user chooses their tools; verified integrations will make it easier to apply the same method. The direction was accepted for incremental implementation; the operational mechanisms of provider policies remain pending according to ADR-101.

## Audience and outcome

Developers and teams who want to go from an idea to traceable specifications, an implementation plan and quality checks. The initial experience must produce a small, verifiable project, with a documented path to grow.

## Identity

- Product: DIXI Spec Kit, by Dixi Project.
- Target first public release: v1.0.0.
- Proposed repository: `dixi-project/dixi-spec-kit`; its availability has not been checked yet.
- Proposed package: `dixi-spec-kit`; its availability in the registry has not been checked yet.
- Local executable: `dixi`.
- Methodological origin: EIS-IA. Do not inherit its release numbering or its private changelog.
- Product independent of GitHub Spec Kit: inspired by its ease of installation and adoption, with Dixi's own methodology and maintenance.

## B1 local experience

```text
dixi init my-project --agent none
cd my-project
dixi doctor
dixi check
make verify
```

Install the package from PyPI or the local artifact following the [es/en guide](local-development.md). `init` creates the directory; the others inspect the current project. The generated Makefile only checks documentary structure. Help/version are also available. `upgrade` and the agent operations shipped after this first increment; the [README](../README.md) lists what is available today.

B2a increment: `dixi workflow list/show/prepare` looks up the eight shared definition/design recipes and prepares instructions plus a source manifest for an explicit ID. It does not produce decisions or run an agent. [Contract and limits](../07-contracts/commands/workflow-preparation-contract.md).

## Required behavior

### Command-based workflow

The product must allow going through discovery, specification, planning, tasks, build, verification and review preparation through agent commands. The [command guide](command-catalog.md) extends that journey with domains, architecture, contracts, threats, traceability analysis and change management, plus the specialized capabilities.

The CLI installs resources and runs deterministic checks; agent commands guide decisions and produce traceable artifacts. Each command requires a contract of inputs, outputs, errors, continuity, gates and tests. The operations are the same for every adapter and the syntax is fixed per adapter; the [support matrix](support-matrix.md) says which ones are verified. Public support requires an example executed end to end and a later modification with impact analysis.

### Initialization

Works without authenticating to GitHub, accessing the private EIS-IA repository, creating remote repos or registering the project in the internal task system. Uses resources included in the distribution and records the template version. Does not automatically run downloaded instructions or hooks. Rejects non-empty destinations and conflicting symbolic links before writing; support for existing projects requires an explicit operation that does not overwrite changes.

### Diagnostics and checking

`doctor` distinguishes local installer requirements from optional requirements of the generated project. `check` verifies structure and traceability, produces explainable output and fails with a non-zero code on violations. It does not read secrets or run arbitrary template commands.

### Upgrade

Compares the installed version and the original files with the state of the project. The `--dry-run` mode does not write and lists new and modified files and conflicts. A later apply step, if it is part of v1, only updates files without local changes and requires conflicts to be resolved without data loss. Do not use a bulk copy over the project as an upgrade.

The concrete proposal of the initial contract limits v1 to `--dry-run`, comparing the resources of the installed version without downloading another version. Automatic application is outside that proposal, pending validation of the scope together with the story.

### Agents and policies

The core defines operations and artifacts without depending on an agent. The person can choose a verified integration or work with the guides and templates without integration. Codex and Claude Code are initial candidates of equal priority, subject to evaluating versions, invocations and controls. Commands inside the agent are documented separately from terminal commands; identical syntax or automation across tools is not promised.

ADR-101 separates the core from the portable public and Dixi organizational sets, with shared guarantees and operational mechanisms still to be specified. The AWS/Bedrock, CodePipeline and CodeBuild policies remain in force in this repository. B1 only installs a documentary base without a provider; it does not invoke a model or AWS to generate files.

### Project languages and frameworks

The kit's implementation language does not limit that of its users. Projects choose a stack and record how to run their checks; stack profiles make that connection easier. Using the method with another language does not require rewriting the specs. A verified profile accredits only its test matrix; automatic generation for any framework is not announced.

### Distribution

B1 implementation: Python with the standard library at runtime, included resources and local wheel/sdist distribution. Python is a requirement of the installer, not of the projects' code. Build with Setuptools 84.2.1, verified and pinned by hash; local installations with pip tested without an index. It does not depend on publishing to PyPI for development. [Evidence and limits](b1-verification.md).

### Documentation and adoption

README and getting-started guide in Spanish and English; CLI messages in language catalogs. Deliberate public examples, a short demo, and explicit requirements/costs of the chosen integrations. Distinguish portable method, verified adapter and verified stack profile. No unverified claims of parity or superiority.

## Boundaries

v1 does not require a SaaS, telemetry, user registration, billing or integration with internal tools. Publishing the package to a registry and creating a public repository are separate operations.

## Related

- [Story](../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Command catalog](command-catalog.md)
- [Joint review](history/v1-design-review.md)
- [Command contract](../07-contracts/commands/command-contract.md)
- [ADR-100](../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101: portability and integrations](../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Support matrix](support-matrix.md)
- [Publication](publication-readiness.md)
