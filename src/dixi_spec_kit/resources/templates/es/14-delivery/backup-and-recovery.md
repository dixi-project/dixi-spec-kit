# Respaldo y recuperación

## Propósito

Registrar qué datos se respaldan, con qué frecuencia, dónde viven las copias y cómo se realiza y prueba una restauración. Un respaldo que nunca se ha restaurado es una suposición, no un respaldo.

## Inventario

| Almacén de datos | Contenido | Método | Frecuencia | Retención | Ubicación de la copia | Cifrado | Responsable |
|---|---|---|---|---|---|---|---|
| Base de datos principal | {{pending: descripción}} | {{pending: snapshot, log continuo o volcado}} | {{pending: frecuencia}} | {{pending: días}} | {{pending: ubicación o cuenta separada}} | {{pending: sí o no}} | {{pending: rol}} |
| Almacenamiento de objetos | {{pending: archivos de usuarios, exportaciones}} | {{pending: versionado o replicación}} | {{pending: frecuencia}} | {{pending: días}} | {{pending: ubicación}} | {{pending: sí o no}} | {{pending: rol}} |
| Configuración | Versionada en el repositorio | Control de versiones | Cada cambio | Historial completo | Repositorio remoto | n/a | {{pending: rol}} |

## Reglas

- Al menos una copia vive fuera de la ubicación principal y fuera del alcance de las credenciales de producción.
- Los respaldos están cifrados; las llaves se gestionan separadas de los datos.
- Borrar respaldos o acortar su retención requiere dos personas.
- La retención respeta la política de retención de datos, incluidas las solicitudes de borrado.

## Procedimiento de restauración

1. Declara la restauración y registra quién la aprobó.
2. Elige el punto de restauración y confirma con la persona responsable la pérdida de datos esperada.
3. Restaura primero en un entorno aislado y verifica la integridad.
4. Cambia la aplicación a los datos restaurados o copia de vuelta los registros necesarios.
5. Registra el tiempo empleado y los datos perdidos.

## Pruebas de restauración

| Almacén de datos | Última prueba | Resultado | Tiempo de restauración | Próxima prueba |
|---|---|---|---|---|
| {{pending: almacén}} | {{pending: fecha}} | {{pending: resultado}} | {{pending: duración}} | {{pending: fecha}} |

Frecuencia de prueba: {{pending: p. ej. trimestral}}. Registra solo resultados reales; nunca marques una prueba como superada sin ejecutarla.

## Relacionados

- [Política de retención de datos](../08-data/retention-policy.md)
- [Arquitectura de datos](../08-data/data-architecture.md)
- [Gestión de secretos](../13-security/secret-management.md)
- [Estrategia de reversión](rollback-strategy.md)
