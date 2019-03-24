mes01 = 31
mes02 = 28
mes03 = 31
mes04 = 30
mes05 = 31
mes06 = 30
mes07 = 31
mes08 = 31
mes09 = 30
mes10 = 31
mes11 = 30

nombre = input("Nombre : " )
print( "hola ",nombre)

edad = int(input("¿Cuantos años tienes? "))
year = int(input("¿Año actual? " ))
mes = int(input("¿En que mes estamos? "))
dia = int(input("¿En que dia estamos? ")) 

if mes == 1:
    transcurridos = dia
elif mes == 2:
    transcurridos = mes01 + dia
elif mes == 3: 
    transcurridos = mes01 + mes02 + dia
elif mes == 4:
    transcurridos = mes01 + mes02 + mes03 + dia
elif mes == 5:
    transcurridos = mes01 + mes02 + mes03 + mes04 + dia
elif mes == 6:
    transcurridos = mes01 + mes02 + mes03 + mes04 + mes05 + dia
elif mes == 7:
    transcurridos = mes01 + mes02 + mes03 + mes04 + mes05 + mes06 + dia
elif mes == 8:
    transcurridos = mes01 + mes02 + mes03 + mes04 + mes05 + mes06 + mes07 + dia
elif mes == 9:
    transcurridos = mes01 + mes02 + mes03 + mes04 + mes05 + mes06 + mes07 + mes08 + dia
elif mes == 10:
    transcurridos = mes01 + mes02 + mes03 + mes04 + mes05 + mes06 + mes07 + mes08 + mes09 + dia
elif mes == 11:
    transcurridos = mes01 + mes02 + mes03 + mes04 + mes05 + mes06 + mes07 + mes08 + mes09 + mes10 + dia
else:
    transcurridos = mes01 + mes02 + mes03 + mes04 + mes05 + mes06 + mes07 + mes08 + mes09 + mes10 + mes11 + dia
    
prob = transcurridos / 365 * 100

nacimiento = year - edad

print( "Naciste en ",nacimiento," con una probabilidad de ",prob )
print( " O en ",nacimiento -1," con una probabilidad de ",100-prob )
