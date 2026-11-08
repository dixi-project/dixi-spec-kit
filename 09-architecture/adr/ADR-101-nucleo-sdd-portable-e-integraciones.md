# ADR-101 — Núcleo SDD portable e integraciones elegibles

## Propósito

Diseñar DIXI Spec Kit como un ecosistema público de desarrollo SDD cuyo método no dependa de un agente, modelo, lenguaje o proveedor de infraestructura específico.

## Estado

Dirección aceptada para implementación incremental el 2026-11-06: núcleo independiente del agente/stack, integraciones opcionales y comienzo por modo documental sin agente. La autorización de B1 se registra en ADR-100 y TASK-001. Los mecanismos operativos de los conjuntos de políticas y sus excepciones de proveedor continúan propuestos para sus bloques; B1 no ejecuta IA ni configura infraestructura. No se han cambiado las normas heredadas de este repositorio.

## Contexto

La propuesta anterior privilegiaba Claude Code porque hay comandos aprovechables en el origen. Esa base no debe convertirse en un requisito del producto público. Python como runtime de la CLI tampoco determina el lenguaje del software generado.

Ofrecer distintas interfaces de agente no resuelve por sí solo las dependencias de proveedor: las normas heredadas fijan Bedrock, CodePipeline, CodeBuild y servicios de secretos de AWS. La portabilidad pública requiere expresar explícitamente cuáles son garantías del método y cuáles son implementaciones organizativas de esas garantías.

## Decisión propuesta

1. **Núcleo SDD compartido.** Historias, dominios, módulos, features, contratos, tareas, decisiones y evidencias usan formatos abiertos y referencias estables. Las operaciones del catálogo tienen una definición común, independiente de cómo se invocan en un agente.
2. **Integraciones elegibles.** La persona selecciona un adaptador publicado o el modo sin integración. Ningún agente se instala, autentica o selecciona de forma implícita. Codex y Claude Code son candidatos iniciales de igual prioridad para demostrar portabilidad; su soporte se anuncia solo después de evaluar cada uno.
3. **Uso documental sin agente obligatorio.** El modo sin integración entrega estructura, plantillas, guías de las operaciones y validaciones locales. Permite aplicar el método con edición manual o herramientas propias. No promete la automatización, hooks o ejecución de `build` de un adaptador verificado.
4. **Lenguaje del producto separado del runtime del kit.** Python implementa el núcleo local B1. Los proyectos pueden elegir su lenguaje y framework, incluso combinar varios. Un perfil de stack conectará sus comprobaciones con `make verify`; no convierte un lenguaje concreto en requisito del método ni promete generar cualquier aplicación completa.
5. **Políticas explícitas.** Proponer un conjunto público portable y un conjunto organizativo Dixi. Ambos conservan trazabilidad, validación de decisiones por riesgo, TDD, protección de pruebas, revisión humana, protección de secretos y evidencia de verificación. Las opciones y requisitos efectivos se muestran al inicializar.
6. **Proveedor elegido por el proyecto.** En el conjunto público, agente/modelo, autenticación, proveedor de IA, alojamiento y herramientas de CI/CD se documentan como decisiones del proyecto. El kit no crea cuentas ni obtiene credenciales. No se deduce proveedor de IA a partir del nombre del agente.
7. **Garantías equivalentes, mecanismos declarados.** Cada adaptador identifica qué controles automatiza, cuáles quedan en CI o revisión y cuáles no soporta. No declara que un hook existe solo por haber escrito instrucciones en Markdown. Si falta un control obligatorio, se bloquea la operación dependiente o se requiere un mecanismo equivalente previamente documentado y verificable.
8. **Cambio de adaptador preservando el proyecto.** Specs, IDs, contratos, tareas y evidencias pertenecen al núcleo. Una futura operación de cambio de adaptador debe preservar esos artefactos y señalar capacidades perdidas; no se añade todavía un nuevo comando público de migración ni se presupone que `init` puede sobrescribir un proyecto existente.

## Excepción propuesta y límites

