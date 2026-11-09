# Plantilla de producto

## Propósito

Describir un producto de la plataforma: su visión, usuarios, features centrales, los módulos que
usa y cómo se mide el éxito. Una plataforma puede alojar varios productos que comparten módulos.
Copia la estructura de abajo para cada producto.

## Plantilla

```markdown
# Producto: <nombre del producto>

ID: {{pending: ID del producto}}
Estado: idea | descubrimiento | en construcción | en producción | retirado
Responsable: {{pending: product owner}}
Objetivo de negocio: GOAL-NNN

## Visión

Un párrafo: para quién, qué problema, por qué ahora y en qué se distingue de las alternativas.

## Usuarios

| Persona | Necesidad | Recorrido principal |
|---|---|---|

## Features centrales

| Feature | Prioridad (debe / debería / podría) | ID |
|---|---|---|

## Módulos que usa

| Módulo | ¿Compartido con otros productos? | Notas |
|---|---|---|

## Dependencias externas

| Sistema | Propósito | Spec de integración |
|---|---|---|

## Requisitos no funcionales

- Disponibilidad: {{pending: objetivo}}
- Rendimiento: {{pending: objetivo}}
- Idiomas y mercados: {{pending: idiomas y regiones soportados}}
- Privacidad y cumplimiento: datos personales tratados, obligaciones aplicables.

## Métricas de éxito

| Métrica | Línea base | Objetivo | Cómo se mide |
|---|---|---|---|

## Hoja de ruta

| Etapa | Alcance | Criterio de salida |
|---|---|---|
```

## Relacionados

- [Objetivo de negocio](../../01-business/vision.md)
- [Plantilla de módulo](module-template.md)
- [Plantilla de integración externa](external-integration-template.md)
- [Plantilla de feature](feature-template.md)
