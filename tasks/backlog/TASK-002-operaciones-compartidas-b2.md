# TASK-002 — Procedimientos compartidos de definición y diseño

## Propósito

Concretar B2a de TASK-001: acceso local a los ocho procedimientos de B2 y preparación verificable del contexto para usarlos manualmente o con la herramienta elegida.

## Registro e historia

- Tipo: feature; prioridad P1; nivel 2. Riesgo medio: lectura de documentos externos y preparación de instrucciones, sin ejecución ni escritura de proyecto.
- Estado: implementado y verificado localmente; revisión humana pendiente. Fecha: 2026-11-07.
- Autorización: el usuario pidió continuar después de entregar B1 y presentar B2 como siguiente bloque. Implementa la separación del núcleo aceptada en ADR-100/101; no cambia proveedor, políticas operativas o licencia.
- Como usuario quiero consultar procedimientos y preparar un objetivo explícito para aplicar el mismo método con mis herramientas y conservar trazabilidad de las fuentes revisadas.

## Criterios de aceptación

1. `workflow list/show` funciona sin proyecto y expone exactamente discover, specify, clarify, domain, architecture, contract, threat-model y plan, en es/en.
2. Cada procedimiento contiene propósito, entradas, pasos, salidas, gates, comprobaciones y próximos pasos. El catálogo es común, sin sintaxis exclusiva de un agente.
3. `prepare` exige operación, ID de objetivo compatible y solicitud no vacía. No escoge el primer elemento ni interpreta una ruta como ID.
4. Devuelve un paquete con contrato, solicitud como dato, objetivo, idioma del proyecto, MODE y un manifiesto con rutas/hashes actuales del objetivo y sus ancestros. No incluye cuerpos de documentos ni evalúa su semántica.
5. Verifica metadata/grafo y rechaza archivos ausentes, rutas inseguras, symlinks, archivos especiales, límites y MODE inválido. No lee enlaces ni ramas ajenas del grafo para preparar el manifiesto.
6. Repetición sin cambios produce el mismo paquete; cambios en las fuentes cambian sus hashes. No escribe, invoca IA, instala agentes, ejecuta herramientas del proyecto ni accede a red.
7. El resultado distingue preparación de ejecución del procedimiento. No marca specs, ADRs, gates ni pruebas como aceptados o completos.
8. Los recursos llegan a wheel/sdist y el recorrido funciona desde ambos artefactos. `make verify` queda verde sin modificar pruebas congeladas.

## Límites de este incremento

B2a prepara instrucciones y contexto, no genera decisiones mediante inferencia ni instala slash commands. La producción/evaluación de artefactos con adaptadores sigue pendiente en B2; no se declara cerrado el recorrido WF-01/WF-02. Se conserva `1.0.0.dev0` durante el desarrollo local, sin promesa de actualización o release.

## Evidencia técnica

Pruebas nuevas congeladas en `ca43f17` antes de implementar; regresión de campos desconocidos en `d4d6f93` antes de corregirla. Ver [resultados, artefactos y límites](../../docs/b2-verification.md). No se alteraron pruebas congeladas ni se realizó publicación, firma o aprobación humana.

## Relacionados

- [Historia principal](TASK-001-lanzamiento-v1.md)
- [Feature](../../05-features/workflow-preparation/feature-spec.md)
- [Contrato](../../07-contracts/commands/workflow-preparation-contract.md)
- [Amenazas](../../13-security/workflow-preparation-threat-model.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
