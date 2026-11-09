# Arquitectura multi-tenant

## Propósito

Describir cómo la plataforma atiende a varios tenants (organizaciones, espacios de trabajo o clientes) desde infraestructura compartida manteniendo aislados sus datos y configuración. Un fallo de aislamiento entre tenants es de los defectos más graves que puede tener una plataforma, así que el modelo debe ser explícito.

## Modelo de tenencia

| Opción | Aislamiento | Coste | Esfuerzo operativo |
|---|---|---|---|
| Esquema compartido con columna de tenant | Lógico | Bajo | Bajo |
| Esquema o base de datos por tenant | Más fuerte | Medio | Medio |
| Stack dedicado por tenant | El más fuerte | Alto | Alto |

Modelo elegido: {{pending: modelo de tenencia, registrado en un ADR}}

## Resolución del tenant

- Cómo identifica una petición su tenant: {{pending: subdominio, ruta, claim del token o cabecera}}
- Dónde se fija el contexto del tenant: {{pending: middleware o gateway}}
- Qué ocurre si falta o no es válido: se rechaza la petición.

## Reglas de aislamiento

- Toda consulta sobre datos de un tenant se filtra por tenant, impuesto de forma centralizada y no por convención: {{pending: mecanismo, p. ej. políticas a nivel de fila o filtro en el repositorio}}.
- Cachés, archivos, índices de búsqueda y colas usan el tenant como clave.
- Las tareas en segundo plano y los eventos llevan el ID del tenant de forma explícita.
- Los logs incluyen el ID del tenant, pero nunca datos de otro tenant.
- Las operaciones entre tenants (soporte, informes) requieren un rol explícito y auditado.

## Configuración por tenant

| Ajuste | Valor por defecto | Quién puede cambiarlo |
|---|---|---|
| {{pending: flag de funcionalidad o límite}} | {{pending: valor}} | {{pending: rol}} |

## Vecinos ruidosos

- Límites de tasa y cuotas por tenant: {{pending: límites}}
- Aislamiento de recursos para tenants con mucha carga: {{pending: estrategia}}

## Ciclo de vida

- Alta: {{pending: pasos para aprovisionar un tenant}}
- Baja y borrado de datos: {{pending: pasos de exportación, retención y borrado}}
- Requisitos de residencia de datos: {{pending: si los tenants exigen ubicaciones concretas}}

## Verificación

- El [plan de pruebas](../11-quality/test-plan.md) debe incluir pruebas de aislamiento que intenten acceder a datos de otro tenant: {{pending: IDs de las pruebas}}.

## Relacionados

- [Arquitectura de seguridad](security-architecture.md)
- [Diagrama de contenedores](container-diagram.md)
- [Arquitectura de rendimiento](performance-architecture.md)
- [Decisiones de arquitectura](adr/README.md)
- [Plan de pruebas](../11-quality/test-plan.md)
