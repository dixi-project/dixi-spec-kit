# Presupuestos de web vitals

## Propósito

Fijar presupuestos de rendimiento centrados en el usuario para las páginas web, de modo que las regresiones de carga, interactividad y estabilidad visual se detecten antes de que los usuarios las noten.

Estado: borrador. {{pending: decidir los presupuestos y cómo se miden}}

## Métricas

| Métrica | Qué mide | Presupuesto | Medido en |
|---------|----------|-------------|-----------|
| Largest contentful paint | Tiempo hasta que el contenido principal es visible | {{pending: presupuesto}} | {{pending: percentil, por ejemplo el 75}} |
| Interaction to next paint | Respuesta a la interacción del usuario | {{pending: presupuesto}} | {{pending: percentil}} |
| Cumulative layout shift | Estabilidad visual durante la carga | {{pending: presupuesto}} | {{pending: percentil}} |
| Time to first byte | Tiempo de respuesta del servidor | {{pending: presupuesto}} | {{pending: percentil}} |
| Peso de página | Tamaño total transferido de una página | {{pending: presupuesto}} | Por tipo de página |

Solo como ejemplo, no como recomendación: algunos equipos parten de umbrales «buenos» ampliamente publicados y los ajustan con el tiempo.

## Páginas en alcance

| Tipo de página | URL de ejemplo | Notas |
|----------------|----------------|-------|
| {{pending: tipo de página}} | {{pending: URL con prefijo de idioma}} | {{pending: notas}} |

Mide cada versión de idioma soportada, porque el contenido traducido puede cambiar tamaño y diseño.

## Medición

- **Laboratorio:** ejecuciones controladas en desarrollo o CI para detectar regresiones pronto. {{pending: cuándo corren las mediciones de laboratorio}}
- **Campo:** datos de usuarios reales, si se recogen, para confirmar la experiencia. {{pending: si se recogen datos de campo, respetando la privacidad}}
- Registra dispositivo y condiciones de red para que los resultados sean comparables.

## Cuando se excede un presupuesto

Trátalo como una verificación fallida: encuentra la causa y corrígela. Un presupuesto nunca se sube para que un cambio pase sin una decisión registrada de la persona responsable.

## Relacionados

- [Requisitos no funcionales](../non-functional-requirements.md)
- [Estrategia de calidad](../quality-strategy.md)
- [Escalera de verificación](../verification-ladder.md)
- [Proyecto](../../00-master-spec.md)
