# Desafio: Criador de Itens Mágicos
class ItemMagico:
    def __init__(self, tipo, dano, resistencia):
        self.tipo = tipo
        self.dano = dano
        self.resistencia = resistencia

    def calcular_dano(self):
        return self.dano * 2 if self.tipo.lower() == "arma" else self.dano

tipo = input("Tipo do item: ")
dano = int(input("Dano do item: "))
resistencia = int(input("Resistência do item: "))

item = ItemMagico(tipo, dano, resistencia)
print(f"Tipo: {item.tipo}")
print(f"Dano: {item.dano}")
print(f"Resistencia: {item.resistencia}")
print(f"Dano em combate: {item.calcular_dano()}")
