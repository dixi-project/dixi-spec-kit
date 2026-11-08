# Contrato B1 — Núcleo local instalable

## Propósito

Concretar el primer bloque autorizado de TASK-001: ayuda, versión, `init --agent none`, `doctor` y `check`. Es un desarrollo local `1.0.0.dev0`, no una release pública. `upgrade` y adaptadores se implementarán en sus bloques.

## Interfaz

`dixi [--lang es|en] [--json] <comando>`; idioma por defecto `es`. JSON usa claves estables en inglés: `status`, `code`, `messages` (cada mensaje tiene `key`, `message` y parámetros), con códigos del contrato general. `--help` y `--version` funcionan sin proyecto. Opciones globales se escriben antes del subcomando.

- `init <directorio> [--agent none]`: destino ausente o vacío, padre existente, sin `..` ni symlinks en la ruta explícita. Solo `none` está distribuido en B1. No ejecuta hooks, Git, Make ni herramientas externas. Un fallo deja estado parcial identificado, sin limpiar archivos ajenos; no se sobrescribe al reintentar.
- `doctor`: diagnóstico local de runtime, recursos del paquete y capacidades de filesystem. No exige agente en modo `none`, ni credenciales, red o proveedor. Si hay metadata de proyecto, comprueba su formato.
- `check`: desde la raíz del proyecto, valida metadata, recursos obligatorios, enlaces Markdown locales y el grafo explícito de trazabilidad. No ejecuta el Makefile ni código del proyecto. Su éxito solo acredita estructura, no preparación para construir ni calidad de aplicación.

Primer entorno evaluado: macOS/POSIX con Python 3.15.2. Código previsto para Python >=3.11; otras versiones/sistemas quedan sin acreditar hasta ejecutar su matriz. El núcleo requiere operaciones POSIX con descriptores de directorio y `O_NOFOLLOW` para evitar seguir symlinks; un sistema sin ellas falla explícitamente, sin degradar esa protección.

## Archivos generados y metadata

Recursos originales de este producto, almacenados en catálogos JSON es/en dentro del paquete. No se copia ninguna norma ni plantilla propietaria del origen. Incluyen README, visión, dominio, módulo, feature, contrato y plan de pruebas en borrador, guía de uso documental, MODE, Makefile de comprobación estructural y exclusiones de contexto/secretos.

`.dixi/project.json`: `schema_version: 1`, `kit_version`, `language`, `agent: none`, `policy: portable`, `managed_files` como mapa ruta relativa → SHA-256 del archivo originalmente generado. No incluye su propio hash. Este registro es dato no confiable al leerlo, no una prueba criptográfica de procedencia. Compatibilidad (v1.0.0): `check` y `doctor` aceptan proyectos con `kit_version` de la misma versión mayor (`1.x.y`, con sufijo `.devN` o `rcN` opcional); otra mayor devuelve 4 y un valor mal formado, 1. `agent` admite `none` o `claude`.

`.dixi/traceability.json`: `schema_version: 1`, `items` como lista de objetos con `id`, `kind`, `path` y `parents`. Tipos y padres permitidos: `goal` sin padres; `domain → goal`; `module → domain`; `feature → module`; `contract → feature|module`; `test → contract|feature`. IDs únicos; padres existentes y del tipo permitido; rutas relativas dentro del proyecto. No se requiere código de aplicación para un borrador estructural válido.

La plantilla incluye un ejemplo de cadena documental marcada como borrador; un elemento `test` puede ser un plan de prueba, nunca evidencia de prueba ejecutada. El informe siempre indica que la verificación fue estructural y la aplicación requiere su propia escalera. Los campos pendientes permanecen marcados en los documentos; B1 no evalúa su completitud ni simula decisiones del usuario. Solo se comprueban los elementos declarados en el grafo, no su cobertura del negocio ni la existencia de pruebas ejecutables.

## Fronteras y límites

Se rechazan rutas absolutas en metadata, `..`, backslashes, caracteres de control, sustitutos Unicode, symlinks y archivos especiales. Se deniegan componentes `.env*`, `.aws`, `.ssh`, `.git`, `.context`, `id_rsa`, `id_ed25519` y extensiones `.pem`/`.key`, sin distinguir mayúsculas. Esto no detecta secretos guardados con otros nombres: tampoco se deben registrar en el inventario o grafo. Las lecturas se limitan a 1 MiB por archivo, 500 elementos de trazabilidad y 500 archivos gestionados; se rechazan tipos inesperados y claves JSON duplicadas.

El chequeo Markdown reconoce enlaces inline simples y definiciones de referencia de una línea, incluso si no se usan. Acepta destinos entre `<...>` con espacios y títulos opcionales. Máximo 500 destinos reconocidos por documento, etiquetas de hasta 999 caracteres y expresiones de destino de hasta 4 096 caracteres; un exceso de destinos devuelve `invalid_file`. Los enlaces web no se visitan; los locales se normalizan respecto al documento y se verifican sin salir de la raíz. Fragmentos y consultas no se validan. Es un analizador acotado, no un parser CommonMark: no interpreta anidación, escapes, HTML ni distingue ejemplos de código de texto. Las formas fuera de ese subconjunto no quedan certificadas por `check`.

La metadata no puede omitir recursos obligatorios del núcleo. Las modificaciones legítimas de documentos no se rechazan solo porque cambie su hash: ese baseline se conserva para la futura comparación de actualización. Un proyecto con versión de esquema o kit no soportada devuelve 4; proyecto ausente devuelve 2; contenido inconsistente devuelve 1; destino inseguro/ocupado devuelve 3; fallo E/S devuelve 5.

La inicialización usa creación exclusiva y descriptores de directorio, con marcador de ejecución. No ofrece transacción multiarchivo ni aislamiento frente a un atacante con control equivalente del proceso o del sistema. El chequeo es una lectura del estado observado; no certifica consistencia transaccional ante edición simultánea.

## Empaquetado y procedencia

Setuptools 84.2.1, exclusivamente para build: verificado en PyPI, autor Python Packaging Authority, origen `pypa/setuptools`, historial de archivos desde 2006-05-12. Wheel publicado 2026-10-20; SHA-256 `ca140b45d5325a9478f880e351484f62fef15f336462e449ca0c03c873d589c2`. Sin dependencias externas de ejecución. La licencia del producto sigue pendiente; no se declara MIT ni se publica.

Wheel y sdist solo incorporan código, recursos nuevos y metadata de empaquetado elegida. La verificación inspecciona el inventario, instala en entornos temporales limpios sin índice ni dependencias y prueba CLI, creación y `make verify` del proyecto generado. Ningún recurso heredado, `.context/`, archivo del workspace o historial privado debe viajar.

## Relacionados

- [Contrato general](command-contract.md)
- [Feature B1](../../05-features/local-core/feature-spec.md)
- [Threat model](../../13-security/local-core-threat-model.md)
- [Historia](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Setuptools en PyPI](https://pypi.org/project/setuptools/84.2.1/)
- [Guía de recursos de Setuptools](https://setuptools.pypa.io/en/latest/userguide/datafiles.html)
