# Pirámide de pruebas

## Propósito

Definir el equilibrio deseado entre tipos de prueba para que la suite sea rápida, fiable y enfocada. Muchas pruebas pequeñas y rápidas en la base; pocas pruebas lentas y amplias en la cima.

Estado: borrador. {{pending: acordar la distribución objetivo para este proyecto}}

## Forma

```
          /\        end-to-end: pocas, solo recorridos críticos
         /  \
        /----\      contrato / integración: fronteras entre componentes
       /      \
      /--------\    unitarias: muchas, rápidas, aisladas
```

## Capas

| Capa | Qué demuestra | Velocidad | Proporción objetivo |
|------|---------------|-----------|---------------------|
| Unitaria | Una unidad se comporta según la especificación, incluidos casos límite | Milisegundos | {{pending: proporción, por ejemplo la mayoría}} |
| Integración | Los componentes funcionan juntos con conexiones reales | Segundos | {{pending: proporción}} |
| Contrato | Productor y consumidor coinciden en una interfaz | Segundos | {{pending: proporción o «no aplica»}} |
| End-to-end | Un recorrido crítico funciona a través de la interfaz real | Segundos a minutos | {{pending: proporción, pequeña}} |

## Pautas

- Lleva cada verificación a la capa más baja que pueda atrapar el defecto.
- Usa pruebas end-to-end para recorridos cuyo fallo bloquearía a los usuarios, no para cada rama.
- Evita el «cono de helado»: muchas pruebas lentas de interfaz y pocas unitarias vuelven la suite frágil y lenta.
- Una prueba inestable es un defecto. Ponla en cuarentena con motivo y responsable registrados, y corrígela; no la borres ni la debilites en silencio.
- La cobertura es una señal, no una meta. {{pending: decidir si existe un mínimo de cobertura y dónde aplica}}

## Recorridos críticos

Lista los recorridos que merecen cobertura end-to-end.

| Recorrido | Funcionalidad | Por qué es crítico |
|-----------|---------------|--------------------|
| {{pending: recorrido}} | [Funcionalidad](../05-features/example/feature-spec.md) | {{pending: motivo}} |

## Relacionados

- [Escalera de verificación](verification-ladder.md)
- [Guía de TDD](tdd-guide.md)
- [Estrategia de aceptación](acceptance-strategy.md)
- [Plan de pruebas](test-plan.md)
