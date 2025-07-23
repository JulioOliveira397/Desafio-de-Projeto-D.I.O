# Desafio: Dama da Masmorra
quantidade_golpes = int(input("Digite a quantidade de golpes: "))
minerais = ["", "Carvao", "Ferro", "Diamante", "Pedra"]

for i in range(1, quantidade_golpes + 1):
    indice = i % 4 if i % 4 != 0 else 4
    print(f"{i}: {minerais[indice]}")
