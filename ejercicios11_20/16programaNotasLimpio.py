notas = ( 2, 4, 6, 8 )

def contenido( lista ,indice ):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    
    return resultado

# sumar notas e items
indice = 0
suma = 0
while contenido( notas, indice ) != None:
    suma = suma + notas[indice]
    indice = indice + 1

# calcular media
media = suma / indice

print( " Número de items : ",indice )
print( " Nota media      : ",media)
print( " nota total      : ",suma )

