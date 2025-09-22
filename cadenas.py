texto = 'Hola Mundo'
texto2 = "Esto de programar en Python no sé yo ..."

print(texto , texto2)
print(texto2 + " " + texto)

texto3 = texto2 + " - " + texto
print(texto3)
print(len(texto3))

print("Me gusta 'Python' \nespero aprender mucho")


# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f' %(radius, area) # 2 refers the 2 significant digits after the point
print(formated_string)
print('The area of circle with a radius %d is %.2f' %(radius, area) )
print('The area of circle with a radius {} is {}'.format(radius, area) )

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Acceso a string por índice
cadena = "I love Python"
print(cadena[0])  # First character
print(cadena[7])  # Eighth character
print(cadena[-1]) # Last character
print(cadena[len(cadena)-1]) # Last character 
print(cadena[-2]) # Second last character
print(cadena[0:4]) # First 4 characters
print(cadena[7:])  # From the eighth character to the end
print(cadena[:])   # The whole string

# Reverse a string
print(cadena[::-1])
print(reversed(cadena))  # returns an object

