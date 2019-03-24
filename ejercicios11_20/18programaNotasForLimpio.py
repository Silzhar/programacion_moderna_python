notas = ( 2, 4, 6, 8 )

def contenido( lista ,indice ):
    try:
        resultado = lista[indice]
    except:
        resultado = None
    
    return resultado

def longitud( lista ):
    indice = 0
    while contenido (lista, indice ) != None :
        indice = indice + 1 
    return indice

suma = 0
longitudNotas = longitud( notas ) # cambiar bucle por variable para optimizar recursos

for indice in range( 0, longitudNotas ):
    suma = suma + notas[indice]
     
media = suma / longitudNotas

print( " Número de items : ",longitud(notas) )
print( " Nota media      : ",media)
print( " nota total      : ",suma )