# Plan de pruebas de seguridad

## Propósito

Planificar cómo el proyecto comprueba sus requisitos de seguridad, para que la seguridad se pruebe junto con las funcionalidades en lugar de darse por supuesta. Este plan lista verificaciones previstas; no es evidencia de que se haya ejecutado ninguna.

Estado: borrador. {{pending: confirmar el alcance de las pruebas de seguridad con la persona responsable de seguridad}}

## Alcance

| Activo o área | Amenazas consideradas | Responsable |
|---------------|-----------------------|-------------|
| {{pending: activo, por ejemplo cuentas de usuario}} | {{pending: amenazas}} | {{pending: responsable}} |
| {{pending: activo, por ejemplo datos personales}} | {{pending: amenazas}} | {{pending: responsable}} |

## Verificaciones previstas

| Verificación | Qué busca | Cuándo | Bloquea la integración |
|--------------|-----------|--------|------------------------|
| Análisis de dependencias | Dependencias con vulnerabilidades conocidas | {{pending: cuándo}} | {{pending: sí/no y severidad}} |
| Análisis de secretos | Credenciales commiteadas en el repositorio | {{pending: cuándo}} | {{pending: sí/no}} |
| Análisis estático | Patrones de código inseguros | {{pending: cuándo}} | {{pending: sí/no}} |
| Pruebas de autenticación y autorización | Acceso sin permiso, escalada de privilegios | En cada cambio a reglas de acceso | {{pending: sí/no}} |
| Pruebas de validación de entradas | Inyección, entradas malformadas, cargas excesivas | En cada cambio a entradas | {{pending: sí/no}} |
| Pruebas dinámicas | Vulnerabilidades en la aplicación en ejecución | {{pending: cuándo}} | {{pending: sí/no}} |

La elección de herramientas es una decisión del proyecto. {{pending: elegir herramientas para cada verificación}}

## Redactar pruebas de seguridad

- Escribe primero las pruebas negativas: la petición sin permiso debe fallar.
- Prueba el camino permitido y el denegado de cada regla de acceso.
- Nunca uses credenciales reales ni datos personales reales en pruebas; usa datos generados y direcciones `@example.com`.

## Hallazgos

- Registra los hallazgos con severidad, responsable y fecha límite. {{pending: escala de severidad y tiempos de respuesta}}
- Un hallazgo solo se cierra cuando una prueba demuestra la corrección.
- Los riesgos aceptados se registran con la persona que los aceptó.

## Relacionados

- [Estrategia de calidad](quality-strategy.md)
- [Requisitos no funcionales](non-functional-requirements.md)
- [Revisión basada en riesgo](risk-based-review.md)
- [Plan de pruebas](test-plan.md)
- [Instrucciones del proyecto](../AGENTS.md)
