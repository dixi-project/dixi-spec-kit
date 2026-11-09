# Pipeline de build

## Propósito

Describir el pipeline que convierte un commit en un artefacto verificado e inmutable. Corre en cada pull request y en cada merge a la rama principal, y nunca despliega a producción.

## Disparadores

- Pull request abierto o actualizado: comprobaciones completas, el artefacto se descarta.
- Merge a main: comprobaciones completas, el artefacto se conserva y se etiqueta.
- Ejecución manual: {{pending: permitida o no}}.

## Pasos

| # | Paso | Comando o acción | Falla el build cuando |
|---|---|---|---|
| 1 | Checkout | Obtener el commit exacto | No se puede obtener el commit |
| 2 | Instalación | Instalar dependencias fijadas desde el lockfile | Lockfile desactualizado o hash distinto |
| 3 | Verificación (compuerta) | `make verify` | Falla cualquier comprobación |
| 4 | Pruebas unitarias y de contrato | {{pending: comando de pruebas}} | Falla cualquier prueba |
| 5 | Análisis estático | {{pending: linters y chequeo de tipos}} | Hallazgos nuevos por encima de {{pending: umbral}} |
| 6 | Escaneo de dependencias y secretos | {{pending: escáneres}} | Vulnerabilidad conocida por encima de {{pending: severidad}} o secreto encontrado |
| 7 | Build del artefacto | {{pending: comando de build}} | Error de build |
| 8 | Etiquetar y guardar | Etiquetar con el identificador del commit y guardar en {{pending: registro}} | Falla la subida |

El paso 3 es obligatorio: si `make verify` falla, no corre ningún paso posterior.

## Reglas del artefacto

- Se construye una vez; el mismo artefacto va a staging y a producción.
- Contiene su identificador de commit y fecha de build; sin valores específicos de un entorno.
- Firmado o con checksum: {{pending: método}}.
- Se conserva durante {{pending: periodo}} para permitir la reversión.

## Rendimiento

- Duración objetivo: {{pending: minutos}}.
- Cachea dependencias por el hash del lockfile; nunca cachees salidas de build entre commits sin una clave.

## Seguridad

- El build corre con acceso de solo lectura al repositorio y de escritura solo al almacén de artefactos.
- Los pull requests desde forks no reciben secretos.

## Relacionados

- [Pipeline de versión](release-pipeline.md)
- [Pipeline de migraciones](migration-pipeline.md)
- [Visión general de CI/CD](../ci-cd-overview.md)
- [Escaneo de dependencias](../../13-security/dependency-scanning.md)
- [Escalera de verificación](../../11-quality/verification-ladder.md)
