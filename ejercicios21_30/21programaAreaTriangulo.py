# ejercicio calcular area de triangulo
def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
        

base = input("Introducir base de triángulo :  ")
if esDecimal(base):
    base = float(base)
else:
    print(base, " debe ser un número ")
    quit()
    
    
altura = input("Introducir altura de triangulo :  ")
if esDecimal(altura):
    altura = float(altura)
else:
    print(altura, " debe ser un número ")
    quit()
    
area = base * altura / 2

print("El área del triángulo es :  ",round(area,2))

