frase = input("Digite uma frase: ")

frase_sem_espacos = frase.strip()
palavras = frase_sem_espacos.split()

letra = input("Digite uma letra pra pesquisar: ")

quantidade_caracteres = len(frase)
quantidade_palavras = len(palavras)
primeira_palavra = palavras[0]
ultima_palavra = palavras[-1]
quantidade_letra = frase.lower().count(letra.lower())

print("Análise:")
print(f"Quantidade de caracteres: {quantidade_caracteres}")
print(f"Quantidade de palavras: {quantidade_palavras}")
print(f"Primeira palavra: {primeira_palavra}")
print(f"Última palavra: {ultima_palavra}")
print(f"Quantidade da letra '{letra}': {quantidade_letra}")
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")