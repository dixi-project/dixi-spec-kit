# Estrategia de entornos

## Propósito

Definir qué entornos usa el proyecto, para qué sirve cada uno, cómo pasan los cambios de uno a otro y qué reglas los mantienen aislados entre sí.

Estado: borrador. {{pending: confirmar la lista de entornos}}

## Entornos

| Entorno | Propósito | Datos | Quién despliega | Quién accede |
|---------|-----------|-------|-----------------|--------------|
| Local | Desarrollo y pruebas en el equipo | Sintéticos | Quien desarrolla | Quien desarrolla |
| Desarrollo | Integración del trabajo integrado | Sintéticos | Pipeline automatizado | Equipo |
| Staging | Validación parecida a producción | Enmascarados o sintéticos | Pipeline automatizado | Equipo, revisores |
| Producción | Usuarios reales | Reales | {{pending: quién o qué despliega}} | {{pending: roles nombrados}} |

{{pending: añadir o quitar entornos, por ejemplo entornos de vista previa por pull request}}

## Reglas

- Cada entorno tiene sus propios secretos, identidades y datos. Nada se comparte con producción.
- Los datos personales reales nunca salen de producción.
- La configuración difiere entre entornos solo mediante configuración, no con ramas de código.
- Se promueve el mismo artefacto de build de un entorno al siguiente.
- Los agentes nunca despliegan en ningún entorno compartido.

## Camino de promoción

1. Integrar en la rama principal tras la revisión.
2. Desplegar en desarrollo automáticamente; ejecutar pruebas de humo.
3. Promover a staging; ejecutar verificaciones de aceptación y regresión.
4. Promover a producción tras la decisión de la persona responsable del release.

Puerta entre staging y producción: {{pending: verificaciones obligatorias y quién aprueba}}

## Paridad

| Aspecto | Debe igualar producción | Puede diferir |
|---------|-------------------------|---------------|
| Runtime y versiones | Sí | |
| Forma de la infraestructura | Sí | |
| Escala y tamaño | | Sí |
| Volumen de datos | | Sí |

## Costo y ciclo de vida

- Los entornos no productivos se dimensionan para su propósito y pueden detenerse cuando están inactivos. {{pending: política de inactividad}}
- Los entornos temporales se eliminan al cerrar su rama.

## Relacionados

- [Estándar de gestión de releases](release-management-standard.md)
- [Base de seguridad](security-baseline.md)
- [Arquitectura de despliegue](../09-architecture/deployment-architecture.md)
- [Gestión de secretos](../13-security/secret-management.md)
