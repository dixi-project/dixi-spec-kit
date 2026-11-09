# Alta de tenants

## Propósito

Crear un tenant nuevo (organización cliente) en una plataforma multitenant de forma repetible, con aislamiento, configuración y monitoreo desde el primer día, y darlo de baja limpiamente cuando se vaya.

Estado: borrador. {{pending: nombrar al responsable de este playbook}}

## Dos caminos

| Camino | Cuándo | Quién lo ejecuta |
|--------|--------|------------------|
| Autoservicio | Planes estándar, flujo de registro | El producto, automáticamente |
| Asistido | Contratos a medida, migración de datos, recursos dedicados | Operaciones con el responsable de la cuenta |

{{pending: decidir qué planes usan cada camino}}

## Antes de crear el tenant

- Acuerdo firmado o términos aceptados, y el plan registrado.
- Requisito de residencia de datos conocido. {{pending: listar las regiones permitidas}}
- Un contacto con nombre del lado del cliente, usando en ejemplos una dirección como `admin@example.com`.
- Modelo de aislamiento confirmado: compartido, esquema por tenant o dedicado. {{pending: elegir el modelo de aislamiento por defecto}}

## Pasos (camino asistido)

1. Crea el registro del tenant con un ID único e inmutable.
2. Aprovisiona recursos según el modelo de aislamiento, con el script o pipeline revisado, no con clics manuales en una consola.
3. Aplica los límites del plan: usuarios, almacenamiento, límites de tasa, cuotas de uso de IA.
4. Configura la identidad: primer usuario administrador, inicio de sesión único si está contratado.
5. Carga los datos iniciales si se acordó, tras validar formato y consentimiento.
6. Etiqueta cada recurso con el ID del tenant para poder asignar costos.
7. Activa el monitoreo: tableros de tasa de error y uso por tenant.
8. Envía el mensaje de bienvenida con instrucciones de acceso y canales de soporte.

Un agente de IA puede preparar la configuración y revisarla contra esta lista; una persona ejecuta en producción los pasos 2 a 5.

## Criterios de cierre

- El administrador del tenant inició sesión correctamente.
- Aislamiento probado: un usuario de prueba de otro tenant no ve los datos de este.
- El uso y el costo aparecen bajo el ID del tenant.

## Baja

1. Confirma la fecha de fin y la exportación de datos que necesita el cliente.
2. Entrega la exportación y obtén confirmación.
3. Desactiva el acceso y luego borra o anonimiza los datos tras {{pending: periodo de retención}}.
4. Elimina recursos y etiquetas; conserva solo lo que exijan la ley o el contrato.

## Relacionados

- [Catálogo de servicios](../service-catalog.md)
- [Modelo de soporte](../support-model.md)
- [Modelo de asignación de costos](../../22-finops/cost-allocation-model.md)
- [Matriz de SLA](../vendor-management/sla-matrix.md)
