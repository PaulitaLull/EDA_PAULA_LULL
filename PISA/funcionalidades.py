import pandas as pd
import numpy as np


# C. Mediana Ponderada (el valor donde se acumula el 50% de la población ponderada)
def calcular_mediana_ponderada(vals, wts):
    df_temporal = pd.DataFrame({'val': vals, 'wt': wts}).sort_values('val')
    wt_acumulado = df_temporal['wt'].cumsum()
    valormedio_wt = df_temporal['wt'].sum() / 2.0
    return df_temporal.loc[wt_acumulado >= valormedio_wt, 'val'].iloc[0]

# Que hace el return: Busca en la tabla el primer momento en el que 
# el peso acumulado (wt_acumulado) alcanza o supera el 50% (wt_acumulado >= valormedio_wt). 
# Una vez encontrado, extrae la puntuación ('val') que está en esa fila exacta (.iloc[0]). 
# Esa puntuación es, por definición matemática, la mediana ponderada.
