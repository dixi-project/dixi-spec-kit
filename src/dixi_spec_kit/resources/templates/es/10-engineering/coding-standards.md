# Estándares de código

## Propósito

Que el código del proyecto se lea igual en todas partes, falle pronto (en el formateador, el
linter o el verificador de tipos, no en producción) y lo pueda revisar cualquier persona o agente
sin aprender convenciones nuevas. Este documento dice **qué** se exige; el comando de verificación
del proyecto dice **cómo** se comprueba.

Stack: {{pending: lenguajes, runtimes y frameworks elegidos para el proyecto, registrados en un ADR}}

## Reglas comunes

1. **Lo que se puede verificar, se verifica.** Formato, lint y tipos corren en `make verify` y en
   la integración continua. Una regla sin herramienta es solo una recomendación.
2. **Tipos estrictos desde el primer commit.** Subir el nivel después cuesta más que empezar en
   estricto. Cada comentario de supresión nuevo se justifica en el pull request.
3. **Versión de runtime fijada** en el repositorio, para que local, CI y producción usen la misma.
4. **Un idioma para los identificadores.** {{pending: idioma de identificadores, mensajes de commit
   y de log; idioma de specs y documentación}}
5. **Nada de textos visibles al usuario en el código.** Viven en catálogos de traducción por idioma.
6. **Ningún secreto, URL de entorno ni identificador de cuenta en el código.** Vienen de la
   configuración, cargada en ejecución desde un almacén de secretos.
7. **Funciones pequeñas y puras donde se pueda.** La lógica de dominio no conoce HTTP, la base de
   datos ni los SDK de proveedores; los recibe por inyección para probarse sin red.
8. **Fechas en UTC** en almacenamiento y contratos; la zona horaria del usuario solo al presentar.
9. **Dinero en enteros de la unidad mínima o en decimal exacto**, nunca en coma flotante binaria.
10. **Errores y seguridad** según [el estándar de código seguro](secure-coding-standard.md).

## Tabla por stack

Llena una tabla por cada lenguaje del proyecto.

| Aspecto | Regla |
|---|---|
| Versión | {{pending: versión de runtime soportada y política de actualización}} |
| Formateador | {{pending: formateador y configuración}} |
| Linter | {{pending: linter, conjunto de reglas y tolerancia a advertencias}} |
| Tipos | {{pending: verificador de tipos y nivel de exigencia}} |
| Dependencias | Manifiesto más archivo de lock versionado |
| Estructura | Dominio separado de la infraestructura; puntos de entrada delgados (controladores, handlers) |
| Pruebas | {{pending: ejecutor de pruebas; librería de pruebas basadas en propiedades, si aplica}} |
| Prohibido | Evaluación dinámica de código, errores silenciados, consultas armadas con cadenas, deserializar datos no confiables con formatos inseguros |

## Lista de revisión

- [ ] Formateador, linter y verificador de tipos en verde sin supresiones nuevas.
- [ ] El comportamiento nuevo tiene una prueba escrita antes, trazada a un ID de feature o contrato.
- [ ] Ningún texto visible, secreto, URL o identificador escrito a mano en el código.
- [ ] Funciones y módulos públicos con nombres que explican la intención; los comentarios explican el *porqué*.
- [ ] Las desviaciones de este estándar están registradas en un ADR.

## Desviaciones

Un proyecto se aparta de estas reglas solo mediante un ADR aceptado que nombre la regla, el motivo
y el control compensatorio. Usa [la plantilla de ADR](templates/adr-template.md).

## Relacionados

- [Estándar de código seguro](secure-coding-standard.md)
- [Plantilla de ADR](templates/adr-template.md)
- [Plan de pruebas](../11-quality/test-plan.md)
- [Instrucciones del proyecto](../AGENTS.md)
