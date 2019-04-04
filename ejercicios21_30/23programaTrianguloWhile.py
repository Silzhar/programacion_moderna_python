# calcular area triangulo con WHILE
def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

base = input(" Base del triángulo : ")
while not esDecimal(base):
    print(base, "debe ser un número ")
    base = input(" Base del triángulo : ")
    
altura = input(" Altura del triángulo : ")
while not esDecimal(altura):
    print(altura, "debe ser un número ")
    altura = input(" altura del triángulo : ")

base = float(base)
altura = float(altura)
area = base * altura / 2

print(" El área del triángulo es ",area)

