#Quantos orangotangos ?
frase = input().replace(" ", "")

contador = {}

for letra in frase:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

print(contador)