numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

while numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Error: os números não podem ser iguais.")

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2:
    if numero2 > numero3:
        maior = numero1
        meio = numero2
        menor = numero3
    elif numero1 > numero3:
        maior = numero1
        meio = numero3
        menor = numero2
    else:
        maior = numero3
        meio = numero1
        menor = numero2

else:
    if numero1 > numero3:
        maior = numero2
        meio = numero1
        menor = numero3
    elif numero2 > numero3:
        maior = numero2
        meio = numero3
        menor = numero1
    else:
        maior = numero3
        meio = numero2
        menor = numero1

print("Ordem do maior ao menor:")
print(f"Maior número: {maior}")
print(f"Número intermediário: {meio}")
print(f"Menor número: {menor}")