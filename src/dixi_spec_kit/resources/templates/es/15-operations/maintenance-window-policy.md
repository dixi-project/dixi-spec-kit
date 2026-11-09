# Política de ventanas de mantenimiento

## Propósito

Definir cuándo puede hacerse trabajo planificado que afecte a usuarios, cómo se aprueba y cómo se avisa con antelación.

Estado: borrador. {{pending: nombrar al responsable de esta política}}

## Ventanas

| Tipo | Cuándo | Aviso a usuarios | Aprobación |
|------|--------|------------------|------------|
| Estándar | {{pending: día, horario y zona horaria de menor tráfico}} | {{pending: p. ej. 5 días hábiles}} | Responsable del servicio |
| Extendida | {{pending: p. ej. una vez por trimestre, en fin de semana}} | {{pending: p. ej. 2 semanas}} | Responsable del servicio y dueño del producto |
| Emergencia | En cualquier momento | Lo antes posible | Líder del incidente |

Elige la ventana estándar con datos reales de tráfico, no por costumbre. {{pending: confirmar el periodo de menor tráfico con métricas}}

## Qué necesita ventana

- Cambios que provocan caída o un periodo de solo lectura.
- Migraciones de base de datos que bloquean tablas o duran más de {{pending: minutos}}.
- Cambios de infraestructura sin un rollback probado.

Los cambios desplegados sin interrupción y con rollback probado no necesitan ventana.

## Antes de la ventana

1. Escribe el plan: pasos, duración esperada, punto de rollback, responsable.
2. Obtén la aprobación indicada arriba.
3. Avisa a los usuarios en la página de estado y los canales del [modelo de soporte](support-model.md).
4. Confirma que la persona de guardia conoce el trabajo.
5. Congela despliegues no relacionados durante la ventana.

## Durante la ventana

- Sigue el plan; cualquier desviación la decide el responsable y queda escrita.
- Si el trabajo se excede {{pending: minutos}}, haz rollback salvo que el responsable decida otra cosa.
- Mantén un canal interno actualizado cada {{pending: intervalo}}.

## Después de la ventana

- Confirma que las señales de salud son normales.
- Cierra el aviso de la página de estado.
- Registra el resultado y lo que se puede mejorar.

## Periodos bloqueados

{{pending: listar periodos sin mantenimiento planificado, p. ej. lanzamientos, días de ventas pico}}

## Relacionados

- [Catálogo de servicios](service-catalog.md)
- [Modelo de soporte](support-model.md)
- [Comunicación interna de caídas](playbooks/comms-outage-internal.md)
- [Comunicación de caída a clientes](playbooks/comms-outage-customer.md)
