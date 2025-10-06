#Solicita dos números enteros y muestra todos los pares que se encuentran en ese intervalo.

num1 = int(input("Dame un número entero: "))
num2 = int(input("Dame otro número entero: "))

if num1 > num2:
    num1, num2 = num2, num1 #Intercambio de valores

for i in range(num1, num2+1):
    if i % 2 == 0:
        print(i)

#Comprensión de listas
#[ variable - for - if]
pares = [i for i in range(num1, num2+1) if i%2 == 0]
print(pares)


    