import pygame, sys
import random

class Runner():
    
    __customes = ("orangeMonster", "purpleMonster", "greenMonster", "yellowMonser")
    
    def __init__(self, x=0, y= 0):
        
        ixCustome = random.randint(0, 4)
        self.custome = pygame.image.load("{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
        
    def avanzar(self):
        self.position[0] += random.randint(1, 2)

class Game():
    runners = []
    __posY = (40, 120, 200, 280) # start position mosters 
    __names = ("Orangeitter", "Purpleittor", "Greencore", "Yellówghotus")
    __startLine = 4
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480)) # width, height
        self.__background = pygame.image.load('racing_road.png')
        pygame.display.set_caption("Carrera !")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
      #  self.runners.append(Runner(self.__starline, 240))
    
    
    def competir(self):
        gameOver = False   # comprobar eventos
        while not gameOver:
            for event in pygame.event.get(): # traer eventos de pygame
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for activeRunner in self.runners: # actualizacion de eventos
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                     print("{} Ha ganado !".format(activeRunner.name))
                     gameOver = True
                
            self.__screen.blit(self.__background, (0, 0)) # refresh background
            
            '''
            self.__screen.blit(self.__background,(0, 0))
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            self.__screen.blit(self.runners[1].custome, self.runners[1].position)
            self.__screen.blit(self.runners[2].custome, self.runners[2].position)
            self.__screen.blit(self.runners[3].custome, self.runners[3].position)
            '''
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            pygame.display.flip() # refresh background 
            
            pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
 
if __name__ =='__main__':
    game = Game()
    pygame.font.init()
    game.competir()
