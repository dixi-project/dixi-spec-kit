# STRIDE threat model — Local core B1

## Purpose

Identify the threats to the installer and verifiers before implementing them. Local scope: CLI inputs, packaged resources, filesystem and project metadata; there is no AI, authentication or deployment in B1.

## Assets and trust boundaries

Assets: the user's local files, distributable resources, verification evidence and the privacy of `.context/`. Paths and the inspected project are untrusted input; the distribution is built from an explicit inventory. The runtime and operating system are trusted, as is the assumption that an attacker does not control the process with the same privilege. Operations run without elevating privileges.

## Threats and tests

| ID / STRIDE | Threat | Mitigation | Executable test |
|---|---|---|---|
| T01 / Spoofing | Fake project or incompatible format. | Typed metadata, explicit schema/version/selection. | `test_invalid_metadata`, `test_missing_project`, `test_unsupported_schema` |
| T02 / Tampering | Overwriting existing work/retry or path escapes. | Prevalidation, exclusive creation, rejection of traversal and preservation of partial state. | `test_nonempty_unchanged`, `test_repeated_init`, `test_traversal_destination`, `test_interrupted_initialization_preserves_partial_files` |
| T03 / Elevation | Following symlinks of the destination, metadata or documents. | Descriptors, O_NOFOLLOW and type checking without blocking open. | `test_symlink_destination`, `test_symlink_parent`, `test_symlink_metadata`, `test_symlink_document`, `test_fifo_document` |
| T04 / Information disclosure | Reading secrets or external files via JSON/links. | Confined paths, case-insensitive denial of sensitive names, no network and no execution. | `test_external_metadata_path`, `test_external_link`, `test_unsafe_path_spellings`, `test_check_does_not_execute`, `test_no_network` |
| T05 / Denial of service | Excessive JSON/text, invalid Unicode, too many links, malformed IDs/types. | Read/count limits and bounded patterns; validation of types/unique keys and paths. | `test_oversized_metadata`, `test_duplicate_json_keys`, `test_invalid_metadata`, `test_duplicate_ids`, `test_invalid_unicode_metadata`, `test_many_links_limit`, `test_unclosed_markdown_is_bounded`, `test_empty_and_spaced_destinations` |
| T06 / Repudiation | Claiming application verification or changing files while inspecting. | Structural scope report, stable codes, read without writes; documented Markdown subset. | `test_check_read_only`, `test_generated_project_passes`, `test_broken_parent`, `test_broken_link`, `test_broken_reference_link`, `test_reference_links_with_valid_destinations` |
| T07 / Information disclosure | Leaking private material through wheel/sdist. | Allowed inventory, original resources, tests on the final archive. | `test_artifact_allowlist`, `test_clean_installations` |
| T08 / Tampering | Omitting mandatory files by altering the inventory. | Compare required names with the resources of the installed version. | `test_missing_required_file`, `test_incomplete_inventory` |

## Residual risk and review

High risk due to filesystem writes and external data. Multi-file atomicity and protection against an attacker controlling the process itself are not guaranteed. Reading does not represent a transactional snapshot. Denial of sensitive names does not detect secrets under arbitrary names. The link analyzer does not cover all of CommonMark nor does it certify semantic completeness of the specs. The distribution is not published until rights, content/history scanning and release controls are resolved. New adapters and agent execution require extending this threat model.

## Related

- [Contract](../07-contracts/commands/local-core-contract.md)
- [Feature](../05-features/local-core/feature-spec.md)
- [Story](../tasks/backlog/TASK-001-lanzamiento-v1.md)
