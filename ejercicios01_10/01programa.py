
nombre = input("Nombre : " )
print( "hola ",nombre)

edad = int(input("¿Cuantos años tienes? "))
year = int(input("¿Año actual? " ))
cumplidos = input("¿Cumpliste ya los años? " )

if cumplidos == "Si" or "si":
    nacimiento = year - edad
else:
    nacimiento2 = year -1 - edad

print(nombre, " naciste en ",nacimiento)


    


    