# Contribuir a DIXI Spec Kit / Contributing

## Propósito

Explicar cómo proponer cambios. `main` es público y de solo lectura para quien no mantiene el proyecto: cualquiera puede clonarlo, usarlo y hacer fork; solo los mantenedores de Dixi integran cambios, siempre por PR revisado y con checks en verde.

## Cómo proponer un cambio

1. Abre una issue para cambios grandes (nuevos comandos, cambios de contrato, nuevas integraciones) antes de escribir código.
2. Haz fork y crea una rama en tu fork.
3. Prepara el entorno: `python3 -m venv .venv` y `.venv/bin/python -m pip --isolated install --index-url https://pypi.org/simple --only-binary=:all: --no-deps --require-hashes -r requirements-build.txt`.
4. Escribe primero la prueba que falla; después el código. No modifiques pruebas existentes para que tu código pase: si una prueba está mal, explícalo en el PR.
5. Mantén mensajes de la CLI en `src/dixi_spec_kit/locales/es.json` y `en.json`, y la documentación en ambos idiomas.
6. Ejecuta `make verify` hasta verlo en verde.
7. Firma cada commit con `git commit -s` (DCO, abajo) y abre el PR contra `main`.

## DCO

Cada commit lleva `Signed-off-by: Nombre <correo>`, con el que certificas el [Developer Certificate of Origin 1.1](https://developercertificate.org/): tienes derecho a enviar la contribución bajo la licencia MIT del proyecto. El check `DCO sign-off` lo comprueba. Si olvidaste firmar: `git rebase --signoff main` y `git push --force-with-lease` en la rama de tu fork.

## IA y responsabilidad

Puedes usar agentes de IA, pero una persona firma cada commit, marca la atestación del PR y responde por el cambio. Un agente nunca firma, atesta ni aprueba.

## Revisión e integración

CODEOWNERS asigna a los mantenedores. Un PR se integra con al menos una aprobación de un mantenedor y todos los checks en verde. Nadie hace push directo a `main` ni force push sobre ella.

## Marca

«DIXI», «DIXI Spec Kit» y «Dixi Project» identifican el proyecto oficial. La licencia MIT permite usar, modificar y redistribuir el código; si publicas una versión modificada, usa otro nombre y no la presentes como oficial.

## English summary

`main` is public and read-only for non-maintainers: anyone can clone, use and fork. Open an issue for large changes, work in a branch of your fork, write the failing test first, keep CLI messages and docs in Spanish and English, run `make verify`, sign every commit with `git commit -s` (DCO 1.1) and open a PR against `main`. Humans sign and attest; AI agents never sign or approve. Only maintainers merge, after review and green checks. "DIXI", "DIXI Spec Kit" and "Dixi Project" identify the official project: if you redistribute a modified version, use another name.

## Relacionados

- [Seguridad / Security](SECURITY.md)
- [Licencia / License](LICENSE)
- [Instrucciones para agentes / Agent instructions](AGENTS.md)
