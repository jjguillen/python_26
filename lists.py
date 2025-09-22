# Creación
lista = list() # lista vacía
lista2 = [] # lista vacía
lista3 = [1, 2, 3, 4, 5]
lista4 = ['Python', 'JavaScript', 'Java', 'C++']

print(lista)  # []
print(lista3) # []

# Longitud de una lista
print(len(lista3)) # 5

# Acceso a elementos -> primera posición es 0
print(lista3[0]) # 1
print(lista3[4]) # 5

# Acceso a elementos desde el final -> -1 es el último elemento
print(lista3[-1]) # 5
print(lista3[len(lista3)-1]) # 5
print(lista3[-5]) # 1

# Desempaquetado de listas
len1, len2, len3, len4 = lista4
print(len1,len2,len3,len4) # Python JavaScript Java C++

lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
len1, len2, len3, *resto = lista5
print(len1,len2,len3) # 1 2 3
print(resto) # [4, 5, 6, 7, 8, 9, 10]

# Cortar listas (slicing) -> El último elemento no entra
print(lista5[0:3]) # [1, 2, 3] -> el elemento en la posición 3 no se incluye
print(lista5[3:6]) # [4, 5, 6]-> el elemento en la posición 6 no se incluye
print(lista5[2:])  # [3, 4, 5, 6, 7, 8, 9, 10
print(lista5[:8]) # [1, 2, 3, 4, 5, 6, 7, 8]
print(lista5[-4:-1])
print(lista5[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] -> lista invertida
lista5 = lista5[::-1]
print(lista5) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Modificar elementos
lista5[4] = 50
print(lista5) 
#lista[10] = 100 # IndexError: list assignment index out of range

lista5[9] = "Pepe" # No es recomendable mezclar tipos de datos
print(lista5)

# Añadir elementos por el final
lista5.append(100)
lista5.append(200)
print(lista5)   

# Insertar elementos en una posición concreta -> el resto de elementos se desplazan a la derecha
lista5.insert(0, 'Inicio')
lista5.insert(5, 'Medio')
lista5.insert(6,200)
print(lista5)

# Eliminar elementos por valor -> elimina la primera ocurrencia
lista5.remove('Pepe')
lista5.remove('Medio')
lista5.remove('Inicio')
lista5.remove(200) # elimina la primera ocurrencia
print(lista5)

# Eliminar elementos por posición -> devuelve el elemento eliminado
eliminado = lista5.pop() # elimina el último elemento
print(eliminado) # 200
print(lista5)
print(lista5.pop(4)) # elimina el elemento en la posición 4
print(lista5)

# Eliminar por rango de posiciones
del lista5[0:3] # elimina los elementos en las posiciones 0, 1 y 2
print(lista5)
del lista5 # elimina todos los elementos y la variable ya no existe
#print(lista5) #Esto da error porque la variable ya no existe

lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista5.clear() # elimina todos los elementos pero la variable sigue existiendo
print(lista5) # []

# Copiar listas
lista6 = [1, 2, 3, 4, 5]
lista7 = lista6 # No es una copia, ambas variables apuntan a la misma lista
lista7.remove(3)
print(lista6) # [1, 2, 4, 5]

lista8 = lista6.copy() # Copia de la lista y crea una nueva lista
lista8.remove(4)
print(lista6) # [1, 2, 4, 5]
print(lista8) # [1, 2, 5]   

# Unir listas
lista9 = lista8 + lista6
print(lista9) # [1, 2, 5, 1, 2, 4, 5]

# Contar los elementos iguales de una lista
print(lista9.count(1)) # 2
print(lista9.count(4)) # 1

# Encontrar el índice de un elemento -> devuelve la primera ocurrencia
print(lista9.index(5)) # 2

# Invertir una lista
lista9.reverse()
print(lista9) # [5, 4, 2, 1, 5, 2, 1]


