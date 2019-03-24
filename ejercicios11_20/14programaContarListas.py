notas = ( 2, 4, 6, 8 )

def contenido( lista ,indice ):
    try:
        resultado = lista[indice]
    except:
        resultado = None
        print(" Fuera de lista")
    return resultado

# CONTAR ITEMS
indice = 0

while contenido( notas, indice ) != None :
    indice = indice + 1
    
print(" Númerod e items :",indice)

