idade = int(input("Digite sua idade: "))

while idade < 0:
    print("Error: a idade não pode ser negativa.")
    idade = int(input("Digite sua idade: "))

if idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print(f"Classificação: {classificacao}")