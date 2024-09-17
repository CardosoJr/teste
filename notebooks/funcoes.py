import pandas as pd

def dropar_na(df, coluna, limite_dados_faltantes):
    if df[coluna].isna().mean() > limite_dados_faltantes:
        df = df.dropna(subset=[coluna])
    return df

def limpar_outlier(df, coluna): 
    media = df[coluna].mean()
    dp = df[coluna].std()
    ls = media + 2*dp
    li = media - 2*dp
    df = df[(df[coluna] > li) & (df[coluna] < ls)]
    return df