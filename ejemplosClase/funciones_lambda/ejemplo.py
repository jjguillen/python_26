from math import pi

cuadrado = lambda x: x * x

print(cuadrado(5))  # Output: 25

area_circulo = lambda r: pi * cuadrado(r)
print(area_circulo(45.23))


def aplicar_funcion(func, valor):
    return func(valor)

resultado = aplicar_funcion(sum, [3,4,5,6])
print(resultado)

# Uso de map, filter y reduce con funciones lambda
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = list(map(lambda x: x * x, lista))
print(lista_cuadrados)

lista2 = [3, 4, 6, 15, 18, 25]
lista_multiplos_de_cinco = list(filter(lambda x: x % 5 == 0, lista2))
print(lista_multiplos_de_cinco)
