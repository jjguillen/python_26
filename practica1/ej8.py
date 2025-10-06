#Tabla multiplicar

numero = int(input("Dime un número: "))
for i in range(1,11):
    print(numero, "x", i, "=", numero*i)

#Comprensión de listas
tabla = [numero*i for i in range(1,11)]
print(tabla)


