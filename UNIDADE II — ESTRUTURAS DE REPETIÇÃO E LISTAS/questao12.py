produtos = []

for i in range(5):
    print(f"\nCadastro do produto {i + 1}")

    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Estoque dele: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

valor_estoque = 0

for produto in produtos:
    valor_estoque += produto["preco"] * produto["quantidade"]

mais_caro = produtos[0]

for produto in produtos:
    if produto["preco"] > mais_caro["preco"]:
        mais_caro = produto

print("\nProdutos cadastrados:")

for produto in produtos:
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print()

print(f"Valor total do estoque: R$ {valor_estoque:.2f}")
print(f"Produto com maior preço: {mais_caro['nome']}")
print(f"Maior preço: R$ {mais_caro['preco']:.2f}")