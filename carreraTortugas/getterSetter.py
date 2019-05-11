class claseConGetterySetter(): #  getter lee y setter fija 
    def __init__(self):
        self.__propiedad_privada = None    #atributo privado
    
    def setPopiedadPrivada(self, valor=None):   # este es setter
        self.__propiedad_privada = valor
        
    def getPropiedadPrivada(self):         # este es getter
        return self.__proppiedad_privada  
    
    def propiedadPrivada(self, valor):  # esto es getter y setter a la vez
        if valor==None:
            return self.__propiedad_prpivada  # actua como getter
        else:
            self.__propiedad_privada = valor    # actua como setter
        
    def __str__(self):
        return "claseConGetterySetter con propiedadPrivada -> {}".format(self.propiedad_privada)
        
if __name__ =='__main__':
    c = claseConGetterySetter()
    