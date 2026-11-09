# Catálogo de estados de interfaz

## Propósito

Listar los estados que cada pantalla y componente debe manejar además del camino feliz (vacío, cargando, error, parcial, sin conexión y otros), para que las especificaciones los describan, los diseños los incluyan y las pruebas los cubran en cada idioma soportado.

Estado: borrador. {{pending: confirmar qué estados son obligatorios en toda pantalla y cuáles solo cuando aplican}}

## Estados estándar

| Estado | Cuándo ocurre | Qué ve el usuario | Nota de accesibilidad |
|--------|---------------|-------------------|-----------------------|
| Vacío (primer uso) | Aún no hay datos | Explicación y la primera acción que puede tomar | El mensaje es texto real, no solo una ilustración |
| Vacío (sin resultados) | Un filtro o búsqueda no devuelve nada | Qué se buscó y cómo ampliar la búsqueda | Se anuncia el número de resultados |
| Cargando | Se están obteniendo datos | Esqueleto o indicador de progreso tras un breve retraso | Se anuncia el estado ocupado; no se pierde el foco |
| Parcial | Algunos datos cargaron y otros no | Los datos disponibles y un aviso sobre lo que falta | Aviso alcanzable con teclado |
| Error (recuperable) | Falló la petición, se puede reintentar | Qué pasó y una acción para reintentar | Se anuncia el error; el foco pasa al mensaje si bloquea la tarea |
| Error (fatal) | No se puede continuar | Disculpa, siguiente paso, forma de regresar | El título de la página refleja el error |
| Sin conexión | No hay red | Aviso y qué sigue funcionando | Se anuncia una vez, no en cada cambio |
| Éxito | La acción terminó | Confirmación breve | Mensaje de estado, no un modal salvo que sea necesario |
| Permiso denegado | El usuario no tiene acceso | Por qué y cómo pedir acceso | — |
| Validación | La entrada no es válida | Mensaje junto al campo y un resumen | Campo vinculado a su mensaje |

## Matriz por pantalla

Llena una fila por cada pantalla del mapa de navegación.

| ID de pantalla | Vacío | Cargando | Parcial | Error | Sin conexión | Éxito | Permiso | Especificación |
|----------------|-------|----------|---------|-------|--------------|-------|---------|----------------|
| {{pending: SCR-001}} | {{pending: sí, no aplica}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |

## Reglas

- El texto de cada estado sale del catálogo de traducciones y se revisa en cada idioma.
- Los indicadores de carga aparecen solo después de un breve retraso para evitar parpadeos. {{pending: fijar el retraso}}
- Los errores nunca muestran trazas de pila, códigos internos sin explicación ni mensajes crudos del servidor.
- Cada estado tiene al menos una prueba: de unidad o componente para el renderizado, de extremo a extremo para los flujos clave.
- Las acciones largas muestran progreso y pueden cancelarse cuando sea posible.

## Definir un estado nuevo

1. Busca en este catálogo un estado existente que encaje.
2. Describe el disparador, el contenido y el comportamiento de accesibilidad.
3. Agrégalo aquí y en las especificaciones afectadas antes de diseñarlo.

## Relacionados

- [Tokens de diseño](design-tokens.md)
- [Mapa de navegación](navigation-map.md)
- [Guía de contenido](content-guidelines.md)
- [Estándar de accesibilidad](accessibility-standard.md)
- [Pirámide de pruebas](../11-quality/test-pyramid.md)
