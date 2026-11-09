# Escaneo de dependencias

## Propósito

Describir cómo el proyecto detecta vulnerabilidades conocidas, licencias riesgosas y paquetes sospechosos en sus dependencias de terceros, y qué ocurre cuando aparece un hallazgo.

Estado: borrador. {{pending: nombrar al responsable de la higiene de dependencias}}

## Alcance

- Ecosistemas de paquetes en uso: {{pending: listar gestores de paquetes y lockfiles}}
- Imágenes de contenedor o imágenes base, si las hay: {{pending: listar}}
- Dependencias de herramientas de build y CI: {{pending: listar}}

## Reglas base

- Versiona los lockfiles e instala desde ellos para que los builds sean reproducibles.
- Fija versiones; prefiere fijar por hash donde el ecosistema lo permita.
- Añade una dependencia nueva solo con una razón explícita; prefiere la biblioteca estándar o una dependencia existente.
- Comprueba que el nombre del paquete es el correcto antes de instalarlo (typosquatting, nombres parecidos).
- Los agentes de IA proponen dependencias; una persona las aprueba.

## Cuándo se ejecutan los escaneos

| Momento | Qué se escanea | ¿Bloquea el merge? |
|---------|----------------|--------------------|
| Pull request | Dependencias modificadas | {{pending: sí / no, y desde qué severidad}} |
| Programado | Árbol completo de dependencias | No, abre un hallazgo |
| Antes de una versión | Árbol completo e imágenes | {{pending: decidir}} |

Herramienta o servicio de escaneo: {{pending: elegir uno o varios escáneres; este kit no exige ninguno}}

## Gestión de hallazgos

1. Confirma que la ruta de código vulnerable es alcanzable, o asume que lo es si hay dudas.
2. Actualiza, reemplaza o elimina la dependencia.
3. Si no hay corrección, registra una excepción temporal con responsable, justificación y fecha de caducidad.
4. Añade o actualiza una prueba cuando la corrección cambie el comportamiento.

## Excepciones

| Paquete | Hallazgo | Razón | Responsable | Caduca |
|---------|----------|-------|-------------|--------|
| {{pending: paquete}} | {{pending: identificador}} | {{pending: razón}} | {{pending: responsable}} | {{pending: fecha}} |

## Relacionados

- [Política de licencias](licensing/licensing-policy.md)
- [Modelo de amenazas](threat-model.md)
- [Respuesta a incidentes](incident-response.md)
- [Plan de pruebas](../11-quality/test-plan.md)
