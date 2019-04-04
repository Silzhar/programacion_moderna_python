texto = "Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda."\
"Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera."\
"Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza."\
"Quieren decir que tenía el sobrenombre de Quijada, o Quesada, que en esto hay alguna diferencia en los autores que deste caso escriben; aunque por conjeturas verosímiles se deja entender que se llamaba Quijana"

'''
palabras = 0

for caracter in texto :
    if caracter == " " :
        palabras += 1

if caracter != " ":
    palabras += 1 # para contar el ultimo espacio y la ultima palabra
    
print(palabras)
'''
palabras = 0
posicion = 0

while posicion < len(texto):
    if texto[posicion] == " " and texto[posicion - 1] != " ":
        palabras += 1
    posicion += 1

if texto[posicion - 1] != " ":
    palabras += 1
  
print(palabras)
    