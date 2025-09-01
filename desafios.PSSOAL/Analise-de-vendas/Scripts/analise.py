def faturamento_por_categoria(df):
    return df.groupby("categoria", as_index=False)["valor"].sum().sort_values("valor", ascending=False)

def produtos_mais_vendidos(df):
    return df.groupby("produto", as_index=False)["quantidade"].sum().sort_values("quantidade", ascending=False)

def total_por_cliente(df):
    return df.groupby("cliente_id", as_index=False)["valor"].sum().sort_values("valor", ascending=False)