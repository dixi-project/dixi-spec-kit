# Política de licencias

## Propósito

Declarar la licencia con la que se distribuye el proyecto y las reglas para aceptar código de terceros, de modo que cada dependencia, fragmento o artefacto generado sea compatible con esa elección.

Estado: borrador. {{pending: nombrar a la persona que aprueba las decisiones de licencias}}

## Licencia del proyecto

- Licencia de este proyecto: {{pending: elegir la licencia de salida}}
- Dónde se declara: archivo `LICENSE` y metadatos del paquete.
- Las contribuciones se aceptan bajo: {{pending: la misma licencia, un acuerdo de contribución u otra}}

## Reglas para código de terceros

1. Toda dependencia debe tener una licencia conocida; «sin licencia» significa «todos los derechos reservados».
2. Las licencias de la lista aprobada pueden usarse sin más revisión.
3. Las marcadas como «revisión» necesitan una decisión registrada antes de usarse.
4. Las marcadas como «no permitidas» se rechazan salvo excepción registrada por el responsable de la política.
5. Los fragmentos copiados (de documentación, foros o salidas de IA) siguen las mismas reglas que las dependencias.
6. Conserva los avisos y atribuciones exigidos en el producto distribuido.

## Modelo de distribución

La forma de entregar el proyecto cambia qué obligaciones aplican. {{pending: describirla, p. ej. servicio alojado, binario distribuido, biblioteca, app móvil}}

## Código generado por IA

- Trata el código generado como entrada no confiable a efectos de licencias: revisa fragmentos largos o distintivos.
- No pegues código propietario de otros proyectos en los prompts.
- {{pending: decidir si debe registrarse la procedencia del código generado}}

## Controles

- La detección de licencias se ejecuta junto con el escaneo de dependencias.
- Las dependencias nuevas con licencia desconocida o no aprobada bloquean el merge hasta revisarse.

## Excepciones

| Componente | Licencia | Razón | Aprobado por | Fecha de revisión |
|------------|----------|-------|--------------|-------------------|
| {{pending: componente}} | {{pending: licencia}} | {{pending: razón}} | {{pending: persona}} | {{pending: fecha}} |

## Relacionados

- [Licencias aprobadas](approved-licenses.md)
- [Escaneo de dependencias](../dependency-scanning.md)
- [Proyecto](../../00-master-spec.md)
