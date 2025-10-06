#Pide al usuario una palabra y muestra cuántas vocales contiene.

palabra = input("Dame una palabra: ")
vocales = "aeiouAEIOU"

contador=0
for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra {palabra} tiene {contador} vocales.")

#Comprensión de listas
lista = [letra for letra in palabra if letra in vocales]
print(f"La palabra {palabra} tiene {len(lista)} vocales.")



