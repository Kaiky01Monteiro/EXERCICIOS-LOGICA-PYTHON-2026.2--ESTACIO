estudantes = []


def cadastrar():
    nome = input("Nome: ")

    while True:
        try:
            idade = int(input("Idade: "))

            if idade > 0:
                break

            print("Error: a idade deve ser positiva.")
        except ValueError:
            print("Error: digite um número inteiro.")

    curso = input("Curso: ")

    while True:
        nota1 = float(input("Primeira nota: "))
        if nota1 >= 0 and nota1 <= 10:
            break
        print("Error: a nota deve estar entre 0 e 10.")

    while True:
        nota2 = float(input("Segunda nota: "))
        if nota2 >= 0 and nota2 <= 10:
            break
        print("Error: a nota deve estar entre 0 e 10.")

    while True:
        nota3 = float(input("Terceira nota: "))
        if nota3 >= 0 and nota3 <= 10:
            break
        print("Error: a nota deve estar entre 0 e 10.")

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": (nota1, nota2, nota3),
        "media": media,
        "situacao": situacao
    }

    estudantes.append(estudante)


def listar():
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
    else:
        for estudante in estudantes:
            print("\nNome:", estudante["nome"])
            print("Idade:", estudante["idade"])
            print("Curso:", estudante["curso"])
            print("Notas:", estudante["notas"])
            print(f"Média: {estudante['media']:.2f}")
            print("Situação:", estudante["situacao"])


def consultar():
    nome = input("Digite o nome do estudante: ")

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():
            print("\nNome:", estudante["nome"])
            print("Idade:", estudante["idade"])
            print("Curso:", estudante["curso"])
            print("Notas:", estudante["notas"])
            print(f"Média: {estudante['media']:.2f}")
            print("Situação:", estudante["situacao"])
            return

    print("Estudante não encontrado.")


def alterar():
    nome = input("Digite o nome do estudante: ")

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():

            print("1 - Nome")
            print("2 - Idade")
            print("3 - Curso")
            print("4 - Notas")

            opcao = input("O que deseja alterar? ")

            if opcao == "1":
                estudante["nome"] = input("Novo nome: ")

            elif opcao == "2":
                while True:
                    try:
                        idade = int(input("Nova idade: "))

                        if idade > 0:
                            estudante["idade"] = idade
                            break

                        print("Error: a idade deve ser positiva.")
                    except ValueError:
                        print("Error: digite um número inteiro.")

            elif opcao == "3":
                estudante["curso"] = input("Novo curso: ")

            elif opcao == "4":
                while True:
                    nota1 = float(input("Primeira nota: "))
                    if nota1 >= 0 and nota1 <= 10:
                        break
                    print("Error: a nota deve estar entre 0 e 10.")

                while True:
                    nota2 = float(input("Segunda nota: "))
                    if nota2 >= 0 and nota2 <= 10:
                        break
                    print("Error: a nota deve estar entre 0 e 10.")

                while True:
                    nota3 = float(input("Terceira nota: "))
                    if nota3 >= 0 and nota3 <= 10:
                        break
                    print("Error: a nota deve estar entre 0 e 10.")

                estudante["notas"] = (nota1, nota2, nota3)
                estudante["media"] = (nota1 + nota2 + nota3) / 3

                if estudante["media"] >= 7:
                    estudante["situacao"] = "Aprovado"
                elif estudante["media"] >= 5:
                    estudante["situacao"] = "Recuperação"
                else:
                    estudante["situacao"] = "Reprovado"

            else:
                print("Opção inválida.")
                return

            print("Dados alterados.")
            return

    print("Estudante não encontrado.")


def remover():
    nome = input("Digite o nome do estudante: ")

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():

            confirmacao = input("Deseja remover este estudante? (s/n): ")

            if confirmacao.lower() == "s":
                estudantes.remove(estudante)
                print("Estudante removido.")
            else:
                print("Remoção cancelada.")

            return

    print("Estudante não encontrado.")


def relatorio():
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    maior = estudantes[0]
    menor = estudantes[0]

    soma = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for estudante in estudantes:
        soma += estudante["media"]

        if estudante["media"] > maior["media"]:
            maior = estudante

        if estudante["media"] < menor["media"]:
            menor = estudante

        if estudante["media"] >= 7:
            aprovados += 1
        elif estudante["media"] >= 5:
            recuperacao += 1
        else:
            reprovados += 1

    media_geral = soma / len(estudantes)

    print("\nRelatório da turma:")
    print(f"Total de estudantes: {len(estudantes)}")
    print(f"Maior média: {maior['nome']} - {maior['media']:.2f}")
    print(f"Menor média: {menor['nome']} - {menor['media']:.2f}")
    print(f"Média geral: {media_geral:.2f}")
    print(f"Aprovados: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}")


while True:
    print("\n========================================")
    print("           SISTEMA ACADÊMICO")
    print("========================================")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Consultar estudante")
    print("4 - Alterar dados")
    print("5 - Remover estudante")
    print("6 - Gerar relatório da turma")
    print("0 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        consultar()

    elif opcao == "4":
        alterar()

    elif opcao == "5":
        remover()

    elif opcao == "6":
        relatorio()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")