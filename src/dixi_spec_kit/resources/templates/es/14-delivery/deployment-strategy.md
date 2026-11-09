# Estrategia de despliegue

## Propósito

Definir cómo una versión nueva reemplaza a la que está corriendo con el menor impacto posible, y cómo decide el equipo que un despliegue terminó o debe revertirse.

## Opciones

| Estrategia | Cómo funciona | Adecuada para | Costo |
|---|---|---|---|
| Recreate | Detener la vieja, arrancar la nueva | Sitios estáticos, herramientas internas que toleran una pausa corta | Tiempo fuera de servicio |
| Rolling | Reemplazar instancias poco a poco | Servicios sin estado | Dos versiones conviven brevemente |
| Blue/green | Correr la nueva junto a la vieja y cambiar el tráfico de golpe | Reversión rápida | Doble capacidad durante el cambio |
| Canary | Enviar una parte pequeña del tráfico a la nueva y aumentar | Servicios con mucho tráfico | Requiere buenas métricas por versión |

Estrategia elegida por componente: {{pending: registrar en la tabla siguiente y en un ADR}}

| Componente | Estrategia | Tiempo de observación | Disparador de reversión |
|---|---|---|---|
| {{pending: web o sitio}} | {{pending: estrategia}} | {{pending: minutos}} | {{pending: condición}} |
| {{pending: servicio}} | {{pending: estrategia}} | {{pending: minutos}} | {{pending: condición}} |

## Antes de desplegar

- [ ] `make verify` en verde sobre el commit exacto que se despliega
- [ ] El mismo artefacto ya verificado en staging
- [ ] Los cambios de base de datos son compatibles con la versión en ejecución
- [ ] Notas de versión y plan de reversión escritos
- [ ] Aprobación humana registrada para producción

## Durante y después

1. Despliega fuera de {{pending: ventanas bloqueadas, p. ej. horas pico}}.
2. Vigila la tasa de errores y la latencia de la versión nueva durante el tiempo de observación.
3. Si salta una alerta o falla una prueba de humo, revierte primero e investiga después.
4. Da el despliegue por terminado solo cuando el tiempo de observación acabe sin alertas.

## Feature flags

- Usa flags para separar desplegar código de liberar una funcionalidad.
- Cada flag tiene responsable y fecha de retiro: {{pending: vida máxima de una flag}}.

## Relacionados

- [Estrategia de reversión](rollback-strategy.md)
- [Entornos](environments.md)
- [Visión general de CI/CD](ci-cd-overview.md)
- [Reglas de alertas](../12-observability/alerting-rules.md)
- [Arquitectura de despliegue](../09-architecture/deployment-architecture.md)
