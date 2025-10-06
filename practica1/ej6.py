
lista = [int(input("Dime un número:")) for i in range(5)]
print(f"La lista es: {lista}")

print("El mayor es ",max(lista))
print("El menor es ",min(lista))

lista.sort()
print("El mayor es ", lista[-1])
print("El menor es ", lista[0])
