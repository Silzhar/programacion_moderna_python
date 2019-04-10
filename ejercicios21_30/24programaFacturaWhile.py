# ejercicio calculo total de factura
precioTotal = 0
totalUnidades = 0
precios = input("Introduzca precio : ")
unidades = input("Introduzca unidades de producto : ")

def productos(cantidades):
    try:
        float(cantidades)
        return float(cantidades)
    except:
        return False
  
while productos(precios) == False:
    print(precios,"Es una cadena,es preciso introducir un número")
    precios = input("Introduzca precio : ")
    productos(precios)
  
while productos(unidades) == False:
    print(unidades,"Es una cadena,es preciso introducir un número")
    unidades = input("Introduzca unidades de producto : ")
    productos(unidades)

while productos(precios) > 0 or roductos(unidades) > 0 : 
    precios = float(precios)
    unidades = float(unidades)
    precioTotal = precioTotal + precios * unidades
    precios = input("Introduzca precio : ")
    unidades = input("Introduzca unidades de producto : ")
    totalUnidades += 1

print("Factura total  :",round(precioTotal, 2))