# Notas de versión

## Propósito

Contar a usuarios y equipos internos qué cambió en cada versión, en lenguaje claro y en cada idioma soportado, para que nadie tenga que leer commits para saber qué es nuevo, qué se corrigió o qué se eliminó.

Estado: borrador. {{pending: decidir dónde se publican las notas de versión y quién las aprueba}}

## Públicos

| Público | Qué necesita | Canal |
|---------|--------------|-------|
| Usuarios finales | Qué pueden hacer ahora, qué cambió para ellos | {{pending: dentro del producto, sitio web, correo}} |
| Soporte y ventas | Qué decir a los clientes, problemas conocidos | {{pending: canal interno}} |
| Integradores | Cambios de contrato, obsolescencias, pasos de migración | {{pending: archivo de cambios, portal para desarrolladores}} |

## Reglas de redacción

- Empieza por el beneficio para el usuario, no por el cambio interno.
- Una entrada por cambio visible; agrupa las correcciones triviales.
- Marca con claridad los cambios incompatibles y las obsolescencias, y di qué debe hacer el usuario.
- Escribe el texto fuente una vez y tradúcelo con el proceso normal del catálogo de traducciones; nunca publiques un solo idioma sin indicarlo.
- No menciones números de ticket internos, personas ni proveedores.
- Los números de versión siguen la política de versionado del proyecto.

## Plantilla de entrada

Copia este bloque para cada versión.

```markdown
## <versión> — <AAAA-MM-DD>

### Nuevo
- <qué pueden hacer ahora los usuarios y por qué importa>

### Mejorado
- <cambio en un comportamiento existente>

### Corregido
- <problema que tenían los usuarios, ya resuelto>

### Obsoleto o eliminado
- <qué desaparece, cuándo y qué usar en su lugar>

### Problemas conocidos
- <problema, solución temporal, corrección prevista>
```

## Entrada de ejemplo

```markdown
## 1.4.0 — 2026-01-15

### Nuevo
- Ahora puedes exportar tus reportes como hoja de cálculo.

### Corregido
- Las fechas se muestran en el formato del idioma que elegiste.
```

## Lista de revisión

- Cada entrada corresponde a un cambio integrado y, cuando aplica, a una especificación de funcionalidad.
- Todos los idiomas soportados están presentes y revisados por alguien con dominio del idioma.
- Los cambios incompatibles incluyen pasos de migración.
- {{pending: agregar cualquier aviso legal o contractual que deba aparecer en cada versión}}

## Relacionados

- [Ciclo de vida de funcionalidades](feature-lifecycle.md)
- [Hoja de ruta](roadmap.md)
- [Política de versionado](../00-governance/policies/versioning-policy.md)
- [Guía de contenido](../17-ux/content-guidelines.md)
- [Política de internacionalización](../00-governance/policies/i18n-policy.md)
