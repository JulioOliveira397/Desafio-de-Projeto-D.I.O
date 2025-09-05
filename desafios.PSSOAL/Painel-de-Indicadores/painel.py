import matplotlib.pyplot as plt
import seaborn as sns

def grafico_barras(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="categoria", y="valor", data=df, palette="Blues_d")
    plt.title("Faturamento por Categoria", fontsize=16)
    plt.xlabel("Categoria")
    plt.ylabel("Faturamento (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_pizza(df):
    plt.figure(figsize=(8, 8))
    plt.pie(
        df["valor"],
        labels=df["categoria"],
        autopct="%1.1f%%",
        startangle=140,
        colors=sns.color_palette("pastel")
    )
    plt.title("Proporção de Faturamento por Categoria")
    plt.axis("equal")
    plt.show()
