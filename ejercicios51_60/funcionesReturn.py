
# devolver el maximo de una lista
def max(*l):  # *l recorre la lista y la devuelve como un array
    if len(l) == 0:
        return 0
    
    m = l[0] #  m es el maximo
    
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]        
    return m

# devolver el minimo de una lista 
def min(*l):
    if len(l) == 0:
        return 0
    
    m = l[0] #  m es el maximo
    
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]        
    return m

# hacer media de una lsita
def media(*l):
    if len(l) == 0:
        return 0
    
    suma = 0
    for valor in l:
        suma += valor
    return suma / len(l)

funciones = {
    'max': max,
    'min': min,
    'mid': media }

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    return None

        