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

print( "Número de items : ",indice )

# sumar notas
indice = 0
suma = 0
while contenido( notas, indice ) != None:
    suma = suma + notas[indice]
    indice = indice + 1
print( " nota total : ",suma )

# calcular media
media = suma / indice

print( " Nota media : ",media)

