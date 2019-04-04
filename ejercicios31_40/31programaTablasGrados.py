# formula de fahrenheit a centígrados o celsius : C = ( F - 32 ) * 5/9
# formula de centígrados a fahrenheit           : F = C * 9/5 + 32
def fahrenheitACentigrados(g):
    return (g - 32) * 5/9

def centigradosAFahrenheit(f):
    return f * 9/5 + 32

def centigrados(ini, fin):
    for grados in range(ini, fin+10, 10):
        print("{}ºF --> {}ºC".format(round(grados,2), round(fahrenheitACentigrados(grados),2)))

def fahrenheit(ini, fin):
    for grados in range(ini, fin+10, 10):
        print("{}ºF --> {}ºC".format(round(grados,2), round(centigradosAFahrenheit(grados),2)))
        
tipo = input("Salida (F/C): ")
entrada = tipo.upper()

if entrada == 'C':
    centigrados(0, 230)
elif entrada == 'F':
    fahrenheit(0, 100)
else:
    print("Tipo incorrecto")
    