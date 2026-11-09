# Estrategia de fixtures

## Propósito

Definir cómo el proyecto crea y usa datos de muestra para desarrollo, pruebas y demos. Todos los datos de muestra son sintéticos: nunca contienen datos reales ni personales copiados de producción o de personas reales, y se pueden commitear, compartir y mostrar con seguridad.

Estado: borrador. {{pending: decidir dónde viven los fixtures y quién los mantiene}}

## Niveles de fixtures

| Nivel | Se usa para | Tamaño | Determinismo | Vive en |
|-------|-------------|--------|--------------|---------|
| Unitario | Casos de prueba individuales | Mínimo, en línea | Totalmente fijo | Junto a la prueba |
| Integración | Pruebas entre componentes | Conjuntos pequeños | Semilla fija | Carpeta de pruebas de cada repositorio |
| Semilla de desarrollo | Entornos locales | Medio | Semilla fija | {{pending}} |
| Demo | Historias curadas para presentaciones | Pequeño, elegido a mano | Fijo | {{pending}} |
| Carga | Pruebas de rendimiento | Grande, generado | Generador con semilla | Se genera bajo demanda, no se commitea |

## Reglas de datos sintéticos

- Nunca copies datos de producción a los fixtures, ni siquiera volcados anonimizados, salvo que una decisión registrada apruebe una técnica concreta.
- Nombres, organizaciones y direcciones son claramente ficticios.
- Los correos usan dominios reservados para ejemplos, por ejemplo `ana.demo@example.com`.
- Los teléfonos usan rangos reservados para ficción o documentación cuando existan.
- Los datos de pago usan solo valores de prueba destinados a ello; nunca números reales de tarjeta o cuenta.
- Los identificadores tienen formato realista pero son generados.
- Los campos de texto libre contienen texto neutro, sin contenido ofensivo ni engañoso.

## Internacionalización

- Los fixtures incluyen nombres, direcciones, monedas, fechas y textos en todos los idiomas soportados.
- Incluye casos difíciles: acentos, cadenas largas, texto de derecha a izquierda si aplica, distintos formatos de fecha y número.

## Generación

- Los generadores usan una semilla fija para que el mismo comando produzca los mismos datos.
- Los datos generados respetan el modelo de datos canónico y sus restricciones.
- Los fixtures se versionan con el esquema; un cambio de esquema actualiza los fixtures en el mismo cambio.

{{pending: decidir el enfoque de generación y el comando que carga cada nivel}}

## Comprobaciones de seguridad

- Una comprobación revisa los fixtures en busca de dominios de correo de apariencia real, secretos y patrones de datos personales.
- Los datos de demo y de semilla nunca se cargan en producción.

## Relacionados

- [Catálogo de datos de muestra](sample-data-catalog.md)
- [Escenarios de demo](demo-scenarios.md)
- [Clasificación de PII](../08-data/pii-classification.md)
- [Entornos](../14-delivery/environments.md)
- [Pirámide de pruebas](../11-quality/test-pyramid.md)
- [Plan de pruebas](../11-quality/test-plan.md)
