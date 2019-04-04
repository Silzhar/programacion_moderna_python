
# bloque de entrada
numero1 = input( "Número uno  :") 
numero2 = input( "Número dos  :") 

isvalidn1 = False
while not isvalidn1:
    if numero1.isdigit():
        numero1 = int(numero1)
        isvalidn1 = True
    elif numero1 != '' and numero1[0] == '-' and numero1[1:].isdigit():
        numero1 = int(numero1)
        isvalidn1 = True
    else:
        print( numero1," Debe ser un entero" )
        numero1 = input(" Introduzca otro número ")

isvalidn2 = False
while not isvalidn2:
    if numero2.isdigit():
        numero2 = int(numero2)
        isvalidn2 = True
    elif numero2 != '' and numero2[0] == '-' and numero2[1:].isdigit():
        numero2 = int(numero2)
        isvalidn2 = True
    else:
        print( numero2," Debe ser un entero" )
        quit()
# [1:].isdigit // 1 representa la posicion en la cadena  // : desde el indice (en este caso 1) hasta...
#  isdigit para saber si una cadena es numerica, retorna True o False

# bloque de procesos
numero1 = int(numero1) / 10
numero2 = int(numero2) / 10

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
division = numero1 / numero2

# bloque de salida de datos
print(" La suma de los valores es :" ,round(suma, 2))
print( " La resta de los valores es :",round(resta, 2) )
print( " El producto de los valores es :",round(producto, 2) )
print( " La división de los valores es :",round( division, 2) )

