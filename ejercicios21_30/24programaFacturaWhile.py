# ejercicio calculo total de factura
precios = 0
unidades = 0
precioTotal = 0
totalUnidades = 0
print("--------Cálculo de facturas--------") 
print("Introcuzca precio y unidades del producto,para salir introduzca 0")
precios = input("Introduzca precio : ")
unidades = input("Introduzca unidades de producto : ")

# bloque comprobación de datos numéricos
def productos(cantidades):
    try:
        float(cantidades)
        return True
    except:
        return False
    
def precio(cantidad):       
    while not productos(precios):
        print(precios,"Es preciso introducir un número")
        precios = input("Introduzca precio : ")
    precios = float(precios)
    return precios

def unidad(totales):
    while not productos(unidades):
        print(unidades,"Es preciso introducir un número")
        unidades = input("Introduzca unidades de producto : ")
    unidades = float(unidades)
    return unidades

while precio(precios) > 0 or unidad(unidades) > 0 :
    productos(precios)
    productos(unidades)
    precios = float(precios)
    unidades = float(unidades)
    precioTotal = precioTotal + precios * unidades
          
print("Factura total  :",round(precioTotal, 2))


    
    
    
    


