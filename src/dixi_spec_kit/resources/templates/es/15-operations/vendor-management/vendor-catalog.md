# Catálogo de proveedores

## Propósito

Mantener una sola lista de los servicios externos de los que depende el proyecto, qué datos reciben, quién gestiona la relación y qué tan críticos son.

Estado: borrador. {{pending: nombrar al responsable del catálogo}}

## Catálogo

| Proveedor | Categoría | Se usa para | Datos compartidos | Criticidad | Responsable | Contrato o plan | Renovación | Plan de salida |
|-----------|-----------|-------------|-------------------|------------|-------------|-----------------|------------|----------------|
| {{pending: nombre del proveedor}} | {{pending: p. ej. hosting, correo, pagos, modelo de IA, analítica}} | {{pending: propósito}} | {{pending: ninguno / metadatos / datos personales}} | {{pending: crítica / alta / normal}} | {{pending: rol}} | {{pending: plan}} | {{pending: fecha}} | {{pending: sí / no / enlace}} |

Registra hechos, no opiniones. No guardes aquí contratos, credenciales ni números de cuenta; enlaza a donde se guardan.

## Categorías

{{pending: ajustar la lista de categorías al proyecto}}

- Hosting e infraestructura
- Almacenamiento de datos y respaldos
- Identidad y autenticación
- Pagos y facturación
- Mensajería (correo, SMS, notificaciones push)
- Modelos y APIs de IA
- Monitoreo y logs
- Herramientas de desarrollo

## Criticidad

| Nivel | Significado |
|-------|-------------|
| Crítica | Su fallo detiene un servicio crítico |
| Alta | Su fallo degrada el producto, hay alternativa |
| Normal | Interno o fácil de sustituir |

## Alta de un proveedor

1. Comprueba si un proveedor existente ya cubre la necesidad.
2. Registra la fila de arriba antes de usarlo en producción.
3. Confirma qué datos recibe y si hace falta un acuerdo de tratamiento de datos.
4. Para proveedores críticos, escribe un plan de salida: cómo exportar los datos y qué podría sustituirlo.

## Revisión

Revisa cada {{pending: frecuencia}}: sigue en uso, el responsable es correcto, fecha de renovación, cambios de precio.

## Relacionados

- [Catálogo de servicios](../service-catalog.md)
- [Matriz RACI](../team/raci-matrix.md)
- [Estrategia de costos](../../22-finops/cost-strategy.md)
