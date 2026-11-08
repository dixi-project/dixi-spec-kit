# Especificación del producto DIXI Spec Kit v1

## Propósito

Convertir materiales seleccionados de EIS-IA en una solución pública que una persona externa pueda instalar, comprender y utilizar sin cuentas ni repositorios internos de Dixi.

DIXI Spec Kit es un ecosistema de desarrollo SDD con núcleo independiente del agente, modelo, lenguaje y framework del proyecto. Cada usuario elige sus herramientas; las integraciones verificadas facilitarán aplicar el mismo método. La dirección fue aceptada para implementación incremental; los mecanismos operativos de políticas de proveedor siguen pendientes según ADR-101.

## Público y resultado

Desarrolladores y equipos que quieren pasar de una idea a especificaciones trazables, un plan de implementación y comprobaciones de calidad. La experiencia inicial debe producir un proyecto pequeño y verificable, con una ruta documentada para crecer.

## Identidad

- Producto: DIXI Spec Kit, de Dixi Project.
- Primera release pública objetivo: v1.0.0.
- Repositorio propuesto: `dixi-project/dixi-spec-kit`; su disponibilidad aún no se comprobó.
- Paquete propuesto: `dixi-spec-kit`; su disponibilidad en el registro aún no se comprobó.
- Ejecutable local: `dixi`.
- Origen metodológico: EIS-IA. No heredar su numeración de release ni su changelog privado.
- Producto independiente de GitHub Spec Kit: inspiración en facilidad de instalación y adopción, con metodología y mantenimiento propios de Dixi.

## Experiencia local B1

```text
dixi init mi-proyecto --agent none
cd mi-proyecto
dixi doctor
dixi check
make verify
```

Requiere instalar el artefacto local siguiendo la [guía es/en](local-development.md); no hay paquete publicado en un registro. `init` crea el directorio; los demás inspeccionan el proyecto actual. El Makefile generado solo comprueba estructura documental. Ayuda/versión también están disponibles. `upgrade --dry-run` y comandos de agente continúan pendientes.

Incremento B2a: `dixi workflow list/show/prepare` consulta las ocho recetas compartidas de definición/diseño y prepara instrucciones más un manifiesto de fuentes para un ID explícito. No produce decisiones ni ejecuta un agente. [Contrato y límites](../07-contracts/commands/workflow-preparation-contract.md).

## Comportamiento requerido

### Flujo de trabajo por comandos

El producto debe permitir recorrer descubrimiento, especificación, planificación, tareas, construcción, verificación y preparación de revisión mediante comandos del agente. El [catálogo propuesto](command-catalog.md) amplía ese recorrido con dominios, arquitectura, contratos, amenazas, análisis de trazabilidad y gestión de cambios, además de capacidades especializadas por priorizar.

La CLI instala recursos y ejecuta comprobaciones deterministas; los comandos del agente guían decisiones y producen artefactos trazables. Cada comando requiere un contrato de entradas, salidas, errores, continuidad, gates y pruebas. La lista y la sintaxis siguen propuestas hasta validar la historia y comprobar el adaptador. El soporte público exige un ejemplo ejecutado de principio a fin y una modificación posterior con análisis de impacto.

### Inicialización

Funciona sin autenticar GitHub, acceder a el repositorio privado de EIS-IA, crear repos remotos o registrar el proyecto en el sistema interno de tareas. Usa recursos incluidos en la distribución y registra la versión de la plantilla. No ejecuta instrucciones descargadas ni hooks automáticamente. Rechaza destinos no vacíos y enlaces simbólicos conflictivos antes de escribir; el soporte a proyectos existentes requiere una operación explícita que no sobrescriba cambios.

### Diagnóstico y comprobación

`doctor` distingue requisitos locales del instalador y requisitos opcionales del proyecto generado. `check` verifica estructura y trazabilidad, produce una salida explicable y falla con código distinto de cero ante incumplimientos. No lee secretos ni ejecuta comandos arbitrarios de la plantilla.

### Actualización

Compara la versión instalada y los archivos originales con el estado del proyecto. El modo `--dry-run` no escribe y enumera archivos nuevos, modificados y conflictos. Una aplicación posterior, si forma parte de v1, solo actualiza archivos sin cambios locales y exige resolver conflictos sin pérdida de datos. No usar una copia masiva sobre el proyecto como actualización.

La propuesta concreta del contrato inicial limita v1 a `--dry-run`, comparando los recursos de la versión instalada sin descargar otra versión. La aplicación automática queda fuera de esa propuesta, pendiente de validar el alcance junto con la historia.

### Agentes y políticas

El núcleo define operaciones y artefactos sin depender de un agente. La persona puede elegir una integración verificada o trabajar con las guías y plantillas sin integración. Codex y Claude Code son candidatos iniciales de igual prioridad, sujetos a evaluar versiones, invocaciones y controles. Los comandos dentro del agente se documentan por separado de los comandos de terminal; no se promete idéntica sintaxis o automatización entre herramientas.

ADR-101 separa el núcleo de los conjuntos público portable y organizativo Dixi, con garantías compartidas y mecanismos operativos todavía por concretar. Las políticas AWS/Bedrock, CodePipeline y CodeBuild siguen vigentes en este repositorio. B1 solo instala una base documental sin proveedor; no invoca un modelo ni AWS para generar archivos.

### Lenguajes y frameworks del proyecto

El lenguaje de implementación del kit no limita el de sus usuarios. Los proyectos eligen stack y registran cómo ejecutar sus comprobaciones; los perfiles de stack facilitan esa conexión. Usar el método con otro lenguaje no requiere reescribir las specs. Un perfil verificado acredita únicamente su matriz de pruebas; no se anuncia generación automática para cualquier framework.

### Distribución

Implementación B1: Python con biblioteca estándar en ejecución, recursos incluidos y distribución wheel/sdist local. Python es un requisito del instalador, no del código de los proyectos. Build con Setuptools 84.2.1, verificado y fijado por hash; instalaciones locales con pip probadas sin índice. No depende de publicar en PyPI para desarrollar. [Evidencia y límites](b1-verification.md).

### Documentación y adopción

README y guía inicial en español e inglés; mensajes de la CLI en catálogos de idioma. Ejemplos públicos deliberados, demostración breve y requisitos/costos de las integraciones elegidas explícitos. Distinguir método portable, adaptador verificado y perfil de stack verificado. Sin afirmaciones de paridad o superioridad no verificadas.

## Fronteras

La v1 no requiere un SaaS, telemetría, registro de usuarios, cobros ni integración con herramientas internas. La publicación del paquete en un registro y la creación de un repositorio público son operaciones separadas.

## Relacionados

- [Historia](../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Catálogo de comandos](command-catalog.md)
- [Revisión conjunta](v1-design-review.md)
- [Contrato de comandos](../07-contracts/commands/command-contract.md)
- [ADR-100](../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101: portabilidad e integraciones](../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
- [Matriz de soporte](support-matrix.md)
- [Publicación](publication-readiness.md)
