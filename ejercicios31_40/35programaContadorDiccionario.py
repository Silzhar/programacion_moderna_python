texto = "Prueba contador de frecuencia repetecion de letras "

frecuencias = dict()

for caracter in texto :
    if caracter in frecuencias: # if frecuencias.get(caracter) != None: (son lo mismo)
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1
        
for letra in frecuencias.keys():
    print(letra, " -- ",frecuencias[letra])
    