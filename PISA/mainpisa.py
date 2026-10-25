import pandas as pd
import pyreadstat

archivo_pisa = 'data/CY09_MS_STU_PUF.sav'
print("Cargando el archivo de microdatos de PISA (puede tardar unos segundos)...")

# Cargamos el dataset completo y leemos los metadatos(información vital sobre las variables, como las etiquetas de texto (qué significa que una columna tenga un código numérico) y los metadatos del archivo SPSS.)
df, meta = pyreadstat.read_sav(archivo_pisa)


# 2. Filtrar España
df_espana = df[df['CNT'] == 'ESP']
df_espana.to_csv("archivo_pisa_esp", index=False)

# print("Desglose de STRATUM en España:")
# print(df_espana['STRATUM'].value_counts(dropna=False))

# # # 2. Buscar automáticamente columnas candidatas a ccaa 
# columnas_candidatas=[]
# for col in df.columns: 
#   if any(k in col.upper() for k in ['STRAT', 'REG', 'NAT', 'PROV']):
#     columnas_candidatas.append(col)
# print("Columnas candidatas encontradas:", columnas_candidatas)

# # 3. Bucle para inspeccionar los valores de cada columna candidata
# for col in columnas_candidatas:
#     print(f"\n========================================")
#     print(f"Columna: {col}")
#     print(f"========================================")
#     # Muestra los 15 valores más repetidos de esa columna
#     print(df[col].value_counts(dropna=False).head(15))

# # Conectamos el nombre técnico de cada variable con su descripción humana, con la funcion zip cremallera para leer bien la info
# for col, label in zip(meta.column_names, meta.column_labels):
#    print(f"**{col}**: {label}")

# #  Muestra la codificación de los valores de una variable determinada. Como ya sabemos que es STRATUM, la miramos a ver qué codificación es vlc
# etiquetas_ccaa = meta.variable_value_labels.get('STRATUM')
# if etiquetas_ccaa:
#     for codigo, texto in etiquetas_ccaa.items():
#         print(f"Código {codigo} -> {texto}")
# else:
#     print("Esta columna no tiene etiquetas de valor predefinidas en el metadato.")

codigos_valencia = ['ESP33', 'ESP34']
df_valencia=df_espana[df_espana["STRATUM"].isin(codigos_valencia)]
df_valencia.to_csv("data/pisa_valencia.csv", index=False)

# # Conectamos el nombre técnico de cada variable con su descripción humana, con la funcion zip cremallera para leer bien la info
# for col, label in zip(meta.column_names, meta.column_labels):
#    print(f"**{col}**: {label}")

# Ver qué valor tiene la variable VER_DAT en las primeras filas
if 'VER_DAT' in df.columns:
    print("Fecha de creación de la base de datos (VER_DAT):")
    print(df['VER_DAT'].value_counts().head(5))