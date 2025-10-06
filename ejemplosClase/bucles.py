# while
i = 1
while i <= 5:
    print(i)
    i += 1          


# while y else
i = 1
while i <= 5:
    print(i)
    i += 1    
else:
    print("Loop finished")
    print(i)

# break
i = 1
while i <= 10:
    if i == 6:
        break  # Sale del bucle cuando i es 6
    print(i)
    i += 1

# continue
i = 0
while i < 10:       
    i += 1
    if i % 2 == 0:
        continue  # Salta el resto del código en esta iteración si i es par
    print(i)  # Solo imprime números impares


# for
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

precios = { 25.95, 15.50, 9.99 }
for precio in precios:
    print(precio)

# for con range
for i in range(5):  # De 0 a 4
    print(i)

print("-----")

for i in range(1, 20):
    print(i)


language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

# range al revés
for i in range(10, 0, -1):
    print(i)

# for del 100 al 0, solo decenas
for i in range(100, -1, -10):
    print(i)


# for sobre set
conjunto = {1, 2, 3, 4, 5}
for num in conjunto:
    print(num)

# for sobre diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,             
    "ciudad": "Madrid"
}
for clave in persona:
    print(clave, ":", persona[clave])

for clave, valor in persona.items():
    print(clave, valor)
else:
    print("Bucle terminado")


# for con break
productos = ["laptop", "tablet", "smartphone", "monitor"]
for producto in productos:
    if producto == "smartphone":
        print("Producto encontrado:", producto)
        break # Sale del bucle al encontrar "smartphone"
    print(producto)

# buscar elemento en lista con index
index = productos.index("smartphone")
if index != -1:
    print("Producto encontrado en el índice:", index)
    print(productos[index])
else:
    print("Producto no encontrado")






