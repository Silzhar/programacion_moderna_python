def anagramaSimple(p1, p2):
    listaComparacion = []
    
    if len(p1) != len(p2):
        return False
        
    for caracter1 in p1:
        noAñadasFalse = False
        for caracter2 in p2:
            if caracter1 == caracter2:
                noAñadasFalse = True
                listaComparacion.append(True)
                
        if not noAñadasFalse:
            listaComparacion.append(False)
        
    if False in listaComparacion:
        return False
    else:
        return True
    
def isAnagram(p1, p2):
    return isAnagram(p1, p2) and isAnagram(p2, p1)

def contarCaracteres(cadena):
    resultado = dict()
    
    for caracter in cadena:
        if caracter in resultado:
            resultado[caracter] += 1
        else:
            resultado[caracter] = 1
    return resultado

def anagramaDic(p1, p2):
    dict1 = contarCaracteres(p1)
    dict2 = contarCaracteres(p2)
    return dict1 == dict2


        