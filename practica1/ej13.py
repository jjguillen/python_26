#Suma de elementos de una matriz

matriz = list()
for i in range(0,2):
    #Hay que crear los elementos antes de acceder a ellos
    matriz.append(list(range(3)))
    for j in range(0,3):
        numero = int(input("Dime un número"))
        print(i,j)
        matriz[i][j] = numero
        
print(matriz)

#Suma de los elementos
contador = 0
for fila in matriz:
    contador += sum(fila) #Que sume la fila entera
print(contador)

#Comprensión de listas
mtx = [list(range(3)) for _ in range(2)]
print(mtx)



