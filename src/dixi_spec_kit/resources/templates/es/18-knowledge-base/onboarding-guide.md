# Guía de incorporación

## Propósito

Ayudar a una persona nueva (o a un agente recién configurado) a ser productiva en el proyecto de forma segura: qué no se negocia, qué preparar, cómo fluye el trabajo diario y cuándo detenerse a preguntar.

Estado: borrador. {{pending: nombrar a la persona de acompañamiento o contacto}}

## Lo que no se negocia

- Las specs mandan; las pruebas van primero; las pruebas commiteadas están congeladas.
- Una persona revisa e integra cada cambio. Los agentes nunca firman, aprueban, integran ni despliegan.
- Sin secretos en el repositorio, los prompts ni los logs.
- Los textos visibles para el usuario viven en catálogos de traducción.

## Prerrequisitos

- [ ] Acceso al repositorio con identidad propia.
- [ ] La CLI de DIXI Spec Kit instalada (`dixi --version`).
- [ ] {{pending: runtime del lenguaje y herramientas de este proyecto}}
- [ ] Acceso al canal del equipo: {{pending: canal}}

## Preparación

1. Clona el repositorio y crea una rama: `feat/<tema>`.
2. Ejecuta `dixi doctor` y `dixi check`.
3. Ejecuta `make verify` y anota el resultado.
4. Lee [AGENTS.md](../AGENTS.md) y el [flujo documental](../docs/guide.md).

## Ruta de lectura (primer día)

| Orden | Documento | Por qué |
|-------|-----------|---------|
| 1 | [Proyecto](../00-master-spec.md) | Alcance y decisiones |
| 2 | [Objetivo de negocio](../01-business/vision.md) | Por qué existe el proyecto |
| 3 | [Principios](../00-governance/principles.md) | Cómo se resuelven los compromisos |
| 4 | [Política de pruebas](../00-governance/policies/testing-policy.md) | Reglas de pruebas |
| 5 | [Glosario](glossary.md) | Vocabulario común |

## Flujo diario

1. Elige una tarea enlazada a una spec de funcionalidad.
2. Lee la spec y sus criterios; pregunta lo que no esté claro.
3. Escribe y commitea una prueba en rojo.
4. Implementa hasta verde; refactoriza.
5. Ejecuta `make verify`; abre un pull request con el resultado real.

## Cuándo detenerse y preguntar

- La spec es ambigua o contradice una prueba.
- Un cambio afecta a seguridad, datos personales, pagos o permisos.
- Tendrías que editar una prueba commiteada.
- Una herramienta pide un secreto o un acceso más amplio.

## Primera tarea

{{pending: una primera tarea pequeña y bien especificada para personas nuevas}}

## Relacionados

- [Preguntas frecuentes](faq.md)
- [Glosario](glossary.md)
- [Registro de decisiones](decision-log.md)
- [Estándares de ingeniería](../00-governance/engineering-standards.md)
