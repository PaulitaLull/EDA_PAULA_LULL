# Análisis PISA Valencia: Nivel Socioeconómico y Rendimiento en Lectura

Este proyecto estudia la correlación existente entre el nivel socioeconómico del alumnado y la nota obtenida en la competencia de lectura utilizando datos de las evaluaciones PISA en Valencia[cite: 5].

## Estructura del Directorio y Datos

Los datos procesados se encuentran almacenados en formato CSV dentro de la carpeta del proyecto[cite: 5]:
* `data/pisa_valencia25.csv`
* `data/pisa_valencia22.csv`
* `data/pisa_valencia18.csv`

## Requisitos y Dependencias

Para ejecutar correctamente el análisis en Python, se emplean las siguientes librerías científicas y de manipulación de datos[cite: 5]:
* `pandas`[cite: 5]
* `numpy`[cite: 5]
* `statsmodels`[cite: 5]
* `matplotlib`[cite: 5]
* `seaborn`[cite: 5]

## Metodología y Procedimiento

El flujo del análisis de datos consta de las siguientes etapas principales:

1. **Preparación y Limpieza de Datos**:
    * Se generan de forma automática las 10 columnas correspondientes a los valores plausibles de lectura (`PV1READ` hasta `PV10READ`)[cite: 5].
    * Se seleccionan estrictamente las columnas necesarias para el estudio: el índice de nivel socioeconómico (`ESCS`), el peso muestral (`W_FSTUWT`) y los 10 valores plausibles[cite: 5].
    * Se realiza una limpieza de datos eliminando aquellas filas que contienen valores nulos (se detectaron 92 valores nulos en la columna `ESCS`)[cite: 5].
    * Como resultado, la muestra inicial de 1,712 alumnos se ajusta a un total de 1,620 alumnos válidos para la regresión[cite: 5].

2. **Regresión Ponderada (WLS)**:
    * Se implementa un bucle de regresiones utilizando Mínimos Cuadrados Ponderados (*Weighted Least Squares* - WLS) sobre los 10 valores plausibles[cite: 5].
    * Se emplea WLS en lugar de OLS (regresión lineal ordinaria) con el objetivo de incorporar los pesos muestrales (`W_FSTUWT`), otorgando mayor ponderación matemática a aquellos estudiantes que representan a un estrato o grupo más amplio[cite: 5].
    * Se calculan de forma independiente los interceptos, pendientes y coeficientes de determinación ($R^2$) para cada modelo, obteniendo finalmente el promedio aritmético de los 10 escenarios[cite: 5].

## Resultados Principales (Valencia)

Tras la ejecución del modelo de regresión ponderada, se obtienen las siguientes conclusiones estadísticas[cite: 5]:
* **Ecuación del modelo**: $\text{Lectura} = 430.98 + (26.55 \cdot \text{ESCS})$[cite: 5].
* **Coeficiente de determinación ($R^2$ promedio)**: $0.0867$, lo que indica que el nivel socioeconómico (`ESCS`) explica el $8.67\%$ de la varianza total en la puntuación de lectura[cite: 5].