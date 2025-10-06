#Crear diccionario
diccionario = {}
for i in range(3):
    clave = input("Dime el nombre: ")
    valor = float(input("Dime la nota: "))
    diccionario[clave] = valor

print(diccionario)

notas = diccionario.values()
print("La media es:", sum(notas)/len(notas))

