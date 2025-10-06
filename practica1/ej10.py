frase = input("Dime una frase: ")
frase = frase.lower()
letras = {} # 'a':0, 'b':2, ...
for letra in frase:
    if letra in letras:
        letras[letra] += 1 # si la letra ya está le sumo 1
    else:
        letras[letra] = 1  # si es la primera vez que aparece la inicializo a 1

print(letras)

