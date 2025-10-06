
lista = list()
for i in range(5):
    num = int(input("Dime un número entero: "))
    lista.append(num)

print(f"La lista es: {lista}")

#Comprensión de listas
lista2 = [int(input("Dime un número entero: ")) for i in range(5)]
print(f"La lista es: {lista2}")


print(lista2[::-1]) #Recorrer Lista invertida pero no la modifica
print("Lista original:", lista2)
lista2.reverse() #Modifica la lista original
print("Lista al revés:", lista2)

