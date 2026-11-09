# Problemas conocidos

## Propósito

Listar problemas que se entienden pero aún no se han corregido, con su alternativa, para que soporte responda rápido y nadie vuelva a investigar lo mismo.

Estado: borrador. {{pending: nombrar a quien mantiene esta lista}}

## Cómo se usa

- Soporte revisa esta lista antes de escalar un ticket.
- Ingeniería añade una entrada en cuanto un problema se confirma y no se corregirá en {{pending: días}}.
- Una entrada solo se elimina cuando la corrección está publicada y verificada.

## Formato de entrada

| ID | Resumen | Afecta a | Alternativa | Severidad | Ticket | Desde | Corrección prevista |
|----|---------|----------|-------------|-----------|--------|-------|---------------------|
| KI-001 | {{pending: descripción breve}} | {{pending: función, plataforma, usuarios}} | {{pending: pasos que pueden seguir usuarios o soporte}} | {{pending: SEV3 / SEV4}} | {{pending: enlace}} | {{pending: fecha}} | {{pending: versión o fecha}} |

## Cómo escribir una buena entrada

- Describe el síntoma como lo ve el usuario, no la causa interna.
- Da una alternativa que soporte pueda compartir tal cual, o di claramente que no la hay.
- Registra qué versiones, navegadores o planes se ven afectados.
- Nunca pegues datos personales, tokens ni nombres de clientes en una entrada.

## Severidad

Las entradas suelen ser SEV3 o SEV4. Un problema que sería SEV2 o mayor es un incidente, no un problema conocido: sigue los [niveles de incidente](incident-levels.md).

## Público o interno

{{pending: decidir si algunas entradas se publican a los usuarios, por ejemplo en una página de ayuda}}

Las entradas marcadas como públicas las revisa el rol de comunicación antes de publicarse.

## Revisión

- Cada {{pending: frecuencia}}, revisa cada entrada: sigue vigente, la alternativa funciona, la fecha de corrección es realista.
- Una entrada con más de {{pending: meses}} recibe una decisión explícita: corregir, aceptar o cerrar.

## Relacionados

- [Modelo de soporte](support-model.md)
- [Catálogo de servicios](service-catalog.md)
- [Niveles de incidente](incident-levels.md)
