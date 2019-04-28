from programaConfig import preciosE
    
fEntradas = open("transacciones.txt","r")

numEntradasBebe = 0
numEntradasNiño = 0
numEntradasAdulto = 0
numEntradasJubilado = 0

linea = fEntradas.readline()
totalEntradas = 0
totalPrecio = 0

while linea != '':
    entradas = linea.split(',') 
    numEntradasbebe += int(entradas[0]) # numEntradasbebe es un entero,entradas es un string y 
    nunEntradasNiño += int(entradas[1])   # para sumarlos con el int() tranformamos el string a entero
    numEntradasAdulto += int(entradas[2])
    nunEntradasjubilado += int(entradas[3])
    
    totalEntradas = totalEntradas + int(entradas[0])
    totalEntradas = totalEntradas + int(entradas[1])
    totalEntradas = totalEntradas + int(entradas[2])
    totalEntradas = totalEntradas + int(entradas[3])
       
    linea = fEntradas.readline()           # 4 enteros uno del punto y 2 decimales,total 7
  # :3d ,poner un entero con 3 digitos   :7.2f en numero de longitud 7 poner 2 decimales(f de float)
print("Entradas de bebé .....:{:3d} -  {:7.2f}".format(numEntradasBebe, numEntradasBebe * preciosE['bebe']))
print("Entradas de niño .....:{:3d} -  {:7.2f}".format(numEntradasNiño, numEntradasNiño * preciosE['niño']))
print("Entradas de adulto ...:{:3d} -  {:7.2f}".format(numEntradasAdulto, numEntradasAdulto * preciosE['adulto']))
print("Entradas de jubilado .:{:3d} -  {:7.2f}".format(numEntradasJubilado, numEntradasJubilado * preciosE['jubilado']))

print("\n Total : {:3d} -  {:7.2f}€".fotmat(totalEntradas,
                                            numEntradasBebe * preciosE['bebe']+numEntradasNiño * preciosE['niño']+\
                                            numEntradasAdulto * preciosE['adulto']+numEntradasJubilado * preciosE['jubilado']))