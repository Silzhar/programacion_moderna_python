
enero = 31
febrero = 28
marzo = 31
abril = 30
mayo = 31
junio = 31
julio = 30
agosto = 31
septiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

totalDias = 0

nombre = input("Nombre : ")
print(" Hola ",nombre)

edad = int(input("¿cuantos años tienes? "))
fecha = int(input("Año actual : "))
mes = int(input("Mes actual : "))
dia = int(input("Día actual : "))

if mes==1 :
    totalDias =  dia
elif mes == 2 :
    totalDias = dia + enero
elif mes == 3 :
    totalDias = dia + febrero
elif mes == 4 :
    totalDias = dia + marzo
elif mes == 5 :
    totalDias = dia + abril
elif mes == 6 :
    totalDias = dia + mayo
elif mes == 7 :
    totalDias = dia + junio
elif mes == 8 :
    totalDias = dia + julio
elif mes == 9 :
    totalDias = dia + agosto
elif mes == 10 :
    totalDias = dia + septiembre
elif mes == 11 :
    totalDias = dia + octubre
elif mes == 12 :
    totalDias = dia + noviembre

nacimiento = fecha - edad
prob = totalDias / 365 * 100

print(nombre, ", has nacido en el año ",nacimiento, " con una probabilidad de ",round(prob, 2))
print("O en el año ",nacimiento - 1, " con una probabilidad de ",round((100 - prob), 2))

