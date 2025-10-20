# try - except --> como try - catch

try:
    print(10 + 'a')
except:
    print("Un error en la operación")
finally:
    print("Esto se ejecuta siempre")
    print("Cerrando conexion BBDD...")


try:
    name = input('Enter your name:')
    year_born = int(input('Year you were born:'))
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
    print(age / year_born)
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
finally:
    print("Gracias por usar")