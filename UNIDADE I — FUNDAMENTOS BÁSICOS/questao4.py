nota1 = float(input("Digite a primeira nota: "))

while nota1 < 0 or nota1 > 10:
    print("Error: a nota deve estar entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

while nota2 < 0 or nota2 > 10:
    print("Erroe: a nota deve estar entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

while nota3 < 0 or nota3 > 10:
    print("Error: a nota deve estar entre 0 e 10.")
    nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("Notas:")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")