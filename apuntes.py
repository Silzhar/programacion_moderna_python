import platform

print(platform.python_version()) # comprobar version de python

a = ["..","1..","2..","3..","4.."]
b = a  # asigna 'b' a la lista,si cambia algo de la lista llamar a 'a' o 'b' es igual
c = a[:] # clona la lista para 'c',si cambia algo de la lista en 'a' en 'c' no cambia

cadena1 = "hola "
cadena2 = cadena1
cadena3 = "Buenos dias"
cadena1 = cadena1+" buenas" # añadir a cadenas,pasa como con listas/tuplas
---------------------------------------------------------------------------------
7 // 2 # da el cociente de la division
7 % 2 # da el resto,con el resto calculamos si un numero es par o impar o buscamos resto 0 o resto 1
2**3 # = 8 , 2 elevado a 3
16**0.5 # = 4 , calcula la raiz                             % este simbolo se llama modulo
---------------------------------------------------------------------------------
def imprimeCosas(*listaCosas):
    for item in listaCosas:
        print(item)
imprimeCosas('cosa 1','cosa 2','cosa 3','cosa 4') # consigue un numero variable de items

def imprimeConDiccionario(**diccionarioParametros):
    if 'line' in diccionarioParametros:
        print('Posicionar en linea',diccionarioParametros['line'])
    else:
        print('No hay line')
imprimeConDiccionario(contenido='la cosa', line=3, column=5)    # posiciones de clave y valor

todo.split('\n') # separa en una lista
---------------------------------------------------------------------------------
                                           # 4 enteros uno del punto y 2 decimales,total 7
  # :3d ,poner un entero con 3 digitos   :7.2f en numero de longitud 7 poner 2 decimales(f de float)
print("Entradas de bebé .....:{:3d} -  {:7.2f}".format(numEntradasBebe, numEntradasBebe * preciosE['bebe']))
---------------------------------------------------------------------------------
numEntradasbebe += int(entradas[0])
#numEntradasbebe es un entero,entradas es un string y para sumarlos con el int() tranformamos el string a entero
---------------------------------------------------------------------------------