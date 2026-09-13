contatos = []

for i in range(5):
    print(f"\nCadastro do contato {i + 1}")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)

nome_busca = input("\nDigite o nome do contato que deseja: ")

encontrado = False

for contato in contatos:
    if contato["nome"].lower() == nome_busca.lower():
        print("\nContato encontrado:")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")

        encontrado = True
        break

if not encontrado:
    print("Contato Não Encontrado.")