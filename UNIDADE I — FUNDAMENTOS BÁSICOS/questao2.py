numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Resultados:")
print(f"Adição: {numero1 + numero2}")
print(f"Subtração: {numero1 - numero2}")
print(f"Multiplicação: {numero1 * numero2}")
print(f"Potenciação: {numero1 ** numero2}")

if numero2 == 0:
    print("Error: Divisão por zero não permitida")
    print("Error inteira: Divisão por zero não permitida")
    print("Error da divisão: Divisão por zero não permitida")
else:
    print(f"Divisão: {numero1 / numero2}")
    print(f"Divisão inteira: {numero1 // numero2}")
    print(f"Resto da divisão: {numero1 % numero2}")