def remover_outliers(df, coluna):
    mean = df[coluna].mean()
    std = df[coluna].std()
    df = df[df[coluna] > mean - 2 * std]
    df = df[df[coluna] < mean + 2 * std]
    return df