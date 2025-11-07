#Escribe una función que valide si una contraseña cumple los siguientes criterios:
#
#    Al menos 8 caracteres
#    Al menos una letra mayúscula
#    Al menos una letra minúscula
#    Al menos un número
#    Al menos un carácter especial (@, #, $, %, etc.)
#
#La función debe retornar True si cumple todos los criterios, False en caso contrario.

def validar_contrasena(contrasena):
    import re

    if len(contrasena) < 8:
        return False
    if not re.search(r'[A-Z]', contrasena):
        return False
    if not re.search(r'[a-z]', contrasena):
        return False
    if not re.search(r'[0-9]', contrasena):
        return False
    if not re.search(r'[@#$%&*!]', contrasena):
        return False

    return True