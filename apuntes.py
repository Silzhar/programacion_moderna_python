import platform

print(platform.python_version()) # comprobar version de python

a = ["..","1..","2..","3..","4.."]
b = a  # asigna 'b' a la lista,si cambia algo de la lista llamar a 'a' o 'b' es igual
c = a[:] # clona la lista para 'c',si cambia algo de la lista en 'a' en 'c' no cambia

cadena1 = "hola "
cadena2 = cadena1
cadena3 = "Buenos dias"
cadena1 = cadena1+" buenas" # añadir a cadenas,pasa como con listas/tuplas

7 // 2 # da el cociente de la division
7 % 2 # da el resto,con el resto calculamos si un numero es par o impar o buscamos resto 0 o resto 1
2**3 # = 8 , 2 elevado a 3
16**0.5 # = 4 , calcula la raiz                             % este simbolo se llama modulo