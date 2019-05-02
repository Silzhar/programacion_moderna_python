# funciones recursivas 
def retrocontador(entrada):
    print('{},'.format(entrada),end= '')
    if entrada == 0:
        return
    retrocontador(entrada - 1)
    ''' otra opcion  :   (si no es igual != ({pcion 1}o es mayor {> 0} a 0 lo volvemos a llamar)
     if entrada > 0 : 
          retrocontador(entrada - 1)'''
    
retrocontador(10)

def sumatorio(n): # sumatorio recursivo
    if n > 0:
        return n + sumatorio(n - 1)
    else:
        return 0
    
print(sumatorio(4))