# Estrategia de identidad y acceso

## Propósito

Definir cómo se identifican personas, servicios y agentes en toda la plataforma y cómo se concede,
comprueba y revoca el acceso. Una estrategia coherente evita que cada producto invente su propio
inicio de sesión y modelo de permisos, lo que provoca huecos, cuentas duplicadas y registros de
auditoría incoherentes.

## Tipos de identidad

| Identidad | Ejemplos | Cómo se autentica | Duración |
|---|---|---|---|
| Usuario final | {{pending: personas}} | {{pending: método}} | {{pending: duración de la sesión}} |
| Personal interno | {{pending: roles internos}} | {{pending: método, incluido el segundo factor}} | {{pending: duración}} |
| Servicio | Backends de producto, tareas programadas | {{pending: credenciales de corta duración o identidad de carga de trabajo}} | {{pending: periodo de rotación}} |
| Agente de IA | Asistentes que actúan por una persona o un servicio | {{pending: credencial delegada y acotada}} | {{pending: duración}} |

Elegir un proveedor de identidad es una decisión del proyecto que se registra en un ADR, no aquí.

## Principios

- Una identidad por persona en todos los productos; los productos no guardan sus propias contraseñas.
- Mínimo privilegio por defecto; el acceso se concede a roles, no a individuos.
- Cada petición lleva identidad y contexto de tenencia, y cada servicio los verifica.
- Los agentes actúan con los permisos de la persona o el servicio que representan, nunca más.
- Los cambios de acceso quedan registrados y se pueden revisar.

## Modelo de autorización

- Modelo: {{pending: basado en roles, en atributos o una combinación}}
- Dónde se decide: {{pending: servicio central, cada producto, o ambos}}
- Alcance de un rol: {{pending: global, por tenencia o por recurso}}

| Rol | Productos | Alcance | Concedido por |
|---|---|---|---|
| {{pending: rol}} | {{pending: productos}} | {{pending: alcance}} | {{pending: quien aprueba}} |

## Ciclo de vida

- Alta: {{pending: cómo se crean las cuentas y se asignan roles}}
- Revisión periódica: {{pending: cada cuánto se revisa quién tiene acceso}}
- Baja: {{pending: tiempo máximo para revocar el acceso tras un cambio de rol}}
- Acceso de emergencia: {{pending: procedimiento de acceso excepcional y quién lo aprueba}}

## Relacionados

- [Estrategia de tenencia](tenant-strategy.md)
- [Modelo de autenticación y autorización](../13-security/authn-authz-model.md)
- [Roles internos](../01-business/actors/internal-roles.md)
- [Mapa de servicios compartidos](shared-services-map.md)
