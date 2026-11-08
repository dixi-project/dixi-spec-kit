# TASK-003 — Adaptador de Claude Code y comandos del recorrido principal

## Propósito

Concretar B3 de TASK-001 bajo la propuesta de [ADR-102](../../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md): instalar en Claude Code los comandos del recorrido principal para que una persona recorra el método dentro de su agente.

## Registro e historia

- Tipo: feature; prioridad P1; nivel 3, estructural (nuevo adaptador, controles y superficie de ejecución del agente).
- Estado: en curso desde el 2026-11-08.
- Dependencia resuelta: ADR-102 validado y licencia MIT + DCO decidida el 2026-11-08 en la validación conjunta de nivel 3.
- Como persona que usa Claude Code quiero instalar los comandos de DIXI Spec Kit en mi proyecto para recorrer descubrimiento, especificación, plan, tareas, construcción, verificación y preparación de revisión, conservando trazabilidad y los gates humanos.

## Criterios de aceptación

1. Existe un contrato de adaptador que declara versión y sintaxis de Claude Code comprobadas, capacidades, controles que automatiza, controles que quedan en CI o revisión y los que no soporta.
2. `dixi init` con el adaptador instala solo archivos del producto, sin sobrescribir los existentes, sin hooks activados implícitamente y sin consumir IA ni red. Se eligen de forma explícita.
3. Cada uno de los diez comandos (`discover`, `specify`, `clarify`, `plan`, `tasks`, `build`, `verify`, `review`, `analyze`, `status`) tiene contrato de entradas, escrituras, errores, gates, repetición e interrupción, y referencia solo recursos distribuidos.
4. Los comandos no modifican pruebas congeladas, no firman, atestan, aprueban ni integran, y no saltan un gate cuando falta información o hay conflicto entre specs.
5. Pruebas deterministas cubren instalación, conflictos, symlinks y recursos; evaluaciones con entradas controladas cubren los comandos sin exigir texto idéntico.
6. Un ejemplo público recorre idea → código verificado → revisión preparada y una evolución con análisis de impacto, con `make verify` en verde.
7. La matriz de soporte publicada no anuncia capacidades sin evidencia, ni sistemas no probados.

## Reglas de negocio

1. Las pruebas de aceptación se registran en rojo en su propio commit antes de implementar.
2. No se anuncia un comando, adaptador o control que no esté verificado.
3. AWS/Bedrock y las normas del origen no se relajan sin ADR propio; el adaptador público sigue ADR-101.

## La historia se considera terminada cuando

1. ADR-102 fue validado y TASK-001 actualizado.
2. Los criterios tienen pruebas y evaluaciones, con el rojo previo registrado.
3. `make verify` pasa, incluido wheel/sdist instalados en entornos limpios.
4. La matriz de soporte y la documentación es/en reflejan la implementación real.

## Avance — 2026-11-08

Implementado con pruebas primero: contrato, feature y amenazas (commit propio), 15 pruebas en rojo (commit propio), adaptador, recursos es/en, ejemplo `examples/notes` con evolución e impacto. Evidencia en [B3](../../docs/b3-verification.md). Pendiente de revisión humana del PR.

## Relacionados

- [Historia principal](TASK-001-lanzamiento-v1.md)
- [ADR-102](../../09-architecture/adr/ADR-102-recorte-de-alcance-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Catálogo de comandos](../../docs/command-catalog.md)
- [Contrato de comandos](../../07-contracts/commands/command-contract.md)
- [Comparación con GitHub Spec Kit](../../docs/spec-kit-comparison.md)
