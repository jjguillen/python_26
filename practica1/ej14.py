#Palíndromo

palabra = input("Dime una plabra ")
palabra = palabra.lower()
if (palabra == palabra[::-1]) :
    print(True)
else:
    print(False)