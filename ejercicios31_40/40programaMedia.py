def media(lista):
    suma = 0
    for n in lista:
        suma += n
        return suma/len(lista)
    
def calcularMedia(*items): # añade un numero variable de parámetros para no crear lista
    suma = 0
    for n in items:
        suma += n
        return suma/len(items)
    