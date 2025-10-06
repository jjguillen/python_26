#Determinar si un número es primo
import math

def es_primo(n):
    if n <= 3:
        return True
    else:
        for i in range(2, int(math.sqrt(numero)) + 1):
            if n%i == 0:
                return False
        return True


numero = 13
print(int(math.sqrt(numero)))
print(es_primo(numero))
