class Objeto():
    __atributoPrivado = None
    atributoPublico = None
    
    def __init__(self):  # constructor oblogatorio para clases
        self.__atributoPrivado = 0
        self.atributoPublico = 14

# para acceder al atributo privado :
    
    def getAtributoPrivado(self):         # getter
        return self.__atributoPrivado 
    
    def setAtributoprivado(self, valor):  # setter
        self.__atributoPrivado = valor
        
    def atributoPrivado(self, valor=None):  # unir getter y setter
        if valor == None:
            return self.__atributoPrivado
        else:
            self.__atributoPrivado = valor
        
        