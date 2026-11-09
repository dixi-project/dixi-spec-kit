# Marco de experimentación

## Propósito

Definir cómo el proyecto ejecuta experimentos controlados, como pruebas A/B, para que las decisiones de producto se basen en resultados estadísticamente sólidos, éticos y reproducibles, y para que ningún experimento dañe a los usuarios ni distorsione las métricas.

Estado: borrador. {{pending: decidir si el proyecto hará experimentos y quién aprueba cada uno}}

## Cuándo experimentar

Ejecuta un experimento cuando:

- Hay una hipótesis clara y una métrica que puede moverse en un tiempo razonable.
- El tráfico alcanza para llegar al tamaño de muestra necesario.
- El cambio puede mostrarse con seguridad solo a una parte de los usuarios.

No experimentes con seguridad, avisos legales, funciones de accesibilidad ni precios mostrados a grupos protegidos. Esos cambios se publican como decisiones normales.

## Plantilla de hipótesis

```text
Creemos que <cambio>
para <público, incluido el idioma y la región>
provocará <efecto esperado>
medido por <métrica principal>.
Sabremos que funcionó si <métrica> cambia al menos <efecto mínimo detectable>
en <duración>, sin empeorar <métricas de protección>.
```

## Registro de experimentos

| ID | Hipótesis | Métrica principal | Protección | Idiomas | Muestra | Inicio | Fin | Resultado | Decisión |
|----|-----------|-------------------|------------|---------|---------|--------|-----|-----------|----------|
| EXP-001 | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | — | — | — | — |

## Reglas de diseño

- Registra antes de empezar la hipótesis, las métricas, el tamaño de muestra y la duración; no los cambies a mitad del experimento.
- Asigna usuarios de forma aleatoria y consistente; un usuario ve la misma variante en todas sus sesiones.
- Ejecuta ciclos semanales completos para evitar sesgos por día de la semana.
- Analiza los idiomas por separado cuando el comportamiento pueda variar por idioma o mercado.
- Cada variante cumple el mismo estándar de accesibilidad y traducción que producción.
- Define una condición de paro por daño, por ejemplo una métrica de protección que empeora más allá de un umbral.

{{pending: fijar el nivel de significancia, la potencia estadística y el efecto mínimo detectable}}

## Ética y privacidad

- Los experimentos usan solo eventos listados en el catálogo de analítica.
- No se engaña a los usuarios sobre precios, condiciones o uso de datos.
- {{pending: decidir si se informa a los usuarios sobre los experimentos y cómo pueden excluirse}}

## Cierre de un experimento

1. Detente en el fin planeado o en una condición de paro, no cuando los resultados se vean bien.
2. Registra el resultado, incluidos los no concluyentes y los negativos.
3. Decide: publicar, iterar o descartar; elimina el código y las banderas de la variante perdedora.
4. Enlaza el resultado desde la especificación de la funcionalidad relacionada.

## Relacionados

- [Catálogo de eventos de analítica](analytics-events-catalog.md)
- [Ciclo de vida de funcionalidades](feature-lifecycle.md)
- [Marco de priorización](prioritization-framework.md)
- [Estándar de accesibilidad](../17-ux/accessibility-standard.md)
- [Clasificación de datos personales](../08-data/pii-classification.md)
