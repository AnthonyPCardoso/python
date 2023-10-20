# Inicializa a lista de produtos vazia e o valor total
lista_de_compras = []
totalProdutos = 0

# Função para adicionar um produto à lista
def add_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    valor_unitario = float(input("Digite o valor unitário: "))
    
    total = quantidade * valor_unitario
    produto = {"produto": nome, "valor": valor_unitario, "quantidade": quantidade, "total": total}
    lista_de_compras.append(produto)
    
    global totalProdutos
    totalProdutos += total
    
    print(f"{nome} foi adicionado à lista de compras. Valor total: R${total:.2f}")
    
# Função para ver a lista de produtos
def lista_compras():
    if len(lista_de_compras) == 0:
        print("A lista de compras está vazia.")
    else:
        print("Lista de Compras:")
        for produto in lista_de_compras:
            print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: R${produto['valor']:.2f}, Total: R${produto['total']:.2f}")
        print(f"Valor total de todos os produtos: R${totalProdutos:.2f}")
        
# Função para atualizar as informações de um produto
def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    for produto in lista_de_compras:
        if produto["produto"] == nome:
            print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: R${produto['valor']:.2f}, Total: R${produto['total']:.2f}")
            quantidade = int(input("Digite a nova quantidade: "))
            valor_unitario = float(input("Digite o novo valor unitário: "))
            total = quantidade * valor_unitario
            produto["quantidade"] = quantidade
            produto["valor"] = valor_unitario
            produto["total"] = total
            global totalProdutos
            totalProdutos -= produto["total"]
            totalProdutos += total
            print(f"As informações de {nome} foram atualizadas. Novo total: R${total:.2f}")
            return
    print(f"{nome} não encontrado na lista de compras.")

# Função para remover um produto da lista
def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ")
    for produto in lista_de_compras:
        if produto["produto"] == nome:
            global totalProdutos
            totalProdutos -= produto["total"]
            lista_de_compras.remove(produto)
            print(f"{nome} foi removido da lista de compras.")
            return
    print(f"{nome} não encontrado na lista de compras.")

# Loop principal do programa
while True:
    print("\nOpções:")
    print("1. Adicionar produto")
    print("2. Ver lista de produtos")
    print("3. Atualizar produto")
    print("4. Remover produto")
    print("5. Encerrar programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        add_produto()
    elif opcao == "2":
        lista_compras()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
