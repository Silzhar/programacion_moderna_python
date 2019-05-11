import turtle
import random

class Circuito():
    corredores = []
    __posStartY = ( -60, -20, 20 , 60) # position start
    __colorTurtle = ('yellow','blue','red','purple' )
    
    def __init__(self, width, height):      
        self.__screen = turtle.Screen() # modulo privado ! --instancia --
        self.__screen.setup( width, height)
        self.__screen.bgcolor('lightgreen')
        self.__starLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.__createRunners()
    
    def __createRunners(self): 
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__starLine, self.__posStartY[i])  # set pos,establece la posicion
            
            
            self.corredores.append(new_turtle)
            
    def competir(self):
        
        winner = False
        
        while not winner:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    winner = True                                # este parentesis abre la funcion de color,fuincion de primera clase
                    print("El ganador es {}".format(tortuga.color()[0]))
                    break # para finalizar cuando llegue la primera y no terminar el bucle
        
        
if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.competir()
    
        
        