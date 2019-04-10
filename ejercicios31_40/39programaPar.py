def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

# toda la funcion anterior es igual a la siguiente :
def par(n):
    return n % 2 == 0

# define el 2º parametro de modo que si no lo piden no lo ejecuta
def par(n, swPrint = False):
    if swPrint:
        print("El número es el ",n)
    return n % 2 == 0