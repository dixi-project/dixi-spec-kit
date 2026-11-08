# Puerta de publicación de DIXI Spec Kit v1.0.0

## Propósito

Definir evidencia concreta por fase: preparación antes de crear el repositorio, configuración antes de exponerlo y verificación del lanzamiento. El usuario autorizó la creación cuando esté listo; no hace falta solicitar de nuevo esa autorización general. Estado al 2026-11-08: v1.0.0 publicada. Siguen abiertas la evaluación manual de los comandos en Claude Code y la validación completa de ADR-101 (conjuntos de políticas, fuera de v1.0.0).

Las secciones de producto/licencia, evidencia técnica y documentación/mantenimiento son requisitos de entrada a publicación. La creación del repositorio y de la release se comprueban después, en sus fases; no son requisitos para iniciar su propia creación.

## Avance local B1 — 2026-11-06

Dirección abierta e inicio incremental autorizados. [B1 verificado](b1-verification.md): 43 pruebas, wheel/sdist locales, instalaciones limpias, modo sin agente y `make verify` del proyecto documental. Esta evidencia es parcial respecto a los requisitos de lanzamiento siguientes; no confirma el alcance completo, actualización, adaptadores, derechos/licencia ni controles de publicación. Las casillas globales permanecen abiertas cuando incluyen trabajo de bloques posteriores.

Actualización 2026-11-07: [B2a verificado](b2-verification.md) amplía la suite a 71 casos y añade consulta/preparación de ocho procedimientos comunes. No acredita aún ejecución/evaluación de agentes ni cierra requisitos globales.

Actualización 2026-11-08: [comparación con GitHub Spec Kit](spec-kit-comparison.md) y [ADR-102](../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md) proponen reducir el alcance mínimo. Validado por la persona responsable el mismo día, junto con licencia MIT + DCO y `upgrade` aplazado a v1.1. Las casillas que dependían del alcance anterior se ajustan a ADR-102.

## Producto y licencia

- [x] Historia TASK-001 y decisiones estructurales validadas (2026-11-08, ADR-102).
- [ ] ADR-101 validado; separación del núcleo, integraciones, stacks y políticas implementada sin contradicciones con las normas efectivas de cada conjunto.
- [x] Derechos de distribución confirmados y licencia pública final aplicada (MIT; solo material escrito para el producto).
- [x] Atribuciones de terceros y alcance de la licencia de proyectos generados documentados (sin material de terceros distribuido; ADR-100 punto 5).
- [x] Nombres del repositorio, paquete y ejecutable comprobados ([B3](b3-verification.md)).
- [x] Primer lanzamiento identificado como v1.0.0; no reutilizar releases privadas.

## Evidencia técnica

- [x] Pruebas de aceptación en su propio commit antes de implementar, sin firma de agente.
- [x] `make verify` definido y en verde en el producto y el ejemplo generado.
- [x] Wheel y sdist contienen todos los recursos y se instalan en un entorno limpio.
- [x] Instalación y `init` no acceden al repo privado, AWS ni el sistema interno de tareas.
- [x] Conflictos, destinos no vacíos y symlinks no pierden archivos locales (actualización aplazada a v1.1).
- [x] Sistemas operativos y agentes anunciados tienen evidencia real de soporte: CI en verde en Ubuntu y macOS con Python 3.11 y 3.13; Claude Code con evidencia local.
- [x] Uso documental sin agente probado; integración elegible sin alterar los formatos canónicos.
- [x] Ejemplo público evaluado con el adaptador anunciado (Claude Code); matriz de capacidades/controles y límites de soporte publicada. El segundo lenguaje pasa a v1.1 (ADR-102).
- [x] Catálogo incluido y contratos validados; todos los comandos instalados referencian recursos presentes y distribuibles.
- [x] Ejemplo ejecutado de descubrimiento a código verificado y revisión preparada, más una evolución con análisis de impacto.
- [ ] Pruebas deterministas y evaluaciones del agente cubren errores, gates, repetición y continuidad de los comandos anunciados. Deterministas listas; falta la evaluación manual en una sesión nueva de Claude Code.
- [x] Manifiesto de recursos revisado (exportador por lista permitida), enlaces válidos y escaneo de secretos sin hallazgos.

## Documentación y mantenimiento

- [x] README y quickstart es/en, ejemplo y demostración reproducible.
- [x] CONTRIBUTING, SECURITY, soporte, mantenedores y política de marca preparados.
- [x] Checks de contribuciones externas aislados de infraestructura y credenciales internas; runners decididos en ADR-103 (aceptado).
- [x] CODEOWNERS real y configuración de reglas preparada antes de recibir contribuciones ([configuración](repository-settings.md)).

## Entrada a publicación y configuración del repositorio

- [x] Nuevo historial construido solo con material distribuible, en un repositorio nuevo; la preparación queda archivada en un repositorio privado aparte.
- [x] Repositorio `dixi-project/dixi-spec-kit` creado, público y protegido con el ruleset `main-protegida`: PR obligatorio, checks y DCO obligatorios, sin force push ni eliminación de `main`.
- [x] Persona firma los commits y realiza la integración según la política aplicable. Un agente no firma, atesta, aprueba ni integra.

La selección distribuible y el historial limpio se revisan antes de crear el remoto. La configuración protectora debe quedar comprobada antes de exponer o anunciar el repositorio. Si la creación es primero privada para configurar protecciones, el cambio a público ocurre después de revisar el contenido final.

## Lanzamiento

- [x] Release v1.0.0 creada desde `f317065` (firmado por la persona y en verde en CI), con wheel y sdist.
- [x] Publicación en PyPI aplazada a v1.1; instalación desde Git, `uv tool install` y wheel de la release documentada y probada.

## Relacionados

- [Historia](../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Plan](../ROADMAP.md)
- [Configuración del repositorio](repository-settings.md)
