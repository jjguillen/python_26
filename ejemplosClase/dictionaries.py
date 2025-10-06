# Diccionarios: son colecciones de datos que almacenan pares clave-valor.
# Las claves deben ser únicas e inmutables (números, cadenas, tuplas).
# Los valores pueden ser de cualquier tipo de dato y pueden repetirse.

# Crear un diccionario vacío
diccionario = {}
print(diccionario)  # Salida: {}


# Crear un diccionario con datos
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "es_soltero": True,
    "hijos": None,
    "lenguajes": ["Python", "Java", "C++"]
}
print(persona)

# Acceder a valores por clave
print(persona["nombre"])  # Salida: Juan
print(persona.get("edad"))  # Salida: 30

# Modificar valores
persona["edad"] = 31
persona["hijos"] = 2
print(persona)

# Longitud del diccionario
print(len(persona))  # Salida: 6

# Añadir nuevos pares clave-valor
persona["profesion"] = "Ingeniero"
print(persona)
persona["nombre"] = "Pedro"  # Modifica el valor de la clave existente
print(persona)

# Eliminar pares clave-valor
del persona["ciudad"]
print(persona)

# Elimina elemento y devuelve su valor
edad = persona.pop("edad")
print(edad)  # Salida: 31
print(persona)

# Elimina el último par clave-valor insertado (Python 3.7+)
ultimo = persona.popitem()
print(ultimo)  # Salida: ('profesion', 'Ingeniero')
print(persona)

# Pasar los valores a una lista
valores = list(persona.values())
print(valores)  # Salida: ['Pedro', True, 2, ['Python', 'Java', 'C++']]

# Pasar las claves a una lista
claves = list(persona.keys())
print(claves)  # Salida: ['nombre', 'es_soltero', 'hijos', 'lenguajes']

# Pasar los pares clave-valor a una lista de tuplas
items = list(persona.items())
print(items)  # Salida: [('nombre', 'Pedro'), ('es _soltero', True), ('hijos', 2), ('lenguajes', ['Python', 'Java', 'C++'])]

# Limpiar diccionario
persona.clear()
print(persona)  # Salida: {}













