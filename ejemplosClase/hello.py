#Este es mi primer programa en Python
print("Hola mundo")

numero = 100
cadena = "Hola Mundo"
flotante = 10.5

#21.5 x 10^3
floatExponencial = 21.5e3
booleano = True

print(numero)
print(cadena)
print(flotante)
print(floatExponencial)
print(booleano) 

print(type(numero))
print(type(cadena))
print(type(flotante))
print(type(floatExponencial))
print(type(booleano))

#El tipo de dato de una variable puede cambiar
numero = "Ahora soy una cadena"
print(numero)
numero = 50
print(numero)

numero, contador, acumulador = 10, 20, 30
mensa1, mensa2 = "Hola", "Mundo"
print(numero, contador, acumulador)
print(mensa1, mensa2)

print( reversed("Mundo Hola"))

area = 3.14 * pow(5, 2)
print("El área del círculo es:", area)

print ( isinstance(area, float) )
print ( isinstance(area, int) )

mi_cadena_de_texto1 = "Texto1"
mi_cadena_de_texto2 = "Texto2"
print("Cadena 1:", mi_cadena_de_texto1, "Cadena 2:", mi_cadena_de_texto2)

#Longitud de una cadena
print(len(mi_cadena_de_texto1))

nombre = "Javier"
#Cuando separa con comas, añade un espacio automáticamente
print("Mi nombre es", nombre)
#Cuando se usa el + no añade espacio
print("Mi nombre es " + nombre)

#Entrada de datos -> input() siempre devuelve una cadena
edad = input("¿Cuál es tu edad? ")
print("Tu edad es " + edad)
print(type(edad))
#Convertir cadena a entero
edad = int(edad)
print(type(edad))

#Leemos un número con decimales y lo convertimos de cadena a float
precio = float(input("¿Cuál es el precio del producto? "))
print("El precio del producto es " + str(precio))
