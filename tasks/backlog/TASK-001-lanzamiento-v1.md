# TASK-001 — Primera distribución pública DIXI Spec Kit v1.0.0

## Propósito

Definir una historia verificable antes de implementar una distribución pública derivada de materiales seleccionados de EIS-IA.

## Metadata

- Tipo: feature. Prioridad: P1. Nivel: 3, estructural.
- Estado: en curso; B1 y B2a implementados; B3 (adaptador Claude Code, [TASK-003](TASK-003-adaptador-claude-code.md)) en curso.
- Creado: 2026-11-06. Product Owner: Alfredo Castillejos.
- Validación: el 2026-11-06 el usuario aceptó continuar con el enfoque abierto a agentes/lenguajes y el primer bloque funcional con pruebas primero. Se autoriza implementación incremental de TASK-001, empezando por CLI/paquete, `init --agent none`, `doctor`, `check`, ayuda/versión. La autorización previa de publicar cuando esté listo continúa. El 2026-11-08 la persona responsable validó el conjunto historia + [ADR-102](../../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md) + supuestos: recorte de alcance, licencia MIT + DCO y `upgrade --dry-run` aplazado a v1.1. Los criterios 5, 12, 13, 15 y 16 se ajustaron a ese recorte.

## Historia de usuario

Como responsable de Dixi Project,
quiero ofrecer DIXI Spec Kit como herramienta pública instalable y versionada con comandos para definir, construir, verificar y evolucionar productos,
para que terceros puedan aplicar nuestro ecosistema de desarrollo SDD con el agente y stack que elijan, crear forks y adoptar mejoras, manteniendo Dixi el control del repositorio oficial.

## Criterios de aceptación

1. Una persona externa instala el artefacto de v1 y consulta ayuda y versión sin credenciales de Dixi.
2. Puede generar un proyecto nuevo y ejecutar sus comprobaciones sin acceso al repositorio privado ni registro en el sistema interno de tareas.
3. Un destino no vacío o un conflicto no provoca sobrescritura ni borrado de trabajo del usuario.
4. Puede conocer requisitos y problemas de su entorno mediante diagnóstico y códigos de salida documentados.
5. ~~Puede previsualizar una actualización sin cambiar ningún archivo~~ — aplazado a v1.1 (ADR-102). En v1.0.0 la documentación no promete actualización y `dixi --help` no la muestra.
6. Encuentra guía de instalación en español e inglés, ejemplo reproducible y soporte de agentes/sistemas anunciado con evidencia.
7. La distribución contiene solo materiales seleccionados con derechos confirmados, sin historia ni configuración operativa privada.
8. El repositorio público permite forks; solo mantenedores autorizados pueden incorporar cambios mediante el proceso de revisión y checks.
9. La primera release pública se identifica como v1.0.0, independientemente de las versiones privadas de EIS-IA.
10. En el agente soportado, una persona recorre descubrimiento → especificación → plan → tareas → construcción → verificación → preparación de revisión sobre el ejemplo público, con artefactos enlazados y resultados comprobables.
11. Los comandos incluidos tienen contratos de entradas, salidas, errores, gates y continuidad; una interrupción o repetición no sobrescribe silenciosamente decisiones ni cambios locales.
12. Puede preparar diseño de dominios, arquitectura, contratos y amenazas mediante `dixi workflow prepare`, y obtener con `/dixi.analyze` un informe de trazabilidad e impacto al cambiar una feature. Los gates aplicables se respetan y las pruebas congeladas no se modifican.
13. Puede consultar el estado y el siguiente paso con `/dixi.status`; la ayuda distingue comandos instalados de capacidades aún no incluidas. `handoff` pasa a v1.1.
14. Puede usar el núcleo documental y sus validaciones sin un agente obligatorio, o elegir una integración publicada; instalar una integración no modifica sus specs, contratos ni tareas para adaptarlos a un formato exclusivo.
15. Puede aplicar el método a distintos lenguajes y frameworks; el runtime de la CLI no fija el del proyecto. En v1.0.0 un ejemplo público demuestra el recorrido; el segundo lenguaje pasa a v1.1 (ADR-102).
16. Puede consultar capacidades y controles de la integración publicada (matriz de soporte); una capacidad ausente se informa y no se presenta como automatización o protección disponible.

## Reglas de negocio

1. el repositorio privado de EIS-IA permanece privado y no se altera para esta preparación.
2. Una instalación no requiere cuentas internas, no crea remotos ni consume IA o AWS por sorpresa.
3. Se preserva la trazabilidad y la responsabilidad humana; la IA no firma, atesta, aprueba ni integra.
4. No se anuncia un comando, integración o licencia que aún no esté implementado o resuelto.
5. Las normas AWS/Bedrock no se relajan sin ADR de excepción.
6. El remoto público se crea cuando se cumpla la puerta de publicación, según la autorización del usuario.
7. El núcleo no exige un agente, modelo, lenguaje o framework específico. La elección de proveedores/políticas para proyectos externos se rige por ADR-101 una vez validado, sin cambiar las normas del origen ni de desarrollo de este repositorio.

## La historia se considera terminada cuando

1. La historia y el ADR fueron validados por la persona responsable.
2. Los criterios tienen pruebas de aceptación y seguridad; primero se registra el rojo en su propio commit.
3. `make verify` pasa y se prueba instalación desde wheel y sdist en entornos limpios, además del ejemplo generado.
4. El inventario distribuido, los derechos y el escaneo de secretos están resueltos.
5. Documentación es/en y procedimiento de mantenimiento reflejan la implementación final.
6. Se verifica la configuración del repositorio público y la release v1.0.0, respetando las acciones reservadas a una persona.
7. Los comandos distribuidos pasan sus pruebas de scripts y evaluaciones del agente; el ejemplo cubre creación y evolución, y no referencia recursos privados o ausentes.

