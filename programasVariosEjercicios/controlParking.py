demos = []
parking = []
camion = []
totalCoches = 0

print("Tipo de entrada. demo, parking , camion .")
print("Para salir del programa escriba en - entrada - : cerrar ")

def entrada():
    tipoEntrada = input("Tipo de entrada : ")
    coche = input("Modelo de vehículo :")
    matricula = input("Matrícula :")
        
    if tipoEntrada == "demo":
        demos.append(coche)
        demos.append(matricula)
        totalCoches = totalCoches + 1
        
    if tipoEntrada == "parking":
        parking.append(coche)
        parking.append(matricula)
        totalCoches = totalCoches + 1
        
    if tipoEntrada == "camion":
        camion.append(coche)
        camion.append(matricula)
        totalCoches = totalCoches + 1
    else:
        print("Total de vehículos ",totalCoches)
        print("total coches demos :",len(demos))
        print("total coches en parking :",len(parking))
        print("total coches para camion :",len(camion))
        
    


entrada()

'''
while entrada() != tipoEntrada :
    if tipoEntrada == "demo":
        demos.append(coche)
        demos.append(matricula)
        
    if tipoEntrada == "parking":
        parking.append(coche)
        parking.append(matricula)
        
    if tipoEntrada == "camion":
        camion.append(coche)
        camion.append(matricula)
    else:
        print("total coches demos :",len(demos))
        print("total coches en parking :",len(parking))
        print("total coches para camion :",len(camion))
    totalCoches = totalCoches + 1
    
print("Total de vehículos ",totalCoches)

    
'''
