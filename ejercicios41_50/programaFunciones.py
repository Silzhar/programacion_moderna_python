import programaPantalla

def tipoEntrada(e):
    if e > 0 and e <= 2:
        tipo = 'bebe'
    elif e <= 12:
        tipo = 'niño'
    elif e < 65:
        tipo = 'adulto'
    else:
        tipo = 'jubilado'
    return tipo

def validaEdad(cadena): # validar solo positivos
    try:
        n = int(cadena)
        if n >= 0:
            return True
        return False
    except:
        return False

def pedirEdad():
    edad = programaPantalla.Input("¿Que edad tienes? ", 1, 1) #esta linea sustituye a las 3 siguientes
   # programaPantalla.locate(1,1)
   # programaPantalla.clearLine()
   # edad = input("¿Que edad tienes? ")
    while validaEdad(edad) == False:
        programaPantalla.Format(0,33,45)
        programaPantalla.Print("Introduzca edad en número ",24, 1,True) #olocar el aviso de error abajo sin cambiar de linea
       # programaPantalla.locate(24,1) # colocar el aviso de error abajo
       # print("Introduzca edad en número ",end="")
        programaPantalla.Reset()
        edad = programaPantalla.Input("¿Que edad tienes? ", 1, 1)
        
    programaPantalla.clearLine(24)
    return int(edad)

def printScreen():
    programaPantalla.clear()
    programaPantalla.Print("Bebé.......:    -", 4, 5) #sustituye las 2 inferiores
#    programaPantalla.locate(4, 5)
 #   print("Bebé.......:    -")
    programaPantalla.Print("Infantil...:    -", 5, 5)
    programaPantalla.Print("Adulto.....:    -", 6, 5)
    programaPantalla.Print("Jubilado...:    -", 7, 5)
    
    programaPantalla.Format(1,37, 40)
    programaPantalla.Print("Total...:",9, 8)
    programaPantalla.Reset()
    