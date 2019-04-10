import platform

print(platform.python_version())

    
print("--------Cálculo de facturas--------") 
print("Introcuzca precio y unidades del producto,para salir introduzca 0")
def llamada( coste, objetos):
    precios = input("Introduzca precio : ")
    unidades = input("Introduzca unidades de producto : ")
    return precios, unidades
    
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

precios = float(precios)
unidades = float(unidades)

while precios > 0 or unidades > 0 :
    productos(precios)
    productos(unidades)
    precios = float(precios)
    unidades = float(unidades)
    precioTotal = precioTotal + precios * unidades
    precios = input("Introduzca precio : ")
    unidades = input("Introduzca unidades de producto : ")
    unidades += 1
          
print("Factura total  :",round(precioTotal, 2))

# version 2º

print("Factura total  :",round(precioTotal, 2),"Total de objetos : ",totalUnidades)
print("--------Cálculo de facturas--------") 
print("Introcuzca precio y unidades del producto,para salir introduzca 0")
precios = float(input("Introduzca precio : "))
unidades = float(input("Introduzca unidades de producto : "))
precioTotal = 0
totalUnidades = 0

def llamada( coste, objeto):
    precios = float(input("Introduzca precio : "))
    unidades = float(input("Introduzca unidades de producto : "))
    return precios, unidades

    
'''    
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
'''
llamada(precios, unidades)

while precios > 0  or unidades > 0:
    llamada(precios, unidades)
    precioTotal = precioTotal + precios * unidades
    if precios == 0 and unidades == 0 :
        print("Factura total  :",round(precioTotal, 2))
    totalUnidades += 1
