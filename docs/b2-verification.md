# Evidencia B2a — Procedimientos compartidos

## Propósito

Registrar la verificación local de TASK-002 el 2026-11-07. B2a aporta consulta y preparación determinista de ocho procedimientos; no certifica ejecución de agentes ni cierra B2 o el lanzamiento v1.0.0.

## Resultado

`make verify` terminó con código 0: **71 pruebas correctas en 24,111 segundos de suite**. Entorno: macOS 27.2 arm64, Python 3.15.2, Setuptools 84.2.1 previamente verificado y fijado por hash. Sin dependencias nuevas.

| Conjunto | Casos | Alcance |
|---|---:|---|
| Regresión B1 | 43 | CLI original, filesystem, enlaces, metadata e instalación. |
| Procedimientos B2a | 24 | Ocho recetas es/en, entradas/objetivos, grafo, límites, manifiesto, repetición y ausencia de escritura/red/ejecución. |
| Casos adicionales | 3 | Campos desconocidos excluidos, solicitud Unicode inválida y ancestro compartido sin duplicados. |
| Distribución B2a | 1 | Instala el wheel y el reconstruido desde sdist en entornos limpios; prepara `plan` en es/en con ambos. |

Se construyeron wheel/sdist, se comprobó sintaxis, paridad es/en y whitespace. Las pruebas congeladas de B1 y B2a permanecen intactas. La salida legible de `workflow show discover` se inspeccionó: propósito, entradas, pasos, salidas esperadas, gates, comprobaciones y guardas en español.

Tras actualizar documentación se verificaron estructura y enlaces locales de 30 archivos Markdown, además de conservar íntegramente las reglas heredadas de `AGENTS.md`. Se repitió la comprobación de sintaxis/catálogos/whitespace; la implementación y recursos no cambiaron después del build final.

El wheel actualizado quedó instalado en `.venv` mediante `--no-index --no-deps`. Un proyecto de notas ficticias creado en `.context/` permitió preparar las ocho operaciones desde ese ejecutable. Es una demostración de preparación: las specs generadas por init siguen en borrador y no se presentan como artefactos completados del procedimiento.

## Secuencia de pruebas

- Baseline previo: 43 pruebas B1 correctas, registrado en `.context/b2-baseline.log`.
- `ca43f17`: 25 casos nuevos congelados antes de implementar. Conjunto rojo frente al CLI sin `workflow`; log `.context/b2-red.log`.
- `d4d6f93`: tres casos adicionales antes de corregir la propagación de campos desconocidos del objetivo. El caso malicioso provocó `UnicodeEncodeError`; el arreglo proyecta solo `id`, `kind`, `path` y `parents`. Log `.context/b2-edges-red.log`.
- Resultado final: `.context/b2-verify.log`. Demostración instalada: `.context/b2-demo-result.json`. Logs y proyectos privados no se distribuyen.

Los commits de pruebas no llevan firma ni atestación humana. Implementación y documentos permanecen en el working tree para revisión. No se hizo push, merge ni publicación, ni se actuó como aprobador.

## Artefactos de la ejecución final

Versión local `1.0.0.dev0`; los hashes identifican este build y sustituyen los artefactos locales anteriores. No se promete reproducción bit a bit.

| Archivo en dist/ | Bytes | SHA-256 |
|---|---:|---|
| `dixi_spec_kit-1.0.0.dev0-py3-none-any.whl` | 28 503 | `045b73f69fa1970d18b4b375348d965bc8ee13d374c421bbaca6502692b89d7c` |
| `dixi_spec_kit-1.0.0.dev0.tar.gz` | 23 471 | `59ad2030b1d52be30aeccb2364f6a57682a47c3959b9493533ae5407f645e71e` |

Se amplió la lista explícita de empaquetado con `workflows.py`, `resources/workflows.json` y recetas `workflows.es.json`/`workflows.en.json`. Los recursos son nuevos del producto; no se copiaron normas privadas. El manifiesto del paquete conserva la exclusión de contexto, historial y configuración operativa del workspace.

## Límites y siguiente paso

Solo se verifica consulta/preparación: ID compatible, referencias declaradas, hashes y recursos. No se verifica semántica, consentimiento, calidad del diseño, ejecución de los pasos ni enforcement de guardas por un LLM externo. Los límites y condiciones de lectura están en el contrato. No hay snapshot transaccional; las fuentes pueden cambiar después de leerlas.

No se ejecutaron evaluaciones de adaptadores, pruebas en otros sistemas/Python, cobertura, mutation, gitleaks o semgrep. Los controles exigidos antes de publicar, derechos/licencia y release siguen pendientes.

El siguiente incremento debe conectar las mismas recetas con integraciones opcionales y evaluar artefactos, preguntas faltantes, conflictos y gates sobre el ejemplo. Esas evaluaciones completarán evidencia de B2; TASK-001 y el recorrido guiado continúan abiertos.

## Relacionados

- [Guía es/en](workflow-quickstart.md)
- [Tarea](../tasks/backlog/TASK-002-operaciones-compartidas-b2.md)
- [Feature](../05-features/workflow-preparation/feature-spec.md)
- [Contrato](../07-contracts/commands/workflow-preparation-contract.md)
- [Amenazas](../13-security/workflow-preparation-threat-model.md)
- [Evidencia histórica B1](b1-verification.md)
- [Publicación](publication-readiness.md)
