# anagrama('amor', 'roma')
def anagrama(p1, p2):
    comparacionLetras = []

    if len(p1) != len(p2): # recorer para comparar longitud de palabras
        return False
    
    for caracter1 in p1:
        haPasado = False
        for caracter2 in p2:
            if caracter1 == caracter2 :
                haPasado = True
                comparacionLetras.append(True)
                
        if not haPasado:
            comparacionLetras.append(False)

    if False in comparacionLetras:
        return False
    else:
        return True

# comprobar en 2 direcciones :
def comprobarAnagrama(p1, p2):
    return anagrama(p1, p2) and anagrama(p2, p1)
                
            