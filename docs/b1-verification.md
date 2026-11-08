# Evidencia B1 — Núcleo local de DIXI Spec Kit

## Propósito

Registrar el resultado técnico del primer bloque autorizado de TASK-001 y sus límites. Fecha: 2026-11-06. Versión local `1.0.0.dev0`; objetivo de lanzamiento `v1.0.0`. Este informe no constituye aprobación humana de PR ni habilita publicación.

## Resultado observado

`make verify` terminó con código 0: **43 pruebas, todas correctas**, en 8,434 segundos de suite. Entorno observado: macOS 27.2, arm64, Python 3.15.2; entorno de build `.venv` con Setuptools 84.2.1. Se comprobó sintaxis Python, paridad de catálogos/recursos es/en y diferencias de whitespace con Git.

| Conjunto | Casos | Evidencia |
|---|---:|---|
| Contrato CLI | 33 | Ayuda/versión, es/en, creación sin agente, errores, preservación de archivos, metadata, enlaces, grafo, symlinks/FIFO, ausencia de ejecución y sockets bloqueados. |
| Distribución | 2 | Inventario de wheel/sdist; reconstrucción desde sdist, instalaciones limpias sin índice/dependencias, CLI instalada y Makefile del proyecto generado. |
| Seguridad adicional | 7 | Unicode inválido, nombres sensibles con mayúsculas, 501 enlaces, Markdown incompleto, referencias válidas/rotas e interrupción de escritura. |
| Destinos Markdown | 1 | Destino vacío, fragmento y rutas con espacios en enlaces inline/por referencia. |

Los tests de distribución usan dos entornos temporales: uno instala el wheel original y otro el reconstruido desde sdist. En ambos funcionan versión, `init`, `check`, `doctor` y el `make verify` generado. La reconstrucción usa el entorno de build local; esto no acredita builds reproducibles bit a bit ni toda la matriz de Python.

Después de actualizar las guías se comprobaron los enlaces locales de 24 documentos Markdown nuevos/modificados y la conservación íntegra de las reglas heredadas de `AGENTS.md`. Se repitió la comprobación de sintaxis/catálogos/whitespace. El wheel quedó instalado en `.venv` con `--no-index --no-deps`; `.venv/bin/dixi --version` confirmó `1.0.0.dev0`.

## Pruebas antes de implementación

| Commit local | Cambio y rojo observado |
|---|---|
| `e768a2a` | 33 casos CLI inicialmente fallaron frente al stub; incluye los dos contratos de distribución. |
| `d80ee0c` | Añade siete casos de seguridad antes de corregir referencias, Unicode/rutas sensibles y exceso de enlaces. Hubo once fallos contando subcasos. |
| `a5143b5` | Añade el caso de destinos vacíos/espaciados; detectó un `IndexError` antes de corregirlo. |

Los tres commits contienen solo pruebas nuevas, sin firma ni `Signed-off-by` de una persona. Ninguna prueba congelada se modificó para alcanzar verde. Implementación y documentación permanecen en el working tree para revisión; no hay push, merge ni release realizados por este bloque. La persona responsable deberá completar la procedencia y revisión requeridas antes de integrar.

Logs privados: `.context/b1-red.log`, `.context/b1-safety-red.log`, `.context/b1-links-red.log` y `.context/b1-verify.log`. No se distribuyen.

## Artefactos de esta ejecución

Registro histórico del build B1 del 2026-11-06. Los archivos locales en `dist/` fueron sustituidos por el incremento B2a; consultar sus [hashes actuales](b2-verification.md).

| Archivo en `dist/` | Bytes | SHA-256 |
|---|---:|---|
| `dixi_spec_kit-1.0.0.dev0-py3-none-any.whl` | 14 663 | `d0c7e932b4d2b200a9c349e88fab1b9d53a011108a3e29d5ea248c47718851ab` |
| `dixi_spec_kit-1.0.0.dev0.tar.gz` | 11 663 | `5170f32706f21fe62ad76bb6ec05fa33d07968315df9aa2bff7cc5ac7d3a0a99` |

Los hashes identifican esta construcción local; una nueva construcción puede cambiar por timestamps. `scripts/build-local.py` copia una lista explícita a staging temporal y `MANIFEST.in` restringe sdist. Los artefactos contienen código y recursos nuevos de B1, metadata de empaquetado y README de uso local; excluyen normas heredadas, contexto, historial, configuración de trabajo y pruebas del repositorio. La licencia de publicación continúa pendiente.

## Alcance y pendientes

- Solo `init --agent none`, `doctor`, `check`, ayuda/versión. Sin comandos de agente, actualización ni perfiles de stack implementados.
- Python >=3.11 es un requisito declarado; solo se probó 3.15.2/macOS. Otras versiones y Linux no tienen evidencia aún. Windows carece del soporte requerido en B1. El tag `py3-none-any` del wheel no certifica sistemas operativos.
- `check` acredita estructura sobre archivos y grafo declarados. No acredita contenido completo, cobertura del negocio, pruebas ejecutadas o preparación para producción. El parser Markdown es limitado; detalles en el contrato.
- El inventario registra hashes originales para una futura actualización; no autentica procedencia. No hay transacción multiarchivo ni snapshot frente a edición concurrente.
- Las pruebas no se modifican desde el CLI. Las reglas para agentes son documentales; B1 no instala hooks, CI, revisión humana ni controles de proveedores.
- No se ejecutaron gitleaks, semgrep, cobertura, mutation testing ni evaluaciones de agentes. El inventario y las pruebas de distribución no sustituyen el escaneo de contenido/historial exigido antes de publicar.
- TASK-001 permanece abierta: B2–B5, derechos/licencia, mecanismos operativos, matriz de soporte, documentación pública, controles de contribución y lanzamiento siguen pendientes.

## Relacionados

- [Guía local es/en](local-development.md)
- [Feature y aceptación](../05-features/local-core/feature-spec.md)
- [Contrato B1](../07-contracts/commands/local-core-contract.md)
- [Amenazas](../13-security/local-core-threat-model.md)
- [Historia](../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Puerta de publicación](publication-readiness.md)
