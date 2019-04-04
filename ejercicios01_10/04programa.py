
nombre = input("Nombre : " )
print( "hola ",nombre)

edad = int(input("¿Cuantos años tienes? "))
year = int(input("¿Año actual? " ))
mes = int(input("¿En que mes estamos? "))
dia = int(input("¿En que dia estamos? ")) 

if mes == 1:
    transcurridos = dia
elif mes == 2:
    transcurridos = 31 + dia
elif mes == 3: 
    transcurridos = 31 + 28 + dia
elif mes == 4:
    transcurridos = 31 + 28 + 31 + dia
elif mes == 5:
    transcurridos = 31 + 28 + 31 + 30 + dia
elif mes == 6:
    transcurridos = 31 + 28 + 31 + 30 + 31 + dia
elif mes == 7:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 31 + dia
elif mes == 8:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 31 + 30 + dia
elif mes == 9:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 31 + 30 + 31 + dia
elif mes == 10:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia
elif mes == 11:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + dia
else:
    transcurridos = 31 + 28 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 30 + dia
    
prob = (transcurridos / 365) * 100

nacimiento = year - edad

print( "Naciste en ",nacimiento," con una probabilidad de ",round(prob ,2))
print( " O en ",nacimiento -1," con una probabilidad de ",100-round(prob, 2))
