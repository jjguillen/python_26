cadena = "Hola Mundo"
lista = [letra for letra in cadena if letra in 'aeiou']
print(lista)

numbers = [(i, i * i) for i in range(11)]
print(numbers) 

#Números pares del 0 al 40
pares = [num for num in range(41) if num % 2 == 0]
print(pares)

