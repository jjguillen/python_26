def clasificacion_edad(edad):
    if edad >= 65:
        return "Eres mayor"
    elif (edad >= 18) and (edad < 65):
        return "Eres adulto"
    else:
        return "Eres menor de 18"
    

print(clasificacion_edad(17))

