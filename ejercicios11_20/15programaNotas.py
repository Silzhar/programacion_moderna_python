notas = ( 2, 4, 6, 8 )

def contenido( lista ,indice ):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    
    return resultado

# contar item de notas
indice = 0
while contenido( notas, indice ) != None:
    indice = indice + 1

# sumar notas
indice = 0
suma = 0
while contenido( notas, indice ) != None:
    suma = suma + notas[indice]
    indice = indice + 1

# calcular media
media = suma / indice

# salida de datos
print( "Número de items : ",indice )
print( " Notas a sumar : ",notas)
print( " Nota total : ",suma )
print( " Nota media : ",media)

