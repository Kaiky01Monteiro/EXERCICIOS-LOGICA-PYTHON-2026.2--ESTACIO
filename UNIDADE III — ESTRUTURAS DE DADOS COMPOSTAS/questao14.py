def cadastrar_aluno():
    nome = input("Nome do aluno: ")

    while True:
        nota1 = float(input("Digite a primeira nota: "))

        if nota1 >= 0 and nota1 <= 10:
            break

        print("Error: a nota deve estar entre 0 e 10.")

    while True:
        nota2 = float(input("Digite a segunda nota: "))

        if nota2 >= 0 and nota2 <= 10:
            break

        print("Error: a nota deve estar entre 0 e 10.")

    while True:
        nota3 = float(input("Digite a terceira nota: "))

        if nota3 >= 0 and nota3 <= 10:
            break

        print("Error: a nota deve estar entre 0 e 10.")

    media = (nota1 + nota2 + nota3) / 3

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    return aluno


alunos = []

for i in range(5):
    print(f"\nCadastro do aluno {i + 1}")
    aluno = cadastrar_aluno()
    alunos.append(aluno)

maior = alunos[0]
menor = alunos[0]

aprovados = 0
recuperacao = 0
reprovados = 0

for aluno in alunos:
    if aluno["media"] > maior["media"]:
        maior = aluno

    if aluno["media"] < menor["media"]:
        menor = aluno

    if aluno["media"] >= 7:
        aprovados += 1
    elif aluno["media"] >= 5:
        recuperacao += 1
    else:
        reprovados += 1

print("\nResultados:")

for aluno in alunos:
    print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")

print(f"\nMaior média: {maior['nome']} - {maior['media']:.2f}")
print(f"Menor média: {menor['nome']} - {menor['media']:.2f}")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")