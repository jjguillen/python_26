#Crea una función que reciba una lista de números y retorne un diccionario con la media, mediana y moda.

def calcular_estadisticas(numeros):
    from collections import Counter

    if not numeros:
        return {"media": None, "mediana": None, "moda": None}

    # Calcular la media
    media = sum(numeros) / len(numeros)

    # Calcular la mediana
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
    else:
        mediana = numeros_ordenados[n // 2]

    # Calcular la moda
    contador = Counter(numeros)
    max_frecuencia = max(contador.values())
    modas = [num for num, freq in contador.items() if freq == max_frecuencia]
    moda = modas[0] if len(modas) == 1 else modas  # Si hay más de una moda, devolver todas

    return {"media": media, "mediana": mediana, "moda": moda}