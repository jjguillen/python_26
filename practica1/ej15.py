#Diccionario de palabras
frase = input("Dime una frase: ")
frase = frase.lower()

palabras = frase.split()
print(palabras)

diccionario = {}
for i in palabras:
    #if not in diccionario.keys()
    if not diccionario.get(i):
        diccionario[i] = 1
    else:
        diccionario[i] += 1

print(diccionario)