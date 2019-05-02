class Doggy():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def ladrar(self):
        if self.peso == None:
            print("perro fantasma !")
        

class Dog():   # clase con su nombre ,atributos (nombre ,edad,peso) y metodos (ladrar)
    def __init__(self, nombre, edad, peso): 
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):           #por convencion el primer parametro de la propia clase
        if self.peso >=8:           #si incluimos parametros hemos de pedirlo
            print('GUAUU ,GUAUU')    # en el print y en la llamada
        else:                        #  *l (listas) **d (diccionarios) 
            print(' Guau guauuu')    # y poniendo la coma(,) posicionales o por defecto
        
    def __str__(self):
        return 'Soy el perro {}, edad: {}, peso: {}'.format(self.nombre, self.edad, self.peso)
    
''' en Shell  :
>>> jash = Dog('Jash', 14, 3)
>>> jash.ladrar()
 Guau guauuu                '''

class DogAsistant(Dog): # subclase 
    def __init__(self,nombre, edad, peso, amo):
        Dog.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__work = False
        
    def __str__(self):
        return 'Perro de asistencia de {}'.format(self.amo)
    
    def pasear(self):
        print('{} ayudo a pasear a {}'.format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.work:
            print('...trabajando no puedo ladrar')
        else:
            Dog.ladrar(self)
    
    def work(self, valor=None): # tipo getter ,setter 
        if valor == None:
            return self.__work
        else:
            self.__work = valor
  
'''     PROBLEMA :
>>> cujo = DogAsistant('Cujo', 4, 32 ,'Zhatu')
>>> cujo.work()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'bool' object is not callable                 '''


        
    