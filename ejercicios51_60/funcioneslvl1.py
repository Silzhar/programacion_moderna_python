def suma(limit):
    resultado = 0
    avance = 0
    for i in range(0,limit):
        resultado += 1
        avance += resultado 
    return  avance

print(suma(100))

def sumaCuadrado(limit):
    resultado = 0
    for i in range(limit+1):
        resultado += i*i
    return resultado

print(sumaCuadrado(3))
#########################################################
def normal(i):
    return i

def cuadrado(x):
    return x * x

def sumaTodos(limit, f):
    resultado = 0
    for i in range(limit+1):
        resultado += f(i)
    return resultado

print(sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))
