
def validacion(mensaje):
    # bloque de entrada
    numero = input( mensaje) 
    

    isvalid = False
    while not isvalid:
        if numero.isdigit():
            numero = int(numero)
            isvalid = True
        elif numero != '' and numero[0] == '-' and numero[1:].isdigit():
            numero = int(numero)
            isvalid = True
        else:
            print( numero," Debe ser un entero" )
            numero = input(mensaje)
        
        return numero

numero1 = validacion( "Introcuzca primer Número  :")
numero2 = validacion( "Introcuzca segundo Número  :")

# bloque de procesos
numero1 = numero1/10
numero2 = numero2/10

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
division = numero1 / numero2

# bloque de salida de datos
print(" La suma de los valores es :" ,round(suma,2) )
print( " La resta de los valores es :",round(resta, 2) )
print( " El producto de los valores es :",round(producto, 2) )
print( " La división de los valores es :",round( division, 2) )



