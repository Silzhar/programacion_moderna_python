# ejercicio calcular area de triangulo solucion con IF para cerrar sin QUIT
def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
        

base = input("Introducir base de triángulo :  ")
altura = input("Introducir altura de triangulo :  ")

if esDecimal(base):
    base = float(base)
    
    if esDecimal(altura):
        altura = float(altura)
    
        area = base * altura / 2
        print("El área del triángulo es :  ",round(area,2))
    
    else:
        print(altura, " debe ser un número ") 
else:
    print(base, " debe ser un número ")
    
