# Estrategia de SBOM

## Propósito

Definir cómo el proyecto produce y conserva una lista de materiales de software (SBOM): un inventario legible por máquina de cada componente de cada versión, que permite responder rápido «¿nos afecta?» cuando aparece una vulnerabilidad o un problema de licencias.

Estado: borrador. {{pending: nombrar al responsable del proceso de SBOM}}

## Alcance

- Artefactos cubiertos: {{pending: p. ej. paquetes de la aplicación, imágenes de contenedor, bibliotecas}}
- Profundidad: dependencias directas y transitivas, imágenes base y binarios incluidos.
- Exclusiones y por qué: {{pending: listar}}

## Formato

- Formato de SBOM: {{pending: elegir un formato estándar abierto}}
- Identificadores de componentes: package URLs e identificadores de licencia SPDX cuando existan.
- Cada SBOM registra nombre del artefacto, versión, fecha de build y revisión del código fuente.

## Generación

| Momento | Artefacto | Ubicación de salida |
|---------|-----------|---------------------|
| Cada build de versión | {{pending: artefacto}} | {{pending: dónde se guarda}} |
| Bajo demanda | Rama principal actual | Salida del build |

Herramienta generadora: {{pending: elegir; este kit no exige ninguna concreta}}

Genera el SBOM a partir del artefacto construido o del lockfile usado en el build, no de una lista escrita a mano.

## Integridad y almacenamiento

- Guarda los SBOM junto a la versión que describen y consérvalos durante {{pending: plazo de conservación}}.
- {{pending: decidir si los SBOM se firman o llevan checksum}}

## Uso

- Alimenta con los SBOM los controles de vulnerabilidades y licencias.
- Cuando aparezca un aviso nuevo, busca en los SBOM guardados qué versiones están afectadas.
- {{pending: decidir si los SBOM se comparten con clientes y cómo}}

## Relacionados

- [Política de licencias](licensing-policy.md)
- [Licencias aprobadas](approved-licenses.md)
- [Escaneo de dependencias](../dependency-scanning.md)
- [Gestión de vulnerabilidades](../vulnerability-management.md)
