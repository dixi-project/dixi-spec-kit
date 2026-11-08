# Contributing to DIXI Spec Kit

## Purpose

Explain how to propose changes. `main` is public and read-only for non-maintainers: anyone can clone, use and fork it; only Dixi maintainers merge, always through a reviewed pull request with green checks.

## How to propose a change

1. Open an issue before writing code for large changes (new commands, contract changes, new integrations).
2. Fork the repository and create a branch in your fork.
3. Set up the environment: `python3 -m venv .venv` and `.venv/bin/python -m pip --isolated install --index-url https://pypi.org/simple --only-binary=:all: --no-deps --require-hashes -r requirements-build.txt`.
4. Write the failing test first, then the code. Do not edit existing tests to make your code pass: if a test is wrong, explain why in the pull request.
5. Keep CLI messages in `src/dixi_spec_kit/locales/en.json` and `es.json`, and user documentation in English (Spanish summaries where they already exist).
6. Run `make verify` until it is green.
7. Sign every commit with `git commit -s` (DCO, below) and open the pull request against `main`.

## DCO

Every commit carries `Signed-off-by: Name <email>`, certifying the [Developer Certificate of Origin 1.1](https://developercertificate.org/): you have the right to submit the contribution under the project's MIT license. The `DCO sign-off` check enforces it. If you forgot: `git rebase --signoff main` and `git push --force-with-lease` to your fork's branch.

## AI and accountability

You may use AI agents, but a human signs every commit, ticks the pull request attestation and answers for the change. An agent never signs, attests or approves.

## Review and merge

CODEOWNERS assigns the maintainers. A pull request is merged only with all required checks green and after a maintainer has reviewed it. Nobody pushes directly or force-pushes to `main`.

## Trademark

"DIXI", "DIXI Spec Kit" and "Dixi Project" identify the official project. The MIT license lets you use, modify and redistribute the code; if you publish a modified version, use another name and do not present it as official.

## Resumen en español

`main` es público y de solo lectura para quien no mantiene el proyecto: cualquiera puede clonarlo, usarlo y hacer fork. Abre una issue para cambios grandes, trabaja en una rama de tu fork, escribe primero la prueba que falla, mantén los mensajes de la CLI en `en.json` y `es.json`, ejecuta `make verify`, firma cada commit con `git commit -s` (DCO 1.1) y abre un PR contra `main`. Las personas firman y atestan; los agentes de IA nunca firman ni aprueban. Solo los mantenedores integran, con revisión y checks en verde. Si redistribuyes una versión modificada, usa otro nombre.

## Related

- [Security](SECURITY.md)
- [License](LICENSE)
- [Agent instructions](AGENTS.md)
