def limpar_valores(df):
    df["valor"] = (
        df["valor"].astype(str)
        .str.replace(r"[^\d,.-]", "", regex=True)  # Remove símbolos como R$, espaços, etc.
        .str.replace(".", "", regex=False)         # Remove separador de milhares
        .str.replace(",", ".", regex=False)        # Troca vírgula decimal por ponto
        .astype(float)                             # Converte para float
    )
    return df