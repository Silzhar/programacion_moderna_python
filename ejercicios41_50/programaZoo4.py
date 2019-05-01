import programaPantalla
import programaFunciones
from programaConfig import preciosE, totales, entradasQ
#de este modo no hay que buscar y poner como en programaFunciones.tipoEntrada(edad)


def main():
        programaFunciones.printScreen()
        edad = programaFunciones.pedirEdad()
        precioTotal = 0
        #linea = 4

        while edad != 0:
            tipoE = programaFunciones.tipoEntrada(edad)
            precioE = preciosE[tipoE]
            totales[tipoE] += 1
            
            programaPantalla.Print(totales[tipoE],entradasQ[tipoE]['cantidad'][0],entradasQ[tipoE]['cantidad'][1])
            
            programaPantalla.Print("{:7.2f}€".format(totales[tipoE]*precioE), \
                                   entradasQ[tipoE]['precioA'][0],entradasQ[tipoE]['precioA'][1])
            # \ la barra hace que continue abajo
            # la linea anterior suple a las 3 siguientes :
   #         print(totales[tipoE])        
   #         programaPantalla.locate(entradasQ[tipoE]['precioA'][0],entradasQ[tipoE]['precioA'][1])
   #         print("{:7.2f}€".format(totales[tipoE]*precioE))
            
            precioTotal += precioE
            programaPantalla.Format(1,37, 40)
            programaPantalla.Print("{:7.2f}€".format(precioTotal),9, 19)
            # sustitutye a las 2 siguientes 
   #         programaPantalla.locate(9, 19)
   #         print("{:7.2f}€".format(precioTotal))
            programaPantalla.Reset()
            
            edad = programaFunciones.pedirEdad()
        # registro de datos                            a+ de append ,agregar datos
        eEntradas = open('transacciones.txt','a+') # w+ de write para fichero de escritura,al poner el + lo crea
        transaccion = "{},{},{},{}".fotmat(totales['bebe'],totales['niño'],totales['adulto'],totales['jubilado'])
        fEntradas.write(transaccion)
        eEntradas.close()
        
        programaPantalla.locate(11 , 1)

main()
    
'''
    if precioE == 0:
        programaPantalla.locate(4, 15)
        print(1)
        programaPantalla.locate(4, 19)
        print(precioE)
        
    if precioE == 14:
        lprogramaPantalla.locate(5, 15)
        print(1)
        programaPantalla.locate(5, 19)
        print(precioE)
        
    if precioE == 23:
        programaPantalla.locate(6, 15)
        print(1)
        programaPantalla.locate(6, 19)
        print(precioE)
    if precioE == 18:
        lprogramaPantalla.locate(7, 15)
        print(1)
        programaPantalla.locate(7, 19)
        print(precioE)
        
    programaPantalla.locate(linea, 1)
    linea += 1
    precioTotal += precioE
    
    edad = pedirEdad()

programaPantalla.locate(linea, 12)
print("Total :{}".format(precioTotal))
'''

'''
while edad != 0:
    precioE = precioEntrada(edad)
    if precioE == 0:
        linea = 4
        entradasB += 1
        print("Precio entrada :{}\tEntradas :{}".format(precioE, entradasB))
    if precioE == 14:
        linea = 5
        entradasN += 1
        print("Precio entrada :{}\tEntradas :{}".format(precioE, entradasN))
    if precioE == 23:
        linea = 6
        entradasA += 1
        print("Precio entrada :{}\tEntradas :{}".format(precioE, entradasA))
    if precioE == 18:
        linea = 7
        entradasJ += 1
        print("Precio entrada :{}\tEntradas :{}".format(precioE, entradasJ))
        
    programaPantalla.locate(linea, 1)
    linea += 1
    precioTotal += precioE
    
    edad = pedirEdad()
    
'''

