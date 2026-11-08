# Comparación con GitHub Spec Kit

## Propósito

Ubicar el avance de DIXI Spec Kit frente a GitHub Spec Kit para priorizar lo que falta antes de publicar. Es un análisis interno de planificación, no material de marketing: no afirma paridad ni superioridad.

## Fuente y vigencia

Datos de github/spec-kit tomados el 2026-11-08 de su README, su página de releases y su sitio de documentación. No se leyeron sus Issues ni su CHANGELOG. Cifras como versión, releases o estrellas cambian con rapidez; verificar antes de citarlas. El estado de DIXI corresponde a la rama de trabajo en esa fecha.

## Estado comparado

| Área | GitHub Spec Kit | DIXI Spec Kit |
|---|---|---|
| Madurez | v1.3.2 publicada el 06-nov; diez releases en unas tres semanas | `1.0.0.dev0` local, sin release |
| Licencia | MIT | MIT propuesta; derechos y decisión pendientes |
| Instalación | `uv tool install`, `uvx`, pipx, pip y wheels air-gapped | Wheel y sdist locales; nombres sin verificar en registro |
| Agentes | 41 integraciones, más `none` y `generic` | Ninguno; solo `--agent none` |
| Comandos en el agente | constitution, specify, clarify, plan, checklist, tasks, analyze, implement, converge | Ninguno instalable; 16 propuestos |
| CLI | init, check, version, self check, integration, extension, mcp | init, doctor, check, workflow list/show/prepare |
| Extensibilidad | Extensiones, presets, workflows, bundles, catálogos | No existe |
| Comunidad | CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT, sitio de docs, READMEs en tres idiomas | No preparada |
| Sistemas | Linux, macOS y Windows | Solo macOS probado |

## Brecha principal

La propuesta de valor de Spec Kit es instalar comandos en el agente que la persona ya usa. DIXI hoy crea documentos y prepara contexto de forma determinista, pero no instala comandos en ningún agente.

## Diferencias que DIXI puede sostener con evidencia propia

Cada una requiere el ejemplo público ejecutado antes de anunciarse.

- Comprobación mecánica de la cadena negocio → dominio → módulo → feature → contrato → prueba mediante `dixi check`.
- Gates humanos explícitos: la IA no firma, atestigua, aprueba ni integra; las pruebas congeladas no se modifican.
- Diseño de dominios, arquitectura, contratos y amenazas, y análisis de impacto al cambiar una feature.
- Núcleo independiente del agente documentado en ADR-101.
- Ejecución de la CLI con biblioteca estándar y verificación de rutas, symlinks y límites con pruebas de regresión.

## Qué falta para publicar

Bloqueantes: licencia y derechos; al menos un adaptador de agente con comandos instalados; nombres verificados; instalación sin clonar el repositorio; ejemplo público de idea a código verificado; README es/en y archivos de comunidad; historial limpio y protección de ramas. Aplazables: `upgrade`, Linux y Windows, comandos especializados, segundo lenguaje y segundo adaptador, extensiones. La propuesta de alcance está en [ADR-102](../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md).

## Relacionados

- [ADR-102](../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md)
- [Catálogo de comandos](command-catalog.md)
- [Publicación](publication-readiness.md)
- [Producto](product-spec.md)
- [TASK-003](../tasks/backlog/TASK-003-adaptador-claude-code.md)
