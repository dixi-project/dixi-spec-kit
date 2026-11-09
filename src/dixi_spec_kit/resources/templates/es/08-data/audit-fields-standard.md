# Estándar de campos de auditoría

## Propósito

Definir los campos estándar que lleva toda entidad persistente para responder quién creó o modificó un registro, cuándo y desde dónde. Una sola convención hace predecibles el diagnóstico de problemas, las revisiones de cumplimiento y las migraciones de datos.

- Alcance: {{pending: qué almacenes y entidades deben seguir este estándar}}

## Campos estándar

| Campo | Tipo | Obligatorio | Lo asigna | Descripción |
| --- | --- | --- | --- | --- |
| `id` | {{pending: tipo de identificador, por ejemplo UUID o ULID}} | Sí | Aplicación | Identificador estable y no reutilizable |
| `created_at` | Timestamp con zona horaria (UTC) | Sí | Capa de persistencia | Instante de creación |
| `created_by` | Referencia a actor | Sí | Aplicación | Usuario, servicio o proceso que creó el registro |
| `updated_at` | Timestamp con zona horaria (UTC) | Sí | Capa de persistencia | Instante de la última modificación |
| `updated_by` | Referencia a actor | Sí | Aplicación | Último actor que modificó el registro |
| `deleted_at` | Timestamp, nulable | Si se usa borrado lógico | Aplicación | Instante del borrado lógico |
| `version` | Entero | {{pending: sí o no}} | Capa de persistencia | Contador de concurrencia optimista |
| `tenant_id` | Referencia | Si es multi-tenant | Aplicación | Tenant propietario |

## Reglas

- [ ] Los timestamps se guardan en UTC; la conversión a hora local ocurre solo en la presentación.
- [ ] Las referencias a actores apuntan a un identificador estable, nunca a un nombre o correo.
- [ ] Los actores de sistema (procesos, integraciones) tienen identificadores propios, distintos de los usuarios.
- [ ] Los campos de auditoría no se pueden editar desde APIs públicas.
- [ ] Los registros con borrado lógico se excluyen de las consultas por defecto y siguen la [política de retención](retention-policy.md).
- [ ] Los nombres de campo son consistentes en todos los almacenes: {{pending: convención de nombres, por ejemplo snake_case}}

## Historial de cambios

Los campos de auditoría muestran solo el último cambio. Decide si hace falta un historial completo:

| Opción | Cuándo encaja | Decisión |
| --- | --- | --- |
| Solo último cambio | Datos de bajo riesgo | {{pending: elegir por categoría de entidad}} |
| Tabla de historial por entidad | Hace falta ver valores anteriores | |
| Log de auditoría append-only | Acciones reguladas, eventos de seguridad | |

Los logs de auditoría no deben copiar valores Sensibles en claro; ver la [clasificación de datos personales](pii-classification.md).

## Acciones auditadas

| Acción | Entidad | Datos registrados | Retención |
| --- | --- | --- | --- |
| Inicio / cierre de sesión | Sesión | Actor, hora, origen | {{pending: plazo}} |
| Cambio de permisos | Rol, usuario | Actor, antes, después | |
| Exportación de datos | | | |

## Cómo verificar

- Las specs de módulo referencian este estándar en lugar de redefinir campos (ver el [ejemplo de módulo](../04-modules/example/module-spec.md)).
- `dixi check` y `/dixi.data` o `$dixi-data` sirven para revisar entidades nuevas contra esta lista.

## Relacionados

- [Clasificación de datos personales](pii-classification.md)
- [Política de retención](retention-policy.md)
- [Ejemplo de módulo](../04-modules/example/module-spec.md)
- [Plan de pruebas](../11-quality/test-plan.md)
