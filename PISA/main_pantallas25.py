import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

archivo_valencia = 'data/pisa_valencia.csv'
df_valencia=pd.read_csv(archivo_valencia)

# print(df_valencia.groupby("CNTSCHID")["ST326Q01JA"].nunique())
# print(df_valencia["ST326Q01JA"].value_counts(dropna=False).sort_index())

# 1) Quitamos los alumnos sin respuesta en la pregunta de horas
datos = df_valencia.dropna(subset=["ST326Q01JA"]).copy()

# 2) Tu diccionario: cada código de respuesta -> horas aproximadas (punto medio del tramo)
mapeo = {1: 0, 2: 0.5, 3: 1.5, 4: 2.5, 5: 3.5, 6: 4.5, 7: 5.5, 8: 6.5, 9: 7.5}

# 3) Creamos la columna "horas" traduciendo cada código con el diccionario
datos["horas"] = datos["ST326Q01JA"].map(mapeo)
datos["pv_por_peso"] = datos["PV1READ"] * datos["W_FSTUWT"]

# # 4) Comprobaciones
# print(len(datos))                          # alumnos que quedan (debería ser 1473)
# print(datos["horas"].isna().sum())         # debería ser 0 (todos los códigos se tradujeron)
# print(datos["horas"].value_counts().sort_index()) 

# Agrupamos a los alumnos por su valor de horas y calculamos,
# para cada grupo, cuántos son y cuál es su lectura media (con PV1READ)
resumen = datos.groupby("horas")["PV1READ"].agg(["count", "mean"])

# Redondeamos para leerlo mejor
print(resumen.round(1))

# 2) Para cada grupo de horas, sumamos (nota x peso) y sumamos los pesos
sumas = datos.groupby("horas")[["pv_por_peso", "W_FSTUWT"]].sum()

# 3) La media ponderada es: suma(nota x peso) / suma(pesos)
sumas["media_ponderada"] = sumas["pv_por_peso"] / sumas["W_FSTUWT"]

# 4) Comparamos la media sin pesos (paso 2) con la media con pesos
comparacion = pd.DataFrame({
    "sin_pesos": resumen["mean"],
    "con_pesos": sumas["media_ponderada"],
})
print(comparacion.round(1))