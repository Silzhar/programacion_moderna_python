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

transcurridos = 0

if mes > 1:
    transcurridos = transcurridos + mes01
if mes > 2:
    transcurridos = transcurridos + mes02 
if mes > 3: 
    transcurridos = transcurridos + mes03
if mes > 4:
    transcurridos = transcurridos + mes04
if mes > 5:
    transcurridos = transcurridos + mes04
if mes > 6:
    transcurridos = transcurridos + mes05
if mes > 7:
    transcurridos = transcurridos + mes06
if mes > 8:
    transcurridos = transcurridos + mes07
if mes > 9:
    transcurridos = transcurridos + mes08
if mes > 10:
    transcurridos = transcurridos + mes09
if mes > 11:
    transcurridos = transcurridos + mes10
else:
    transcurridos = transcurridos + mes11

transcurridos = transcurridos + dia

prob = transcurridos / 365 * 100

nacimiento = year - edad

print( "Naciste en ",nacimiento," con una probabilidad de ",prob )
print( " O en ",nacimiento -1," con una probabilidad de ",100-prob )

