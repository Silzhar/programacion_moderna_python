
precios = float(input("Introduzca precio : "))
unidades = float(input("Introduzca unidades de producto : "))

precioTotal = 0
totalUnidades = 0
cadenaImpresion = " "

listaPrecios = []
listaUnidades = []

while precios > 0 or unidades > 0 :
    costeTotal = precios * unidades
    listaPrecios.append(precios)
    listaUnidades.append(unidades)
    
    # cadenaImpresion += str(precios) + " € -" + str(unidades) + " unidades - " + str(costeTotal) + " €\n "
    # es = : cadenaImpresion += "{} € - {} unidades - {} €\n".format(precios,unidades,costeTotal)
    
    print(precios," € - ", unidades, " - ",costeTotal, " € ")
    
    totalUnidades += unidades # totalUniades = TotalUnidades + unidades ( es lo mismo )
    precioTotal += costeTotal
    
    precios = float(input("Introduzca precio : "))
    unidades = float(input("Introduzca unidades de producto : "))

for precio, unidades in zip(listaPrecios, listaUnidades):
    print(precios, " € - ", unidades," unidades - ", precios * unidades," € ")
    
print("                  ")
print(cadenaImpresion)
print("Total factura    : ",precioTotal)
print("Total de objetos : ",totalUnidades)