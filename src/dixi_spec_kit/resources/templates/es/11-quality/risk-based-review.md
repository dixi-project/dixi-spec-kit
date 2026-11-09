# Revisión basada en riesgo

## Propósito

Ajustar la profundidad de la revisión humana al riesgo de cada cambio, para que quienes revisan dediquen su atención donde un error costaría más.

Estado: borrador. {{pending: acordar niveles de riesgo y revisores requeridos}}

## Niveles de riesgo

| Nivel | Cambios típicos | Revisión requerida |
|-------|-----------------|--------------------|
| Bajo | Textos, estilos, documentación, refactorizaciones aisladas con pruebas en verde | Una persona lee el diff y el resultado de `make verify` |
| Medio | Nueva funcionalidad tras interfaces existentes, pruebas nuevas, actualización de dependencias | Una persona revisa especificación, pruebas y comportamiento |
| Alto | Modelo de datos, contratos, autenticación, permisos, pagos, datos personales, infraestructura | {{pending: número y rol de revisores}}; decisiones estructurales validadas antes de construir |

{{pending: ajustar los ejemplos a las áreas de riesgo reales de este proyecto}}

## Señales que elevan el riesgo

- Cambios en contratos o esquemas que otros consumen.
- Código que toca secretos, control de acceso o datos personales.
- Diffs grandes, código generado con poca cobertura o ediciones a archivos de prueba.
- Operaciones irreversibles (migraciones de datos, borrados).
- Áreas con incidentes previos.

## Lista de revisión

- ¿El cambio corresponde a la especificación y sus criterios de aceptación?
- ¿Se escribieron primero las pruebas y se dejaron intactas las ya commiteadas?
- ¿Se ejecutó `make verify` y se incluye la salida real?
- ¿Se manejan los caminos de error y los casos límite?
- ¿Se afirma como verificado algo que no se ejecutó?
- ¿Se relajó algún umbral, presupuesto o regla? Si es así, ¿hay una decisión humana registrada?

## Agentes y revisión

Los agentes pueden preparar evidencia y señalar riesgos, por ejemplo con `/dixi.quality` o `$dixi-quality`, pero nunca aprueban ni integran. La decisión final siempre es de una persona.

## Relacionados

- [Estrategia de calidad](quality-strategy.md)
- [Escalera de verificación](verification-ladder.md)
- [Requisitos no funcionales](non-functional-requirements.md)
- [Plan de pruebas](test-plan.md)
- [Instrucciones del proyecto](../AGENTS.md)