## Supuestos para revisar

- S1: adoptado en B1: CLI Python con biblioteca estándar en ejecución y recursos empaquetados. Esto no restringe los lenguajes de los proyectos. Setuptools se usa solo para build; procedencia y versión en el contrato B1.
- S2: `dixi` como ejecutable y `dixi-spec-kit` como paquete/repositorio. El repositorio `dixi-project/dixi-spec-kit` ya existe (privado); la disponibilidad en PyPI se resuelve al publicar el paquete, operación separada de v1.0.0.
- S3: núcleo independiente del agente por indicación del usuario. Validado ADR-102: Claude Code es el único adaptador de v1.0.0, junto con uso documental sin integración; Codex pasa a v1.1. No anunciar compatibilidad por tener AGENTS.md; cada adaptador necesita pruebas propias y matriz de controles.
- S4: resuelto: MIT + DCO (2026-11-08). Solo se distribuyen materiales escritos para este producto.
- S5: resuelto: actualización aplazada a v1.1.
- S6: el catálogo propuesto cubre el recorrido principal y las capacidades de diseño y trazabilidad de Dixi; las interfaces especializadas se priorizan explícitamente antes de anunciar v1. El usuario pidió contemplar comandos faltantes; la selección y los contratos concretos siguen pendientes de validación.
- S7: los nombres `/dixi.*` son conceptuales hasta comprobar la sintaxis del adaptador. Las pruebas deterministas y las evaluaciones del agente aportan evidencias distintas y ambas son necesarias.
- S8: propuesta concreta de revisión: 16 comandos del agente y cuatro operaciones CLI; nueve entradas especializadas por priorizar. El contrato propone limitar actualización a dry-run en v1 y usar un ejemplo público de notas ficticias para evaluar el recorrido y su evolución. Estas decisiones siguen pendientes de validación conjunta.
- S9: ADR-101 registra la dirección aceptada y propone mecanismos de políticas públicas portables y organizativas Dixi. Las excepciones operativas siguen pendientes para sus bloques. La apertura no acredita soporte técnico universal ni autoriza otras plataformas para desarrollar/publicar este repositorio; B1 no consume IA ni despliega.

## Avance B1

Implementados ayuda/versión, creación sin agente, diagnóstico, comprobación estructural y distribución local `1.0.0.dev0`. Pruebas de aceptación congeladas antes de implementar; regresiones de seguridad añadidas en commits separados. Recursos escritos para este producto, sin copiar plantillas propietarias. Ver [informe de verificación](../../docs/b1-verification.md) y [guía local](../../docs/local-development.md).

Esto aporta evidencia parcial a los criterios 1–4, 6, 11 y 14. No completa la historia: faltan actualización, comandos/adaptadores, ejemplos en dos lenguajes, controles operativos, matriz ampliada, derechos/licencia, escaneo de publicación y release.

## Avance B2a — 2026-11-07

[TASK-002](TASK-002-operaciones-compartidas-b2.md) implementa `workflow list/show/prepare` para las ocho recetas de definición/diseño. Ver [evidencia](../../docs/b2-verification.md). Aporta preparación común y contexto verificable; la producción de artefactos y evaluación en integraciones siguen pendientes. No completa los criterios de ejecución del agente ni el lanzamiento.

## Recorte validado — 2026-11-08

[ADR-102](../../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md) quedó aceptado: un adaptador, diez comandos, un ejemplo y upgrade aplazado, tras la [comparación con GitHub Spec Kit](../../docs/spec-kit-comparison.md). El bloque derivado es [TASK-003](TASK-003-adaptador-claude-code.md).

## Avance v1.0.0 — 2026-11-08

Adaptador Claude Code, ejemplo, documentación pública, CI (ADR-103 propuesto), exportador por lista permitida, licencia MIT y versión 1.0.0 verificados ([evidencia](../../docs/b3-verification.md)). Quedan las acciones reservadas a una persona de la [puerta de publicación](../../docs/publication-readiness.md).

## Trazabilidad

- [Producto](../../docs/product-spec.md)
- [Catálogo de comandos propuesto](../../docs/command-catalog.md)
- [Revisión conjunta de diseño](../../docs/v1-design-review.md)
- [Objetivo de negocio](../../01-business/vision/product-vision.md)
- [Dominio](../../03-domains/spec-driven-delivery/domain-spec.md)
- [Módulo](../../04-modules/command-workflow/module-spec.md)
- [Feature y escenarios](../../05-features/guided-workflow/feature-spec.md)
- [Contrato de comandos](../../07-contracts/commands/command-contract.md)
- [Feature B1](../../05-features/local-core/feature-spec.md)
- [Contrato B1](../../07-contracts/commands/local-core-contract.md)
- [ADR-100](../../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Tablero](../TASKS.md)
- [Publicación](../../docs/publication-readiness.md)

La cadena documental negocio → dominio → módulo → feature → contrato → escenarios BDD cubre el diseño de los criterios 10 a 16; sus escenarios de flujo guiado aún no tienen runner. B1 sí tiene pruebas ejecutables específicas de instalación, estructura y seguridad local. Cada bloque posterior debe completar sus casos particulares y registrar pruebas en rojo antes de implementar.
