numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("Dados:")
print(f"Números informados: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")