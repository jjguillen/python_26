from math import pi
from functools import reduce

cuadrado = lambda x: x * x

print(cuadrado(5))  # Output: 25

area_circulo = lambda r: pi * cuadrado(r)
print(area_circulo(45.23))


def aplicar_funcion(func, valor):
    return func(valor)

resultado = aplicar_funcion(sum, [3,4,5,6])
print(resultado)

# Uso de map, filter y reduce con funciones lambda
## map -> aplicar una función a cada elemento de la lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = list(map(lambda x: x * x, lista))
print(lista_cuadrados)

## filter --> eliminar los elementos de la lista que no cumplan la condición
lista2 = [3, 4, 6, 15, 18, 25]
lista_multiplos_de_cinco = list(filter(lambda x: x % 5 == 0, lista2))
print(lista_multiplos_de_cinco)

## reduce --> aplicar una función de varios parámetros a un único resultado, lo va aplicando a la lista
lista3 = [1,2,3,4,5]
total_multiplicado = reduce(lambda x,y: x*y, lista3)
print(total_multiplicado)


