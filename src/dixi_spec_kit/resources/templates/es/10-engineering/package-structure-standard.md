# Estándar de estructura de paquetes

## Propósito

Que cualquier persona o agente encuentre lo mismo en el mismo sitio del repositorio, y que las
dependencias apunten en una sola dirección para que los módulos cambien de forma independiente.

## Organización del repositorio

{{pending: monorepo o varios repositorios, y el motivo, registrado en un ADR}}

Organización sugerida para un monorepo (adapta los nombres al stack elegido):

```text
/                      documentación SDD (00- a 13-) y archivos del proyecto
apps/ o services/      unidades desplegables (web, API, worker)
packages/              código compartido por más de una unidad desplegable
infra/                 infraestructura como código
tests/                 pruebas transversales (extremo a extremo, contrato), si el stack lo pide
Makefile               `make verify` corre todos los controles del repositorio
```

## Reglas

1. **Organizar por módulo de dominio, no por capa técnica.** Cada módulo de `04-modules/`
   corresponde a una carpeta de código con sus partes de dominio, aplicación e infraestructura.
2. **Las dependencias apuntan hacia el dominio.** La infraestructura depende del dominio, nunca al
   revés. El dominio no importa frameworks, bases de datos ni SDK de proveedores.
3. **Los módulos se comunican por interfaces públicas** (punto de entrada del paquete, API o
   evento), nunca importando internos ajenos ni compartiendo tablas.
4. **Los paquetes compartidos son pequeños y estables.** Si solo lo usa un módulo, no es compartido.
5. **Pruebas junto al código o en un árbol espejo**, según la convención del stack.
   {{pending: convención de ubicación de pruebas}}
6. **El código generado** está claramente separado y nunca se edita a mano.
7. **Un solo punto de verificación**: `make verify` en la raíz corre formato, lint, tipos y pruebas
   de todo el repositorio.
8. **La configuración por entorno** viene del runtime, no de archivos versionados por entorno.

## Carpeta de un módulo

```text
<module>/
  domain/          entidades, objetos de valor, errores de dominio, reglas puras
  application/     casos de uso que orquestan el dominio
  infrastructure/  adaptadores: persistencia, clientes HTTP, colas
  interface/       puntos de entrada: rutas, handlers, consumidores
```

Nombres: {{pending: convención de nombres de carpetas y paquetes}}

## Relacionados

- [Estándares de código](coding-standards.md)
- [Plantilla de módulo](templates/module-template.md)
- [Plantilla de dominio](templates/domain-template.md)
- [Módulo de ejemplo](../04-modules/example/module-spec.md)
