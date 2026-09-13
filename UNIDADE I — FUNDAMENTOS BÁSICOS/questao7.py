numero = int(input("Digite um número inteiro: "))

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "nulo"

if numero % 2 == 0:
    par_impar = "par"
else:
    par_impar = "ímpar"

print(f"O número {numero} é {sinal} e {par_impar}.")