
# El primer caracter en mayúscula
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# Número de ocurrencias de un caracter en una cadena
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 7 -> start, 14 -> end

# Si termina en un substring específico
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True

# Devuelve el índice de la primera ocurrencia de un substring
challenge = 'thirty days of python'
print(challenge.find('ty'))  # 5

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
#print(challenge.index(sub_string, 9)) # error 9 -> start

# Si todos los caracteres en la cadena son alfanuméricos
challenge = '30DaysPython'
print(challenge.isalnum()) # True
challenge = 'thirtydaysofpython 2019'
print(challenge.isalnum()) # False -> espacio en blanco

# Si todos los caracteres en la cadena son alfabéticos (no incluye números)
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True

# Si todos los caracteres están en minúscula o mayúscula
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

# Concatenar un array de cadenas en una sola cadena
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

# Reemplazar una subcadena por otra
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# Dividir una cadena según un separador
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
challenge = '192.168.1.10'
print(challenge.split('.')) # ['192', '168', '1', '10']

# Cambiar mayúsculas por minúsculas y viceversa
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON

