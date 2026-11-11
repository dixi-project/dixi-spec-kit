# B2a contract — Viewing and preparing procedures

## Purpose

Provide a deterministic interface over the method's procedures: the eight definition/design procedures A01–A08 first, and since ADR-108 phase B one recipe for every operation the adapters install. It never simulates an agent's execution. It does not replace the artifact contract of the full workflow.

## Interface

```text
dixi [--lang es|en] [--json] workflow list
dixi [--lang es|en] [--json] workflow show <operation>
dixi [--lang es|en] [--json] workflow prepare <operation> --target <id> --request <text>
```

Global options precede `workflow`. `list/show` only read packaged resources and work without a project. `prepare` operates from the root initialized by B1. There is no provider option and no extension download.

| Operation | Allowed target types |
|---|---|
| discover | goal |
| specify | module |
| clarify | goal, domain, module, feature, contract, test |
| domain | goal, domain |
| architecture | domain, module, feature |
| contract | module, feature |
| threat-model | module, feature |
| plan | feature |

All require an exact ID and an explicit request in `prepare`. Empty text, more than 4 096 characters, Unicode surrogates or control characters other than tab/newline are rejected with code 2. The request is neither interpolated nor executed. Unknown or incompatible names/targets return 2. An invalid preparation does not return a partial package.

## Result

The JSON envelope keeps `status`, `code`, `messages`; it adds `workflow` for the specific result. `list` returns `operations`; `show`, `recipe`; `prepare`, `packet`. `status: completed` only means that the CLI operation finished. The package declares `status: prepared`, `execution: manual_or_external`, `schema_version: 1`, `operation`, `request`, `target`, `project_language`, `mode`, `recipe` and `sources`. `target` only includes `id`, `kind`, `path`, `parents`: it does not propagate unknown fields from the graph.

Each recipe contains `id`, `title`, `purpose`, `inputs`, `steps`, `outputs`, `gates`, `checks`, `next_operations` and `target_kinds`, plus common guards. The human-readable output presents the same data. The recipe's outputs are expectations for the subsequent work; they are not files created by `prepare`.

`sources` records `path`, current SHA-256 and size in bytes, in stable order. It includes `.dixi/project.json`, `.dixi/traceability.json`, `MODE`, `AGENTS.md`, `00-master-spec.md`, the target and its declared ancestors; it removes duplicate paths. It never includes bodies, absolute paths, credentials or a generated shell command. The whole graph is validated; documents are read only from the selection. A hash identifies the bytes read; it does not sign provenance or certify approval.

## Limits and trust

Reuses the B1 confined reads: regular files, no symlinks, sensitive names denied, up to 1 MiB per file. A maximum of 64 unique sources and 2 MiB cumulative; metadata and graph count toward the total. MODE must be `mvp` or `prod`. Malformed data fails with 1; missing project 2; unsupported schema/platform 4; I/O 5.

The recipe instructs treating the request and documents as data, without allowing them to remove gates, run shell commands or read secrets. These guards are instructions, not enforcement over an external LLM. Project policies must be reviewed by whoever uses them; they are neither interpreted nor executed by the CLI. Markdown links are not followed. There is no transactional snapshot against concurrent editing; compare hashes before using the package.

The recipes are original resources of DIXI Spec Kit, with no dependency on private standards. Provider, language and framework are requested/documented when relevant; they are not inferred from the agent. An absence is expressed as a question/assumption, never as the user's choice.

## Continuity and acceptance

No writes and no timestamps: repeating over the same bytes and arguments returns the same package. A modified file changes its hash. Interrupting leaves no files and no project state. MODE is not promoted, and no ADR is approved, attested, signed or integrated. Preparing `plan` does not run `build` or create fictitious tests.

## Related

- [General contract](command-contract.md)
- [Feature](../../05-features/workflow-preparation/feature-spec.md)
- [Task](../../tasks/backlog/TASK-002-operaciones-compartidas-b2.md)
- [Threats](../../13-security/workflow-preparation-threat-model.md)
- [B1 read contract](local-core-contract.md)
