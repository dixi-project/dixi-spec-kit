# Playbook de abandono

## Propósito

Definir cómo el proyecto detecta clientes en riesgo de irse, qué acciones responden a cada señal de alerta y cómo se gestionan las cancelaciones con respeto. El objetivo es corregir las razones por las que la gente se va, no dificultar la salida.

Estado: borrador. {{pending: definir qué cuenta como abandono para este producto y la tasa objetivo}}

## Tipos de abandono

| Tipo | Definición |
|------|------------|
| Voluntario | El cliente decide cancelar o dejar de usar el producto |
| Involuntario | El acceso termina por otras razones, como un pago fallido |
| Contracción | El cliente se queda pero reduce su uso o su plan |

## Métricas

| Métrica | Definición | Objetivo |
|---------|------------|----------|
| Tasa de abandono de clientes | Clientes perdidos en un periodo / clientes al inicio | {{pending}} |
| Tasa de abandono de ingresos, si aplica | Ingresos perdidos en un periodo / ingresos al inicio | {{pending}} |
| Tasa de recuperación | Clientes en riesgo que vuelven a estar sanos | {{pending}} |

Mide por segmento, mercado e idioma.

## Señales de alerta

- Caída brusca del uso activo o sin actividad durante {{pending: días}}.
- Funcionalidad clave nunca adoptada tras el onboarding.
- Solicitudes de soporte repetidas o sin resolver.
- Opinión de satisfacción baja.
- Pago fallido o solicitud de bajar de plan.
- El contacto principal deja la organización cliente, en cuentas grandes.

## Playbooks por disparador

| Disparador | Acción | Canal | Responsable | Momento |
|------------|--------|-------|-------------|---------|
| Inactividad | Mensaje útil con el siguiente paso relevante | {{pending}} | {{pending}} | {{pending}} |
| Satisfacción baja | Seguimiento personal para entender el problema | {{pending}} | {{pending}} | {{pending}} |
| Pago fallido | Avisos claros y una forma sencilla de actualizar el pago | {{pending}} | {{pending}} | {{pending}} |
| Solicitud de cancelación | Preguntar el motivo; ofrecer opciones relevantes una vez | {{pending}} | {{pending}} | Inmediato |

## Reglas de cancelación

- Cancelar es tan fácil como registrarse y nunca exige llamar ni esperar.
- Las ofertas para quedarse (pausa, plan menor, ayuda) se muestran una vez y se pueden rechazar en un paso.
- El cliente puede exportar sus datos antes de irse, según la política de retención.
- Los mensajes se envían en el idioma del cliente.

## Aprender del abandono

1. Registra el motivo de cada cancelación con una lista fija más texto libre.
2. Revisa los motivos {{pending: frecuencia}} y vincula los recurrentes con trabajo de producto o soporte.
3. Sigue si los cambios reducen el abandono por ese motivo.

## Relacionados

- [Estrategia de éxito del cliente](success-strategy.md)
- [Niveles de soporte](support-tiers.md)
- [Estructura del centro de ayuda](help-center-structure.md)
- [Política de retención](../08-data/retention-policy.md)
- [Estrategia de crecimiento](../25-growth/growth-strategy.md)
