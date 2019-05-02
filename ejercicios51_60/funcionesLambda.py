from funcioneslvl1 import sumaTodos

print(sumaTodos(3, lambda x: x**3))
# lambda es funcion sin nombre o sin nombrar (autodefinida)
'''   es igual a :
doble = lambda x: x*2
print(sumaTodos(3,doble))   '''

triple = lambda x: x*3
print(sumaTodos(100,triple))
