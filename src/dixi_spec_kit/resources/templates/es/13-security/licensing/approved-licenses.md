# Licencias aprobadas

## Propósito

Mantener la lista de licencias de terceros que el proyecto acepta, las que requieren revisión y las que rechaza. Las listas siguientes son una sugerencia inicial, no asesoría legal; ajústalas a la licencia del proyecto y a su modelo de distribución.

Estado: borrador. {{pending: confirmar las listas con el responsable de la política o con asesoría legal}}

## Permitidas

Licencias permisivas que normalmente solo exigen conservar los avisos.

| Identificador SPDX | Notas |
|--------------------|-------|
| MIT | Conservar aviso de copyright |
| BSD-2-Clause | Conservar aviso de copyright |
| BSD-3-Clause | Conservar aviso; sin uso para respaldo |
| Apache-2.0 | Conservar archivo NOTICE; concesión de patentes |
| ISC | Conservar aviso de copyright |
| {{pending: añadir o quitar}} | |

## Requieren revisión

Licencias cuyas obligaciones dependen de cómo se usa o distribuye el componente.

| Identificador SPDX | Preocupación habitual |
|--------------------|-----------------------|
| LGPL-2.1, LGPL-3.0 | Obligaciones de enlazado y sustitución |
| MPL-2.0 | Copyleft a nivel de archivo |
| EPL-2.0 | Copyleft débil, términos de licencia secundaria |
| CC-BY-4.0 | Adecuada para contenido, inusual para código |
| {{pending: añadir}} | |

## No permitidas sin excepción

| Identificador SPDX | Razón |
|--------------------|-------|
| GPL-2.0, GPL-3.0 | Copyleft fuerte; {{pending: confirmar frente a la licencia del proyecto}} |
| AGPL-3.0 | Copyleft de red; afecta a servicios alojados |
| Licencia desconocida o ausente | No concede derechos |
| Restricciones no comerciales o de campo de uso | {{pending: confirmar}} |

## Cómo cambiar esta lista

1. Propón el cambio con la licencia, el componente que la necesita y la razón.
2. El responsable de la política registra la decisión y la fecha.
3. Actualiza los controles de licencias si están automatizados.

## Relacionados

- [Política de licencias](licensing-policy.md)
- [Escaneo de dependencias](../dependency-scanning.md)
