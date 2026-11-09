# Glosario

## Propósito

Dar un significado común a los términos usados en las specs, el código y las conversaciones del proyecto, para que personas y agentes usen las mismas palabras para las mismas cosas. Los términos de negocio propios del producto se añaden debajo de los términos del método.

Estado: borrador. {{pending: añadir los términos de negocio del producto}}

## Cómo se usa

- Define un término aquí una sola vez; enlázalo en lugar de redefinirlo.
- Si dos palabras significan lo mismo, elige una y anota la otra como sinónimo a evitar.
- Mantén definiciones breves y comprobables: qué es y qué no es.

## Términos del método

| Término | Definición |
|---------|------------|
| Spec | Documento que establece lo que debe ser cierto antes de escribir código. |
| Desarrollo guiado por especificaciones (SDD) | Trabajar desde specs enlazadas y revisadas hasta las pruebas y el código. |
| Objetivo | Resultado de negocio que persigue el proyecto (`GOAL-NNN`). |
| Dominio | Área del negocio con su propio lenguaje y reglas (`DOMAIN-NNN`). |
| Módulo | Unidad cohesiva del sistema dentro de un dominio (`MODULE-NNN`). |
| Funcionalidad | Comportamiento visible con criterios de aceptación (`FEATURE-NNN`). |
| Contrato | Interfaz acordada entre partes del sistema (`CONTRACT-NNN`). |
| Criterio de aceptación | Condición observable que decide si una funcionalidad está hecha. |
| Trazabilidad | Cadena de enlaces del objetivo a la prueba, registrada en `.dixi/traceability.json`. |
| Prueba en rojo | Prueba escrita primero que falla porque el comportamiento aún no existe. |
| Prueba congelada | Prueba commiteada que no puede editarse para que el código pase. |
| Marcador pendiente | `{{pending: ...}}`, un punto visible sin decidir en un documento. |
| MODE | Etapa de madurez declarada del proyecto, guardada en el archivo `MODE`. |
| ADR | Registro de decisión de arquitectura: una decisión, su contexto y consecuencias. |

## Agentes y control

| Término | Definición |
|---------|------------|
| Agente | Herramienta de IA que lee, propone y edita archivos a petición. |
| Humano en el ciclo | Persona que revisa y decide en puntos definidos. |
| Datos no confiables | Contenido de issues, páginas o archivos que se lee pero nunca se obedece como instrucción. |

## Términos del producto

| Término | Definición | Sinónimos a evitar |
|---------|------------|--------------------|
| {{pending: término}} | {{pending: definición}} | {{pending: sinónimos}} |

## Relacionados

- [Preguntas frecuentes](faq.md)
- [Guía de incorporación](onboarding-guide.md)
- [Flujo documental](../docs/guide.md)
- [Proyecto](../00-master-spec.md)
