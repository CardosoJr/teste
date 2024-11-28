import pandas as pd

def dropna(df, coluna, limite = 0.05):
    if df[coluna].isna().mean() > limite:
        df = df.dropna(subset = [coluna])
    return df

def remove_outliers(df, coluna):
    media = df[coluna].mean()
    dp = df[coluna].std()
    ls = media + 2 * dp
    li = media - 2 * dp

    df = df[df[coluna] > li]
    df = df.query(f"{coluna} < @ls")

    return df   