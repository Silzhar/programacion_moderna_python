import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):   # constructor 
        self.custome = pygame.image.load("termometro_azul.jpg")
        
    def  convertir(self, grados, toUnidad):
        resultado = 0 
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == ' C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        
        return "{:9.2f}".format(resultado)
    
       
class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad="C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("celsiusBarStatus.png"))
        self.__customes.append(pygame.image.load("fahrenheitBarSatus.png"))
        
        self.__tipoUnidad = unidad
        
    def Custome(self):
        if self.__tipoUnidad == "F":
            return self.__customes[0]
        else:
            return self.__customes[1]
        
    def change(self):
        if self.__tipoUnidad == 'F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
            
    def unidad(self):  # para acceder al metodo privado self.__tipoUnidad
        return self.__tipoUnidad  
        
                         
class NumberInput():
    __value = 0
    __strValue = ""  # para pasar valor a cadena y renderizar
    __position = [0, 0]
    __size = [0, 0]
    __pointsCount = 0
    
    
    def __init__(self, value=0):
        self.__font = pygame.font.SysFont('ubuntu', 24)
        # self. llama al atributo del objeto, llama a toda la clase 
        self.value(value)   # evitar entrada de cadenas
        
        ''' otra  entrada con mismo resultado : 
            try:
                self.__value = int(value)
                self.__strValue = str(value)
            except:
                pass      '''
         
    def on_event(self,event ):
                if event.type == KEYDOWN:
                    if event.unicode.isdigit() and len(self.__strValue) < 9 or (event.unicode == '.' and self.__pointsCount == 0): #  es = a :if event.unicode in '01234567890':
                          self.__strValue += event.unicode 
                          self.value(self.__strValue)
                          if event.unicode == '.':
                              self.__pointsCount += 1
                    elif event.key == K_BACKSPACE: # para borrar 
                        if self.__strValue[-1] == '.':
                            self.__pointsCount -= 1
                        self.__strValue = self.__strValue[:-1] # =  [0:-1],  el 0 no suele ponerse 
                        self.value(self.__strValue) # = a self.value =int(self.__strValue) pero si se queda vacio da error,del primer modo no
    

    def render(self): # getter pasa sacar argumentos 
        textBlock = self.__font.render(self.__strValue, True , (255, 255, 255))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock) 
        '''
        return {
                "fondo": rect,
                "texto": textBlock
                }               // igual al anterior return      '''
          
      
    def value(self, val=None): # transformar la entrada en cadena
        if val==None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
            except:
                pass
            
    def width(self, val=None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
            
    def height(self, val=None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
    
    def size(self, val=None):
        if  val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass

    def posX(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
            
    def posY(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
    
    def pos(self, val=None):
        if  val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass


class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
       # self.__screen.fill((255, 255, 255))
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((110, 58)) # posicion del rectangulo
        self.entrada.size((133, 28)) # tamaño del rectangulo
        
        self.selector = Selector()
        
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event)
                '''  entradas con mismo resultado 
                if event.type == KEYDOWN:
                    if event.unicode in '01234567890:
                    if event.isdigit()
                    if event.unicode =='1' or event.unicode == '2'   '''
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad )
                    self.entrada.value(temperatura)
            
            # pintar fondo de pantalla 
            self.__screen.fill((255, 255, 255))
            
            # pintar termometro en posicion
            self.__screen.blit(self.termometro.custome, (-40, 120))
            
            # pintar cuadro de texto
            text = self.entrada.render() # rectangulo, foto de texto y asignacion a text
            pygame.draw.rect(self.__screen, (0, 0, 255), text[0]) # crear rectangulo( pos y tamaño)
            self.__screen.blit(text[1],self.entrada.pos()) # pintar foto de texto (text[1])
            
            # pintar selector :
            self.__screen.blit(self.selector.Custome(),( 130, 153))
            
            pygame.display.flip()


if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()
    

