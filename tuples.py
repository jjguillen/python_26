asignaturas = ("Servidor", "Cliente", "Despliegue", "Diseño", "Optativa")
#asignaturas.append("Proyecto") --> No se puede modificar una tupla
print(asignaturas)

# Longitud de una tupla
print(len(asignaturas)) # 5

print(asignaturas[2]) # Despliegue
print(asignaturas[-1]) # Optativa

# Buscar un elemento
print(asignaturas.index("Diseño")) # 3

# Cortar tuplas (slicing) -> El último elemento no entra
print(asignaturas[0:3]) # ('Servidor', 'Cliente', 'Despliegue') -> el elemento en la posición 3 no se incluye

# Convertir tupla en lista
asignaturas_lista = list(asignaturas)
print(asignaturas_lista) # ['Servidor', 'Cliente', 'Despliegue', 'Diseño', 'Optativa']
asignaturas_lista.append("Proyecto")
print(asignaturas_lista) 

# Preguntar si un elemento está en la tupla
print("Cliente" in asignaturas) # True
print("Proyecto" in asignaturas) # False

# Unir tuplas
asignaturas2 = ("Proyecto", "IPE2")
asignaturas = asignaturas + asignaturas2
print(asignaturas) 



