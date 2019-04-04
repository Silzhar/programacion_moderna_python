
precios = float(input("Introduzca precio : "))
unidades = float(input("Introduzca unidades de producto : "))

precioTotal = 0
totalUnidades = 0
_PRECIOS = 0
_UNIDADES = 1

def informaItem( precios, Unidades ):
    item = dict()
    item['precios'] = precios
    item['unidades'] = unidades
    return item

listaLineasFacturas = []

while precios > 0 or unidades > 0 :
    costeTotal = precios * unidades
    item = informaItem( precios, unidades )
    listaLineasFacturas.append(item)
    
    totalUnidades += unidades # totalUniades = TotalUnidades + unidades ( es lo mismo )
    precioTotal += costeTotal
    
    precios = float(input("Introduzca precio : "))
    unidades = float(input("Introduzca unidades de producto : "))
    
# cadenaImpresion += str(precios) + " € -" + str(unidades) + " unidades - " + str(costeTotal) + " €\n "
# es = : cadenaImpresion += "{} € - {} unidades - {} €\n".format(precios,unidades,costeTotal)

for item in listaLineasFacturas:
    print(item['precios'], " € -", item['unidades'], " unidades -  Total : ",item['precios'] * item['unidades'], " € ")
          
print("                  ")
print("Total factura    : ",precioTotal)
print("Total de objetos : ",totalUnidades)

print("   \nTotal factura    :\t{:.2f}\nTotal de objetos : \t{}".format(precioTotal, totalUnidades))
# .format formatea la salida , primera llamada al primer hueco {} y 2ª al segundo hueco {}
# \t{} la t es tabulador //  {:.2f} : es el formato .2f es float y los decimales que se quieren