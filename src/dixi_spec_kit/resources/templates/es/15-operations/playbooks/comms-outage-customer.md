# Comunicación de caída a clientes

## Propósito

Contar a los usuarios qué está pasando durante una caída de forma clara, honesta y oportuna, sin especular ni prometer lo que no se puede cumplir.

Estado: borrador. {{pending: nombrar el rol de líder de comunicación}}

## Cuándo aplica

Cualquier incidente que los usuarios puedan notar, normalmente SEV1 y SEV2 (ver [niveles de incidente](../incident-levels.md)).

## Canales

| Canal | Se usa para | Responsable |
|-------|-------------|-------------|
| {{pending: página de estado}} | Todos los incidentes visibles | Líder de comunicación |
| {{pending: banner en la aplicación}} | Caída en curso | Líder de comunicación |
| {{pending: correo, p. ej. support@example.com}} | Cuentas afectadas, resumen final | Soporte |

## Pasos

1. **Primer aviso** en menos de {{pending: minutos}} desde que se declara el incidente, aunque no se conozca la causa.
2. **Actualizaciones** cada {{pending: intervalo}} mientras el incidente siga abierto, aunque nada haya cambiado.
3. **Aviso de resolución** cuando se cumplan los criterios de cierre de [restaurar el servicio](restore-service.md).
4. **Seguimiento** con un resumen breve para SEV1 en {{pending: días}}.

El líder del incidente revisa cada mensaje antes de publicarlo. Un agente de IA puede redactar; una persona publica.

## Plantillas de mensaje

Primer aviso:

> Estamos investigando un problema que afecta a {{pending: función}}. Algunos usuarios pueden {{pending: síntoma}}. Próxima actualización a las {{pending: hora y zona horaria}}.

Actualización:

> Identificamos la causa y estamos aplicando una corrección. {{pending: qué funciona y qué no}}. Próxima actualización a las {{pending: hora}}.

Resolución:

> El problema que afectaba a {{pending: función}} quedó resuelto a las {{pending: hora}}. {{pending: si los usuarios deben hacer algo}}. Lamentamos las molestias.

## Reglas

- Describe lo que viven los usuarios, no nombres de componentes internos.
- Nunca culpes a un proveedor ni a una persona en mensajes públicos.
- No des una hora de fin de la que no estés seguro.
- Publica en todos los idiomas que soporta el producto. {{pending: listar idiomas}}
- Si pueden estar involucrados datos personales, detente y consulta al líder del incidente antes de escribir nada.

## Relacionados

- [Niveles de incidente](../incident-levels.md)
- [Matriz de escalamiento](../escalation-matrix.md)
- [Restaurar el servicio](restore-service.md)
- [Respuesta a incidentes](../../13-security/incident-response.md)
