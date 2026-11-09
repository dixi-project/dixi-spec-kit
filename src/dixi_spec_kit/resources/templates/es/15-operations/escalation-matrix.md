# Matriz de escalamiento

## Propósito

Dejar claro a quién se llama, en qué orden y con qué rapidez para cada nivel de incidente, para que nadie tenga que improvisar contactos durante una caída.

Estado: borrador. {{pending: nombrar al responsable de mantener esta matriz al día}}

## Roles

| Rol | Responsabilidad durante un incidente |
|-----|--------------------------------------|
| Primera respuesta | Reconoce la alerta, clasifica, inicia la mitigación |
| Líder del incidente | Coordina, decide, lleva la cronología |
| Líder de comunicación | Redacta los avisos internos y a clientes |
| Experto técnico | Conoce a fondo el componente afectado |
| Contacto ejecutivo | Decisiones de negocio, legales y declaraciones públicas |

En un equipo pequeño una persona puede tener varios roles; deja escrito quién tiene cuál.

## Matriz por nivel

| Nivel | Paso 1 | Paso 2 (si no hay respuesta) | Paso 3 | Notificar |
|-------|--------|------------------------------|--------|-----------|
| SEV1 | Primera respuesta, de inmediato | Líder del incidente tras {{pending: minutos}} | Contacto ejecutivo tras {{pending: minutos}} | Líder de comunicación al instante |
| SEV2 | Primera respuesta | Líder del incidente tras {{pending: minutos}} | Experto técnico si hace falta | Líder de comunicación si los clientes lo notan |
| SEV3 | Primera respuesta en horario laboral | Líder del equipo al día siguiente | — | — |
| SEV4 | Triaje del backlog | — | — | — |

## Contactos

| Rol | Principal | Suplente | Canal |
|-----|-----------|----------|-------|
| {{pending: rol}} | {{pending: persona o rotación}} | {{pending: suplente}} | {{pending: herramienta de avisos, teléfono, chat}} |

Usa direcciones de rol como `oncall@example.com`, no personales, y mantén los teléfonos personales fuera del repositorio.

## Reglas

- Escalar pronto nunca es un error; quedarse callado sí.
- Si un paso no responde a tiempo, pasa al siguiente sin esperar.
- Con terceros (proveedores, autoridades, clientes) solo contacta el rol indicado aquí.
- Un posible incidente de seguridad o privacidad sigue además la [respuesta a incidentes](../13-security/incident-response.md).

## Revisión

Prueba la matriz con un simulacro de avisos cada {{pending: frecuencia}} y tras cada cambio en el equipo.

## Relacionados

- [Niveles de incidente](incident-levels.md)
- [Restaurar el servicio](playbooks/restore-service.md)
- [Comunicación de caída a clientes](playbooks/comms-outage-customer.md)
- [Respuesta a incidentes](../13-security/incident-response.md)
