cidades = []

for i in range(5):
    print(f"\nCadastro da cidade {i + 1}")

    nome = input("Nome da cidade: ")
    estado = input("Sigla do estado: ")
    populacao = int(input("População: "))

    cidade = {
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    }

    cidades.append(cidade)

maior = cidades[0]
menor = cidades[0]
populacao_total = 0

for cidade in cidades:
    populacao_total += cidade["populacao"]

    if cidade["populacao"] > maior["populacao"]:
        maior = cidade

    if cidade["populacao"] < menor["populacao"]:
        menor = cidade

media = populacao_total / len(cidades)

print("\nResultados:")
print(f"Maior população: {maior['nome']} - {maior['populacao']}")
print(f"Menor população: {menor['nome']} - {menor['populacao']}")
print(f"População total: {populacao_total}")
print(f"Média populacional: {media:.2f}")

print("\nCidades cadastradas:")

for cidade in cidades:
    print(f"Nome: {cidade['nome']}")
    print(f"Estado: {cidade['estado']}")
    print(f"População: {cidade['populacao']}")
    print()