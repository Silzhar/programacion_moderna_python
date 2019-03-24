
notas = ( 2, 4, 6, 8 )

def existe( lista ,indice ):
    try:
        resultado = lista[indice]
    except:
        resultado = None
        print(" Fuera de lista")
    return resultado
