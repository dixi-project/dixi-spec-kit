# Dominio — Desarrollo guiado por especificaciones

## Propósito

Definir las reglas del recorrido público de DIXI Spec Kit. Estado: propuesta para GOAL-001; no describe una implementación existente.

## Límites y conceptos

El dominio coordina proyecto, objetivo, artefacto, decisión, tarea, evidencia y gate. Un comando transforma o inspecciona esos elementos con un alcance explícito. La interfaz del agente y la CLI comparten sus reglas, aunque solo el agente interpreta necesidades en lenguaje natural.

Quedan fuera la ejecución de producción, la aprobación humana, la certificación de cumplimiento y los servicios internos de Dixi. Un proyecto puede tener repos de código separados; el plan identifica las raíces autorizadas antes de construir.

## Reglas de negocio

- BR-001: toda tarea enlaza su objetivo de negocio, dominio, módulo y feature; los contratos y pruebas completan la cadena según la etapa. Los enlaces pendientes impiden declarar preparación para construir.
- BR-002: instalar y generar no requiere credenciales privadas, registro en el sistema interno de tareas ni consumo de IA/AWS. Usar el agente sí requiere el entorno autorizado documentado.
- BR-003: repetir o retomar preserva decisiones, identificadores y cambios locales. Un conflicto no se resuelve sobrescribiendo silenciosamente.
- BR-004: una evidencia corresponde a una revisión o estado concreto y distingue ejecución, fallo y ausencia de ejecución. Un cambio posterior obliga a reevaluar la evidencia afectada.
- BR-005: la validación de una historia estructural, la aceptación de ADRs, las firmas, atestaciones, aprobaciones e integración corresponden a la persona según la norma; el kit registra su estado, no lo suplanta.
- BR-006: el cambio incompatible de un contrato publicado y la revisión de una prueba congelada requieren resolver el gate correspondiente antes de aplicar el cambio.
- BR-007: las normas heredadas siguen vigentes y las excepciones necesitan ADR propio. Un comando especializado aplazado no elimina sus controles obligatorios.
- BR-008: ayuda, documentación y publicación anuncian solo capacidades verificadas y materiales con derechos resueltos.
- BR-009: agente, stack y políticas son elecciones explícitas y separadas del núcleo. La ausencia de integración no impide el uso documental; no implica automatización del flujo. Un cambio de herramienta conserva los artefactos canónicos y sus identificadores.
- BR-010: cada adaptador declara sus controles efectivos; una capacidad ausente no se presenta como implementada. La separación de proveedores para proyectos externos se aplica solo tras validar ADR-101.

## Relacionados

- [Objetivo GOAL-001](../../01-business/vision/product-vision.md)
- [Módulo](../../04-modules/command-workflow/module-spec.md)
- [Historia](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
