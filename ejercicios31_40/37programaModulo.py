import math

tupla = ('A','B','C','D','F','E','F','G','H','I','J','K','L','LL','M')

indice = 0

while indice < len(tupla):
    if indice+1 == 3 or indice+1 == 6 or indice+1 == 9 or indice+1 == 12:
        mataletra()
        print(mataletra)
    indice += 1

while indice < len(tupla):
    if (indice + 1) % 3 == 0:
        print(tupla[indice])
    indice += 1
    