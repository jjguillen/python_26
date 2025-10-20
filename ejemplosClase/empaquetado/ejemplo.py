# *variable -> empaquetar los elementos restantes en una lista
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries

print(fin)
print(sw)
print(nor)
print(rest)

def mult(*params):
    for i in params:
        print(i * 5)


mult(1,2,3,4,5)