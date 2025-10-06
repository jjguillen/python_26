# If condition
a = 10
if a > 5:
    print("a is greater than 5")

# If-Else condition
b = 3
if b % 2 == 0:
    print("b is even")
    print("b es par")
else:
    print("b is odd")
    print("b es impar")

# If-Elif-Else condition
c = 29
if c < 10:   # menor que 10
    print("c is less than 10")
elif c < 20: # entre 10 y 19
    print("c is between 10 and 19")
elif c < 30: # entre 20 y 29
    print("c is between 20 and 29")
else:        # 30 o más
    print("c is 30 or more")


# Operadores lógicos
a = 4
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')


# Anidamiento de condicionales
x = 15
if x > 10:      # mayor que 10
    if x < 20:  # entre 11 y 19
        print("x is between 11 and 19")
    else:       # 20 o más
        print("x is 20 or more")
else:           # 10 o menos
    print("x is 10 or less")    


    


