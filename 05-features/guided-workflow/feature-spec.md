# Feature — Recorrido guiado y evolución de una funcionalidad

## Propósito

Definir cómo una persona usa los comandos del kit desde una necesidad hasta una revisión preparada y cómo retoma o cambia ese trabajo. Estado: borrador de aceptación, sin implementación ni pruebas ejecutadas.

## Historia y alcance

Como persona que desarrolla con Dixi, quiero comandos que mantengan conectadas mis decisiones, especificaciones, tareas y comprobaciones, para construir y evolucionar una funcionalidad conservando su contexto y sus controles.

Esta feature desarrolla los criterios 10 a 16 de TASK-001 y depende de instalación local verificada. La preparación/publicación del paquete y los controles del repositorio oficial siguen en TASK-001; los escenarios de esta feature no acreditan esos otros criterios.

## Criterios de aceptación

- WF-01: discovery y especificación producen artefactos enlazados y preguntas explícitas ante información faltante.
- WF-02: dominio, arquitectura, contratos y amenazas alimentan el mismo plan tanto por entrada directa como por el recorrido guiado; cada amenaza aplicable queda enlazada a una mitigación y prueba prevista.
- WF-03: las tareas cubren criterios del plan, tienen nivel y verificación, y no contienen dependencias circulares.
- WF-04: build respeta el gate de historia nivel 3 y TDD; no altera pruebas congeladas.
- WF-05: analyze, verify y review distinguen contradicciones, controles no ejecutados y evidencia desactualizada, sin aprobar el cambio.
- WF-06: repetir, interrumpir y retomar preserva identificadores y cambios locales; status no escribe y handoff queda privado.
- WF-07: change documenta impacto y bloqueos de compatibilidad sin aplicar automáticamente cambios a contratos publicados o pruebas congeladas.
- WF-08: los comandos instalados tienen recursos completos y su ayuda no anuncia capacidades aplazadas; el recorrido funciona en el adaptador y matriz anunciados.
- WF-09: la persona puede elegir una integración distribuida o ninguna; el núcleo y sus validaciones no exigen un agente y los artefactos canónicos tienen el mismo formato.
- WF-10: los ejemplos acreditan el recorrido en dos lenguajes, evaluados con cada adaptador anunciado; las diferencias de capacidades/controles se muestran y un control obligatorio ausente bloquea la operación dependiente si no hay mecanismo equivalente verificado.

## Ejemplo de evaluación propuesto

Una biblioteca local de notas ficticias, sin cuentas ni datos personales, permite crear y listar notas. La evolución añade un filtro compatible y después solicita cambiar un contrato publicado de forma incompatible para comprobar que el gate se respeta. Los textos es/en y las comprobaciones se declaran en su plan. Se preparan ejemplos equivalentes en dos lenguajes y se evalúa cada adaptador anunciado contra ambos; los stacks y ubicaciones se fijan antes del bloque de construcción. La matriz acreditará esas combinaciones, no soporte universal.

No se usa información de clientes. La versión publicada del contrato se representa con una fixture de evaluación identificada, sin publicar un servicio real. La evidencia incluye entradas, artefactos, estado de archivos, controles ejecutados y dictamen humano sobre la rúbrica.

## Estrategia de verificación

Los [escenarios](scenarios.feature) son especificaciones BDD aún sin step definitions ni runner. [acceptance.yaml](acceptance.yaml) es una matriz de diseño local, no afirma conformidad con un schema heredado todavía no seleccionado. Antes de implementar se añaden pruebas ejecutables en rojo en su propio commit y casos de seguridad por comando.

Las pruebas deterministas verifican rutas, estructura, inventarios, duplicados y resultados de scripts. Las evaluaciones del agente verifican decisiones, artefactos y respeto de gates con una rúbrica, sin comparar texto literal. Cada uno de los 16 comandos necesita además sus casos particulares antes de su bloque de implementación; estos escenarios de recorrido no sustituyen esa cobertura.

## Relacionados

- [Módulo padre](../../04-modules/command-workflow/module-spec.md)
- [Historia TASK-001](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Contrato](../../07-contracts/commands/command-contract.md)
- [Escenarios BDD](scenarios.feature)
- [Matriz de aceptación](acceptance.yaml)
