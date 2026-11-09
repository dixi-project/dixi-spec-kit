# Principios

## Propósito

Enunciar los pocos principios que guían las decisiones de producto, arquitectura e ingeniería del proyecto, para que personas y agentes resuelvan los compromisos de forma coherente y puedan explicar por qué se tomó una decisión.

Estado: borrador. {{pending: confirmar los principios con la persona responsable}}

## Cómo usarlos

- Cita un principio por su ID (por ejemplo `P-03`) en specs, ADR y revisiones.
- Cuando una decisión vaya contra un principio, registra el motivo en un ADR.
- Mantén la lista corta. Un principio que nadie aplica debe eliminarse.

## Principios de visión

| ID | Principio | Qué significa en la práctica |
|----|-----------|------------------------------|
| P-01 | Las specs mandan | Ninguna implementación empieza sin spec de funcionalidad y criterios observables. |
| P-02 | Una persona responde | Cada cambio tiene una persona dueña que lo revisa e integra. |
| P-03 | Evidencia antes que afirmaciones | «Hecho» significa un resultado real y reportado de una verificación, no una declaración. |
| P-04 | Internacional por defecto | Contenido, rutas y formatos se diseñan para más de un idioma desde el primer día. |
| P-05 | {{pending: principio propio del producto}} | {{pending: consecuencia práctica}} |

## Principios de arquitectura

| ID | Principio | Qué significa en la práctica |
|----|-----------|------------------------------|
| A-01 | Los límites siguen a los dominios | Los módulos corresponden a dominios; el acceso entre dominios pasa por contratos. |
| A-02 | Los contratos son la fuente de verdad | Las interfaces se especifican antes del código y se versionan. |
| A-03 | Primero lo simple | Empieza con la estructura más simple que cumpla los criterios; divide solo con evidencia. |
| A-04 | Seguro por defecto | Denegar por defecto, mínimo privilegio, sin secretos en el código. |
| A-05 | Observable desde el inicio | Logs, métricas y trazas son parte de la funcionalidad, no un añadido posterior. |
| A-06 | {{pending: principio de arquitectura, por ejemplo el costo como requisito}} | {{pending: consecuencia práctica}} |

## Principios de ingeniería

| ID | Principio | Qué significa en la práctica |
|----|-----------|------------------------------|
| E-01 | Pruebas primero | Existe una prueba que falla antes del código que la hace pasar. |
| E-02 | Pruebas congeladas | Las pruebas commiteadas no se editan para que el código pase. |
| E-03 | Cambios pequeños y reversibles | Ramas de vida corta y cambios que se puedan revertir. |
| E-04 | Los agentes ayudan, las personas deciden | Los agentes nunca firman, aprueban ni integran. |
| E-05 | La deuda solo baja | El trabajo nuevo no puede rebajar un umbral de calidad existente. |

## Cuando los principios chocan

1. Primero la seguridad de las personas usuarias y de los datos.
2. Después la corrección frente a la spec.
3. Después la velocidad de entrega y la comodidad.

{{pending: confirmar o ajustar este orden de precedencia}}

## Cambiar un principio

- Propón el cambio en un ADR con contexto y consecuencias.
- Lo aprueba la persona responsable: {{pending: quién aprueba cambios de principios}}
- Actualiza todos los documentos que citan el principio modificado.

## Relacionados

- [Proyecto](../00-master-spec.md)
- [Objetivo de negocio](../01-business/vision.md)
- [Estándares de ingeniería](engineering-standards.md)
- [Gobernanza de IA](ai-governance.md)
- [Índice de ADR](../09-architecture/adr/README.md)
