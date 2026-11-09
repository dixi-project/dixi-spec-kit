# Modelo de madurez

## Propósito

Dar a la plataforma una escala común para evaluar la madurez de cada área, decidir qué brechas cerrar primero y evitar declarar un nivel que la evidencia no respalda.

Estado: borrador. {{pending: confirmar el nivel objetivo por área}}

## Niveles

| Nivel | Nombre | Rasgos típicos |
|-------|--------|----------------|
| 1 | Exploratorio | Funciona en un equipo; pocas pruebas; pasos manuales. |
| 2 | Prototipo | Specs de las funcionalidades principales; pruebas de los caminos centrales; release manual. |
| 3 | Listo para producción | Pruebas primero; pipeline automatizado; monitoreo y alertas; runbooks. |
| 4 | Nivel industrial | Niveles de servicio medidos; recuperación probada; revisiones de seguridad; cambios auditados. |
| 5 | Misión crítica | Redundancia entre dominios de fallo; simulacros de recuperación periódicos; control formal de cambios. |

La etapa declarada del proyecto se guarda en `MODE`; promoverla es una decisión humana.

## Señales por nivel

| Área | Evidencia de nivel 3 | Evidencia de nivel 4 |
|------|----------------------|----------------------|
| Specs | Cada funcionalidad integrada se traza a una spec | Trazabilidad verificada en cada cambio |
| Pruebas | Pruebas en rojo commiteadas primero; `make verify` en el pipeline | Umbrales por riesgo aplicados; pruebas de mutación o de propiedades en código crítico |
| Seguridad | Controles base implantados | Modelos de amenazas revisados; revisión externa periódica |
| Operación | Alertas con runbooks | Objetivos de nivel de servicio medidos; recuperación probada |
| Entrega | Despliegue automático a staging | Despliegue progresivo con reversión automática |
| IA | Agentes limitados a redactar | Acciones de agentes auditadas y revisadas |

## Lo que un nivel no significa

- Un nivel no es una certificación.
- Un nivel alto en un área no compensa uno bajo en otra.
- Un nivel solo se declara con evidencia que un revisor pueda comprobar.

## Evaluación

| Área | Nivel actual | Nivel objetivo | Evidencia | Siguiente paso | Responsable |
|------|--------------|----------------|-----------|----------------|-------------|
| {{pending: área}} | {{pending: nivel}} | {{pending: nivel}} | {{pending: evidencia}} | {{pending: paso}} | {{pending: responsable}} |

Cadencia de evaluación: {{pending: p. ej. trimestral}}

## Relacionados

- [Principios](../00-governance/principles.md)
- [Estándares de ingeniería](../00-governance/engineering-standards.md)
- [Escalera de verificación](../11-quality/verification-ladder.md)
- [Registro de decisiones](decision-log.md)
