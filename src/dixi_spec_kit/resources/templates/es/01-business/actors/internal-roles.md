# Roles internos

## Propósito

Enumerar los roles dentro de la organización que operan, dan soporte o gobiernan el producto, con
sus responsabilidades y los permisos que necesitan. Esta página alimenta el modelo de autorización,
las rutas de escalado y las puertas de revisión humana del flujo SDD. Describe roles, no individuos.

## Catálogo de roles

| ID | Rol | Responsabilidades | Usa el producto para | Derechos de decisión |
|---|---|---|---|---|
| ROLE-001 | {{pending: p. ej. responsable de producto}} | {{pending: responsabilidades}} | {{pending: tareas}} | {{pending: qué aprueba este rol}} |
| ROLE-002 | {{pending: p. ej. agente de soporte}} | {{pending: responsabilidades}} | {{pending: tareas}} | {{pending: qué aprueba este rol}} |
| ROLE-003 | {{pending: p. ej. operador o administrador}} | {{pending: responsabilidades}} | {{pending: tareas}} | {{pending: qué aprueba este rol}} |

## Necesidades de acceso

Aplica mínimo privilegio: parte de ningún acceso y añade solo lo que cada tarea requiere.

| Rol | Datos que puede leer | Acciones que puede realizar | Acciones que requieren una segunda persona |
|---|---|---|---|
| {{pending: rol}} | {{pending: alcance de datos}} | {{pending: acciones}} | {{pending: acciones sensibles}} |

## Puertas de revisión humana

Quién valida cada tipo de cambio antes de construirlo o fusionarlo:

| Tipo de cambio | Rol que valida |
|---|---|
| Decisiones estructurales (dominios, contratos, arquitectura) | {{pending: rol}} |
| Reglas de negocio y precios | {{pending: rol}} |
| Impacto en seguridad y privacidad | {{pending: rol}} |

Los agentes de IA pueden redactar y proponer, pero nunca sustituyen al rol que valida.

## Segregación de funciones

- {{pending: pares de acciones que un mismo rol no debe realizar en solitario}}

## Relacionados

- [Personas](personas.md)
- [Socios externos](external-partners.md)
- [Modelo de autenticación y autorización](../../13-security/authn-authz-model.md)
- [Instrucciones para agentes](../../AGENTS.md)
