from functools import reduce

def doble(x):
    return x+x

def sumarClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
    return resultado
        
def sumarDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor * 2
    return resultado

def productoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
    return resultado
    
lista = [1, 3, -2 , 15, 9]
# copia de la lista o clon de lista:
l = lista[:]
# añadir el neutro para la suma en la posicion cero
l.insert(0,0)

listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)

listaPares = filter(lambda x: x % 2 == 0, lista)
'''       equivale a  :
def f(x):
    if x / 2 == 0:
        return x
    else:
        return None   '''

def esPar(x):
    return x % 2 == 0

listaPares1 = filter(esPar, lista)

sumatorio = reduce(lambda x, y: x + y, lista) # reduce suma todos los elementos de la lista
suma100 = reduce(lambda x, y: x + y, range(101))

print(sumarClasico)
print(sumarDobleClasico)
print(productoTotal)