import programaPantalla

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
    programaPantalla.locate(2,1)
    edad = input("¿Que edad tienes? ")
    while validaEdad(edad) == False:
        print("Introduzca edad en número ")
        edad = input("¿Que edad tienes? ")

    return int(edad)

programaPantalla.clear()
edad = pedirEdad()
precioTotal = 0
linea = 4

entradasB = 0
entradasN = 0
entradasA = 0
entradasJ = 0

while edad != 0:
    precioE = precioEntrada(edad)
    if precioE == 0:
        linea = 4
        entradasB += 1
        print("Precio entrada :{}\tEntradas :{}".format(precioE, entradasB))
    if precioE == 14:
        linea = 5
        entradasN += 1
        print("Precio entrada :{}\tEntradas :{}".format(precioE, entradasN))
    if precioE == 23:
        linea = 6
        entradasA += 1
        print("Precio entrada :{}\tEntradas :{}".format(precioE, entradasA))
    if precioE == 18:
        linea = 7
        entradasJ += 1
        print("Precio entrada :{}\tEntradas :{}".format(precioE, entradasJ))
        
    programaPantalla.locate(linea, 1)
    linea += 1
    precioTotal += precioE
    
    edad = pedirEdad()

programaPantalla.locate(linea, 2)
print("Total :{}".format(precioTotal))
