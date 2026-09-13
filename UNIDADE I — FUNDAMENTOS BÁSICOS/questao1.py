nome = input("Qual seu nome completo: ")
cidade = input("Qual cidade você mora: ")

while True:
    try:
        idade = int(input("Qual sua idade: "))

        if idade < 0:
            print("Error: a idade não pode ser negativa.")
        else:
            break

    except ValueError:
        print("Error: digite a idade usando um número inteiro.")

while True:
    try:
        altura = float(input("Digite sua altura em metros: "))

        if altura <= 0:
            print("Error: a altura deve ser positiva.")
        else:
            break

    except ValueError:
        print("Error: digite a altura usando números.")

print("       Perfil Pessoal")
print(f"Nome completo : {nome}")
print(f"Idade         : {idade} anos")
print(f"Altura        : {altura:.2f} m")
print(f"Cidade        : {cidade}")