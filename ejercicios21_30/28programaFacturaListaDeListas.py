
precios = float(input("Introduzca precio : "))
unidades = float(input("Introduzca unidades de producto : "))

precioTotal = 0
totalUnidades = 0
cadenaImpresion = " "
_PRECIOS = 0
_UNIDADES = 1

def informaItem( precios, Unidades ):
    item = []
    item.append(precios)
    item.append(unidades)
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
    print(item[_PRECIOS], " € -", item[_UNIDADES], " unidades -  Total : ",item[_PRECIOS] * item[_UNIDADES], " € ")
          
print("                  ")
print(cadenaImpresion)
print("Total factura    : ",precioTotal)
print("Total de objetos : ",totalUnidades)