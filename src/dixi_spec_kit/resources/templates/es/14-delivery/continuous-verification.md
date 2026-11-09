# Verificación continua

## Propósito

Seguir comprobando una versión después de salir de CI: confirmar que lo que corre es lo aprobado, que se comporta bien en el entorno real y que se mantiene dentro de los objetivos. Pasar pruebas antes de desplegar es necesario, pero no suficiente.

## Comprobaciones tras cada despliegue

| Comprobación | Qué demuestra | Dónde | Bloquea la promoción |
|---|---|---|---|
| Comprobación de versión | El endpoint de versión devuelve el identificador de commit aprobado | staging, production | Sí |
| Pruebas de humo | Salud, inicio de sesión de un usuario sintético y flujo principal en solo lectura | staging, production | Sí |
| Vigilancia de errores y latencia | Sin regresión de la versión nueva durante el tiempo de observación | staging, production | Sí |
| Escaneo dinámico de seguridad | Sin hallazgos nuevos por encima de {{pending: severidad}} en el sistema desplegado | staging | {{pending: sí o solo reporte}} |
| Consumo del SLO | El presupuesto de error no se consume rápido | production | Dispara reversión |

## Pruebas de humo

- Pocas y críticas; terminan en menos de {{pending: minutos}}.
- Usan usuarios y datos sintéticos; en producción nunca crean datos que vea una persona usuaria real.
- Las credenciales de usuarios sintéticos viven en el almacén de secretos, nunca en el repositorio.
- Son un paso separado que no reconstruye ni reinstala la aplicación.

## Tiempo de observación

- Tiempo mínimo de observación en producción: {{pending: minutos}}.
- Durante ese tiempo la versión anterior sigue disponible y la reversión es rápida.
- El despliegue termina solo cuando el tiempo de observación cierra sin alertas.

## Monitoreo sintético

- Ejecuta el recorrido principal desde fuera cada {{pending: intervalo}} en producción.
- Alerta tras {{pending: número}} fallos seguidos, según las reglas de alertas.

## Evidencia

Cada despliegue a producción registra: identificador de commit, resultado de `make verify`, resultado de las pruebas de humo, persona que aprobó y hora. Ubicación: {{pending: dónde se guarda el registro}}.

## Ensayo

Practica un fallo forzado en staging {{pending: frecuencia}} para confirmar que las comprobaciones bloquean la promoción y que la reversión funciona.

## Relacionados

- [Estrategia de despliegue](deployment-strategy.md)
- [Estrategia de reversión](rollback-strategy.md)
- [SLIs, SLOs y SLAs](../12-observability/slis-slos-slas.md)
- [Reglas de alertas](../12-observability/alerting-rules.md)
- [Plan de pruebas de seguridad](../11-quality/security-test-plan.md)
