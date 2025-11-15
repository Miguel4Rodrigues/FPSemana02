#Quantos orangotangos ?
frase1 = input()

#Quantos ornitorrincos ?
frase2 = input()


palavras1 = set(frase1.split())
palavras2 = set(frase2.split()) 

comum = palavras1.intersection(palavras2)
        
resultado = " ".join(word for word in frase1.split() if word in comum)

print(resultado)
