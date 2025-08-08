def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Listar produtos")
    print("4. Sair")

# Estoque fora da função (não zera ao chamar o menu)
estoque = {}

while True:
    mostrar_menu() 
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade
        print(f"{quantidade} unidades de {produto} adicionadas ao estoque.")

    elif opcao == '2':
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade a remover: "))
        if produto in estoque:
            if estoque[produto] >= quantidade:
                estoque[produto] -= quantidade
                print(f"{quantidade} unidades de {produto} removidas do estoque.")
            else:
                print(f"Não há {quantidade} unidades de {produto} no estoque.")
        else:
            print(f"{produto} não encontrado no estoque.")

    elif opcao == '3':
        print("\nEstoque atual:")
        for item, qntd in estoque.items():
            print(f"{item}: {qntd} unidades")

    elif opcao == "4":
        print("Saindo... Resumo final do estoque:")
        for item, qtd in estoque.items():
            print(f"{item}: {qtd} unidades")
        break

    else:
        print("Opção inválida. Tente novamente.")