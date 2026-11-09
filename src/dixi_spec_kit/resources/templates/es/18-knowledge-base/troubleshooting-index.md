# Índice de resolución de problemas

## Propósito

Llevar de un síntoma a su causa más probable y al documento o runbook que lo resuelve, para que los problemas comunes se arreglen en minutos y no se repita la misma investigación.

Estado: borrador. {{pending: rellenar con los problemas que realmente aparezcan en este proyecto}}

## Cómo se usa

- Busca el síntoma tal como lo viste (texto del error, verificación que falla).
- Sigue el enlace; si la solución falta o es incorrecta, actualiza la entrada.
- Añade una entrada tras cualquier problema que haya llevado más de {{pending: tiempo}} resolver.

## Entorno local y agentes

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| `dixi check` reporta un enlace roto | Se movió o renombró un archivo | Actualiza el enlace relativo y `.dixi/traceability.json` |
| `dixi check` reporta un ID desconocido | Elemento no registrado | Añádelo con sus padres en `.dixi/traceability.json` |
| Un agente se niega a leer un archivo | El archivo parece un secreto | Es lo esperado; ofrece un ejemplo sin secretos |
| `make verify` pasa pero la aplicación falla | Pruebas reales sin conectar | Conecta la suite de pruebas a `make verify` |

## Verificaciones del pull request

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| Una prueba cambió tras commitearse | Se editó una prueba congelada | Revierte; sigue la [política de pruebas](../00-governance/policies/testing-policy.md) |
| Falta una clave de traducción | Texto añadido en el código | Muévelo a los catálogos de idioma |
| {{pending: síntoma}} | {{pending: causa}} | {{pending: solución}} |

## Entrega y ejecución

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| Funciona en staging y falla en producción | Deriva de configuración | Compara con la [estrategia de entornos](../00-governance/environment-strategy.md) |
| Alerta sin runbook | Alerta añadida sin responsable | Escribe un runbook a partir de la [plantilla](../10-engineering/templates/runbook-template.md) |
| {{pending: síntoma}} | {{pending: causa}} | {{pending: solución}} |

## Seguridad

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| Secreto encontrado en el historial | Commiteado por error | Primero rota, después limpia; ver [gestión de secretos](../13-security/secret-management.md) |

## Relacionados

- [Preguntas frecuentes](faq.md)
- [Política de incidentes](../00-governance/policies/incident-policy.md)
- [Estándar de observabilidad](../00-governance/observability-standard.md)
