import pandas as pd
import numpy as np


# C. Mediana Ponderada (el valor donde se acumula el 50% de la población ponderada)
def calcular_mediana_ponderada(vals, wts):
    df_temporal = pd.DataFrame({'val': vals, 'wt': wts}).sort_values('val')
    wt_acumulado = df_temporal['wt'].cumsum()
    valormedio_wt = df_temporal['wt'].sum() / 2.0
    return df_temporal.loc[wt_acumulado >= valormedio_wt, 'val'].iloc[0]

def media_pond(notas, pesos):
    return (notas * pesos).sum() / pesos.sum()

def media_con_error(df, pv_cols, rep_cols, peso="W_FSTUWT"):

    medias_pv = []
    varianzas_pv = []
    for pv in pv_cols:
        media_total = media_pond(df[pv], df[peso])
        suma_cuadrados = 0
        for c in rep_cols:
            m = media_pond(df[pv], df[c])
            suma_cuadrados = suma_cuadrados + (m - media_total) ** 2
        medias_pv.append(media_total)
        varianzas_pv.append(suma_cuadrados / 20)

    media_final = np.mean(medias_pv)
    # varianza muestral media
    u = np.mean(varianzas_pv)
    # varianza entre las 10 PV (imputación)
    b = np.var(medias_pv, ddof=1)

    error = np.sqrt(u + (1 + 1 / len(pv_cols)) * b)
    return media_final, error, len(df)


# Devuelve, la diferencia de la media entre dos años, el nuevo error actualizado,
# y el intérvalo de confianza al 95% +-
def comparar(m_a, e_a, m_b, e_b, ee_enlace=0):
    dif = m_b - m_a                                     # diferencia de las medias totales de los años
    se = np.sqrt(e_a**2 + e_b**2 + ee_enlace**2)        # Error tipico total añadiendo factor de comparación
    return dif, se, dif - 1.96 * se, dif + 1.96 * se

# Función porcentaje con pesos. Le paso df y el valor del idioma test que busco (depende del ciclo)
# 1ºfiltro a hispanoablantes

def pct_idioma(df, casa, prueba):
    # 1. Convertimos 'casa' a lista si es un valor único
    if not isinstance(casa, list):
       casa = [casa]
    # 2. Convertimos 'prueba' a lista si es un valor único
    if not isinstance(prueba, list):
       prueba = [prueba]

    # Subconjunto filtrado por el idioma de casa
    d = df[df["LANGN"].isin(casa)].dropna(subset=["W_FSTUWT"])

    # Indicador (1 si cumple el idioma de prueba, 0 en caso contrario)
    ceros_unos = d["LANGTEST_COG"].isin(prueba).astype(float)

    # NUMERADOR: Suma ponderada de la combinación específica (1s * peso)
    numerador = (ceros_unos * d["W_FSTUWT"]).sum()

    # DENOMINADOR: Suma de los pesos de TODA la base de datos (con pesos válidos). Eliminamos cols con respuestas NAN
    denominador = df.dropna(subset=["W_FSTUWT", "LANGN", "LANGTEST_COG"])["W_FSTUWT"].sum()

    # Devolvemos el porcentaje sobre el total de la base
    return 100 * (numerador / denominador)

def pct_inmigracion(df):
    # Base: alumnos con IMMIG válido (1, 2 o 3) y peso NO NULO
    d = df[df["IMMIG"].isin([1, 2, 3])].dropna(subset=["W_FSTUWT"])
    w = d["W_FSTUWT"]
    return {
        "Nativos":       100 * w[d["IMMIG"] == 1].sum() / w.sum(),
        "2ª generación": 100 * w[d["IMMIG"] == 2].sum() / w.sum(),
        "1ª generación": 100 * w[d["IMMIG"] == 3].sum() / w.sum(),
    }