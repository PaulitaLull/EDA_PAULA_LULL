# ¿Por qué cae la lectura en la Comunidad Valenciana? Análisis exploratorio de PISA 2018-2025

Proyecto individual del módulo **Data Analysis** de The Bridge Bootcamp. 

Autora: **Paula Lull Rios**.

## De qué trata

En PISA 2025, la puntuación media en lectura del alumnado de 15 años de la Comunidad Valenciana cae **58 puntos** respecto a 2022, más del doble que la media española. El proyecto mide esa caída con rigor estadístico y explora, con los microdatos de la OCDE, **si algún factor observable la acompaña**: nivel socioeconómico, titularidad del centro, origen migratorio, idioma de la prueba y uso de pantallas.

## Resultados principales

| | 2018 | 2022 | 2025 |
|---|---|---|---|
| Lectura media (10 valores plausibles) | 472,7 | 481,8 | 423,5 |
| Error típico | 4,5 | 4,0 | 5,8 |
| Alumnos / centros en la muestra | 1.753 / 53 | 1.625 / 53 | 1.712 / 54 |

- **Caída 2022 → 2025: −58,2 puntos** (de −72,2 a −44,3 con un IC del 95% incluyendo el error de enlace). Entre 2018 y 2022 no hay un cambio tan notable (+9).
- **Nivel socioeconómico (ESCS):** +26,55 puntos de lectura por punto de ESCS en 2025, y solo explica el 8,7% de la varianza. 
- **Titularidad:** los centros privados puntúan unos 20 puntos más en 2025 (427 frente a 448 de media en la muestra), con un ESCS medio más alto.
- **Origen migratorio:** el alumnado de origen inmigrante pasa del 14,0% en 2018 al 27,6% en 2025, pero **todos los grupos caen** (nativos −49, segunda generación −59, primera −61 puntos). El cambio de composición puede explicar solo una pequeña parte de la caida.
- **Idioma de la prueba:** el alumnado evaluado en valenciano es del 22% en 2018, 4% en 2022 y 20% en 2025. Este último año se parece al del 2018, así que explica poco la caida.
- **Pantallas:** las horas de uso digital en el centro parecen pasar de 1,33 a 1,41 al día entre 2022 y 2025, sin cambios relevantes, y la lectura cae en todos los tramos de uso. De la misma manera, el tiempo invertido en pantallas e IA por los alumnos fuera del aula no refleja una posible causa.

**Conclusión:** ninguno de los factores explorados explica por sí solo la caída, que aparece en todos los grupos, incluido el alumnado nativo. Quedan abiertos nuevos frentes de exploración como las metodologías docentes, las políticas educativas propias de los centros valencianos, un estudio más detallado de el uso de pantallas e IA y las respectivas comparaciones con el resto de comunidades autónomas de España. 

## Estructura del repositorio

```
.
├── README.md
├── presentacion_PISA_Valencia.pptx       # presentación de 10 minutos
└── src/
    ├── mainpisa.ipynb                    # introducción, fuentes de datos, carga y limpieza
    ├── estudio_PVREAD.ipynb              # distribuciones, medidas estadísticas, errores y la caída
    ├── estudio_escs.ipynb                # nivel socioeconómico (ESCS) y lectura
    ├── estudio_portitularidad.ipynb      # centros públicos frente a privados
    ├── estudio_immingracion.ipynb        # origen migratorio por año
    ├── estudio_idioma.ipynb              # idioma en casa e idioma de la prueba
    ├── estudio_pantallas.ipynb           # horas de pantalla en y fuera del centro, uso de IA
    ├── funcionalidades.py                # funciones auxiliares 
    ├── data/                             # CSV filtrados de Valencia
    └── imgs/                             # gráficos generados por los notebooks
```

## Datos

- **Fuente:** microdatos del cuestionario de alumnado de PISA 2018, 2022 y 2025 ([OCDE](https://www.oecd.org/en/data/datasets.html)), junto con los codebooks correspondientes. Los ficheros originales son: `CY07_MSU_STU_QQQ.sav`, `CY08MSP_STU_QQQ.SAV` y `CY09_MS_STU_PUF.sav`, los cuales **no se incluyen** por su tamaño, sino que se cargan directamente filtrados a los datos de la Comunidad Valenciana y a las variables a estudiar.
- **Filtrado:** `mainpisa.ipynb` selecciona solo las columnas necesarias y los estratos de la Comunidad Valenciana (pública y privada), y los guarda como `pisa_valencia18.csv`, `pisa_valencia22.csv` y `pisa_valencia25.csv`. Los códigos de estrato se verifican con las etiquetas del propio fichero (2018: `ESP9038`, `ESP1738`, `ESP9039`, `ESP1739`; 2022: `ESP34`, `ESP35`; 2025: `ESP33`, `ESP34`).


## Metodología

PISA no evalúa a todo el alumnado, sino a una muestra de centros y, dentro de ellos, de estudiantes ([Tratamiento de los datos](https://www.yuliakuzmina.com/post/pisa-s-plausible-values-and-how-to-work-with-them#:~:text=PISA%27s%20documentation%20strongly%20warns%20that%20averaging%20PVs,reflects%20the%20uncertainty%20inherent%20in%20the%20PVs.)). Por eso:

- Todas las cifras usan el **peso final del alumno** (`W_FSTUWT`), haciendo que los resultados de la muestra poblacional describan a toda ella y no solo a los alumnos evaluados.
- La lectura se estima con los **10 valores plausibles** (las múltiples estimaciones desde `PV1READ` a `PV10READ` sobre el rendimiento de cada estudiante), calculando el resultado con cada uno de ellos y promediándolos al final. Esta medida se toma dado que los estudiantes no realizan una prueba entera, sino una muestra de la misma.
- El error típico combina la **varianza muestral** (método de replicación repetida balanceada con el ajuste de Fay de los 80 pesos replicados) y la **varianza de imputación** (reglas de Rubin).
- Al comparar ciclos se añade el **error de enlace** de la OCDE (2022-2025: 1,094; 2018-2025: 1,83; 2018-2022: unos 1,47, deducido de los otros dos).

## Cómo reproducirlo

Requiere Python 3.12 con `pandas`, `numpy`, `statsmodels`, `matplotlib`, `seaborn`, `pyreadstat` y Jupyter.

1. No ejecutar la parte de carga de datos de los archivos .sav dentro de `mainpisa.ipynb`, ya que no están subidos.  
2. Ejecuta simplemente las celdas iniciales de cada apartado del estudio para leer directamente los tres CSV filtrados que ya existen en `src/data/`.
3. Ejecuta los notebooks `estudio_*.ipynb` en cualquier orden. Todos importan `funcionalidades.py` y leen los CSV de `src/data/`.

## Limitaciones

- Análisis descriptivo y exploratorio: los resultados no permiten conclusiones causales.
- Varias comparaciones (idioma, origen migratorio, pantallas, titularidad) se presentan sin margen de error.
- Las preguntas sobre pantallas y metodologías cambian de formulación entre ediciones, y la pregunta sobre IA solo existe en 2025, por lo que no se pueden comparar con años anteriores.

## Presentación

La presentación de 10 minutos se encuentra en este mismo repositorio.