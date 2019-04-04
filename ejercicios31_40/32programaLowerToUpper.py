def upper(cadena):
    resultado = " "
    
    for caracter in cadena :
        codigoCaracter = ord(caracter) # ord pasa el caracter a valor numérico
        if codigoCaracter >= 97 and codigoCaracter <=122 :
            codigoMays = codigoCaracter - 32
            caracterMays = chr(codigoMays) # chr pasa el valor numérico a caracter
            resultado = resultado + caracterMays
        else:
            resultado += caracter
            
    return resultado
        
entrada = input("Escribe en minúsculas : ")
print("En mayúsculas es : ",upper(entrada))

def lower(cadena):
    resultado = " "
    
    for caracter in cadena :
        codigoCaracter = ord(caracter) # ord pasa el caracter a valor numérico
        if codigoCaracter >= 65 and codigoCaracter <=90 :
            codigoMays = codigoCaracter + 32
            caracterMays = chr(codigoMays) # chr pasa el valor numérico a caracter
            resultado = resultado + caracterMays
        else:
            resultado += caracter
            
    return resultado
        
entrada2 = input("Escribe en mayúsculas : ")
print("En minúsculas es : ",lower(entrada2))