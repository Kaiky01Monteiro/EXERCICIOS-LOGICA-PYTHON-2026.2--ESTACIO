temperaturas = []

for i in range(7):
    temperatura = float(input(f"Digite a temperatura do dia {i + 1}: "))
    temperaturas.append(temperatura)

maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / 7

acima_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_media += 1

print("Temperaturas registradas:")
print(temperaturas)
print(f"Maior temperatura: {maior:.2f} °C")
print(f"Menor temperatura: {menor:.2f} °C")
print(f"Média da semana: {media:.2f} °C")
print(f"Dias acima da média: {acima_media}")