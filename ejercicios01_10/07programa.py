diasMes = ( 31, 28, 31, 30, 31, 31, 30, 31, 30 )

nombre = input("Nombre : " )
print( "hola ",nombre)

edad = int(input("¿Cuantos años tienes? "))
year = int(input("¿Año actual? " ))
mes = int(input("¿En que mes estamos? "))
dia = int(input("¿En que dia estamos? "))

transcurridos = 0
indice = 0

while indice < mes - 1:
    transcurridos = transcurridos + diasMes[indice]
    indice = indice + 1 

transcurridos = transcurridos + dia

prob = transcurridos / 365 * 100

nacimiento = year - edad

print( "Naciste en ",nacimiento," con una probabilidad de ",prob )
print( " O en ",nacimiento -1," con una probabilidad de ",100-prob )