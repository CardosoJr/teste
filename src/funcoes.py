def remover_coluna_missing(df, col_name, limite = 0.10):
    if df[col_name].isna().mean() > limite:
        df = df.drop(columns = col_name)
    return df

def analisar_outlier(df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    li = q1 - 1.5 * iqr
    ls = q3 + 1.5 * iqr
    df = df[df[col] >= li]
    df = df[df[col] <= ls]
    return df 