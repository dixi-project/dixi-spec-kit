# Catálogo de datos de muestra

## Propósito

Listar los conjuntos de datos sintéticos canónicos que usa el proyecto, qué contiene cada uno, qué estados cubre y dónde se usa. Todo el mundo usa los mismos registros con nombre, para que pruebas, demos y reportes de errores puedan referirse a ellos sin ambigüedad.

Estado: borrador. {{pending: confirmar los primeros conjuntos de datos a partir del modelo de dominio}}

## Conjuntos de datos

| Conjunto | Propósito | Registros | Estados cubiertos | Idiomas | Usado por |
|----------|-----------|-----------|-------------------|---------|-----------|
| Usuarios | Cuentas con distintos roles | {{pending}} | Activo, invitado, suspendido, eliminado | ES, EN | Pruebas, semilla, demo |
| Organizaciones | Tenants o cuentas cliente, si aplica | {{pending}} | Prueba, activa, cancelada | ES, EN | Pruebas, semilla, demo |
| Planes | Planes o niveles del producto, si aplica | {{pending}} | Vigentes y retirados | ES, EN | Pruebas, semilla |
| {{pending: entidad central del dominio}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |
| Solicitudes de soporte | Solicitudes de cada severidad | {{pending}} | Abierta, en espera, resuelta | ES, EN | Demo |

## Registros con nombre

Da a algunos registros nombres estables y rasgos documentados, para poder decir «entra como el administrador de la organización en prueba».

| Clave | Descripción | Idioma | Contacto de ejemplo |
|-------|-------------|--------|---------------------|
| `user.admin` | Administrador con todos los permisos | EN | `admin.demo@example.com` |
| `user.member_es` | Miembro regular que usa español | ES | `miembro.demo@example.com` |
| `user.suspended` | Cuenta suspendida para probar reglas de acceso | EN | `suspended.demo@example.com` |
| `org.trial` | Organización en periodo de prueba | {{pending}} | n/a |

Las contraseñas o tokens de estas cuentas se generan por entorno y nunca se escriben en este catálogo.

## Esquema y formato

- Cada conjunto tiene un esquema documentado y alineado con el modelo de datos canónico.
- {{pending: elegir el formato de archivo de los fixtures y dónde viven los esquemas}}
- Cada registro incluye los campos de auditoría que exigen los estándares de datos, con valores sintéticos.

## Casos límite a incluir

- Campos vacíos y de longitud máxima.
- Caracteres con acentos, símbolos y escrituras mezcladas.
- Fechas cerca de límites: fin de mes, 29 de febrero, cambios de zona horaria.
- Importes en varias monedas y con valores cero o negativos cuando sean válidos.
- Registros en cada estado de su ciclo de vida, incluidos eliminados o archivados.

## Responsables

| Conjunto | Responsable | Última revisión |
|----------|-------------|-----------------|
| {{pending}} | {{pending}} | {{pending}} |

## Relacionados

- [Estrategia de fixtures](fixtures-strategy.md)
- [Escenarios de demo](demo-scenarios.md)
- [Clasificación de PII](../08-data/pii-classification.md)
- [Personas](../01-business/actors/personas.md)
- [Plan de pruebas](../11-quality/test-plan.md)
