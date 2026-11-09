# Clasificación de datos personales (PII)

## Propósito

Definir cómo el proyecto clasifica los datos personales y sensibles, para que cada campo, tabla, archivo y evento tenga un nivel de sensibilidad conocido y un conjunto de reglas de tratamiento asociado. Specs, contratos y pruebas se refieren a estos niveles en lugar de repetir reglas.

- Responsable: {{pending: persona o rol responsable de la clasificación de datos}}
- Leyes y obligaciones aplicables: {{pending: leyes de privacidad y obligaciones contractuales que aplican en cada mercado objetivo}}

## Niveles de clasificación

| Nivel | Significado | Ejemplos | Resumen de tratamiento |
| --- | --- | --- | --- |
| Público | Puede publicarse | Nombre del producto, precios publicados | Sin restricciones |
| Interno | No secreto, no para publicar | Identificadores internos, feature flags | Solo acceso autenticado |
| Personal (PII) | Identifica o se refiere a una persona | Nombre, correo, teléfono, dirección IP | Mínimo privilegio, enmascarado en logs |
| Sensible | Causa daño si se expone | Documentos de identidad, salud, finanzas, ubicación precisa | Cifrado a nivel de campo, acceso auditado |
| Secreto | Credenciales y llaves | Contraseñas, tokens, llaves de firma | Nunca en texto plano, nunca en logs |

Ajusta los niveles al proyecto: {{pending: confirmar o renombrar los niveles de clasificación}}

## Inventario de datos

Registra cada elemento que contenga datos de nivel Personal o superior.

| Elemento | Ubicación (tabla, archivo, evento) | Nivel | Finalidad del tratamiento | Base legal | Regla de retención |
| --- | --- | --- | --- | --- | --- |
| `user.email` | {{pending: ubicación}} | Personal | Inicio de sesión y avisos | {{pending: base}} | Ver [política de retención](retention-policy.md) |
| | | | | | |

## Reglas de tratamiento por nivel

- [ ] Los datos Personales o superiores nunca se escriben en claro en los logs; se enmascaran o se aplica hash.
- [ ] Los datos Sensibles se cifran en reposo a nivel de campo o columna, no solo a nivel de disco.
- [ ] El acceso a datos Sensibles se restringe por rol y cada lectura es auditable.
- [ ] Fixtures y seeds de prueba usan datos sintéticos; nunca se copian datos de producción a entornos inferiores sin anonimizar.
- [ ] Exportaciones, informes y conjuntos analíticos declaran el nivel más alto que contienen.
- [ ] Los datos compartidos con terceros se listan con su nivel y el acuerdo que los cubre.
- [ ] Los secretos viven en un almacén de secretos, no en el repositorio ni en archivos de configuración.

## Solicitudes de titulares

| Solicitud | Soportada | Proceso y plazo de respuesta |
| --- | --- | --- |
| Acceso / exportación | {{pending: sí o no}} | |
| Rectificación | | |
| Supresión | | |
| Oposición / limitación | | |

## Cómo usar este documento

1. Cuando una feature introduce un campo nuevo, clasifícalo aquí antes de implementar.
2. Los contratos marcan los campos de nivel Personal o superior (ver el [ejemplo de contrato](../07-contracts/example.md)).
3. `dixi check` y `/dixi.data` (Claude Code) o `$dixi-data` (Codex) ayudan a revisar que los datos nuevos estén clasificados.
4. El [plan de pruebas](../11-quality/test-plan.md) incluye casos de enmascarado y control de acceso.

## Relacionados

- [Política de retención](retention-policy.md)
- [Proyecto](../00-master-spec.md)
- [Plan de pruebas](../11-quality/test-plan.md)
- [Ejemplo de contrato](../07-contracts/example.md)
