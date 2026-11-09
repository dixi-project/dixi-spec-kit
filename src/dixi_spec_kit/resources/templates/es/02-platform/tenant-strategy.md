# Estrategia de tenencia

## Propósito

Decidir cómo separa la plataforma a sus clientes (inquilinos o tenants) entre sí: datos,
configuración, capacidad y facturación. La tenencia es cara de cambiar más adelante, así que toma la
decisión de forma explícita y temprana, documenta los compromisos y aplica el mismo modelo en todos
los productos.

## Definiciones

- Inquilino: {{pending: qué representa, p. ej. una organización, un espacio de trabajo o un hogar}}
- Identificador de inquilino: {{pending: formato y dónde se asigna}}
- Usuarios por inquilino: {{pending: uno o varios; ¿puede un usuario pertenecer a varios inquilinos?}}

## Modelos de aislamiento

| Modelo | Descripción | Fortalezas | Costes |
|---|---|---|---|
| Todo compartido | Un almacén, filas marcadas con el ID de inquilino | Lo más barato y simple de operar | Filtrado estricto en todas partes, vecinos ruidosos |
| Esquema o partición separados | Ejecución compartida, área de datos aislada | Aislamiento más claro, exportación más fácil | Más migraciones que gestionar |
| Pila dedicada | Despliegue separado por inquilino | El aislamiento más fuerte | Mayor coste y esfuerzo operativo |

- Modelo elegido: {{pending: modelo y enlace al ADR}}
- Excepciones: {{pending: inquilinos o tipos de datos que necesitan un modelo más fuerte}}

## Reglas que sigue cada producto

- Todo registro que pertenece a un inquilino guarda su ID.
- Toda consulta y todo mensaje se acota por inquilino; las pruebas incluyen intentos de acceso cruzado.
- Cachés, archivos e índices de búsqueda también se particionan por inquilino.
- Registros y métricas incluyen el ID de inquilino sin exponer sus datos.
- Las tareas en segundo plano procesan un inquilino cada vez o llevan su contexto de forma explícita.

## Ciclo de vida del inquilino

| Etapa | Qué ocurre | Responsable |
|---|---|---|
| Alta | {{pending: pasos de aprovisionamiento}} | {{pending: rol}} |
| Configuración | {{pending: qué puede personalizar el inquilino}} | {{pending: rol}} |
| Suspensión | {{pending: qué se bloquea y qué se conserva}} | {{pending: rol}} |
| Baja | {{pending: exportación, conservación y borrado}} | {{pending: rol}} |

## Equidad y límites

- Cuotas por inquilino: {{pending: peticiones, almacenamiento, usuarios}}
- Comportamiento al superar una cuota: {{pending: limitar, bloquear o facturar}}

## Relacionados

- [Arquitectura multiinquilino](../09-architecture/multi-tenant-architecture.md)
- [Estrategia de identidad y acceso](identity-and-access-strategy.md)
- [Visión general de la plataforma](platform-overview.md)
