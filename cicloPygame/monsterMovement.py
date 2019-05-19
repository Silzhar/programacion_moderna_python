"""
Created on Sat May 11 18:05:08 2019  @author: silzhar
"""
import pygame, sys
import random
from pygame.locals import *

class Runner():
    
    __customes = ("orangeMonster", "purpleMonster", "greenMonster", "yellowMonser")
    
    def __init__(self, x=0, y= 0):
        
        ixCustome = random.randint(0, 4)
        self.custome = pygame.image.load("{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
        
class Game():
        def __init__(self):
            self.__screen = pygame.display.set_mode((640, 480)) # width, height
            self.__background = pygame.image.load('racing_road.png')
            pygame.display.set_caption("Carrera !")
        
            self.runner = Runner(320, 240)
  
        def start(self):
            gameOver = False
            while not gameOver:
                for event in pygame.event.get(): # traer eventos de pygame
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_UP: # mover arriba runner
                            self.runner.position[1] -= 10
                        elif event.key == K_DOWN: # mover abajo runner
                            self.runner.position[1] += 10
                        elif event.key == K_LEFT: # mover izquierda runner
                            self.runner.position[0] -= 10
                        elif event.key == K_RIGHT: # mover derecha runner
                            self.runner.position[0] += 10
                        else:
                            pass
                   
                self.__screen.blit(self.__background, (0, 0)) # refresh background
                self.__screen.blit(self.runner.custome, self.runner.position)
                
                pygame.display.flip()

print("My name is{}".format(__name__))                       
    
if __name__ =='__main__':
    game = Game()
    pygame.font.init()
    game.start()                         
        
    
