# Conjuntos (sets) en Python
# Colección desordenada de elementos únicos (sin duplicados)
# No se puede acceder a los elementos por índice    

compra = set()
compra.add("pan")
compra.add("huevos")
compra.add("leche")
compra.add("pan")  # No se añade porque ya existe

print(compra)  # Salida: {'pan', 'huevos', 'leche'}

compra = {"pan", "huevos", "leche", "pan"}  # No se añade el duplicado
print(compra) 

print(len(compra))  # Salida: 3
print("huevos" in compra)  # Salida: True
#print(compra[2]) --> No accesible por índice

# Añadir varios elementos de golpe
compra.update(["carne", "pescado", "verduras", "leche"])
print(compra)

# Eliminar elementos --> discard
compra.remove("pan")  # Error si el elemento no existe
print(compra)
# compra.remove("yogures")  --> da error si el elemento no existe
compra.discard("yogures")  # No da error si el elemento no existe
compra.discard("verduras")
print(compra)

# Eliminar todos los elementos
compra.clear()
print(compra)  # Salida: set()

# Convertir lista a conjunto (elimina duplicados)
lista = [1, 2, 3, 4, 5, 1, 2, 3]
conjunto = set(lista)
print(conjunto)  # Salida: {1, 2, 3, 4, 5}

# OPERADORES DE CONJUNTOS
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Unión -> elementos que están en A o en B
print(A | B)  # Salida: {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))

# Intersección -> elementos que están en A y en B
print(A & B)  # Salida: {4, 5}
print(A.intersection(B))

# Diferencia -> elementos que están en A pero no en B
print(A - B)  # Salida: {1, 2, 3}
print(A.difference(B))  
print(B - A)  # Salida: {6, 7, 8}
print(B.difference(A))

# Preguntar si es subconjunto o superconjunto
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

# Diferencia simétrica -> elementos que están en A o en B pero no en ambos
print(A ^ B)  # Salida: {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))    

# Diferencia de A con B Unión La diferencia de B con A
print((A - B) | (B - A))  # Salida: {1, 2, 3, 6, 7, 8}







