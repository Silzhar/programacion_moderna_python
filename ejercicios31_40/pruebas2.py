diasMes = [ 31 ,28, 31, 30, 31, 31, 30, 31, 30, 31, 30 ]

totalDias = 0
indice = 0

nombre = input("NOMBRE : ")
print("Hola ",nombre)
edad = int(input("¿Cuantos años tienes? "))
fecha = int(input("¿Año actual? "))
mes = int(input("¿En que mes estamos? "))
dia = int(input("¿En que dia estamos? "))

while indice < mes - 1 :
    totalDias = totalDias + diasMes[indice]
    indice = indice + 1

totalDias = totalDias + dia
nacimiento = fecha - edad
prob = totalDias / 365 * 100

print(nombre, ", has nacido en el año ",nacimiento, " con una probabilidad de ",round(prob, 2))
print("O en el año ",nacimiento - 1, " con una probabilidad de ",round((100 - prob), 2))
