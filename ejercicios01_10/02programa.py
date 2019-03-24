# calcular fecha ( de información )
fecha = int(input("Fecha actual :" ))
año = fecha.año
mes = fecha.mes
dia = fecha.dia

# P = dias transcurridos / 365 * 100

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
    transcurridos = 31 + 28 + 31 + 30 31 + dia
elif mes == 7:
    transcurridos = 31 + 28 + 31 + 30 31 + 31 + dia
elif mes == 8:
    transcurridos = 31 + 28 + 31 + 30 31 + 31 + 30 + dia
elif mes == 9:
    transcurridos = 31 + 28 + 31 + 30 31 + 31 + 30 + 31 + dia
elif mes == 10:
    transcurridos = 31 + 28 + 31 + 30 31 + 31 + 30 + 31 + 30 + dia
elif mes == 11:
    transcurridos = 31 + 28 + 31 + 30 31 + 31 + 30 + 31 + 30 + 31 + dia
else:
    transcurridos = 31 + 28 + 31 + 30 31 + 31 + 30 + 31 + 30 + 31 + 30 + dia 