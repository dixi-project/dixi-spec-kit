# Estándar de gestión de releases

## Propósito

Definir cómo un cambio se convierte en release: qué contiene, quién decide que sale, qué verificaciones deben pasar y cómo se comunica y se revierte si hace falta.

Estado: borrador. {{pending: confirmar el proceso de release con la persona responsable}}

## Tipos de release

| Tipo | Contenido | Cadencia | Aprobación |
|------|-----------|----------|------------|
| Regular | Funcionalidades y correcciones integradas desde el último release | {{pending: cadencia}} | {{pending: quién aprueba}} |
| Parche | Solo correcciones urgentes | Según necesidad | {{pending: quién aprueba}} |
| Mayor | Cambios incompatibles, con notas de migración | Planificado | {{pending: quién aprueba}} |

## Checklist de preparación

- [ ] Una persona revisó e integró cada cambio incluido.
- [ ] `make verify` y la suite real de pruebas pasaron en el commit del release.
- [ ] El número de versión sigue la [política de versiones](policies/versioning-policy.md).
- [ ] Las notas del release listan cambios visibles, cambios incompatibles y migraciones.
- [ ] Las migraciones de datos tienen una reversión probada o un plan de corrección hacia delante.
- [ ] Hay monitoreo y alertas para las áreas modificadas.
- [ ] Se conoce el camino de reversión y tiene responsable.

## Roles

| Rol | Responsabilidad |
|-----|-----------------|
| Responsable del release | Coordina y decide si sale o no. |
| Revisor | Confirma la checklist con evidencia. |
| Guardia | Vigila el release y puede activar la reversión. |

Los agentes pueden preparar notas del release y ejecutar verificaciones; nunca aprueban ni despliegan.

## Despliegue gradual

- Promueve por los entornos en orden: [Estrategia de entornos](environment-strategy.md).
- {{pending: técnica de despliegue, por ejemplo todo de una vez, canario o feature flags}}
- Ventanas de congelación: {{pending: periodos en que no se permiten releases}}

## Después del release

- Vigila los indicadores clave durante {{pending: ventana de observación}}.
- Registra el resultado y cualquier incidente en el registro de decisiones.
- Si hubo reversión, escribe un postmortem.

## Relacionados

- [Política de versiones](policies/versioning-policy.md)
- [Estrategia de entornos](environment-strategy.md)
- [Estándar de observabilidad](observability-standard.md)
- [Política de incidentes](policies/incident-policy.md)
- [Arquitectura de despliegue](../09-architecture/deployment-architecture.md)
