# Threat model STRIDE — Núcleo local B1

## Propósito

Identificar amenazas del instalador y verificadores antes de implementarlos. Alcance local: entradas CLI, recursos empaquetados, filesystem y metadata del proyecto; no hay IA, autenticación ni despliegue en B1.

## Activos y límites de confianza

Activos: archivos locales del usuario, recursos distribuibles, evidencia de verificación y privacidad de `.context/`. Las rutas y el proyecto inspeccionado son entrada no confiable; la distribución se construye con inventario explícito. Se confía en el runtime, sistema operativo y en que un atacante no controle el proceso con el mismo privilegio. Las operaciones se ejecutan sin elevar privilegios.

## Amenazas y pruebas

| ID / STRIDE | Amenaza | Mitigación | Prueba ejecutable |
|---|---|---|---|
| T01 / Spoofing | Proyecto falso o formato incompatible. | Metadata tipada, esquema/versión/selección explícitos. | `test_invalid_metadata`, `test_missing_project`, `test_unsupported_schema` |
| T02 / Tampering | Sobrescribir trabajo existente/reintento o escapes de ruta. | Prevalidación, creación exclusiva, rechazo de traversal y conservación del estado parcial. | `test_nonempty_unchanged`, `test_repeated_init`, `test_traversal_destination`, `test_interrupted_initialization_preserves_partial_files` |
| T03 / Elevation | Seguir symlinks del destino, metadata o documentos. | Descriptores, O_NOFOLLOW y comprobación de tipo sin apertura bloqueante. | `test_symlink_destination`, `test_symlink_parent`, `test_symlink_metadata`, `test_symlink_document`, `test_fifo_document` |
| T04 / Information disclosure | Leer secretos o archivos externos mediante JSON/enlaces. | Rutas confinadas, denegación de nombres sensibles independiente de mayúsculas, sin red ni ejecución. | `test_external_metadata_path`, `test_external_link`, `test_unsafe_path_spellings`, `test_check_does_not_execute`, `test_no_network` |
| T05 / Denial of service | JSON/texto excesivos, Unicode inválido, demasiados enlaces, IDs/tipos malformados. | Límites de lectura/cantidad y patrones acotados; validación de tipos/claves únicas y rutas. | `test_oversized_metadata`, `test_duplicate_json_keys`, `test_invalid_metadata`, `test_duplicate_ids`, `test_invalid_unicode_metadata`, `test_many_links_limit`, `test_unclosed_markdown_is_bounded`, `test_empty_and_spaced_destinations` |
| T06 / Repudiation | Afirmar verificación de aplicación o cambiar archivos al inspeccionar. | Informe de alcance estructural, códigos estables, lectura sin escrituras; subconjunto Markdown documentado. | `test_check_read_only`, `test_generated_project_passes`, `test_broken_parent`, `test_broken_link`, `test_broken_reference_link`, `test_reference_links_with_valid_destinations` |
| T07 / Information disclosure | Filtrar material privado mediante wheel/sdist. | Inventario permitido, recursos originales, pruebas del archivo final. | `test_artifact_allowlist`, `test_clean_installations` |
| T08 / Tampering | Omitir archivos obligatorios alterando el inventario. | Comparar nombres requeridos con recursos de la versión instalada. | `test_missing_required_file`, `test_incomplete_inventory` |

## Riesgo residual y revisión

Riesgo alto por escritura en filesystem y datos externos. No se garantiza atomicidad multiarchivo ni protección frente a un atacante con control del propio proceso. La lectura no representa un snapshot transaccional. La denegación de nombres sensibles no detecta secretos bajo nombres arbitrarios. El analizador de enlaces no cubre todo CommonMark ni acredita completitud semántica de las specs. La distribución no se publica hasta resolver derechos, escaneo de contenido/historial y controles de release. Nuevos adaptadores y ejecución de agentes requieren extender este threat model.

## Relacionados

- [Contrato](../07-contracts/commands/local-core-contract.md)
- [Feature](../05-features/local-core/feature-spec.md)
- [Historia](../tasks/backlog/TASK-001-lanzamiento-v1.md)
