# Arquitectura de rendimiento

## Propósito

Definir los objetivos de rendimiento y capacidad del sistema y las tácticas arquitectónicas para alcanzarlos: caché, trabajo asíncrono, patrones de acceso a datos y escalado. Las cifras son presupuestos de diseño hasta que se midan.

## Presupuestos

| Métrica | Presupuesto | Ámbito |
|---|---|---|
| Tiempo de respuesta del servidor (p95) | {{pending: milisegundos}} | Operaciones de lectura principales |
| Tiempo de respuesta del servidor (p95) | {{pending: milisegundos}} | Operaciones de escritura principales |
| Carga de página (contenido principal) | {{pending: segundos}} | Páginas clave en un dispositivo de gama media |
| Rendimiento | {{pending: peticiones por segundo}} | Pico esperado |
| Latencia de tareas en segundo plano | {{pending: duración}} | Desde que se encola hasta que termina |

## Carga esperada

- Personas usuarias y crecimiento: {{pending: estimación actual y a 12 meses}}
- Patrones de pico: {{pending: picos diarios, estacionales o por eventos}}
- Volumen de datos: {{pending: registros y ritmo de crecimiento}}

## Tácticas

- **Caché**: {{pending: qué se cachea, dónde y cómo se invalida}}.
- **Procesamiento asíncrono**: mover el trabajo lento o no crítico a tareas en segundo plano.
- **Acceso a datos**: indexar las consultas principales, paginar listados, evitar patrones N+1.
- **Tamaño de respuestas**: comprimir, enviar solo los campos necesarios, optimizar medios.
- **Escalado**: {{pending: horizontal, vertical o automático, y su disparador}}.
- **Entrega estática**: servir recursos estáticos desde una caché de borde.

## Rutas críticas

| Ruta | Por qué importa | Diseño actual | Riesgo |
|---|---|---|---|
| {{pending: operación}} | {{pending: impacto en las personas usuarias}} | {{pending: enfoque}} | {{pending: riesgo}} |

## Medición

- Herramientas y entorno para pruebas de carga: {{pending: herramienta y entorno objetivo}}
- Cuándo se revisa el rendimiento: {{pending: por versión, cada noche, antes del lanzamiento}}
- Regla de regresión: {{pending: qué bloquea una versión}}

## Relacionados

- [Arquitectura de resiliencia](resilience-architecture.md)
- [Diagrama de contenedores](container-diagram.md)
- [Arquitectura de despliegue](deployment-architecture.md)
- [Plan de pruebas](../11-quality/test-plan.md)
- [Decisiones de arquitectura](adr/README.md)
