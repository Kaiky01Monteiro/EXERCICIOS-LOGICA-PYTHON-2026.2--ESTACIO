import math

numero = float(input("Digite um número: "))

if numero >= 0:
    print(f"Raiz quadrada: {math.sqrt(numero):.2f}")
else:
    print("Raiz quadrada: não existe raiz real para números negativos.")

print(f"Valor absoluto: {math.fabs(numero):.2f}")
print(f"Arredondamento para cima: {math.ceil(numero)}")
print(f"Arredondamento para baixo: {math.floor(numero)}")

if numero >= 0 and numero.is_integer():
    print(f"Fatorial: {math.factorial(int(numero))}")
else:
    print("Erro: disponível somente para números inteiros e não negativos.")