# ADR-100 — DIXI Spec Kit como distribución pública independiente

## Propósito

Proponer la arquitectura y los límites de la primera distribución pública, sin cambiar las normas del repositorio privado.

## Estado

Aceptado para ejecución incremental local el 2026-11-06. Tras aclarar el enfoque abierto a agentes y lenguajes, el usuario indicó «ok, pues vamos a darle adelante» y autorizó el primer bloque funcional: paquete/CLI Python, modo sin agente, ayuda, diagnóstico, comprobación y pruebas primero. Esto valida la dirección y el inicio de TASK-001; no confirma licencia, derechos, soporte de adaptadores ni disponibilidad de los comandos posteriores.

## Contexto

EIS-IA contiene método, scripts y configuración interna. Cambiar su visibilidad expondría un historial y una operación que no forman parte del producto público. El usuario dispone de una carpeta vacía dedicada a DIXI Spec Kit y pidió crear el repositorio público cuando esté listo.

## Decisión y alcance de ejecución

1. Mantener el repositorio privado de EIS-IA privado y crear una distribución pública independiente con historial nuevo y selección explícita de materiales.
2. Iniciar la numeración pública en v1.0.0, sin heredar la numeración de EIS-IA.
3. Paquete Python, ejecutable `dixi` y recursos incluidos en el artefacto; sin necesidad de credenciales privadas para generar proyectos.
4. Definir un núcleo SDD independiente del agente y stack, separado de adaptadores, perfiles de stack y conjuntos de políticas. ADR-101 concreta la dirección de apertura indicada por el usuario y propone la excepción para proveedores de proyectos externos; no se anuncian integraciones sin evidencia ni se cambian las normas heredadas silenciosamente.
5. Licencia MIT para el producto público, con DCO para contribuciones (decisión de la persona, 2026-11-08). Solo se distribuyen materiales escritos para este producto; la licencia propietaria de EIS-IA no cambia. Los proyectos generados pertenecen a quien los crea; los archivos iniciales que produce `dixi init` pueden usarse sin atribución, como declara la licencia.
6. Reservar escritura a mantenedores de Dixi y permitir forks. `main` es público y cualquiera puede descargarlo o instalarlo; nadie fuera de los mantenedores puede modificarlo. Las contribuciones llegan desde forks por PR y se incorporan solo revisadas y con checks en verde (confirmado por la persona el 2026-11-08).
7. Una vez extraído, el núcleo público es la fuente oficial de los materiales compartidos; la operación privada consume versiones de ese núcleo y conserva extensiones propias. No crear dos copias editadas manualmente del mismo núcleo.
8. Distribuir un flujo de trabajo por comandos: CLI determinista, contratos y plantillas compartidos, validadores y adaptador del agente. El catálogo cubre las capacidades propias de Dixi; los pasos guiados y las invocaciones directas reutilizan el mismo contrato para evitar divergencia. Cada comando distribuido necesita pruebas y evaluación en el agente soportado.
9. El plan inicial concreta 16 comandos del agente y cuatro operaciones CLI, con actualización limitada a previsualización local. Las nueve entradas especializadas quedan por priorizar; las normas que cubren siguen vigentes dentro del recorrido principal. El contrato B1 concreta solo ayuda/versión, `init --agent none`, `doctor` y `check`; el resto necesita contratos detallados y evidencia en sus bloques.

## Consecuencias

La extracción y el soporte inicial cuestan trabajo adicional, pero no exponen el historial interno. El producto necesita sus propias pruebas, documentación, releases y controles de seguridad. La interfaz CLI será un contrato publicado y sus cambios posteriores deberán respetar compatibilidad o versionarse.

## Decisiones pendientes

Resueltas el 2026-11-08 por [ADR-102](ADR-102-recorte-de-alcance-v1.md): licencia (MIT + DCO), alcance del catálogo (diez comandos), un adaptador (Claude Code) y actualización aplazada a v1.1. Siguen abiertas: plataforma de build y CI del producto conforme a normas heredadas. La excepción propuesta para proveedores de proyectos públicos se revisa en ADR-101, sin afectar automáticamente la operación de este repositorio.

## Relacionados

- [Historia](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-101: núcleo portable](ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Especificación](../../docs/product-spec.md)
- [Catálogo propuesto](../../docs/command-catalog.md)
- [Revisión conjunta](../../docs/v1-design-review.md)
- [Contrato propuesto](../../07-contracts/commands/command-contract.md)
- [Exportador por lista permitida](../../docs/repository-settings.md)
