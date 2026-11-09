# Seguridad de aplicaciones con LLM

## Propósito

Fijar las reglas de seguridad para funcionalidades en las que el propio producto llama a un modelo de lenguaje: chat, resumen, clasificación, extracción, agentes con herramientas. La regla central: la salida del modelo es un dato no confiable, nunca una instrucción que el sistema ejecute sin validar.

Estado: borrador. {{pending: decidir si el producto usa modelos de lenguaje y en qué funcionalidades}}

## Cuándo aplica

Cualquier funcionalidad que envíe datos de usuarios o del negocio a un modelo, o que actúe sobre lo que el modelo devuelve. Los agentes de desarrollo que usa el equipo se cubren en el endurecimiento de agentes de IA.

## Riesgos principales

| Riesgo | Ejemplo | Control base |
|--------|---------|--------------|
| Inyección de prompts | Texto del usuario o un documento obtenido anula las instrucciones | Separar instrucciones de datos; nunca otorgar autoridad por la salida del modelo |
| Manejo inseguro de la salida | La salida se renderiza como HTML o se ejecuta como consulta | Validar contra un esquema; codificar antes de renderizar |
| Divulgación de datos sensibles | El prompt incluye secretos o datos de otro usuario | Minimizar el contexto; filtrar por los permisos de quien llama |
| Agencia excesiva | El modelo llama a una herramienta que borra o paga | Herramientas en lista permitida, mínimo privilegio, confirmación humana para acciones irreversibles |
| Consumo ilimitado | Peticiones grandes o repetidas agotan el presupuesto | Límites de tokens, frecuencia y coste por usuario y globales |
| Cadena de suministro | Modelo, plugin o dataset no confiable | Aprobar explícitamente modelos e integraciones |

## Patrones de diseño

1. **Salida estructurada**: pide un esquema definido y rechaza todo lo que no valide.
2. **Solo lectura por defecto**: si el modelo necesita datos, dale acceso estrecho y de solo lectura filtrado por los permisos del usuario.
3. **Control de herramientas**: cada herramienta tiene lista permitida, validación de argumentos y responsable; las destructivas requieren confirmación humana.
4. **Higiene del contexto**: nunca incluyas secretos, credenciales ni datos que el usuario actual no pueda ver.

## Decisiones del proyecto

- Proveedor y alojamiento del modelo: {{pending: elegir; registrar las condiciones de tratamiento de datos}}
- Datos que nunca deben enviarse al modelo: {{pending: listar}}
- Límites de tokens, peticiones y coste: {{pending: definir}}
- Registro de prompts y salidas sin datos personales: {{pending: definir}}

## Lista de comprobación para la spec de una funcionalidad

- [ ] Están definidas las entradas y salidas del modelo.
- [ ] La salida se valida antes de usarse.
- [ ] Los casos de abuso (inyección, extracción de datos) tienen pruebas en el plan.
- [ ] Se especifican límites y alternativas de respaldo.

## Relacionados

- [Endurecimiento de agentes de IA](ai-agent-hardening.md)
- [Modelo de amenazas](threat-model.md)
- [Controles de protección de datos](data-protection-controls.md)
- [Plan de pruebas](../11-quality/test-plan.md)
