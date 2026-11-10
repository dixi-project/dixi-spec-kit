# ADR-107 — Windows support with the same filesystem guarantees

## Purpose

Decide whether DIXI Spec Kit can run on Windows with the same safety guarantees it gives today on macOS and Linux (no following of links, no escape from the destination, no overwriting) and, if so, how to get there without weakening the guarantees or adding runtime dependencies.

## Status

**Proposed** on 2026-11-10. Requires validation by the responsible person before any change to code, tests, CI or the [support matrix](../../docs/support-matrix.md). Until then [ADR-102](ADR-102-recorte-de-alcance-v1.md) item 5 stands: Windows is declared unsupported.

## Context

### What the core relies on today

Every command that touches a project goes through `src/dixi_spec_kit/filesystem.py`. The guarantees come from descriptor-relative, no-follow POSIX calls, not from path checks:

| Location | Operation | Threat it mitigates |
|---|---|---|
| `filesystem.py:19-21` | `supported()` requires `os.name == "posix"`, `os.O_NOFOLLOW`, and `os.open`/`os.mkdir` in `os.supports_dir_fd`. | Refuses to run where the next rows cannot be honoured: no unsafe fallback. |
| `filesystem.py:24-32` | `safe_path()` rejects `\`, `:`, control characters, surrogates, empty, `.`, `..`, `.git`, `.context`, `.aws`, `.ssh`, `.env*`, `id_rsa`, `id_ed25519`, `*.pem`, `*.key` (case-folded). | Traversal in metadata, traceability and links; reading secrets by name. |
| `filesystem.py:42` | `os.mkdir(part, 0o700, dir_fd=fd)` | Creates each directory relative to an already verified parent; private mode. |
| `filesystem.py:45` | `os.open(part, O_RDONLY \| O_DIRECTORY \| O_NOFOLLOW, dir_fd=fd)`, one component at a time. | Symlink swap of any intermediate directory; TOCTOU between check and use, since the held descriptor, not the path, is what the next step uses. |
| `filesystem.py:50-51`, `89-90` | `ELOOP`/`ENOTDIR` mapped to `unsafe_path`. | A link found anywhere fails closed. |
| `filesystem.py:59-60` | `root_directory()` raises `unsupported_platform` with **exit code 4**. | The single native-Windows exit point for the file-touching commands. |
| `filesystem.py:62-67` | Rejects `..`, uses `os.path.abspath` (never `realpath`), opens `/` and walks every absolute component with the no-follow walk. | A symlinked ancestor of the destination or project is refused, not resolved. |
| `filesystem.py:79` | `os.open(name, O_RDONLY \| O_NOFOLLOW \| O_NONBLOCK, dir_fd=parent)` | Symlinked file leaf; blocking on a FIFO. |
| `filesystem.py:81-86` | `fstat` on the open descriptor: `S_ISREG` and a 1 MiB limit. | Special files and oversized reads, checked on the object actually opened. |
| `filesystem.py:101-102` | `os.open(name, O_WRONLY \| O_CREAT \| O_EXCL \| O_NOFOLLOW, 0o600, dir_fd=parent)` | Overwriting existing work; writing through a planted link; private mode. |
| `core.py:165-167` | `init` rejects an empty destination, `..` and a nameless path (`unsafe_destination`, code 3). | Escape from the requested destination. |
| `core.py:178-190` | `init` creates the destination with `mkdir(dir_fd=...)`, re-opens it no-follow, requires `os.listdir(fd)` to be empty, writes a lock file and every file through `write_file`, then `os.unlink(..., dir_fd=root)`. | Writing into a non-empty or swapped destination; partial state identified by the lock. |
| `core.py:322-323` | `doctor` raises `unsupported_platform` (code 4) before anything else. | Same as above, for the diagnostic. |
| `upgrade.py:16-22`, `26`, `43-53` | `upgrade --dry-run` reads every managed file through `read_file` and compares SHA-256 digests with `managed_files`. | Read-only plan; it inherits the read guarantees. |

`init`, `check`, `doctor`, `workflow prepare`, `upgrade --dry-run` and `placeholders` therefore exit 4 on Windows; `cli.py:70-76` swallows the same error when guessing the project language. `--help`, `--version`, `workflow list/show` and `pr-size` (`core.py:379-399`, which only runs `git` through `subprocess`) do not open the project and already run.

The [local core threat model](../../13-security/local-core-threat-model.md) (T02, T03) and the [local core contract](../../07-contracts/commands/local-core-contract.md) state that a system without these operations "fails explicitly, without degrading that protection". No test exercises the code-4 path today.

### What Windows offers through the standard library

- `dir_fd` is not supported on Windows: `os.supports_dir_fd` is empty there ([os: paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd), [`os.supports_dir_fd`](https://docs.python.org/3/library/os.html#os.supports_dir_fd)). `os.open` cannot open a directory at all, so there is no stdlib equivalent of `openat`.
- `O_NOFOLLOW`, `O_DIRECTORY` and `O_NONBLOCK` are documented as Unix-only; Windows only adds `O_BINARY`, `O_NOINHERIT`, `O_TEMPORARY` and similar ([open flag constants](https://docs.python.org/3/library/os.html#os.O_NOFOLLOW)). `FILE_FLAG_OPEN_REPARSE_POINT`, the Win32 way of not following a link, is not reachable through `os.open`.
- `O_CREAT | O_EXCL` exists and maps to `CREATE_NEW`, which fails if the leaf name already exists, including when it is a link. It says nothing about intermediate components, which are always followed.
- `os.lstat()` does not follow the final reparse point and exposes `st_file_attributes` and `st_reparse_tag` ([`st_reparse_tag`](https://docs.python.org/3/library/os.html#os.stat_result.st_reparse_tag)); `os.path.isjunction()` exists since 3.12 ([docs](https://docs.python.org/3/library/os.path.html#os.path.isjunction)). Both are check-then-use: a junction can be put in place between the `lstat` and the `open`.
- `os.path.realpath(path, strict=True)` resolves symlinks and junctions ([docs](https://docs.python.org/3/library/os.path.html#os.path.realpath)); comparing it with the expected path detects a static link, but is again check-then-use.
- Junctions (`IO_REPARSE_TAG_MOUNT_POINT`) can be created by any user without privileges; symbolic links need a privilege or Developer Mode. The realistic swap vector on Windows is a junction, and the code cannot rely on lack of privilege.
- Names that are not what they look like ([Naming files](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file)): reserved device names (`CON`, `PRN`, `AUX`, `NUL`, `COM1`-`COM9`, `LPT1`-`LPT9`, also with an extension, such as `nul.md`; `os.path.isreserved()` exists only since 3.13, [docs](https://docs.python.org/3/library/os.path.html#os.path.isreserved)); trailing dots and spaces are stripped, so `.git.` and `.git ` open `.git` and escape the `safe_path` denylist; 8.3 short names (`GIT~1`, `ENV~1`) are aliases that the denylist cannot see; alternate data streams (`file:stream`) and drive-relative names (`C:x`) are already rejected because `safe_path` refuses `:`; `\` is already rejected. NTFS is case-insensitive, which `safe_path` already handles with `casefold`.
- Paths over 260 characters fail unless long paths are enabled in the system and in the process ([Maximum path length](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation)).
- `root_directory()` opens `/` and walks `absolute.parts[1:]` (`filesystem.py:65-67`); on Windows the anchor is a drive (`C:\`) or a UNC share, so the walk itself must change.

### What the Win32 API offers through `ctypes`

`CreateFileW` with `FILE_FLAG_BACKUP_SEMANTICS | FILE_FLAG_OPEN_REPARSE_POINT` opens a directory handle without following a final reparse point ([CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew)). `GetFileInformationByHandleEx(FileAttributeTagInfo)` then tells whether the opened object is a reparse point, on the handle, not the path. Opening each ancestor without `FILE_SHARE_DELETE` and keeping the handle open prevents that directory from being renamed, deleted or replaced while the operation runs, which closes the swap window that `dir_fd` closes on POSIX. `CREATE_NEW` with `FILE_FLAG_OPEN_REPARSE_POINT` gives exclusive, no-follow creation of the leaf; `GetFileType`/attributes on the handle replace `S_ISREG`; `GetFinalPathNameByHandleW` confirms the handle is under the expected root. `NtCreateFile` with a `RootDirectory` handle is the true `openat` equivalent, but lives in `ntdll` and is better avoided.

`ctypes` is part of the standard library ([docs](https://docs.python.org/3/library/ctypes.html)); using it adds no package to install and does not break the letter of the "no runtime dependencies" rule in `AGENTS.md` or ADR-105 item 2. It does change the risk profile: hand-written Win32 signatures run outside Python's memory safety, a wrong type or constant fails silently or crashes, the code is reviewable only by someone who knows the API, and it can be tested only on Windows. This ADR treats `ctypes` as allowed standard library, but as a structural decision that needs the person's validation, not as a free choice.

### Other pieces that assume POSIX

- **Hooks (`--controls`).** `core.py:120-123` writes `python3 "$CLAUDE_PROJECT_DIR/.dixi/hooks/<script>.py"` for Claude Code and `python3 "$(git rev-parse --show-toplevel 2>/dev/null || pwd)/..."` for Codex. On Windows `python3` is often missing or the Store alias that exits with a non-2 code; `$VAR`, `$(...)`, `2>/dev/null` and `||` are POSIX shell syntax that `cmd.exe` and Windows PowerShell 5 do not accept. A hook that fails with any code other than 2 does not block, so the controls would **fail open silently**. The Claude Code matcher is `Bash` only (`core.py:144`); a different shell tool would not be inspected. `protect_tests.py:44`, `guard_attestation.py:37` and `mode_gate.py:40` parse commands with `shlex` in POSIX mode; `guard_secrets.py:37` already splits on both separators.
- **`verify_on_stop`.** It runs `make verify` (`verify_on_stop.py:58`); without `make` it lets the agent stop and only notifies (`verify_on_stop.py:63-65`).
- **`Makefile`.** `Makefile:1` looks for `.venv/bin/python`; on Windows the interpreter is `.venv\Scripts\python.exe`, and `make` is not installed by default. CI (`.github/workflows/verify.yml:35`) also uses `.venv/bin/python`.
- **Line endings and hashes.** `managed_files` stores the SHA-256 of the exact bytes written (`core.py:176`), and `upgrade --dry-run` compares raw bytes (`upgrade.py:50-53`). With Git for Windows' default `core.autocrlf=true`, a project committed on one machine and checked out on Windows gets CRLF bytes, so every managed text file is reported as `conflict`. The same applies to this repository: resources under `src/dixi_spec_kit/resources/` are packaged as bytes, so a wheel built from a CRLF checkout differs from one built on Linux. The repository's `.gitattributes` does not set `eol`.
- **Scripts.** `scripts/verify-source.py:14,15,21,44` call `read_text()` without `encoding`, which uses the locale code page on Windows and fails on non-ASCII files. `scripts/build-local.py` already uses `as_posix()` and refuses symlinked sources.
- **Tests.** `tests/test_local_core.py:111,119,209,218` and `tests/test_workflows.py:209` use `symlink_to` (needs privilege on Windows); `tests/test_local_core.py:227` and `tests/test_workflows.py:149,216` use `os.mkfifo` (absent on Windows); `tests/test_distribution.py:66,71` use `bin/python` and `bin/dixi`. Existing tests must not be edited to make code pass, so a Windows run cannot simply reuse the whole suite.
- **Git checkouts.** Git for Windows defaults to `core.symlinks=false` and checks symlinks out as plain files, and Git never creates junctions. The "planted link in a cloned repository" threat is smaller on Windows; the concurrent swap by a local process is not.

## Options

### A. Keep Windows unsupported

Keep code 4. Cost: none. Windows users have no native path, and nothing documents an alternative.

### B. Native support with the standard library and documented reduced guarantees

Replace the descriptor walk with `lstat` checks on every component (reparse attributes and tag), `realpath(strict=True)` comparison, `O_EXCL` creation, a reserved-name, trailing-dot/space and short-name filter, and long-path handling. It detects links that already exist, but every check is separate from the use, so a junction swapped in between is followed. That is the exact guarantee the core exists to give (T03), and it contradicts the contract ("without degrading that protection") and the `unsupported_platform` message ("no unsafe fallback was used"). The guarantee would differ by platform for the same command and exit code.

### C. Native support through `ctypes` against Win32

A Windows backend (separate module, same interface as `directory`, `read_file`, `write_file`, `root_directory`) built on `CreateFileW` handles with `FILE_FLAG_OPEN_REPARSE_POINT`, handle-based type checks, ancestors held without `FILE_SHARE_DELETE`, `CREATE_NEW` leaves, plus the name filters of option B. It can reach parity with POSIX on the threats of T02/T03, with a larger and harder-to-review surface, Windows-only tests, and the changes to hooks, scripts, line endings and CI listed above. It is the only native option with the same guarantee.

### D. WSL 2 as the supported Windows path

Run `dixi`, the agent and its hooks inside a WSL 2 Linux distribution, with the project on the Linux filesystem (for example `~/project`, not `/mnt/c/...`). The code path is the Linux one already covered by CI, so the guarantees are identical with no code change. Projects under `/mnt/c` are reachable from Windows processes that can create junctions and are served through a translation layer whose link semantics are not the ext4 ones; they stay out of the supported scope. Cost: documentation, one recorded manual run and, optionally, a CI job.

## Decision (proposed)

1. **Adopt D now.** Declare "Windows through WSL 2, project on the Linux filesystem" as supported once phase 1 is done, with the same evidence standard as Linux.
2. **Keep A for native Windows.** `dixi` keeps exiting 4 natively. Phase 0 adds a native Windows CI job that proves the refusal is explicit and writes nothing, without announcing support.
3. **Reject B.** A guarantee that changes by platform under the same exit code and message is worse than an explicit refusal; it would also require rewriting T03, the contract and the locale message to say less than today.
4. **Keep C as a conditional phase**, started only if there is demand that WSL cannot meet and after the person validates the use of `ctypes` and the larger review burden. It reaches parity only when every test of phase 2 passes on Windows; until then native Windows stays at code 4.

Reasoning: the product's promise is the guarantee, not the platform list. D delivers that promise to Windows users at once and with zero new code; C is the only native route that keeps it, and its cost is justified only by real demand.

## Consequences

- The support matrix gains a "Windows (WSL 2, Linux filesystem)" row and keeps "Windows (native): Not supported, exit 4". README and local development docs explain WSL 2 and why `/mnt/c` is out of scope.
- Phase 0 adds the first test of the code-4 path on every platform, closing an existing gap.
- Hooks stay POSIX-only; under WSL 2 they behave as on Linux. Native hooks are part of phase 2 only.
- If phase 2 is approved, the repository carries a second filesystem backend that only Windows CI can exercise, and every future change to `filesystem.py` must be mirrored and tested on both.
- `.gitattributes` with `eol=lf` (phase 0 for this repository, phase 2 for generated projects) makes hashes independent of the checkout platform.

## Plan

Each phase starts with tests written and seen failing (red), in new test modules; existing tests are not edited. A phase is done only when `make verify` is green on the existing matrix and its own criteria hold.

### Phase 0 — Explicit refusal, verified (no new platform announced)

Tests first:

- `tests/test_platform_refusal.py`: with `supported()` patched to return false, `init`, `check`, `doctor`, `workflow prepare`, `upgrade --dry-run` and `placeholders` exit 4 with `unsupported_platform` in both languages and create no file in the destination; `--help`, `--version`, `workflow list` and `pr-size` do not exit 4.
- A source test that `scripts/verify-source.py` reads every file with an explicit `encoding="utf-8"`.

Work: fix `scripts/verify-source.py` encodings; add `* text=auto eol=lf` to `.gitattributes`; add a `windows-latest` job to `.github/workflows/verify.yml` that runs only the new modules with `python -m unittest` (no `make`, `.venv\Scripts\python.exe`), plus a real `dixi init` that must exit 4 and leave the destination absent.

Done when: the new modules pass on Ubuntu, macOS and Windows runners; the Windows job shows exit 4 and no written file; the support matrix row links to the job.

### Phase 1 — WSL 2 as a supported path

Tests first: none new in code; the existing suite is the evidence because the code path is Linux.

Work: a "Windows (WSL 2)" section in local development docs and the support matrix; a recorded manual run (Ubuntu LTS on WSL 2, Python 3.11+, project under `~`) of `make verify`, `dixi init --agent claude --controls`, `dixi check`, `dixi upgrade --dry-run` and one blocked hook, stored in the contracts like the existing manual runs. Optional CI: a job on `windows-latest` that sets up a WSL distribution through an action pinned by SHA and runs `make verify` inside it.

Done when: the manual run is recorded with versions and outputs; the support matrix shows the WSL 2 row with that evidence and states that `/mnt/c` is unsupported; README es/en mention it.

### Phase 2 — Native backend through `ctypes` (only after validation)

Tests first, in `tests/test_windows_filesystem.py`, skipped off Windows and required on the Windows job:

- Junction as destination, as destination parent and as an intermediate project directory: `init` exits 3, `check` reports `unsafe_path`, nothing is written outside.
- Symlinked file and directory leaves (when the runner has the privilege): rejected.
- Race test: a thread swaps an intermediate directory for a junction in a loop while `init` runs; no byte is ever written outside the destination.
- Names: `nul.md`, `COM1`, `.git.`, `.git `, `.env ` and the 8.3 alias of a denied entry are rejected for reading and writing; `a:b` and `a\b` stay rejected.
- Long paths over 260 characters work or fail with a stable code, never partially.
- CRLF checkout: `upgrade --dry-run` on a project with `eol=lf` reports `unchanged`.
- Hooks: generated commands run with the Windows interpreter launcher and the agent's Windows shell; a missing interpreter is detected and reported by `doctor`, never silently allowed.

Work: `filesystem` backend split by platform with one interface; `supported()` true on Windows only when the backend loads and a self-test passes; native hook commands; `.gitattributes` in generated projects (declared in `pyproject.toml`, `MANIFEST.in` and `scripts/build-local.py`); threat model T02/T03 and the local core contract extended with the Windows mechanisms; the Windows CI job running the full new module plus the platform-neutral existing modules.

Done when: every phase 2 test passes on `windows-latest` with Python 3.11 and 3.13; the threat model lists each Windows test next to T02/T03; a manual run with Claude Code on native Windows is recorded; the support matrix announces native Windows with that evidence. If any of these fails, native Windows stays at exit 4.

## Related

- [ADR-102](ADR-102-recorte-de-alcance-v1.md)
- [ADR-103](ADR-103-ci-publica-en-github-actions.md)
- [ADR-105](ADR-105-opt-in-automated-controls.md)
- [Local core contract](../../07-contracts/commands/local-core-contract.md)
- [Automated controls contract](../../07-contracts/commands/automated-controls-contract.md)
- [Local core threat model](../../13-security/local-core-threat-model.md)
- [Support matrix](../../docs/support-matrix.md)
