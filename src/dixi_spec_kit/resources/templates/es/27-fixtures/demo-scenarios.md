# Escenarios de demo

## Propósito

Definir historias de demo curadas y repetibles construidas sobre datos sintéticos. Un escenario permite a cualquiera mostrar el producto siempre de la misma forma, sin improvisar datos ni exponer información real.

Estado: borrador. {{pending: elegir los primeros escenarios y quién mantiene el entorno de demo}}

## Por qué escenarios curados

- Las demos son coherentes y se pueden ensayar.
- Los datos cuentan una historia clara en lugar de registros al azar.
- Nunca se muestran datos reales de clientes ni datos personales.
- Los escenarios sirven también como comprobaciones de aceptación end-to-end cuando se automatizan.

## Catálogo de escenarios

| ID | Nombre | Audiencia | Historia | Idiomas | Duración |
|----|--------|-----------|----------|---------|----------|
| DEMO-001 | Primer uso | Usuarios nuevos | Registrarse, completar la configuración, llegar al primer valor | ES, EN | {{pending}} |
| DEMO-002 | Uso diario | Usuarios actuales | Completar la tarea principal de principio a fin | ES, EN | {{pending}} |
| DEMO-003 | Multi-idioma | Audiencia internacional | El mismo recorrido en dos idiomas, con URLs con prefijo de idioma | ES, EN | {{pending}} |
| DEMO-004 | Administración | Administradores | Gestionar usuarios, roles y ajustes | {{pending}} | {{pending}} |
| DEMO-005 | {{pending: escenario}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |

## Plantilla de escenario

Para cada escenario, documenta:

1. Objetivo: qué debe entender la audiencia al final.
2. Estado inicial: conjuntos de datos y registros con nombre cargados.
3. Pasos: acciones numeradas y el resultado esperado de cada una.
4. Puntos a comentar: el valor mostrado en cada paso, sin afirmaciones no verificadas.
5. Reinicio: cómo devolver el entorno al estado inicial.
6. Límites conocidos: qué no mostrar todavía.

## Entorno de demo

- Separado de producción, con su propia configuración y sin datos de producción.
- Se carga con un comando desde los fixtures de demo y se reinicia con otro.
- El acceso está limitado y las credenciales se gestionan como secretos, no se escriben aquí.

{{pending: definir cada cuánto se refresca y revisa el entorno de demo}}

## Añadir un escenario

1. Escribe el escenario con la plantilla anterior.
2. Añade o reutiliza registros del catálogo de datos de muestra.
3. Ensáyalo en cada idioma listado.
4. Opcionalmente, automatízalo como prueba end-to-end.

## Relacionados

- [Estrategia de fixtures](fixtures-strategy.md)
- [Catálogo de datos de muestra](sample-data-catalog.md)
- [Entornos](../14-delivery/environments.md)
- [Estrategia de aceptación](../11-quality/acceptance-strategy.md)
- [Personas](../01-business/actors/personas.md)
