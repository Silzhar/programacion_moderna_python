notas = ( 2, 4, 6, 8 )

suma = 0
for indice in range( len( notas )):
    suma = suma + notas[indice]
     
media = suma / len(notas)

print( " Número de items : ",len(notas) )
print( " Nota media      : ",media)
print( " nota total      : ",suma )

print("    ")
# optimizando mas lo anterior :
notas = ( 2, 4, 6, 8 )

suma = 0
longitudNotas = len(notas)
for indice in range( 0, longitudNotas):
    suma = suma + notas[indice]
     
media = suma / longitudNotas

print( " Número de items : ",longitudNotas )
print( " Nota media      : ",media)
print( " nota total      : ",suma )