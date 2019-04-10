digitos16 = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','f')
angulo = 360/16

cadena = "Hola"

for caracter in cadena:
    valorHexadecimal = hex(ord(caracter))
    
#    print(valorHexadecimal) # python lo muestra : 0x'y el numero asignado'. para ver solo el numero:
    digito1 = valorHexadecimal[2]
    angulo1 = digitos16.index(digito1) * angulo
    digito2 = valorHexadecimal[3]
    angulo2 = digitos16.index(digito2) * angulo
    '''
    print(digito1)
    print(digito2) # para ver los 2 números del valor:
    segundopar = valorHexadecimal[2:4]
    print(segundopar)
    '''
    print(digito1, " - ", angulo1)
    print(digito2, " - ", angulo2)
    