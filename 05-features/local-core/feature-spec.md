# Feature — Núcleo local instalable B1

## Propósito

Entregar el primer recorrido local de TASK-001: instalar, consultar ayuda, generar sin agente, diagnosticar y comprobar estructura. El usuario autorizó avanzar con este bloque tras validar el enfoque abierto.

## Historia y criterios

Como usuario externo quiero crear una base SDD con recursos locales para aplicar el método con mis herramientas sin requerir cuentas internas ni agentes específicos.

- LC-01: ayuda y versión funcionan fuera de un proyecto; solo anuncian operaciones implementadas.
- LC-02: init crea recursos, baseline y trazabilidad es/en en destino nuevo/vacío y no ejecuta código externo.
- LC-03: destinos ocupados, rutas inseguras y adaptadores ausentes se rechazan antes de escribir; repetir preserva archivos.
- LC-04: doctor no exige agente en `none`; check diferencia estructura válida, enlaces/IDs/padres incorrectos y proyecto ausente, sin modificar archivos.
- LC-05: metadata malformada, rutas externas, symlinks, archivos especiales y tamaños excesivos producen errores controlados sin lectura fuera del proyecto.
- LC-06: wheel/sdist incluyen solo material elegido, se instalan en entornos limpios y producen el mismo resultado verificable.

## Verificación

`tests/test_local_core.py` cubre el contrato observable por CLI; `tests/test_distribution.py` valida artefactos e instalación. `tests/test_safety_edges.py` y `tests/test_link_destinations.py` cubren regresiones de lectura, rutas, límites e interrupciones. La matriz BDD enlaza esos casos sin requerir un runner Gherkin adicional. `make verify` integra pruebas y comprobación de distribución; su resultado está en el [informe B1](../../docs/b1-verification.md), separado del lanzamiento completo.

## Relacionados

- [Módulo padre](../../04-modules/command-workflow/module-spec.md)
- [Contrato B1](../../07-contracts/commands/local-core-contract.md)
- [Escenarios](scenarios.feature)
- [Aceptación](acceptance.yaml)
- [Amenazas](../../13-security/local-core-threat-model.md)
- [Historia](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