La excepción propuesta se limita a la distribución pública y a los proyectos externos que eligen el conjunto portable. No cambia las políticas del origen privado ni autoriza otras plataformas para construir/publicar este propio repositorio. Las reglas heredadas de este repositorio permanecen efectivas. La etiqueta `policy: portable` de B1 identifica una base documental sin proveedor configurado; no certifica controles operativos ni implementa aún selección de conjuntos.

| Norma o acoplamiento | Conjunto público propuesto | Conjunto Dixi y desarrollo de este repositorio |
|---|---|---|
| ADR-012 / regla 15: IA por Bedrock con IAM. | Proveedor y autenticación elegidos/documentados por el proyecto, con protección de credenciales y límites de datos. | Conserva Bedrock e IAM salvo otra excepción propia. |
| ADR-006 y ADR-014 / reglas 10–12: CodePipeline, CodeBuild y runners AWS. | Herramientas elegibles con PR revisado, checks, build y deployment separados, artefacto trazable y gate humano de producción. Ningún deploy productivo desde el agente. | Conserva la cadena y separación de credenciales heredadas. |
| Regla 14: Secrets Manager/SSM. | Almacén de secretos equivalente elegido por el proyecto; secretos fuera del repo y fuera de la lectura del agente. | Conserva servicios AWS definidos por la norma. |
| Supuestos de stack en comandos/plantillas del origen. | Plantillas neutrales y perfiles opcionales de stack; validación conectada a las herramientas del proyecto. | Preferencias Dixi se mantienen en su conjunto, sin trasladarlas como requisito universal. |

No se propone quitar firmas humanas, atestación, revisión, límites de riesgo, i18n, MODE, pruebas congeladas ni la escalera `make verify`. Elegir un proveedor distinto no equivale a desactivar controles. La promoción de MODE y los demás gates siguen supervisados.

Los conjuntos de políticas no son los perfiles S/A/P heredados: son una dimensión distinta. Su formato, nombres de opciones y mecanismo de selección se concretan antes de implementar. No se publica una combinación portable con cláusulas contradictorias que sigan exigiendo exclusivamente AWS.

## Compatibilidad y evidencia

| Nivel | Qué puede afirmarse | Evidencia necesaria |
|---|---|---|
| Método portable | Las operaciones y artefactos se comprenden sin un agente o stack concreto. | Revisión del núcleo, guías y recorrido documental sin integración. |
| Adaptador verificado | Los comandos funcionan en una herramienta/versiones indicadas. | Recorrido, interrupciones, gates, preservación de artefactos y matriz de controles por adaptador. |
| Perfil de stack verificado | El ejemplo y sus comprobaciones funcionan en un stack/sistemas indicados. | Ejecución real de `make verify` y del ejemplo en la matriz declarada. |
| Integración comunitaria o manual | Existe una ruta de adaptación documentada. | Identificación de procedencia, limitaciones y estado sin equipararlo a soporte oficial. |

Propuesta de validación de neutralidad: el mismo caso de uso con Codex y Claude Code y ejemplos equivalentes en dos lenguajes diferentes, a elegir antes de implementar esos bloques. Cada adaptador se prueba contra ambos ejemplos para detectar acoplamientos. Esto acredita esas combinaciones, no compatibilidad universal. Los adaptadores pueden traducir la misma operación a distintas sintaxis.

## Consecuencias

El producto necesita una matriz de compatibilidad y controles, además del catálogo de operaciones. Mantener dos adaptadores y perfiles de ejemplo aumenta pruebas y documentación. A cambio, el núcleo conserva una sola fuente de verdad y los usuarios pueden elegir herramientas sin rehacer sus specs.

La disponibilidad de una integración no implica ausencia de costos ni permisos adicionales. Instalar y validar estructura siguen sin consumir IA; usar un agente requiere su entorno y proveedor elegidos conforme a las políticas del proyecto.

## Relacionados

- [ADR-100](ADR-100-distribucion-publica-v1.md)
- [Producto](../../docs/product-spec.md)
- [Revisión conjunta](../../docs/v1-design-review.md)
- [Contrato](../../07-contracts/commands/command-contract.md)
- [Historia](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
