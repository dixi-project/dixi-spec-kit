# Escalera de verificación

## Propósito

Ordenar cada verificación automática de la más barata a la más cara, para que las máquinas atrapen lo que puedan antes de que una persona dedique atención a un cambio. Cada peldaño atrapa una clase distinta de defecto; ninguno sustituye al siguiente.

Estado: borrador. {{pending: asociar cada peldaño a un comando real del stack elegido}}

## La escalera

```
barato / rápido                                                   caro / lento
1 formato/lint -> 2 tipos -> 3 unitarias -> 4 integración -> 5 contrato -> 6 e2e -> persona
```

| Peldaño | Atrapa | No atrapa | Comando |
|---------|--------|-----------|---------|
| 1. Formato y lint | Diffs ruidosos, imports sin uso, código muerto, patrones riesgosos | Lógica de negocio incorrecta | {{pending: comando}} |
| 2. Tipos | Tipos que no coinciden, nulos sin manejar, firmas inventadas | Valor incorrecto del tipo correcto | {{pending: comando}} |
| 3. Pruebas unitarias | Lógica incorrecta dentro de una unidad, casos límite | Conexión entre componentes | {{pending: comando}} |
| 4. Pruebas de integración | Conexiones rotas, persistencia, configuración | Desvíos respecto a consumidores externos | {{pending: comando}} |
| 5. Pruebas de contrato | Desvíos de interfaz entre productor y consumidor | Recorridos completos de usuario | {{pending: comando}} |
| 6. Pruebas end-to-end | Recorridos críticos de usuario rotos | Casos límite raros (demasiado lentas para cubrirlos) | {{pending: comando}} |

## `make verify`

El proyecto define `make verify` como punto de entrada único de la verificación local. La base solo ejecuta `dixi check`, que comprueba la estructura de los documentos, no el comportamiento de la aplicación.

- Añade cada peldaño a `make verify` en cuanto el stack lo ofrezca.
- Mantén la ejecución local lo bastante rápida para correrla en cada cambio. {{pending: presupuesto de tiempo local, por ejemplo unos minutos}}
- Los peldaños más lentos (e2e completo, análisis de seguridad profundos) pueden correr en integración continua. {{pending: qué peldaños corren solo en CI}}

## Reglas

- Ejecuta los peldaños en orden y detente en el primer fallo.
- Informa el resultado real de cada peldaño: pasó, falló o no se ejecutó. Nunca informes como aprobado un peldaño que no corrió.
- Un fallo se corrige en el código o en la especificación, nunca relajando una regla, saltando una prueba o bajando un umbral.
- Con Claude Code, `/dixi.quality` puede guiar esta revisión; con Codex, `$dixi-quality`.

## Dónde corre cada peldaño

| Momento | Peldaños | Disparador |
|---------|----------|------------|
| Local | {{pending: peldaños}} | Desarrollador o agente antes de pedir revisión |
| Pull request | {{pending: peldaños}} | Integración continua |
| Programado | {{pending: peldaños}} | {{pending: calendario}} |

## Relacionados

- [Estrategia de calidad](quality-strategy.md)
- [Pirámide de pruebas](test-pyramid.md)
- [Guía de TDD](tdd-guide.md)
- [Plan de pruebas](test-plan.md)
- [Guía](../docs/guide.md)
