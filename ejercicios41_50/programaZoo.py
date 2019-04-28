def precioEntrada(e):
    if e > 0 and e <= 2:
        precio = 0
    elif e <= 12:
        precio = 14
    elif e < 65:
        precio = 23
    else:
        precio = 18
    return precio

def validaEdad(cadena): # validar solo positivos
    try:
        n = int(cadena)
        if n >= 0:
            return True
        return False
    except:
        return False

def pedirEdad():
    edad = input("¿Que edad tienes? ")
    while validaEdad(edad) == False:
        print("Introduzca edad en número ")
        edad = input("¿Que edad tienes? ")
        
    return int(edad)

edad = pedirEdad()
precioTotal = 0

while edad != 0:
    precioE = precioEntrada(edad)
    print("Precio entrada :{}".format(precioE))
    precioTotal += precioE
    
    edad = pedirEdad()

print("Total :{}".format(precioTotal))
