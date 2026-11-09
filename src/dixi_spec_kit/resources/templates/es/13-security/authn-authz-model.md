# Modelo de autenticación y autorización

## Propósito

Describir cómo usuarios y servicios demuestran quiénes son (autenticación) y qué puede hacer cada uno (autorización), para que todas las funcionalidades apliquen las mismas reglas y cada decisión de acceso pueda probarse.

Estado: borrador. {{pending: nombrar al responsable del modelo de acceso}}

## Identidades

| Tipo de identidad | Ejemplo | Cómo se autentica |
|-------------------|---------|-------------------|
| Usuario final | Cuenta de cliente | {{pending: p. ej. contraseña más segundo factor, inicio de sesión único, enlace mágico}} |
| Administrador | Operador de back-office | {{pending: método; ¿segundo factor obligatorio?}} |
| Servicio | Tarea en segundo plano, otro sistema | {{pending: p. ej. token de vida corta, TLS mutuo}} |
| Agente de IA o automatización | Tarea programada | {{pending: método y alcance}} |

## Reglas de autenticación

- Proveedor de identidad o mecanismo: {{pending: elegir}}
- Política de contraseñas y segundo factor: {{pending: definir}}
- Duración de sesión, expiración por inactividad y revocación: {{pending: definir}}
- Recuperación de cuenta que no pueda usarse para robarla: {{pending: definir}}
- Limitación de intentos y bloqueo en los endpoints de inicio de sesión y recuperación.

## Modelo de autorización

Enfoque: {{pending: basado en roles, en atributos, en relaciones o mixto}}

| Rol | Puede | No puede |
|-----|-------|----------|
| {{pending: rol}} | {{pending: acciones}} | {{pending: acciones}} |

## Reglas que sigue toda funcionalidad

- Denegar por defecto; conceder de forma explícita.
- Comprobar la autorización en el servidor en cada petición, nunca solo en la interfaz.
- Comprobar la propiedad del recurso concreto, no solo el rol (evita acceder a registros de otro usuario cambiando un ID).
- Aislamiento entre inquilinos, si es multi-tenant: {{pending: definir cómo se imponen los límites entre inquilinos}}
- Las acciones privilegiadas se registran con quién, qué y cuándo.

## Verificación

Cada regla anterior se corresponde con pruebas en el plan: un caso permitido, uno denegado y uno de propiedad por cada recurso protegido. {{pending: listar los IDs de prueba}}

## Relacionados

- [Modelo de amenazas](threat-model.md)
- [Gestión de secretos](secret-management.md)
- [Controles de protección de datos](data-protection-controls.md)
- [Plan de pruebas](../11-quality/test-plan.md)
