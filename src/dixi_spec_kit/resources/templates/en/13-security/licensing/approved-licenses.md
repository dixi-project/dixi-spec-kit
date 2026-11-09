# Approved licenses

## Purpose

Keep the list of third-party licenses the project accepts, those that need review and those it rejects. The lists below are a starting suggestion, not legal advice; adjust them to the project license and distribution model.

Status: draft. {{pending: confirm the lists with the policy owner or legal counsel}}

## Allowed

Permissive licenses that usually only require keeping notices.

| SPDX identifier | Notes |
|-----------------|-------|
| MIT | Keep copyright notice |
| BSD-2-Clause | Keep copyright notice |
| BSD-3-Clause | Keep notice; no endorsement use |
| Apache-2.0 | Keep NOTICE file; patent grant |
| ISC | Keep copyright notice |
| {{pending: add or remove}} | |

## Review required

Licenses whose obligations depend on how the component is used or distributed.

| SPDX identifier | Typical concern |
|-----------------|-----------------|
| LGPL-2.1, LGPL-3.0 | Linking and replacement obligations |
| MPL-2.0 | File-level copyleft |
| EPL-2.0 | Weak copyleft, secondary license terms |
| CC-BY-4.0 | Fine for content, unusual for code |
| {{pending: add}} | |

## Not allowed without an exception

| SPDX identifier | Reason |
|-----------------|--------|
| GPL-2.0, GPL-3.0 | Strong copyleft; {{pending: confirm against the project license}} |
| AGPL-3.0 | Network copyleft; affects hosted services |
| Unknown or missing license | No rights granted |
| Non-commercial or field-of-use restrictions | {{pending: confirm}} |

## How to change this list

1. Propose the change with the license, the component that needs it and the reason.
2. The policy owner records the decision and the date.
3. Update the license checks if they are automated.

## Related

- [Licensing policy](licensing-policy.md)
- [Dependency scanning](../dependency-scanning.md)
