# Plantilla de integración externa

## Propósito

Documentar una dependencia de un sistema que el proyecto no controla (pagos, mensajería,
identidad, proveedor de datos, etc.): qué se usa, cómo falla y cómo se protege. Copia la estructura
de abajo para cada integración.

## Plantilla

```markdown
# Integración: <nombre del sistema>

ID: {{pending: ID de la integración}}
Responsable: {{pending: persona responsable de la relación}}
Estado: en evaluación | activa | deprecada

## Propósito

Para qué usa el proyecto este sistema y qué features dependen de él.

## Interfaz

- Protocolo y contrato: (API, webhook, intercambio de archivos, SDK)
- Versión del contrato o documentación usada:
- Entornos disponibles (sandbox, producción):

## Autenticación y secretos

- Método: {{pending: método de autenticación}}
- Los secretos viven en el almacén de secretos; aquí solo nombres, nunca valores.
- Rotación: {{pending: periodo y procedimiento de rotación}}

## Datos intercambiados

| Dirección | Datos | ¿Datos personales? | Base legal o acuerdo |
|---|---|---|---|

## Límites y costos

- Límites de uso y cuotas:
- Modelo de precios y alerta de presupuesto:

## Comportamiento ante fallos

| Fallo | Detección | Nuestro comportamiento |
|---|---|---|
| Timeout | | reintento con backoff, luego ... |
| Respuesta de error | | |
| Caído durante horas | | modo degradado: ... |

## Aislamiento

La integración queda envuelta en un adaptador dentro del módulo dueño; el dominio no
depende de su SDK ni de sus formas de datos.

## Pruebas

- Pruebas de contrato contra respuestas grabadas o un sandbox.
- Pruebas de fallo para cada fila de la tabla anterior.

## Plan de salida

Cómo reemplazar este sistema y qué se perdería.
```

## Relacionados

- [Plantilla de módulo](module-template.md)
- [Estándar de manejo de errores](../error-handling-standard.md)
- [Estándar de código seguro](../secure-coding-standard.md)
- [Plantilla de runbook](runbook-template.md)
