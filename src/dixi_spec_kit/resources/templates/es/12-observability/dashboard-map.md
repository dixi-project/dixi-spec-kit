# Mapa de tableros

## Propósito

Listar los tableros en los que confía el equipo, para quién es cada uno y qué pregunta responde. Un conjunto corto de tableros conocidos vale más que muchos olvidados.

## Reglas

- Cada tablero responde a una audiencia y a pocas preguntas; nómbralo según ellas.
- Los paneles usan solo métricas del [catálogo de métricas](metrics-catalog.md).
- Muestra SLOs y marcas de despliegue donde ayuden a explicar cambios.
- Los tableros se versionan como código cuando la herramienta lo permite: {{pending: ubicación en el repositorio}}.
- Revisa la lista {{pending: frecuencia}}; archiva los tableros que nadie abrió.

## Inventario de tableros

| Tablero | Audiencia | Preguntas que responde | Paneles clave | Responsable | Enlace |
|---|---|---|---|---|---|
| Resumen del servicio | Persona de guardia | ¿Está sano ahora mismo? | Tasa de peticiones, tasa de errores, latencia p95, saturación | {{pending: rol}} | {{pending: enlace}} |
| Estado de SLOs | Ingeniería y producto | ¿Estamos dentro de los objetivos? | SLI en la ventana, presupuesto de error restante, velocidad de consumo | {{pending: rol}} | {{pending: enlace}} |
| Salud de la versión | Quien publica la versión | ¿Empeoró algo el último despliegue? | Errores y latencia por versión, marcas de despliegue | {{pending: rol}} | {{pending: enlace}} |
| Trabajo asíncrono | Persona de guardia | ¿Las tareas y colas van al día? | Acumulación, antigüedad del mensaje más viejo, fallos, mensajes muertos | {{pending: rol}} | {{pending: enlace}} |
| Negocio | Producto | {{pending: pregunta de negocio}} | {{pending: métricas de negocio}} | {{pending: rol}} | {{pending: enlace}} |

## Guía de diseño

1. Fila superior: los pocos números que dicen «sano o no».
2. Centro: desglose por ruta, tarea o dependencia.
3. Abajo: recursos y capacidad.
4. Cada panel tiene un título que indica cómo se ve «mal».

## Acceso

- Lectura: {{pending: roles}}
- Edición: {{pending: roles}}
- Los tableros nunca muestran datos personales ni secretos.

## Relacionados

- [Catálogo de métricas](metrics-catalog.md)
- [SLIs, SLOs y SLAs](slis-slos-slas.md)
- [Reglas de alertas](alerting-rules.md)
- [Estrategia de observabilidad](observability-strategy.md)
