# Niveles de soporte

## Propósito

Definir los niveles de soporte que ofrece el proyecto, qué incluye cada uno, cómo se clasifican las solicitudes por severidad y cómo se escalan. Los compromisos escritos aquí deben coincidir con lo que el equipo puede entregar de verdad.

Estado: borrador. {{pending: definir los niveles de soporte y los objetivos de respuesta de cada uno}}

## Niveles

| Nivel | Para quién | Canales | Horario | Objetivo de primera respuesta | Idiomas |
|-------|-----------|---------|---------|-------------------------------|---------|
| Autoservicio | Todos los usuarios | Centro de ayuda, comunidad | Siempre disponible | n/a | ES, EN |
| Estándar | {{pending}} | {{pending: por ejemplo correo o formulario}} | {{pending}} | {{pending}} | ES, EN |
| Prioritario | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |

Los objetivos de respuesta son metas salvo que un acuerdo firmado diga otra cosa. No prometas más de lo que permite el personal disponible.

## Severidad

| Severidad | Definición | Ejemplo |
|-----------|------------|---------|
| SEV1 | Servicio no disponible o datos en riesgo para muchos usuarios | Nadie puede iniciar sesión |
| SEV2 | Funcionalidad importante rota, sin alternativa razonable | Los pagos fallan en un mercado |
| SEV3 | Funcionalidad degradada, existe alternativa | La exportación es lenta |
| SEV4 | Pregunta, problema menor o solicitud | Cómo cambiar un ajuste |

SEV1 y SEV2 siguen el proceso de incidentes además de la atención de soporte.

## Triaje

1. Confirma que la solicitud se entiende; pide los datos faltantes con una plantilla.
2. Asigna la severidad según el impacto, no según cómo está redactada la solicitud.
3. Busca problemas conocidos y artículos de ayuda antes de investigar.
4. Envía a la cola o equipo correcto; registra la decisión.
5. Mantén informado al cliente en su idioma en los intervalos acordados.

## Escalamiento

| Desde | Hacia | Cuándo |
|-------|-------|--------|
| Soporte | Ingeniería de guardia | SEV1 o SEV2, o sospecha de defecto |
| Soporte | Contacto de seguridad | Posible problema de seguridad o privacidad |
| Soporte | {{pending: rol}} | Disputas de facturación o preguntas contractuales |

## Idiomas de soporte

- Cada idioma soportado del producto tiene contenido de ayuda.
- Idiomas con atención en vivo: {{pending}}. Cuando un idioma no tiene atención en vivo, dilo con claridad y ofrece la alternativa.

## Métricas

| Métrica | Objetivo |
|---------|----------|
| Tiempo de primera respuesta por nivel | {{pending}} |
| Tiempo de resolución por severidad | {{pending}} |
| Satisfacción tras la resolución | {{pending}} |
| Solicitudes resueltas con contenido de autoservicio | {{pending}} |

## Relacionados

- [Estrategia de éxito del cliente](success-strategy.md)
- [Estructura del centro de ayuda](help-center-structure.md)
- [Niveles de incidente](../15-operations/incident-levels.md)
- [Matriz de escalamiento](../15-operations/escalation-matrix.md)
- [Comunicación de caídas al cliente](../15-operations/playbooks/comms-outage-customer.md)
