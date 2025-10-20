def pintar(lista):
    for i in lista:
        if (i < 0):
            raise Exception("Número negativo")
        print(i)



lista = [1,2,3,4,5,6,-1,7,8]
try:
    pintar(lista)
except Exception as e:
    print({e})

